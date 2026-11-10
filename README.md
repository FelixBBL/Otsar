# Otsar · אוֹצָר

**Focused practice for the vocabulary of the Hebrew Bible — and its Aramaic.**

**▶ Use it now at [otsar.space](https://otsar.space)** — nothing to install.

Otsar (*ʼôṣār*, "treasure-house / word-hoard") is a small app for drilling Biblical Hebrew and Aramaic words. It runs on the web at [otsar.space](https://otsar.space), as a single offline file in any browser, or as a desktop app. What sets it apart is what it stands on: the ETCBC **BHSA** database of the entire Hebrew Bible — so your study material *is* the text, not a deck you have to build by hand.

## What it does

The defining feature is flexibility. Want to learn the rare nouns of Proverbs 9? Parse every verb in the corpus by binyan and conjugation? Mix Hebrew and Aramaic in a single session? Without Otsar some of these tasks would take up hours of meticulous *Ctrl+C/Ctrl+V*, some would be simply impossible. With Otsar each of these is a few clicks. And many more study scenarios are on the way.

## Why not just Anki or Quizlet?

Because those are empty boxes you fill yourself. Otsar is built for this one corpus (for now!), and it shows in three ways:

- **It knows the text.** A study set is a *query* — "nouns in Proverbs 9," "all Piel verbs," "Aramaic only," "hapax legomena only." Veritable seconds — and you are ready to begin your study. In case you want to know the precise lexis from a certain part of the Bible, you can build a study set card by card.
- **It knows the language.** Answers are graded on the consonants (vowel-points optional), *qere/ketiv* and vocalization are handled, and parsing comes from real ETCBC morphology — Otsar asks only the categories a given form actually carries. A generic flashcard treats אָמַר as a string; Otsar treats it as a Qal perfect 3MS.
- **It joins reading to drilling.** A built-in reader of the actual text lets you meet a word in its verse, drop it into a deck, and drill it immediately. In Anki or Quizlet the word and its source live apart.

Anki and Quizlet are excellent general tools. Otsar is the specialist for this language.

## Practice modes

Four modes are currently available:

**1. Typed answer.** Type the gloss into the field. Unsure of the meaning? Open the context verse. The classic method for a serious study session.

<img width="2157" height="1326" alt="typed_0 4 0" src="https://github.com/user-attachments/assets/a1e32a4c-59e6-48c9-acae-5eadd41178f5" />

**2. Self-rate.** Reveal the answer and grade yourself. Best for a fast review before a test, or if you prefer to write on paper and check against the screen. The mechanic is self-explanatory.

<img width="2156" height="1332" alt="self-rate_0 4 0" src="https://github.com/user-attachments/assets/7dacd47d-1edd-4ff6-abee-b61855342fce" />

**3. Match.** Hebrew and Aramaic words on one side, English glosses on the other — pair them up. The gentlest way to meet unfamiliar vocabulary for the first time.

<img width="2154" height="1335" alt="match_0 4 0" src="https://github.com/user-attachments/assets/15b84b2c-4f3e-42a6-90d9-d276a5bffbf0" />

**4. Cloze** *(new in 0.5)*. A word is taken out of a real verse, and you supply it — by its meaning, or by its exact vowelled form. Otsar picks verses where you can already read most of the other words. Type the form or choose it among forms with the same consonants; a wrong form gets an explanation of what you wrote and what the verse needs.

## Decks

Since 0.4, study sets live on shelves of their own, in the **Decks** tab.

- **Built-in** decks are generated from your vocabulary the moment it loads: frequency tiers, the most frequent proper names, the Aramaic core. They are always in step with your data.
- **Your decks** are the ones you make — from the current Practice filters in one click, card by card through a lexeme search, from words collected in the Reader, or by taking a copy of any other deck and editing it.
- **Community** decks ship curated with the app; this shelf is where shared decks will gather.

Any deck is one click from a drill: **Study** loads it into Practice with your progress tracked as usual.

<img width="2157" height="1332" alt="decks_0 4 0" src="https://github.com/user-attachments/assets/eb116e49-028d-4f05-98a1-8f695cbc9633" />

**A deck is a reference, not a copy of the text.** Exported decks (`.deck.json`) carry only lexeme pointers plus the glosses you wrote yourself — a few kilobytes. The Hebrew and the morphology are resolved from the importer's own data, so sharing a deck never means redistributing the BHSA text: that stays on each user's machine, under its own license.

## Worksheets

Every deck prints. Pick a layout — **Test sheet** (blanks to fill, with an optional answer-key page), **Study sheet** (a compact two-column reference), or **Flashcards** (cut-out cards, duplex-ready) — then shape it in a live editor: page size, columns, type sizes, order, per-item tweaks, even the glosses themselves. Print, or save as PDF. Made for handing out in class as much as for your own desk.

<img width="2156" height="1338" alt="export_0 4 0" src="https://github.com/user-attachments/assets/5f55638f-1544-4da4-84c9-cff15be23e0a" />

## Beyond the cards

- **Your own glosses.** BHSA's glosses don't capture every shade of meaning in the Biblical lexicon. Add the rendering you judge correct, and Otsar will accept it from then on. You can delete your reading in the progress section. 
- **An acquisition strip.** Beneath each word, a small bar shows how far along you are in learning it — dormant to active.
- **A built-in reader.** Read the text itself and tap any word for its gloss and full parsing. Show the ketiv, the qere, or both, and choose which words get a gloss. Collect the ones you don't know into a deck, then jump straight into drilling them — or just read, and look things up as you go. Any card opens its verse in the Reader, and **Esc** brings you back to the card.

<img width="2157" height="1337" alt="reader_0 4 0" src="https://github.com/user-attachments/assets/c0db64e9-43c5-45ec-9141-6e65a3f20799" />

- **Progress.** A statistics view tracks how your vocabulary is coming along.
- **A say-so.** Between night mode and settings sits a small form to report a bug or propose a new feature. Please use it — whether you've hit something broken or had a genius idea for making Otsar better. You'll see notifications for new versions when you open Otsar.

This brief introduction barely covers all the potential the app has. I invite you to explore it on your own!

## How to get it

### On the web — nothing to install

Open **[otsar.space](https://otsar.space)**. On your first visit Otsar downloads the vocabulary and the text of the Hebrew Bible (about 10 MB); your browser keeps them, along with your progress, settings and decks, so later visits start straight away. Works in any modern browser, on any computer.

### Offline or as a desktop app

Download **`Otsar.zip`** from the [latest release](https://github.com/FelixBBL/Otsar/releases/latest). It contains:

- **`Otsar.exe`** — the Windows desktop app. Portable, no installation.
- **`Otsar_web_v0.5.0.html`** — the same app as a single file. Open it in any browser; it works fully offline. The best option on macOS and Linux.
- **`vocab.json`** and **`tanakh.json`** — the data. Load them once:
  - **`vocab.json`** — the vocabulary for drilling. In the app: **Settings → Load vocabulary file**.
  - **`tanakh.json`** — the running text for the Reader and Cloze. In the app: the **Read** tab → **Load text…**.

Both are remembered after the first load, so this is a one-time step. Pick a study set and start.

> *Already work with BHSA?* The data files are generated from it with the small export scripts in this repo, so you can regenerate or customize them yourself.

---

*Hebrew text and morphology are from the ETCBC [BHSA](https://github.com/ETCBC/bhsa) dataset — CC BY-NC 4.0, DOI [10.17026/dans-z6y-skyh](https://doi.org/10.17026/dans-z6y-skyh) — accessed via [Text-Fabric](https://github.com/annotation/text-fabric). Influenced by [ch-jensen/Vocab](https://github.com/ch-jensen/Vocab) (Christian Canu Højgaard) and [codykingham/Mahir](https://github.com/codykingham/Mahir) (Cody Kingham). Otsar was built with help from Claude (Anthropic). Code and the BHSA-derived data under CC BY-NC 4.0 (non-commercial, with attribution). See [LICENSE](LICENSE).*
