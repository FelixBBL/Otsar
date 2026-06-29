#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# export_vocab.py  --  build vocab.json for the Otsar Hebrew/Aramaic vocab app
#
# OCCURRENCE-LEVEL export. Instead of one entry per lexeme, this writes one
# entry per distinct *attested form together with its parse*
# (form + binyan + conjugation + person + gender + number + state).
#
# That is what makes the app's PARSING drill work on real data -- grammatical
# features live on word occurrences, not on lexemes -- and it makes "Forms"
# mode show genuine attested inflections. Each record also carries the book and
# a reference, and (optionally) the full text of the verse it was taken from, so
# the app can show book selection and a context verse.
#
#   pip install text-fabric
#   python export_vocab.py
#
# Then: Otsar -> Settings -> "Load vocabulary file (.json)" -> pick vocab.json.
# -----------------------------------------------------------------------------

import json, re, unicodedata
from collections import defaultdict

# ---- options ----------------------------------------------------------------
OUT_PATH              = "vocab.json"
STRIP_CANTILLATION    = True   # remove te'amim (accents U+0591-U+05AF); keep niqqud
INCLUDE_ARAMAIC       = True   # set False for Hebrew only
MIN_LEX_FREQUENCY     = 1      # skip lexemes occurring fewer than this many times
MAX_FORMS_PER_LEXEME  = 0      # cap distinct forms kept per lexeme (0 = keep all)
                               # lower this (e.g. 6) to shrink the file a lot
EXPORT_CONTEXT        = True   # include the verse text of each form (bigger file)

# Cantillation accents occupy U+0591-U+05AF. Niqqud (vowel points, dagesh,
# shin/sin dots, etc.) sit in U+05B0-U+05C7 and are kept.
_ACCENTS = re.compile("[\u0591-\u05AF]")
def clean(s):
    if s is None:
        return ""
    if STRIP_CANTILLATION:
        s = _ACCENTS.sub("", s)
    s = unicodedata.normalize("NFC", s)
    # holam-male: keep the holam dot on the vav, not the preceding letter
    # (tolerate cantillation / meteg sitting between the holam and the vav)
    s = s.replace("\u05BA", "\u05B9")
    s = re.sub(r"\u05B9([\u0591-\u05AF\u05BD]*)\u05D5", "\\1\u05D5\u05B9", s)
    return s

# ETCBC marks an inapplicable / unknown grammatical slot in several ways; the app
# treats an empty string as "this category does not apply to this form", so it
# won't quiz it. Normalise all of those to "".
_EMPTY = {"", "na", "n/a", "none", "unknown", "absent"}
def code(v):
    if v is None:
        return ""
    s = str(v).strip()
    return "" if s.lower() in _EMPTY else s

# ---- load BHSA ---------------------------------------------------------------
# Easiest: this downloads + caches the data the first time (needs internet once).
from tf.app import use
A = use("ETCBC/bhsa", version="2021", silent="deep")
F, L, T = A.api.F, A.api.L, A.api.T

# To use your existing local copy at D:\bhsa2021 instead of the auto-download,
# comment out the three lines above and use this instead:
#
#   from tf.fabric import Fabric
#   TF = Fabric(locations="D:/bhsa2021/tf/2021")   # folder with the .tf files
#   api = TF.load("g_word_utf8 lex voc_lex_utf8 gloss sp language "
#                 "vs vt ps gn nu st")
#   F, L, T = api.F, api.L, api.T

def wfeat(node, name, default=""):
    fobj = getattr(F, name, None)
    if fobj is None:
        return default
    val = fobj.v(node)
    return default if val is None else val

PARSE = ("vs", "vt", "ps", "gn", "nu", "st")   # binyan, conj., person, gender, number, state

_need = ("g_word_utf8", "lex", "voc_lex_utf8", "gloss", "sp", "language") + PARSE
_miss = [f for f in _need if getattr(F, f, None) is None]
if _miss:
    print("WARNING: these expected features did not load:", ", ".join(_miss),
          "\n         the export will be missing data (e.g. an empty 'gloss' skips every lexeme).")

# cache verse-text lookups so we build each verse only once
_verse_cache = {}
def verse_text(w):
    if not EXPORT_CONTEXT:
        return ""
    vs = L.u(w, otype="verse")
    if not vs:
        return ""
    vn = vs[0]
    if vn in _verse_cache:
        return _verse_cache[vn]
    txt = ""
    try:
        txt = T.text(vn)
    except Exception:
        try:
            txt = T.text(L.d(vn, otype="word"))
        except Exception:
            txt = ""
    txt = clean(txt).strip()
    _verse_cache[vn] = txt
    return txt

# ---- build one record per distinct (lexeme, form, parse) --------------------
records = []
lex_nodes = list(F.otype.s("lex"))
print(f"Lexemes in dataset: {len(lex_nodes)}")

for lx in lex_nodes:
    occ = L.d(lx, otype="word")
    if not occ:
        continue
    lex_freq = len(occ)
    if lex_freq < MIN_LEX_FREQUENCY:
        continue

    lang = wfeat(occ[0], "language", "Hebrew")
    if not INCLUDE_ARAMAIC and str(lang).strip().lower() in ("aramaic", "arc"):
        continue

    gloss = wfeat(lx, "gloss").strip()
    if not gloss:
        continue                                  # nothing to drill against

    lex_id = wfeat(lx, "lex") or wfeat(occ[0], "lex") or ""
    lemma  = clean(wfeat(lx, "voc_lex_utf8"))
    sp     = wfeat(occ[0], "sp", "subs")

    # group this lexeme's occurrences by (surface form + full parse signature)
    groups = defaultdict(list)
    for w in occ:
        form = clean(wfeat(w, "g_word_utf8"))
        if not form:
            continue
        sig = (form,) + tuple(code(wfeat(w, p)) for p in PARSE)
        groups[sig].append(w)

    if not groups:
        continue

    items = sorted(groups.items(), key=lambda kv: -len(kv[1]))
    if MAX_FORMS_PER_LEXEME > 0:
        items = items[:MAX_FORMS_PER_LEXEME]

    for sig, ws in items:
        form = sig[0]
        parse = dict(zip(PARSE, sig[1:]))
        rep = ws[0]                                # earliest occurrence (node order = canon order)
        sec = T.sectionFromNode(rep)               # (book, chapter, verse)
        book = sec[0] if sec else ""
        chap = str(sec[1]) if sec else ""
        vers = str(sec[2]) if sec else ""
        ref  = f"{sec[0]} {sec[1]}:{sec[2]}" if sec else ""
        rid  = "|".join([lex_id, form, "-".join(parse[p] for p in PARSE)])

        rec = {
            "id":    rid,
            "lex":   lex_id,
            "form":  form,
            "lemma": lemma or form,
            "gloss": gloss,
            "sp":    sp,
            "freq":  lex_freq,                     # lexeme frequency (used for the freq band)
            "n":     len(ws),                      # how often THIS form+parse is attested
            "lang":  lang,
            "book":  book,
            "c":     chap,
            "v":     vers,
            "ref":   ref,
            **parse,
        }
        if EXPORT_CONTEXT:
            rec["ctx"] = verse_text(rep)
        records.append(rec)

# heaviest/most useful first: by lexeme frequency, then by this form's count
records.sort(key=lambda r: (-r["freq"], -r["n"]))

if not records:
    print("\n!!! 0 records — vocab.json will be an empty array [], and the app will reject it.")
    miss = [f for f in _need if getattr(F, f, None) is None]
    if miss:
        print("    Missing features:", ", ".join(miss))
    print("    Other causes: every lexeme had an empty gloss, or the filters removed everything "
          f"(INCLUDE_ARAMAIC={INCLUDE_ARAMAIC}, MIN_LEX_FREQUENCY={MIN_LEX_FREQUENCY}).")

with open(OUT_PATH, "w", encoding="utf-8") as fh:
    json.dump(records, fh, ensure_ascii=False, indent=1)

import os
size_mb = os.path.getsize(OUT_PATH) / (1024 * 1024)
n_lex = len({r["id"].split("|")[0] for r in records})
print(f"Wrote {len(records)} form-records from {n_lex} lexemes to {OUT_PATH} "
      f"({size_mb:.1f} MB)")
print("First few:",
      ", ".join(f"{r['form']} [{r.get('vt') or r.get('st') or r['sp']}]"
                for r in records[:8]))
if size_mb > 4:
    print("NOTE: the file is larger than ~4 MB, so the app will keep it in memory "
          "for this session rather than remembering it across restarts. To shrink: "
          "set EXPORT_CONTEXT = False and/or MAX_FORMS_PER_LEXEME = 6 near the top.")
