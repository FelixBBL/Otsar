# Otsar · אוֹצָר

**Focused practice for the vocabulary of the Hebrew Bible — and its Aramaic.**

Otsar (*ʼôṣār*, "treasure-house / word-hoard") is a small, offline app for drilling Biblical Hebrew and Aramaic words. It runs as a single file in any browser, or as a desktop app. What sets it apart is what it stands on: the ETCBC **BHSA** database of the entire Hebrew Bible — so your study material *is* the text, not a deck you have to build by hand.

## What it does

The defining feature is flexibility. Want to learn the rare nouns of Proverbs 9? Parse every verb in the corpus by binyan and conjugation? Mix Hebrew and Aramaic in a single session? Without Otsar some of these tasks would take up hours of meticulous *Ctrl+V/Ctrl+C*, some would be simply impossible. With Otsar each of these is a few clicks. And many more study scenarios are on the way.

## Why not just Anki or Quizlet?

Because those are empty boxes you fill yourself. Otsar is built for this one corpus (for now!), and it shows in three ways:

- **It knows the text.** A study set is a *query* — "nouns in Proverbs 9," "all Piel verbs," "Aramaic only," "hapax legomena only." Veritable seconds — and you are ready to begin your study. In case you want to know the precise lexis from a certain part of the Bible, you can build a study set card by card.
- **It knows the language.** Answers are graded on the consonants (vowel-points optional), *qere/ketiv* and vocalization are handled, and parsing comes from real ETCBC morphology — Otsar asks only the categories a given form actually carries. A generic flashcard treats אָמַר as a string; Otsar treats it as a Qal perfect 3MS.
- **It joins reading to drilling.** A built-in reader of the actual text lets you meet a word in its verse, drop it into a deck, and drill it immediately. In Anki or Quizlet the word and its source live apart.

Anki and Quizlet are excellent general tools. Otsar is the specialist for this language.

## Practice modes

Three modes are currently available:

**1. Typed answer.** Type the gloss into the field. Unsure of the meaning? Open the context verse. The classic method for a serious study session.

<img width="2157" height="1341" alt="typed" src="https://github.com/user-attachments/assets/abc3895d-b7cb-47b9-b654-6580d032da61" />

**2. Self-rate.** Reveal the answer and grade yourself. Best for a fast review before a test, or if you prefer to write on paper and check against the screen. The mechanic is self-explanatory.

<img width="2157" height="1326" alt="selfrate" src="https://github.com/user-attachments/assets/22bdd285-90ee-4c9e-858e-696ec622629d" />

**3. Match.** Hebrew and Aramaic words on one side, English glosses on the other — pair them up. The gentlest way to meet unfamiliar vocabulary for the first time.

<img width="2157" height="1332" alt="match" src="https://github.com/user-attachments/assets/b203bb6b-f918-4627-b877-284b0bb75c38" />

## Beyond the cards

- **Your own glosses.** BHSA's glosses don't capture every shade of meaning in the Biblical lexicon. Add the rendering you judge correct, and Otsar will accept it from then on. You can delete your reading in the progress section. 
- **An acquisition strip.** Beneath each word, a small bar shows how far along you are in learning it — dormant to active.
- **A built-in reader.** Read the text itself and tap any word for its gloss and full parsing. Collect the ones you don't know into a deck, then jump straight into drilling them — or just read, and look things up as you go.

<img width="2157" height="1334" alt="reader" src="https://github.com/user-attachments/assets/24f62a79-20a9-4927-ae66-3b2a54256b5a" />

- **Progress.** A statistics view tracks how your vocabulary is coming along.
- **A say-so.** Between night mode and settings sits a small form to report a bug or propose a new feature. Please use it — whether you've hit something broken or had a genius idea for making Otsar better. You'll see notifications for new versions when you open Otsar.

This brief introduction barely covers all the potential the app has. I invite you to explore it on your own!

## How to install

Otsar needs two things: the app, and the data to drill.

### 1. Get the app

- **Any computer, no installation.** Download `Otsar web.html` from the [latest release](https://github.com/FelixBBL/Otsar/releases/latest) and open it in any browser. It works offline and needs nothing else — the best option on macOS and Linux, or if you just want to try it.
- **Windows, as a native app.** Download `Otsar.exe` from the same release and run it — it's portable, no installation. 

### 2. Load the data

From the same release, download the data files and load them once:

- **`vocab.json`** — the vocabulary for drilling. In the app: **Settings → Load vocabulary file**.
- **`tanakh.json`** — the running text for the reader. In the app: the **Read** tab → **Load text…**.

Both are remembered after the first load, so this is a one-time step. Pick a study set and start.

> *Already work with BHSA?* The data files are generated from it with the small export scripts in this repo, so you can regenerate or customize them yourself.

---

*Hebrew text and morphology are from the ETCBC [BHSA](https://github.com/ETCBC/bhsa) dataset — CC BY-NC 4.0, DOI [10.17026/dans-z6y-skyh](https://doi.org/10.17026/dans-z6y-skyh) — accessed via [Text-Fabric](https://github.com/annotation/text-fabric). Influenced by [ch-jensen/Vocab](https://github.com/ch-jensen/Vocab) (Christian Canu Højgaard) and [codykingham/Mahir](https://github.com/codykingham/Mahir) (Cody Kingham). Otsar was built with help from Claude (Anthropic). Code and the BHSA-derived data under CC BY-NC 4.0 (non-commercial, with attribution). See [LICENSE](LICENSE).*
