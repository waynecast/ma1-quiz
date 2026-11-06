# Builds questions.json for the MA1 practice app from every bank in banks/.
# To add a quiz: create banks/quizN.py (copy quiz2.py's layout) and add it to QUIZZES below.
import json
from collections import Counter
from banks import quiz1, quiz2, quiz3

QUIZZES = [quiz1.QUIZ, quiz2.QUIZ, quiz3.QUIZ]

out = {"title": "MA1 Quiz Practice", "quizzes": []}
for qz in QUIZZES:
    c = Counter(q["topic"] for q in qz["questions"])
    for t in qz["topics"]:
        assert c[t] >= 3, (qz["id"], t, c[t])
    for t in qz["studyGuideTopics"]:
        assert t in qz["topics"], (qz["id"], t)
    out["quizzes"].append(qz)
    print(qz["id"], len(qz["questions"]), "questions;", sum(q["f"] for q in qz["questions"]), "flagged;",
          len(qz["topics"]), "topics")
json.dump(out, open("questions.json", "w"), ensure_ascii=False, indent=1)
