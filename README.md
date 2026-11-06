# MA1 Quiz Practice

Mobile-friendly practice quizzes for NYIM MA1 (Intro to Massage), with a cumulative mode.

**Use it:** https://waynecast.github.io/ma1-quiz/
Direct links: [Quiz #3](https://waynecast.github.io/ma1-quiz/#q3) · [Quiz #2](https://waynecast.github.io/ma1-quiz/#q2) · [Quiz #1](https://waynecast.github.io/ma1-quiz/#q1) · [Cumulative](https://waynecast.github.io/ma1-quiz/#cumulative)

| Quiz | Classes | Covers | Questions |
|---|---|---|---|
| Quiz #1 | 1–2 | History, Universal Precautions, communication, SOAP, SUDS, blood pressure | 211 |
| Quiz #2 | 3–4 (week 2) | Sending the client home, postural & gait analysis, indications, contraindications, extreme cautions, endangerment sites, body mechanics, draping | 191 |
| Quiz #3 | 5–6 (week 3, quiz 11/9) | Body mechanics, foot stances, table mechanics, tools of the trade, draping rules & NYIM draping policy, stroke elements, Swedish guidelines, session timing, effleurage, petrissage, beneficial effects of massage | 212 |

- **Practice quiz:** 25 questions in study-guide order, a new random set every time, with shuffled answer choices.
- **Weighted toward flagged slides:** topics whose slide points are starred, red, highlighted, underlined or set apart (or a handout marked "Quiz material") show up about twice as often. Inside a topic, the flagged question is picked 75% of the time. Flagged questions carry a ★ tag.
- **Flagged facts only:** every flagged question, shuffled.
- **Drill one topic:** every question for one study-guide item or extra slide/handout topic.
- **Cumulative practice** (quizzes are cumulative): a 40-question weighted quiz drawn from every quiz, a full cumulative set (one question per study-guide item from every quiz), all flagged facts, and review of everything missed. Results show a score per quiz.
- **Review missed:** retry the questions you got wrong, per quiz or across all quizzes. Progress is stored only in your own browser.
- Each answer shows a short explanation and its source: the deck and slide (MA1-1, MA1-2a, MA1-3, MA1-3a, MA1-4, MA1-5, MA1-6, MA1-14), the handout, or the Salvo textbook page.
- Add it to your phone's home screen to open it like an app. It also works offline after the first visit.

## Editing questions

Each quiz has its own bank in `banks/` (`quiz1.py`, `quiz2.py`, `quiz3.py`). Each question is one `add(...)` call:

```python
add(TOPIC_NUMBER, "Question?", "Correct answer",
    ["Wrong 1", "Wrong 2", "Wrong 3"], "Explanation.", "MA1-3, slide 8", True)  # True = flagged on the slide
```

Run `python3 build.py` to regenerate `questions.json`, then commit and push. To add a quiz, copy `banks/quiz3.py` to `banks/quiz4.py`, edit it, and add it to `QUIZZES` in `build.py`; the cumulative mode picks it up automatically.

Unofficial study aid made by a student. Not affiliated with or reviewed by NYIM.
