# MA1 Quiz #2 question bank (Week 2: MA1-3 Postural & Gait Analysis, MA1-3a Indications / Contraindications /
# Extreme Cautions / Endangerment Sites, MA1-4 Body Mechanics & Draping, plus "Sending the Client Home" from MA1-2a).
# Built by build.py. Per question: topic, q, a, w (3 wrong), e (explanation), s (source), f (flagged).
# f=True when the point is red, highlighted, underlined or set apart on the slide, or the handout is marked "Quiz material".
# Sources: MA1-2a / MA1-3 / MA1-3a / MA1-4 = slide decks; handouts by name; Salvo = Massage Therapy Principles & Practices, 7th ed.

TOPICS = {
    # Study guide page 1 - MA1-3 Sending Client Home / Postural Analysis / Gait
    1: "Define gait",
    2: "Normal gait: 3 qualities",
    3: "Define posture",
    4: "What maintains posture",
    5: "Baseline position for balance and alignment",
    6: "Formulating a treatment plan",
    7: "What is used for postural assessment",
    8: "Postural deviations usually found together",
    9: "Postural muscles under stress",
    10: "Causes of gait abnormalities",
    11: "Post-massage recommendations",
    12: "Define misalignment",
    13: "How the client stands for a baseline assessment",
    # Study guide page 2 - MA1-4 Indications, Contraindications, Extreme Cautions, Endangerment Sites
    14: "Define endangerment site",
    15: "Name the endangerment sites",
    16: "Other name for endangerment sites",
    17: "Two types of contraindications",
    18: "Define indication",
    19: "Conditions indicated for massage",
    20: "Considerations for extreme cautions",
    21: "Contraindicated by NYS",
    22: "Define contraindication",
    23: "Extreme caution: what and why",
    24: "Matching: key terms",
    # Also on the slides / handouts
    25: "Plumb line landmarks",
    26: "The gait cycle",
    27: "Spinal curves and ergonomics",
    28: "NYS cautions, local contraindications, clinic rules",
    29: "Mechanical vs. reflex responses",
    30: "Body mechanics and foot stances",
    31: "Draping and turning the client",
    32: "Hot, cold, stretching and self-massage",
}
STUDY_GUIDE_TOPICS = list(range(1, 25))  # 1-13 = page 1, 14-23 = page 2, 24 = the 4 matching questions

from banks.common import Bank
B = Bank()
add = B.add
Q = B.Q

# ================= Study guide page 1 =================

# ---------- 1. Define gait ----------
add(1, "Gait is defined as:", "A person's walking pattern",
    ["A person's standing posture", "The range of motion of the hip", "The curvature of the spine"],
    "Gait = a person's walking pattern.", "MA1-3, slide 8")
add(1, "'The manner in which a person moves on foot' describes:", "Gait",
    ["Posture", "Ergonomics", "Alignment"],
    "Handout definition of gait.", "Postural Assessment handout")
add(1, "A client's walking pattern is called their:", "Gait",
    ["Stance", "Cadence", "Posture"],
    "Gait = walking pattern. (Cadence is steps per minute.)", "MA1-3, slide 8")
add(1, "Observing how a client walks from the front, back and side is called:", "Gait observation (gait analysis)",
    ["Plumb line analysis", "Palpation", "Range of motion testing"],
    "Salvo: ask the client to walk at a normal pace and watch from the front, back and side.", "Salvo p. 291")
add(1, "Which statement about gait is TRUE?", "It is a pattern of movement used while walking or running",
    ["It is the position of the body over a base of support", "It is measured with a plumb line only", "It never changes with injury or age"],
    "Gait patterns are influenced by health, disease, injury, age and more.", "Salvo p. 291")

# ---------- 2. Normal gait qualities ----------
add(2, "A normal gait should be:", "Smooth, coordinated and rhythmic",
    ["Fast, forceful and long-strided", "Slow, deliberate and wide-based", "Stiff, even and heel-heavy"],
    "The three qualities: smooth, coordinated, rhythmic.", "MA1-3, slide 8")
add(2, "Which is NOT one of the 3 qualities of a normal gait?", "Rapid",
    ["Smooth", "Coordinated", "Rhythmic"],
    "Smooth, coordinated, rhythmic.", "MA1-3, slide 8")
add(2, "In a normal gait, the arms:", "Swing forward in opposition to the legs",
    ["Stay still at the sides", "Swing with the same-side leg", "Are held slightly flexed in front of the body"],
    "Arms extended at the sides, swinging forward in opposition to the legs.", "MA1-3, slide 8")
add(2, "During a normal gait, the posture is _____ and the eyes are _____.", "Erect; looking forward",
    ["Slightly flexed; looking down", "Erect; looking at the feet", "Leaning forward; looking up"],
    "Posture erect, eyes looking forward.", "MA1-3, slide 8")
add(2, "Per the handout, in a normal gait the toes point:", "Forward, with feet about hip-width apart",
    ["Outward at 45 degrees", "Inward", "Forward, with feet touching"],
    "Toes point forward, feet hip-width apart; thumb and forefinger point forward.", "Postural Assessment handout")

# ---------- 3. Define posture ----------
add(3, "Posture is defined as:", "The position of the body in space",
    ["A person's walking pattern", "The study of anatomy as it relates to work", "The curvature of the lumbar spine"],
    "Posture = position of the body in space (standing, sitting, lying prone, lying supine).", "MA1-3, slide 2")
add(3, "The handout defines posture as the position of the body:", "Over a base of support",
    ["Against a wall", "In anatomical position", "While walking"],
    "Posture: the position of the body over a base of support.", "Postural Assessment handout")
add(3, "Which is NOT one of the positions of posture listed in the lecture?", "Running",
    ["Standing", "Sitting", "Lying supine"],
    "Standing, sitting, lying prone, lying supine.", "MA1-3, slide 2")
add(3, "The slide says posture:", "Will tell you just about everything",
    ["Only matters for athletes", "Cannot be changed by massage", "Is only assessed lying down"],
    "Posture 'will tell you just about everything.'", "MA1-3, slide 2")

# ---------- 4. What maintains posture ----------
add(4, "Standing posture is maintained by:", "The strength and tone of muscles against gravity",
    ["The ligaments alone", "Bone density", "The nervous system's reflexes only"],
    "Strength & tone of muscles against gravitational forces.", "MA1-3, slide 2", True)
add(4, "Muscles maintain standing posture by working against:", "Gravitational forces",
    ["Atmospheric pressure", "Friction from the floor", "Blood pressure"],
    "Strength and tone of muscles against gravity.", "MA1-3, slide 2", True)
add(4, "Which two qualities of muscle maintain your posture?", "Strength and tone",
    ["Length and color", "Speed and flexibility", "Size and temperature"],
    "Strength & tone of muscles.", "MA1-3, slide 2", True)
add(4, "Muscles that help maintain the body's position are called:", "Postural muscles",
    ["Phasic muscles", "Voluntary muscles", "Cardiac muscles"],
    "Postural muscles maintain position; phasic muscles provide movement.", "Postural Assessment handout")

# ---------- 5. Baseline position ----------
add(5, "Which position is the baseline measure of balance and alignment?", "Standing",
    ["Sitting", "Lying prone", "Lying supine"],
    "Standing is considered the baseline measure of balance and alignment.", "MA1-3, slide 2", True)
add(5, "Why is standing used as the baseline for posture?", "Posture there is maintained by muscle strength and tone against gravity",
    ["It is the most comfortable position", "The client is draped", "It hides postural deviations"],
    "Standing = baseline because muscles must hold the body against gravity.", "Postural Assessment handout")
add(5, "To get a baseline measure of a client's balance and alignment, the client should be:", "Standing",
    ["Lying face down on the table", "Seated in the red chair", "Walking on a treadmill"],
    "Standing = baseline.", "MA1-3, slide 2", True)
add(5, "Salvo describes a postural assessment as an evaluation of the client's posture while:", "Relaxed, barefoot and standing",
    ["Lying prone on the table", "Seated in a massage chair", "Wearing shoes and walking"],
    "Static postural assessment: relaxed, barefoot, standing.", "Salvo p. 290")

# ---------- 6. Treatment plan ----------
add(6, "When formulating a treatment plan, which should you consider?", "Health history, the chief complaint and your assessment findings",
    ["Only what the client prefers to talk about", "Only the client's blood pressure", "Only the strokes you like to use"],
    "Documentation covers history, reason for care, interview and exam findings, and a suggested course of treatment.", "SOAP Notes handout")
add(6, "In SOAP notes, short- and long-term goals and home care go in the:", "Plan",
    ["Subjective", "Objective", "Action"],
    "Plan = the day's treatment, short- and long-term goals, and home care.", "SOAP Notes handout")
add(6, "Gait analysis and postural assessment findings are recorded as:", "Objective information",
    ["Subjective information", "The plan", "The client's goals"],
    "Objective = observable, measurable findings, incl. gait analysis & postural assessment, vital signs, ROM.", "SOAP Notes handout")
add(6, "A short-term goal for a treatment plan focuses on:", "The immediate problem, e.g. decreasing pain this session",
    ["Restoring full function over months", "Eliminating all symptoms permanently", "Rescheduling the client"],
    "Short-term = IMMEDIATE problem; long-term = restore normal or enhanced function.", "MA1-2a, slide 11")
add(6, "A long-term goal focuses on:", "Restoring normal or enhanced function",
    ["Decreasing pain in the current session", "Taking the client's BP", "Choosing a lubricant"],
    "Long-term goals: restore function, eliminate pain if possible, decrease frequency & intensity of symptoms.", "MA1-2a, slide 11")
add(6, "Documentation lets the treatment plan be:", "Evaluated and modified as the client progresses",
    ["Kept secret from the client", "Fixed and never changed", "Skipped if the client pays cash"],
    "Documentation allows progress to be evaluated and/or modified as needed.", "SOAP Notes handout")

# ---------- 7. Postural assessment tool ----------
add(7, "What is used for a postural assessment in the lecture?", "Plumb line analysis",
    ["A blood pressure cuff", "SUDS scale", "A goniometer"],
    "Plumb line analysis: posterior, lateral and anterior views.", "MA1-3, slides 5-7")
add(7, "A plumb line shows the:", "Line of gravity, a vertical line through the center of the body to its base",
    ["Horizontal alignment of the eyes", "Range of motion of each joint", "The client's center of mass while walking"],
    "Salvo: a plumb line determines the line of gravity.", "Salvo p. 290")
add(7, "Plumb line analysis is done from which views?", "Anterior, posterior and lateral",
    ["Superior and inferior only", "Anterior only", "Prone and supine"],
    "Three views on slides 5-7.", "MA1-3, slides 5-7")
add(7, "Besides a plumb line, Salvo mentions which tool for postural assessment?", "A posture grid",
    ["A pulse oximeter", "A reflex hammer", "A tape measure on the thigh"],
    "A posture grid gives horizontal and vertical lines as visual cues.", "Salvo p. 290")
add(7, "The handout's 'Postural Alignment Guidelines' compare a client's posture to:", "What is considered 'normal'",
    ["The therapist's posture", "Last year's photos", "The client's family members"],
    "Posture must be assessed and compared to what is considered normal.", "Postural Assessment handout")

# ---------- 8. Deviations found together ----------
add(8, "Which two postural deviations may co-exist?", "Hyperkyphosis and hyperlordosis",
    ["Scoliosis and genu valgum", "Pes planus and torticollis", "Lordosis and a neutral pelvis"],
    "Salvo: 'Hyperkyphosis and hyperlordosis may co-exist.'", "Salvo p. 429")
add(8, "Rounded shoulders and a dowager's hump are considered mild forms of:", "Hyperkyphosis",
    ["Hyperlordosis", "Scoliosis", "Genu varum"],
    "Salvo classifies both as mild forms of hyperkyphosis.", "Salvo p. 429")
add(8, "Hyperlordosis is accompanied by:", "Increased anterior pelvic tilt",
    ["Posterior pelvic tilt", "A flattened lumbar curve", "Knock-knees"],
    "Hyperlordosis: exaggerated lumbar curve and increased anterior pelvic tilt.", "Salvo p. 429")
add(8, "An exaggerated thoracic curve often appears together with:", "An exaggerated lumbar curve",
    ["A perfectly straight lumbar spine", "Flat feet only", "A lateral curve of the neck only"],
    "Kyphosis and lordosis may co-exist.", "Salvo p. 429")
add(8, "Kyphosis is an excessive curvature of the _____ spine; lordosis is an excessive curvature of the _____ spine.", "Thoracic; lumbar",
    ["Lumbar; thoracic", "Cervical; sacral", "Thoracic; cervical only"],
    "Handout: lordosis = lumbar, kyphosis = thoracic, scoliosis = lateral.", "Postural Assessment handout")

# ---------- 9. Postural muscles under stress ----------
add(9, "Which is TRUE regarding postural muscles?", "They tend to shorten and strengthen when stressed",
    ["They tend to lengthen and weaken when stressed", "They provide most body movement", "They never fatigue"],
    "Postural muscles shorten and strengthen when stressed (study guide answer).", "Postural Assessment handout")
add(9, "Which pair are examples of postural muscles?", "Iliopsoas and erector spinae",
    ["Abdominals and gluteus maximus", "Biceps and triceps", "Deltoid and pectoralis major"],
    "Handout examples of postural muscles.", "Postural Assessment handout")
add(9, "Muscles that provide movement, such as the abdominals and gluteus maximus, are called:", "Phasic muscles",
    ["Postural muscles", "Stabilizers", "Tonic muscles"],
    "Phasic muscles provide movement.", "Postural Assessment handout")
add(9, "When stressed, the iliopsoas and erector spinae tend to:", "Shorten and strengthen",
    ["Lengthen and weaken", "Atrophy", "Become hypotonic"],
    "These are postural muscles: they shorten and strengthen under stress.", "Postural Assessment handout")
add(9, "Postural muscles mainly:", "Help maintain the body's position",
    ["Provide quick movement", "Pump blood", "Control breathing only"],
    "Postural = maintain position; phasic = movement.", "Postural Assessment handout")

# ---------- 10. Causes of gait abnormalities ----------
add(10, "Common abnormalities in gait result from:", "Muscle weakness, postural imbalance, pain, connective tissue restrictions",
    ["Dehydration, fever, hunger, fatigue", "Height, weight, age, gender", "Shoes, flooring, weather, lighting"],
    "Red text on the slide.", "MA1-3, slide 8", True)
add(10, "Which is NOT listed on the slide as a cause of gait abnormalities?", "High blood pressure",
    ["Muscle weakness", "Pain", "Connective tissue restrictions"],
    "Causes: muscle weakness, postural imbalance, pain, CT restrictions.", "MA1-3, slide 8", True)
add(10, "A limp adopted to avoid pain on a weight-bearing structure is called:", "Antalgic gait",
    ["Ataxic gait", "Cadence", "Swing phase"],
    "Salvo: antalgic gait = limp to avoid pain.", "Salvo p. 292")
add(10, "Per the handout, gait can be adversely affected by:", "Surgeries that fuse joints and neurologic conditions",
    ["Drinking water and sleeping well", "Wearing loose clothing", "Deep breathing"],
    "Also: pain, trauma, muscle imbalance, myofascial restrictions, arthritic changes.", "Postural Assessment handout")
add(10, "Postural imbalance is a cause of:", "Gait abnormalities",
    ["Contagious disease", "High diastolic pressure", "Fomites"],
    "Gait abnormalities result from muscle weakness, postural imbalance, pain, CT restrictions.", "MA1-3, slide 8", True)

# ---------- 11. Post-massage recommendations ----------
add(11, "Post-massage recommendations help to:", "Preserve and prolong the benefits of a massage",
    ["Replace the need for future massages", "Diagnose the client's condition", "Raise the client's blood pressure"],
    "Post Massage Recommendations: help preserve and prolong the benefits.", "MA1-2a, slide 18")
add(11, "Which is a post-massage recommendation from the lecture?", "Engage in relaxing activities and avoid stress",
    ["Go straight to a heavy workout", "Take a very hot shower to increase inflammation", "Skip stretching"],
    "Relaxing activities, cryo/thermotherapy, avoid stress, stretch/exercise, self-massage, referral, follow-up.", "MA1-2a, slide 18")
add(11, "Referring a client to a PCP or DC is part of:", "Post-massage recommendations",
    ["The pre-massage interview", "Draping", "Plumb line analysis"],
    "Referral to PCP, DC is on the post-massage recommendations list.", "MA1-2a, slide 18")
add(11, "The handout recommends a post-massage bath that is:", "Warm, ideally with Epsom salts",
    ["Ice cold", "Scorching hot", "Skipped entirely"],
    "Warm, not cold and not scorching hot (which increases inflammation).", "Post Massage Recommendations handout")
add(11, "Why does the handout suggest eating after a massage?", "Massage affects circulation and digestion; light-headedness may come from not eating",
    ["To raise blood pressure above 170/100", "To prevent the client from rescheduling", "To reverse the relaxation"],
    "Your body needs to refuel after a massage.", "Post Massage Recommendations handout")
add(11, "Self-massage tools mentioned for clients include:", "A bouncy ball, golf ball or lacrosse ball",
    ["A hydrocollator", "A stethoscope", "A face cradle"],
    "Self-massage and prevention measures slide.", "MA1-2a, slide 19")

# ---------- 12. Define misalignment ----------
add(12, "Structural misalignment is often the source of:", "Chronic pain",
    ["Acute infection", "High blood pressure", "Fever"],
    "Misalignment: structural misalignment is often the source of chronic pain.", "MA1-3, slide 3")
add(12, "Misalignment can cause:", "Degenerative disc disease, chronic myofascial pain and compensation",
    ["Contagious disease", "Anemia", "Hypertension"],
    "Listed on the misalignment slide.", "MA1-3, slide 3")
add(12, "Which is a sign of structural misalignment?", "Visible deviation from the midsagittal, coronal or horizontal planes",
    ["A fever above 99 degrees", "Pitting edema", "Normal gait"],
    "Signs: visual deviation from the planes, chronic pain, spasm and trigger points.", "Postural Assessment handout")
add(12, "Which is listed as a CAUSE of structural misalignment?", "Muscle imbalance between anterior and posterior muscles",
    ["Drinking water", "Wearing gloves", "Taking blood pressure"],
    "Also: trauma, aging, emotional stress, obesity, repetitive overuse, leg-length difference, fallen arches.", "Postural Assessment handout")
add(12, "A difference in leg length or fallen arches can cause:", "Structural misalignment",
    ["Contagious disease", "Hematoma", "Fever"],
    "Both are on the handout's list of causes.", "Postural Assessment handout")

# ---------- 13. How the client stands for a baseline ----------
add(13, "For a baseline postural assessment, the client should be standing:", "Naturally, NOT in anatomical position",
    ["In anatomical position", "With feet together and arms raised", "On one leg"],
    "Purple text on every plumb line slide: standing naturally, not in anatomical position.", "MA1-3, slides 2, 5-7", True)
add(13, "Why should the client NOT stand in anatomical position for a baseline?", "You want to see their natural posture",
    ["Anatomical position is uncomfortable for the therapist", "It is against NYS law", "It raises blood pressure"],
    "Baseline = standing naturally.", "MA1-3, slide 2", True)
add(13, "Salvo tells you to have the client stand upright, look straight ahead, relax their shoulders and:", "Let their arms hang naturally",
    ["Turn their palms forward", "Lock their knees", "Hold their breath"],
    "Relaxed, barefoot standing posture.", "Salvo p. 290")
add(13, "Assessing posture with the client in anatomical position is:", "Incorrect: the client should stand naturally",
    ["Required by the clinic", "Best for the lateral view", "Only done prone"],
    "STANDING NATURALLY, not in anatomical position.", "MA1-3, slides 5-7", True)

# ================= Study guide page 2 =================

# ---------- 14. Define endangerment site ----------
add(14, "An endangerment site is:", "An area with superficial, delicate, relatively unprotected structures that are prone to injury",
    ["Any area with a lot of muscle", "A place where the client feels ticklish", "An area that must always be draped"],
    "Definition from the slide and the 'Quiz material' handout.", "MA1-3a, slide 10; Endangerment Sites handout", True)
add(14, "Why are endangerment sites prone to injury?", "Their structures are superficial and relatively unprotected",
    ["They have too much muscle", "They are always inflamed", "They are covered by thick fascia"],
    "Superficial, delicate structures not well protected by bones and muscles.", "MA1-3a, slide 10", True)
add(14, "Over an endangerment site, you should use:", "Very light pressure or none at all",
    ["Deep, sustained pressure", "Tapotement", "Cross-fiber friction"],
    "Salvo: only very light pressure, or no pressure, over endangerment sites.", "Endangerment Sites handout", True)
add(14, "Which structures make an area an endangerment site?", "Nerves, blood vessels, organs, glands, lymph nodes, small bony projections",
    ["Large muscle bellies", "Thick fat pads", "Callused skin"],
    "Listed on the slide.", "MA1-3a, slide 10", True)

# ---------- 15. Name the endangerment sites ----------
add(15, "Which of these is an endangerment site?", "Popliteal fossa",
    ["Belly of the gastrocnemius", "Middle of the trapezius", "Gluteus maximus"],
    "Popliteal fossa (back of the knee) is on the handout's list.", "Endangerment Sites handout", True)
add(15, "Which of these is an endangerment site?", "Anterior triangle of the neck",
    ["Upper trapezius", "Rhomboids", "Lateral thigh"],
    "Anterior triangle: carotid artery, jugular vein, thyroid, trachea.", "Endangerment Sites handout", True)
add(15, "Which of these is an endangerment site?", "Axilla (armpit)",
    ["Deltoid", "Forearm extensors", "Calf"],
    "Axilla: axillary artery, brachial plexus, lymph nodes.", "Endangerment Sites handout", True)
add(15, "Which of these is an endangerment site?", "Femoral triangle (groin)",
    ["Quadriceps belly", "Iliotibial band", "Hamstring belly"],
    "Femoral triangle: femoral artery, vein and nerve.", "Endangerment Sites handout", True)
add(15, "Which of these is an endangerment site?", "Kidney area of the low back",
    ["Upper back between the scapulae", "Gluteal muscles", "Erector spinae at T6"],
    "Kidney area (floating ribs) is a posterior endangerment site.", "Endangerment Sites handout", True)
add(15, "Which of these is NOT on the endangerment sites list?", "Gluteus maximus",
    ["Inferior to the ear", "Cubital area (ulnar notch)", "Linea alba"],
    "Gluteus maximus is a large muscle, not an endangerment site.", "Endangerment Sites handout", True)
add(15, "The 'upper abdomen' endangerment site is marked by which bony landmark?", "Xiphoid process",
    ["Iliac crest", "Coccyx", "Acromion"],
    "Upper abdomen (xiphoid process).", "Endangerment Sites handout", True)
add(15, "The cubital area endangerment site is also called the:", "Ulnar notch",
    ["Popliteal fossa", "Femoral triangle", "Linea alba"],
    "Cubital area (ulnar notch) at the elbow.", "Endangerment Sites handout", True)
add(15, "The fibrous band down the center of the abdomen that is an endangerment site is the:", "Linea alba",
    ["Iliotibial band", "Inguinal ligament", "Xiphoid"],
    "Linea alba = fibrous band down the center of the abdomen.", "Endangerment Sites handout", True)
add(15, "Just above the clavicle is the:", "Posterior triangle of the neck",
    ["Anterior triangle of the neck", "Axilla", "Medial brachium"],
    "Posterior triangle: brachial plexus, subclavian artery, external jugular.", "Endangerment Sites handout", True)
add(15, "Salvo notes the most serious adverse events have been linked to pressure on the:", "Neck",
    ["Calves", "Gluteals", "Feet"],
    "The most serious AEs are associated with pressure applied to the neck.", "Endangerment Sites handout", True)

# ---------- 16. Other name ----------
add(16, "Another name for endangerment sites is:", "Cautionary sites",
    ["Trigger points", "Pressure points", "Contraindication zones"],
    "Endangerment Sites OR Cautionary Sites.", "MA1-3a, slide 10", True)
add(16, "'Cautionary sites' is another name for:", "Endangerment sites",
    ["Local contraindications", "Indications", "Trigger points"],
    "Same thing.", "MA1-3a, slide 10", True)
add(16, "Salvo also calls endangerment sites:", "Areas of caution",
    ["Safe zones", "Indications", "Hot spots"],
    "Also called cautionary sites or areas of caution.", "Endangerment Sites handout", True)
add(16, "Salvo's Figure 8-49 is titled:", "Cautionary sites",
    ["Plumb line analysis", "The gait cycle", "Foot stances"],
    "Figure 8-49 Cautionary sites (the calendar's 'Diagram Figure 8-').", "Endangerment Sites handout", True)

# ---------- 17. Two types of contraindications ----------
add(17, "What are the 2 types of contraindications?", "Absolute and local",
    ["Acute and chronic", "Mechanical and reflex", "Primary and secondary"],
    "Red text: absolute and local contraindications.", "MA1-3a, slide 3", True)
add(17, "An absolute contraindication means:", "You would NOT work on the client at all",
    ["Avoid only the affected area", "Massage with lighter pressure", "Massage only with a doctor in the room"],
    "Absolute: a condition where you would NOT work on them at all.", "MA1-3a, slide 3", True)
add(17, "A local contraindication means:", "Avoid the affected area but massage the rest of the body",
    ["Do not massage at all", "Massage only the affected area", "Use only tapotement"],
    "Local: avoid the affected area; can be done on the rest of the body.", "MA1-3a, slide 3", True)
add(17, "In the NYIM clinic, a BP of 170/100 is listed as a(n):", "Absolute contraindication",
    ["Local contraindication", "Indication", "Extreme caution only"],
    "High BP = 170/100 in NYIM clinic, under absolute contraindication.", "MA1-3a, slide 3", True)
add(17, "Contagious viral or bacterial ailments are a(n):", "Absolute contraindication",
    ["Local contraindication", "Indication", "Endangerment site"],
    "Listed under absolute contraindication.", "MA1-3a, slide 3", True)
add(17, "A client with a fresh bruise on one shin can still get a massage elsewhere. The bruise is a(n):", "Local contraindication",
    ["Absolute contraindication", "Indication", "Endangerment site"],
    "Hematomas are local contraindications: avoid the area.", "MA1-3a, slide 7", True)
add(17, "How often would an MD order massage for a client with an absolute contraindication?", "Rarely, though some exceptions occur",
    ["Always", "Never under any circumstance", "Only in the first trimester"],
    "Rare that an MD would order massage, but some exceptions do occur.", "MA1-3a, slide 3", True)

# ---------- 18. Define indication ----------
add(18, "An indication is:", "A condition for which massage may help alleviate the symptoms",
    ["A condition where massage must not be done", "An area prone to injury", "A required draping area"],
    "Indication: condition for which research indicates massage may help.", "MA1-3a, slide 2")
add(18, "A condition in which massage is beneficial is called a(n):", "Indication",
    ["Contraindication", "Extreme caution", "Endangerment site"],
    "Indication = massage is beneficial.", "MA1-3a, slide 2")
add(18, "'Research indicates that massage may help alleviate the symptoms.' This defines:", "Indication",
    ["Contraindication", "Local contraindication", "Adverse event"],
    "Definition of indication.", "MA1-3a, slide 2")
add(18, "Which is the opposite of an indication?", "Contraindication",
    ["Extreme caution", "Endangerment site", "Mechanical response"],
    "Indication = beneficial; contraindication = should not be done.", "MA1-3a, slides 2-3")

# ---------- 19. Conditions indicated ----------
add(19, "Which condition is listed on the slide as an indication for massage?", "Tension headaches",
    ["Fever", "Contagious disease", "Acute phlebitis"],
    "Slide examples: tension headaches, hypertonic muscles, stress.", "MA1-3a, slide 2")
add(19, "Which is an indication for massage?", "Hypertonic muscles",
    ["Open wounds", "Deep vein thrombosis", "Active infection"],
    "Hypertonic muscles are on the slide.", "MA1-3a, slide 2")
add(19, "Which is an indication for massage?", "Stress",
    ["Fever", "Cellulitis", "Hepatitis"],
    "Stress is on the slide.", "MA1-3a, slide 2")
add(19, "Per the Indications handout, which is generally indicated for massage?", "Insomnia",
    ["Phlebitis", "Septic arthritis", "Lymphangitis"],
    "Insomnia: relaxation massage balances the ANS.", "Indications for Massage handout")
add(19, "Per the Indications handout, which is generally indicated for massage?", "Myofascial pain syndrome",
    ["Acute bursitis", "Tuberculosis", "Aortic aneurysm"],
    "Massage, stretching and gentle exercise are usually the best treatment.", "Indications for Massage handout")
add(19, "Per the Indications handout, which is generally indicated for massage?", "TMJ dysfunction",
    ["Erysipelas", "Pitted edema", "Malignant melanoma"],
    "Massage relieves the masseter, temporalis and pterygoids.", "Indications for Massage handout")
add(19, "Which type of edema does massage help?", "Edema due to inactivity",
    ["Edema due to heart failure", "Edema due to kidney failure", "Pitted edema"],
    "Edema due to inactivity is indicated; organ-failure and pitted edema are not.", "Indications for Massage handout")
add(19, "Fatigue, whether mental or physical, is:", "Indicated for massage",
    ["An absolute contraindication", "A local contraindication", "An endangerment site"],
    "Mental: relieves stress. Physical: removes metabolic wastes.", "Indications for Massage handout")

# ---------- 20. Extreme caution considerations ----------
add(20, "When dealing with extreme cautions, you should:", "Do your research and use your BEST judgment",
    ["Always refuse the client", "Ignore it if the client signs consent", "Use deeper pressure"],
    "Extreme Cautions umbrella slide: do your research and use your BEST judgement.", "MA1-3a, slide 6", True)
add(20, "With an extreme caution, the general routine:", "Requires some type of change to fit the client",
    ["Stays exactly the same", "Is always cancelled", "Is done only on the face"],
    "Highlighted: special considerations or a change to the routine.", "MA1-3a, slide 4", True)
add(20, "THE BIG 3 to be aware of are:", "Fever, acute, inflammation",
    ["Pain, swelling, bruising", "Cancer, tumors, infection", "Pregnancy, burns, scars"],
    "Be aware of THE BIG 3: FEVER - ACUTE - INFLAMMATION.", "MA1-3a, slide 7", True)
add(20, "The signs of inflammation listed with the Big 3 are:", "Redness, swelling, heat",
    ["Cold, numbness, pallor", "Itching, flaking, dryness", "Bruising, scarring, scabbing"],
    "(Redness - Swelling - Heat).", "MA1-3a, slide 7", True)
add(20, "If you're not sure massage is appropriate for a condition, you should:", "Check with the client's doctor",
    ["Diagnose it yourself", "Massage it more deeply", "Ask another client"],
    "Diagnosis is not in our scope; check with the doctor when in doubt.", "Indications for Massage handout")
add(20, "Many conditions are OK to massage in the _____ phase but not the acute phase.", "Subacute",
    ["Hyperacute", "Infectious", "Febrile"],
    "Subacute = between acute and chronic; massage generally indicated then, not when acute.", "Indications for Massage handout")

# ---------- 21. NYS contraindications ----------
add(21, "Per NYS, you should NOT treat a client when:", "The therapist or client is in an altered state of awareness from substance use",
    ["The client is nervous", "The client has tight shoulders", "The client has never had a massage"],
    "Red/highlighted: altered state of awareness.", "MA1-3a, slide 5", True)
add(21, "Per NYS, you should NOT treat a client who:", "Refuses to let you confer with their MD",
    ["Asks for light pressure", "Wants to keep their socks on", "Is over 65"],
    "NO consent for consult = do not treat.", "MA1-3a, slide 5", True)
add(21, "Which TWO situations does NYS say you should NOT treat?", "Altered state of awareness, and no consent to confer with the MD",
    ["Fever, and recent surgery", "Pregnancy, and burns", "Varicose veins, and new scars"],
    "Both on the NYS contraindications slide.", "MA1-3a, slide 5", True)
add(21, "If the THERAPIST is in an altered state from substance use, NYS says:", "Do not treat the client",
    ["Treat with lighter pressure", "Treat only if the client agrees", "Have the client sign a waiver"],
    "Applies to the therapist OR the client.", "MA1-3a, slide 5", True)

# ---------- 22. Define contraindication ----------
add(22, "A contraindication is a condition in which massage:", "May NOT be done: it is inappropriate, unadvised or may be harmful",
    ["Is always beneficial", "Must be done daily", "Must be deeper than normal"],
    "Red text: NOT be done; inappropriate, unadvised; may be harmful.", "MA1-3a, slide 3", True)
add(22, "Which word best matches 'contraindication'?", "Unadvised",
    ["Recommended", "Beneficial", "Required"],
    "Inappropriate, unadvised, may be harmful.", "MA1-3a, slide 3", True)
add(22, "'Conditions which massage may be harmful' defines:", "Contraindication",
    ["Indication", "Endangerment site", "Mechanical response"],
    "Contraindication definition.", "MA1-3a, slide 3", True)
add(22, "Contraindications are divided into:", "Absolute and local",
    ["Mechanical and reflex", "Short-term and long-term", "Subjective and objective"],
    "Two types on the same slide.", "MA1-3a, slide 3", True)

# ---------- 23. Extreme caution: what and why ----------
add(23, "An extreme caution is:", "A condition requiring special considerations or a change in the routine",
    ["A condition where massage is never done", "An area that must stay draped", "A type of stroke"],
    "Highlighted definition.", "MA1-3a, slide 4", True)
add(23, "With an extreme caution, you:", "May or may not do the massage",
    ["Must always do the massage", "Must never do the massage", "Must use only deep pressure"],
    "A circumstance where you may or may not do the massage.", "MA1-3a, slide 4", True)
add(23, "Why is a condition labeled an extreme caution rather than a contraindication?", "Massage may be beneficial, but it needs to be modified",
    ["Massage is always harmful", "The client is contagious", "It is an endangerment site"],
    "Where it may be beneficial but it needs to be modified.", "MA1-3a, slide 4", True)
add(23, "Why is phlebitis / DVT a serious caution?", "Massage could dislodge a clot to the lungs, heart or brain",
    ["It makes the client ticklish", "It lowers body temperature", "It causes postural deviations"],
    "Danger: dislodging the clot (pulmonary embolism, coronary thrombosis, stroke).", "Indications for Massage handout")
add(23, "Why is edema from heart or kidney failure a caution?", "Circulation may not handle the extra load from massage",
    ["Massage will cure it", "It is contagious", "It is an endangerment site"],
    "Back-pressure: the client can't handle increased flow. Pitted edema is always contraindicated.", "Indications for Massage handout")

# ---------- 24. Matching ----------
add(24, "Match: 'A condition in which massage is beneficial.'", "Indication",
    ["Contraindication", "Extreme caution", "Endangerment site"],
    "Indication.", "MA1-3a, slide 2")
add(24, "Match: 'Avoid the affected area; massage the rest of the body.'", "Local contraindication",
    ["Absolute contraindication", "Indication", "Extreme caution"],
    "Local contraindication.", "MA1-3a, slide 3", True)
add(24, "Match: 'Do not work on the client at all.'", "Absolute contraindication",
    ["Local contraindication", "Extreme caution", "Indication"],
    "Absolute contraindication.", "MA1-3a, slide 3", True)
add(24, "Match: 'Massage may help, but the routine must be modified.'", "Extreme caution",
    ["Indication", "Absolute contraindication", "Endangerment site"],
    "Extreme caution.", "MA1-3a, slide 4", True)
add(24, "Match: 'Superficial, delicate, unprotected structures prone to injury.'", "Endangerment site",
    ["Local contraindication", "Indication", "Reflex response"],
    "Endangerment (cautionary) site.", "MA1-3a, slide 10", True)
add(24, "Match: 'Inappropriate, unadvised or potentially harmful.'", "Contraindication",
    ["Indication", "Extreme caution", "Mechanical response"],
    "Contraindication.", "MA1-3a, slide 3", True)
add(24, "Match: 'Occurs as a result of pressure or range of motion.'", "Mechanical response",
    ["Reflex response", "Indication", "Extreme caution"],
    "Mechanical response.", "MA1-3a, slide 9")
add(24, "Match: 'Nerves are stimulated, which in turn activate a reflex arc.'", "Reflex response",
    ["Mechanical response", "Local contraindication", "Endangerment site"],
    "Reflex response.", "MA1-3a, slide 9")

# ================= Also on the slides / handouts =================

# ---------- 25. Plumb line landmarks ----------
add(25, "In the posterior plumb line view, the fixed point is the:", "Middle of the medial malleoli",
    ["Slightly anterior to the lateral malleolus", "External occipital protuberance", "Gluteal cleft"],
    "Posterior and anterior views: middle of medial malleoli = fixed point.", "MA1-3, slide 5")
add(25, "In the lateral plumb line view, the line passes through the:", "External auditory meatus, shoulder joint and greater trochanter",
    ["Nasal septum, umbilicus and pubic symphysis", "Gluteal cleft and spine", "Medial malleoli and knees only"],
    "Lateral: slightly anterior to lateral malleolus, slightly anterior to knee midline, greater trochanter, trunk midline, shoulder joint, EAM.", "MA1-3, slide 6")
add(25, "The fixed point of the lateral plumb line view is:", "Slightly anterior to the lateral malleolus",
    ["The middle of the medial malleoli", "The greater trochanter", "The external auditory meatus"],
    "Lateral view fixed point.", "MA1-3, slide 6")
add(25, "Which landmark is on the ANTERIOR plumb line?", "Umbilicus",
    ["Gluteal cleft", "External occipital protuberance", "Greater trochanter"],
    "Anterior: medial malleoli, knees, pubic symphysis, umbilicus, manubrium, nasal septum.", "MA1-3, slide 7")
add(25, "The top landmark of the posterior plumb line is the:", "External occipital protuberance",
    ["Nasal septum", "External auditory meatus", "Center of the manubrium"],
    "Posterior: medial malleoli, knees, gluteal cleft, spine, EOP.", "MA1-3, slide 5")
add(25, "The inferior angle of the scapula should be level with:", "T7",
    ["T1", "L1", "C7"],
    "Other things to look at: inferior angle of scapula level with T-7.", "MA1-3, slide 7")
add(25, "The scapulae should be about how far apart?", "3-4 inches",
    ["1 inch", "8-10 inches", "They should touch"],
    "Scapula 3-4 inches apart.", "MA1-3, slide 7")
add(25, "Knock-knees are called _____; bowlegs are called _____.", "Genu valgum; genu varum",
    ["Genu varum; genu valgum", "Pes planus; pes cavus", "Lordosis; kyphosis"],
    "'Gum' keeps your knees together, 'rum' keeps your knees apart.", "Salvo p. 290")

# ---------- 26. The gait cycle ----------
add(26, "The gait cycle has two phases. What are their proportions?", "Stance 60%, swing 40%",
    ["Stance 40%, swing 60%", "Stance 50%, swing 50%", "Stance 75%, swing 25%"],
    "Stance phase = 60%, swing phase = 40%.", "MA1-3, slide 9", True)
add(26, "How many parts does the stance phase have in the lecture?", "Four",
    ["Three", "Two", "Six"],
    "Heel strike, foot flat, mid-stance, toe off.", "MA1-3, slide 10")
add(26, "How many parts does the swing phase have in the lecture?", "Three",
    ["Four", "Two", "Five"],
    "Acceleration, mid-swing, deceleration.", "MA1-3, slide 11")
add(26, "At heel strike, the dorsiflexors contract:", "Concentrically",
    ["Eccentrically", "Isometrically", "Not at all"],
    "Heel strike: dorsiflexion, concentric contraction.", "MA1-3, slide 10")
add(26, "At foot flat, the dorsiflexors contract:", "Eccentrically",
    ["Concentrically", "Isometrically", "Not at all"],
    "Foot flat: dorsiflexion, eccentric contraction.", "MA1-3, slide 10")
add(26, "During deceleration in the swing phase, which muscles contract for control?", "Hamstrings",
    ["Quadriceps", "Dorsiflexors", "Gluteus medius"],
    "Deceleration: hamstrings contract for control; ends with heel strike.", "MA1-3, slide 11")
add(26, "Toe off involves:", "Plantar flexion",
    ["Dorsiflexion", "Hip abduction", "Knee hyperextension"],
    "Toe off = plantar flexion.", "MA1-3, slide 10")
add(26, "Acceleration in the swing phase involves which muscles contracting?", "Quadriceps",
    ["Hamstrings", "Calf muscles", "Abdominals"],
    "Acceleration = quads contract.", "MA1-3, slide 11")

# ---------- 27. Spinal curves and ergonomics ----------
add(27, "Lordosis is:", "An inward curvature of the lumbar or cervical regions",
    ["An outward curvature of the thoracic region", "A sideways curvature of the spine", "A flat back"],
    "Lordosis: inward curvature of lumbar or cervical regions.", "MA1-3, slide 3")
add(27, "Kyphosis is:", "An outward (convex) curvature of the thoracic and sacral regions",
    ["An inward curvature of the lumbar region", "A sideways curvature of the spine", "Rotation of the pelvis"],
    "Kyphosis: outward (convex) curvature, thoracic & sacral.", "MA1-3, slide 3")
add(27, "Scoliosis is:", "A sideways curvature of the spine",
    ["An inward lumbar curve", "An outward thoracic curve", "A forward head position"],
    "Scoliosis: lateral curvature.", "MA1-3, slide 3")
add(27, "Dowager's hump is also called:", "Neck hump, text hump or hunchback",
    ["Swayback", "Saddleback", "Flat back"],
    "Spine curves excessively forward.", "MA1-3, slide 3")
add(27, "Hyperlordosis is also called:", "Swayback or saddleback",
    ["Hunchback", "Text hump", "Wry neck"],
    "Salvo: hyperlordosis = swayback or saddleback.", "Salvo p. 429")
add(27, "Ergonomics is:", "The scientific study of individual anatomy and physiology as it relates to performing work",
    ["The study of massage history", "A method of draping", "A type of gait abnormality"],
    "Highlighted definition.", "MA1-3, slide 4", True)
add(27, "Ergonomics asks how you set up your equipment to:", "Support your body",
    ["Impress clients", "Save money", "Speed up the massage"],
    "How do you set up your equipment to SUPPORT your body.", "MA1-3, slide 4", True)

# ---------- 28. NYS cautions, local contraindications, clinic rules ----------
add(28, "Per NYS, which is a LOCAL contraindication (massage OK, avoid the area)?", "Varicosities",
    ["Fever", "Contagious disease", "Altered state of awareness"],
    "Red list: fractures, open wounds, hematomas, varicosities, new scars, burns, foreign bodies/hardware.", "MA1-3a, slide 7", True)
add(28, "During the 1st trimester of pregnancy, NYS guidelines say:", "No sacral or abdominal work",
    ["No massage at all", "Only abdominal work", "Deep pressure on the ankles"],
    "Pregnancy - 1st trimester - no sacral or abdominal work.", "MA1-3a, slide 7", True)
add(28, "Per NYS, you should confer with the client's MD for:", "Cancer, tumors, and acute or chronic infection",
    ["Tension headaches", "Hypertonic muscles", "Stress"],
    "Confer with MD: cancer, tumors, acute/chronic infection.", "MA1-3a, slide 7", True)
add(28, "Which is on NYS's 'use caution in treating' list?", "Medication that weakens connective tissue or increases bleeding",
    ["Tension headaches", "Mild stress", "Tight hamstrings"],
    "Also: fever, contagious disease, organ-failure edema, decreased sensation, acute inflammation, phlebitis/DVT, recent surgery.", "MA1-3a, slide 6")
add(28, "Which is NOT a NYIM clinic-specific contraindication (as of 7-22-24)?", "Tension headache",
    ["Active cancer or chemotherapy", "Any active infection, even on antibiotics", "Treated for osteoporosis in the last 2 months"],
    "Clinic list: active cancer/chemo, active infection, COVID positive or exposed within 5 days, osteoporosis treatment in last 2 months.", "MA1-3a, slide 8")
add(28, "A clinic client exposed to COVID 3 days before their appointment:", "Cannot be massaged in the clinic",
    ["Can be massaged with gloves", "Can be massaged if fever-free", "Can be massaged prone only"],
    "COVID positive or exposed up to 5 days prior = clinic contraindication.", "MA1-3a, slide 8")
add(28, "A clinic client with an active infection who is taking antibiotics:", "Cannot be massaged in the clinic",
    ["Can be massaged once they start antibiotics", "Can be massaged with lighter pressure", "Can be massaged on the back only"],
    "Any active infection, even if taking antibiotics.", "MA1-3a, slide 8")
add(28, "Edema due to organ failure that is 'pitted' falls under:", "NYS use-caution list",
    ["Indications", "Endangerment sites", "Mechanical responses"],
    "Edema due to organ failure (CHF, kidney failure) (pitted).", "MA1-3a, slide 6")

# ---------- 29. Mechanical vs. reflex ----------
add(29, "A mechanical response to massage occurs as a result of:", "Pressure or range of motion",
    ["A reflex arc", "The client's mood", "Room temperature"],
    "Mechanical: result of pressure or ROM.", "MA1-3a, slide 9")
add(29, "Which is a MECHANICAL response to massage?", "Reduced swelling",
    ["Decreased sympathetic arousal", "General relaxation", "Reduced blood pressure"],
    "Mechanical: increased circulation, reduced swelling, reduced scar tissue.", "MA1-3a, slide 9")
add(29, "Which is a REFLEX response to massage?", "Decreased arousal of the sympathetic nervous system",
    ["Reduced scar tissue formation", "Reduced swelling", "Increased blood circulation from pressure"],
    "Reflex: decreased sympathetic arousal, relaxation, stretch receptors, vasodilation, reduced BP.", "MA1-3a, slide 9")
add(29, "A reflex response happens when:", "Nerves are stimulated and activate a reflex arc",
    ["Pressure physically moves fluid", "The joint moves through ROM", "The sheet is tucked"],
    "Reflex definition.", "MA1-3a, slide 9")
add(29, "Triggering the muscle spindles (stretch receptors) is a:", "Reflex response",
    ["Mechanical response", "Contraindication", "Gait phase"],
    "Listed under reflex.", "MA1-3a, slide 9")

# ---------- 30. Body mechanics ----------
add(30, "Body mechanics is:", "Proper use of postural techniques to deliver massage with the most efficiency and least trauma to the therapist",
    ["The study of the client's gait", "A draping technique", "A blood pressure procedure"],
    "Definition on the Body Mechanics slide.", "MA1-4, slide 2")
add(30, "The Bow / Archer / Lunge stance is used for:", "Long strokes, down and away from the therapist",
    ["Short, multidirectional strokes", "Sitting work", "Turning the client"],
    "Bow-Archer-Lunge = long strokes.", "MA1-4, slide 5")
add(30, "The Horse / Warrior stance is used for:", "Short, multidirectional strokes",
    ["Long strokes away from the therapist", "Lifting the client", "Taking BP"],
    "Horse-Warrior = short strokes, multidirectional.", "MA1-4, slide 5")
add(30, "Repetitive motion injuries are:", "Self-inflicted injuries from POOR body mechanics",
    ["Caused by clients", "Contagious", "Only from lifting tables"],
    "Carpal tunnel, tennis elbow, TOS, rotator cuff strain, tendonitis.", "MA1-4, slide 7")
add(30, "What is the number 1 reason people leave the massage therapy industry?", "Repetitive motion injuries",
    ["Low pay", "Difficult clients", "Licensing exams"],
    "Repetitive motion injuries: the number 1 reason people leave.", "MA1-4, slide 7")
add(30, "Table mechanics includes:", "Table height, client positioning, bolstering and draping",
    ["Foot stance and breathing", "Client's diet", "SOAP notes"],
    "Anything that has to do with equipment and client.", "MA1-4, slide 3")
add(30, "Which is an element of proper body mechanics?", "Work from hara",
    ["Lock your knees", "Lift with your back", "Hold your breath"],
    "Also: check table height, warm up, correct stance, vary strokes, breathe, brace digits, stretch, lift with legs.", "MA1-4, slide 8")
add(30, "Per the Body Mechanics handout, when do you contract the chi muscle?", "On the exhale, as you apply pressure",
    ["On the inhale", "Only between strokes", "Never during massage"],
    "Breathe out: contract chi muscle, apply pressure. Breathe in: relax, return stroke.", "Massage Body Mechanics handout")
add(30, "In the lunge stance, weight shifts onto the forward leg up to about:", "60%",
    ["100%", "30%", "90%"],
    "Beyond about 60 percent, balance could be lost.", "Massage Body Mechanics handout")
add(30, "Stand with your feet angled about how many degrees to the table?", "45",
    ["90", "10", "180"],
    "Feet angled 45 degrees to the table.", "Massage Body Mechanics handout")
add(30, "'Zero gravity posture' involves:", "Tucking the chin, flattening the low back and sinking the sacrum slightly",
    ["Locking the knees and arching the back", "Leaning on the client", "Bending at the waist"],
    "Optimum line of force with no blocks at the neck or low back.", "Massage Body Mechanics handout")

# ---------- 31. Draping and turning ----------
add(31, "Draping gives:", "Therapist professionalism, client modesty and boundaries",
    ["Deeper pressure", "Faster massages", "A diagnosis"],
    "Draping 'to cover the body with cloth.'", "MA1-4, slide 10")
add(31, "The primary comfort consideration in draping is:", "Warmth",
    ["Color of the sheets", "Speed", "Scent"],
    "As the client goes parasympathetic, temperature and BP may drop.", "MA1-4, slide 12")
add(31, "Which areas MUST stay draped?", "Genital region, gluteal cleft and breast area",
    ["Feet and hands", "Back and shoulders", "Face and neck"],
    "MUST stay draped. In clinic, breasts of both men and women stay draped.", "MA1-4, slide 13", True)
add(31, "Which draping method MUST be used at NYIM?", "Diaper draping",
    ["Towel-only draping", "No draping", "Top-sheet-only draping"],
    "Underlined on the slide: DIAPER DRAPING must be used at NYIM.", "MA1-4, slide 16", True)
add(31, "Local laws on draping are:", "The minimum standard; you CANNOT use less",
    ["Optional", "The maximum allowed", "Only for the clinic"],
    "Follow local laws: the minimum draping standard.", "MA1-4, slide 14", True)
add(31, "If you accidentally expose a client, you should:", "Look away, re-drape and stay composed",
    ["Apologize at length and stop the massage", "Ignore it", "Call the CA immediately"],
    "If you expose: look away, re-drape, stay composed.", "MA1-4, slide 15")
add(31, "When turning a client at NYIM, the client turns:", "Toward you",
    ["Away from you", "Off the table first", "With the sheet removed"],
    "Have client turn toward you (NYIM).", "MA1-4, slide 17")
add(31, "When turning a client, you anchor the sheet with your:", "Thighs",
    ["Hands", "Elbows", "Feet"],
    "Anchor sheet with your thighs, elevate sheet on the opposite side at shoulder and hip.", "MA1-4, slide 17")
add(31, "Turning supine to prone, after the turn you:", "Have the client move up into the face cradle and place a bolster under the ankles",
    ["Have the client move down out of the face cradle", "Remove the top sheet", "Place a bolster under the knees"],
    "Prone: face cradle + bolster under ankles. Prone to supine: move down out of the cradle first.", "MA1-4, slide 17")

# ---------- 32. Hot, cold, stretching, self-massage ----------
add(32, "Cryotherapy (cold) is used for:", "Acute conditions and inflammation",
    ["Chronic conditions and hypertonicity", "Relaxation only", "Pregnancy"],
    "Cold = acute; heat = chronic.", "MA1-2a, slide 20")
add(32, "Thermotherapy should be applied as:", "MOIST heat",
    ["Dry heat only", "Ice packs", "Biofreeze"],
    "Red text: MOIST HEAT (hydrocollator, hot towel cabi, rice packs, sauna, hot tub, bath or shower).", "MA1-2a, slide 20", True)
add(32, "Thermotherapy (heat) is used for:", "Chronic conditions and hypertonicity",
    ["Acute inflammation", "Fresh sprains", "Swelling right after injury"],
    "Red text: heat for chronic and hypertonicity.", "MA1-2a, slide 20", True)
add(32, "Stretching is contraindicated:", "After surgery or a fracture, or with joint inflammation or a herniated disc",
    ["For chronic tension", "To increase ROM", "After a relaxing massage"],
    "Highlighted: when it disrupts healing.", "MA1-2a, slide 22", True)
add(32, "Which is a relaxation technique to recommend to a client?", "Tai chi",
    ["Heavy lifting", "Caffeine", "A cold plunge right after massage"],
    "Highlighted list: deep breathing, meditation, yoga, tai chi, aromatherapy, music/art, biofeedback, hydrotherapy.", "MA1-2a, slide 21", True)
add(32, "The handout says stretching after massage helps by:", "Realigning muscle fibers and improving muscle recovery",
    ["Raising blood pressure", "Increasing inflammation", "Replacing the need for water"],
    "Stretching realigns fibers and trains the nervous system for flexibility.", "Post Massage Recommendations handout")
add(32, "Self-massage between sessions helps the client:", "Prolong and extend the massage benefits",
    ["Avoid ever needing massage again", "Diagnose problems", "Raise blood pressure"],
    "How can the client prolong, extend massage benefits between sessions.", "MA1-2a, slide 19")

c = {}
for q in Q:
    c[q["topic"]] = c.get(q["topic"], 0) + 1
for t in TOPICS:
    assert c.get(t, 0) >= 4, (t, c.get(t, 0))

QUIZ = {"id": "q2", "title": "MA1 Quiz #2", "lectures": "Class 3–4 (week 2)",
        "blurb": "Posture, gait, sending the client home, indications, contraindications, extreme cautions, endangerment sites, plus body mechanics and draping.",
        "sgNote": "1–13 are study-guide page 1, 14–23 are page 2, 24 is the matching section.",
        "studyGuideTopics": STUDY_GUIDE_TOPICS, "topics": TOPICS, "questions": Q}
