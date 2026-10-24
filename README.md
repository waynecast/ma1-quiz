# MA1 Quiz #1 Practice

A mobile-friendly practice quiz for NYIM MA1 (Intro to Massage) Quiz #1: classes 1 and 2 plus the Universal Precautions handout.

**Use it:** https://waynecast.github.io/ma1-quiz/

- **Practice quiz:** 25 questions in study-guide order (1 → 33), a new random set every time, with shuffled answer choices.
- **Weighted toward flagged slides:** topics whose slide points are starred, red, highlighted, or set apart show up about twice as often (≈87% of quizzes vs ≈46% for other study-guide topics). Inside a topic, the flagged question is picked 75% of the time. Flagged questions carry a ★ tag.
- **Flagged facts only:** every flagged question, shuffled.
- **Drill one topic:** every question for one study-guide item (1–32, 33 = review line) or extra slide topic (34–38).
- **Review missed:** retry the questions you got wrong. Progress is stored only in your own browser.
- Each answer shows a short explanation and the deck/slide it comes from (MA1-1 = Intro, History & Universal Precautions; MA1-2a = Communication, Documentation, SOAP, SUDS, BP).
- Add it to your phone's home screen to open it like an app. It also works offline after the first visit.

## Editing questions

Questions live in `build_bank.py`. Each one is a single `add(...)` call:

```python
add(TOPIC_NUMBER, "Question?", "Correct answer",
    ["Wrong 1", "Wrong 2", "Wrong 3"], "Explanation.", "MA1-1, slide 4", True)  # True = flagged on the slide
```

Run `python3 build_bank.py` to regenerate `questions.json`, then commit and push.

Unofficial study aid made by a student. Not affiliated with or reviewed by NYIM.
