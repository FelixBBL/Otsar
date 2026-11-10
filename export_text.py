#!/usr/bin/env python3
"""
Otsar — running-text export for the Reader.

Emits one JSON file per book: an ordered stream of word objects carrying the
fields the Reader needs — pointed form, trailer (so the text flows with the
right spacing/maqqef/sof-pasuq), lemma, gloss, part of speech, parse, and the
qere form whenever a word has one. This is the *running text*, not the
deduplicated vocabulary that export_vocab.py produces.

Setup (once):
    pip install text-fabric
Run:
    python export_text.py
Output:
    ./otsar-text/text_<Book>.json   ->  load it in the Reader ("Load text…")

Each file is shaped { "book": <name>, "words": [ {word}, ... ] } and each word is:
    w      pointed form as written (ketiv consonants with qere vowels, BHS style)
    tr     trailer that follows the word (space, "־" maqqef, "׃" sof pasuq …)
    c, v   chapter, verse
    lex    ETCBC lexeme id (unique per homonym)
    lemma  vocalised citation form (voc_lex_utf8)
    gloss  ETCBC gloss
    sp     part of speech
    vs vt ps gn nu st   parse features (only those that apply)
    q      qere form, present ONLY when the word has a qere
    qtr    qere trailer (present with q)
"""
import json, os, re, unicodedata

# ---- options -----------------------------------------------------------------
BOOKS = None             # None = whole Tanakh (all 39 books); or a list like ["Genesis","Exodus"]
STRIP_CANTILLATION = False     # keep te'amim (cantillation accents); set True to strip
OUTDIR = "otsar-text"
BHSA_VERSION = "2021"
# To use a local clone instead of auto-download, set LOCAL_TF to the tf path,
# e.g. r"D:\bhsa2017\tf\2017", and the script will load from there.
LOCAL_TF = ""
# ------------------------------------------------------------------------------

_ACCENTS = re.compile(r"[\u0591-\u05AF\u05BD\u05BF\u05C0\u05C3]")
# holam-male: BHSA puts the holam on the letter BEFORE the vav (הִמֹּו, יֹּום, רִאשֹׁון).
# After NFC the holam also precedes dagesh and shin/sin dots, so accents, meteg, dagesh
# and those dots can all sit between the holam and the vav. Move the dot onto the vav
# unless the vav has a vowel or dagesh of its own (consonantal vav: לֹוֶה, שֹׁוֶה).
_HOLAM_MALE = re.compile("\u05B9([\u0591-\u05AF\u05BC\u05BD\u05BF\u05C1\u05C2\u05C4\u05C5]*)\u05D5(?![\u05B0-\u05BC\u05C7])")
_STRAY_DIGITS = re.compile("([\u0591-\u05F4])[0-9]+(?=[\u0591-\u05F4])")   # e.g. "יִנֹּ97ון" in Ps 72:17
def fix_holam(s):
    s = unicodedata.normalize("NFC", s).replace("\u05BA", "\u05B9")
    s = _STRAY_DIGITS.sub(r"\1", s)
    s = _HOLAM_MALE.sub(lambda m: m.group(1) + "\u05D5\u05B9", s)
    return unicodedata.normalize("NFC", s)

def clean(s):
    s = s or ""
    if STRIP_CANTILLATION:
        s = _ACCENTS.sub("", s)
    return fix_holam(s)

def trail(s):
    s = s or ""
    if STRIP_CANTILLATION:
        s = _ACCENTS.sub("", s)
    return s

_EMPTY = {"", "na", "n/a", "none", "unknown", "absent"}
def code(v):
    if v is None:
        return ""
    s = str(v).strip()
    return "" if s.lower() in _EMPTY else s

PARSE = ["vs", "vt", "ps", "gn", "nu", "st"]

print("Loading BHSA (first run downloads the app + data)…")
if LOCAL_TF:
    from tf.fabric import Fabric
    TF = Fabric(locations=[LOCAL_TF], silent="deep")
    api = TF.load("g_word_utf8 trailer_utf8 qere_utf8 qere_trailer_utf8 "
                  "lex voc_lex_utf8 gloss sp " + " ".join(PARSE), silent="deep")
    F, T, L, Fall = api.F, api.T, api.L, api.Fall
else:
    from tf.app import use
    A = use(f"ETCBC/bhsa", version=BHSA_VERSION, silent="deep")
    F, T, L = A.api.F, A.api.T, A.api.L

def feat(name, node):
    f = getattr(F, name, None)
    return f.v(node) if f is not None else None

all_books = [T.sectionFromNode(b)[0] for b in F.otype.s("book")]
books = BOOKS or all_books
os.makedirs(OUTDIR, exist_ok=True)

for book in books:
    bnode = T.nodeFromSection((book,))
    if not bnode:
        print(f"  ! book not found: {book}  (known: {', '.join(all_books[:5])} …)")
        continue
    words = []
    for w in L.d(bnode, otype="word"):
        sec = T.sectionFromNode(w)            # (book, chapter, verse)
        lexn = L.u(w, otype="lex")
        rec = {
            "w":     clean(feat("g_word_utf8", w)),
            "tr":    trail(feat("trailer_utf8", w)),
            "c":     sec[1],
            "v":     sec[2],
            "lex":   feat("lex", w) or "",
            "lemma": clean((feat("voc_lex_utf8", lexn[0]) if lexn else None) or feat("voc_lex_utf8", w)),
            "gloss": (feat("gloss", lexn[0]) if lexn else "") or "",
            "sp":    feat("sp", w) or "",
        }
        for p in PARSE:
            val = code(feat(p, w))
            if val:
                rec[p] = val
        q = feat("qere_utf8", w)
        if q:
            rec["q"]   = clean(q)
            rec["qtr"] = trail(feat("qere_trailer_utf8", w))
        words.append(rec)
    out = {"book": book, "words": words}
    path = os.path.join(OUTDIR, f"text_{book}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False)
    print(f"  {book}: {len(words)} words  ->  {path}")

print("Done. In the Reader, click “Load text…” and pick a text_<Book>.json.")
