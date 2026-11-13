# MA1 Quiz #4 question bank (Week 4). Built by build.py.
# Study guides: "MA1-7 Effleurage, Petrissage" and "MA1-8 Friction, Tapotement". As with Quiz #3, the study guides are
# numbered one ahead of the slide decks: guide "MA1-7" = deck MA1-6 (Effleurage & Petrissage) and guide "MA1-8" = deck
# MA1-7 (Friction & Tapotement).
# Per the NYIM Program Calendar (term 209), MA1 Quiz #4 is on 11/16 (MA1-9 day), after MA1-7 Friction, Tapotement (11/9)
# and MA1-8 Vibration, Ancillary Strokes (11/11; handout "Introduction to Massage: Massage Strokes"), so topics 24-31
# cover the MA1-8 deck. Salvo 7th ed. pages from the calendar: effleurage 143-147, petrissage 148-150, friction 150-151 &
# 152-154, tapotement 156-159, vibration 159-161, compression 151 & 155.
# Per question: topic, q, a, w (3 wrong), e (explanation), s (source), f (flagged).
# f=True when the point is underlined, colored, or set apart in bold body text on the slide (not just a slide heading).

TOPICS = {
    # Study guide page 1 - "MA1-7" Effleurage, Petrissage (deck MA1-6)
    1: "Define effleurage",
    2: "Effleurage variations",
    3: "Purpose of effleurage",
    4: "Direction of effleurage on the limbs, and why",
    5: "Benefits of effleurage",
    6: "Stance for effleurage",
    7: "Define petrissage",
    8: "What petrissage follows",
    9: "Petrissage variations",
    10: "Benefits of petrissage",
    11: "Stance for petrissage",
    # Study guide page 2 - "MA1-8" Friction, Tapotement (deck MA1-7)
    12: "Describe friction",
    13: "What friction follows",
    14: "What follows friction, and why",
    15: "Superficial vs. deep friction",
    16: "Benefits of friction",
    17: "3 types of superficial friction",
    18: "3 types of deep friction",
    19: "Define tapotement",
    20: "When/where to avoid tapotement",
    21: "The 7 types of percussion",
    22: "Benefits of tapotement",
    23: "Who is credited for cross-fiber friction",
    # Also on Quiz #4 per the calendar: deck MA1-8 Vibration & Ancillary Strokes (11/11)
    24: "Vibration: definition and effects",
    25: "Benefits of vibration",
    26: "4 variations of vibration",
    27: "Compression",
    28: "Treating muscle cramps and spasms",
    29: "Trigger points: definition and classifications",
    30: "Trigger points: the Big Six causes and treatment",
    31: "Tender points, local twitch response and jump sign",
}
STUDY_GUIDE_TOPICS = list(range(1, 24))  # 1-11 = "MA1-7" study guide, 12-23 = "MA1-8" study guide

from banks.common import Bank
B = Bank()
add = B.add
Q = B.Q

# ================= Study guide "MA1-7" (deck MA1-6) =================

# ---------- 1. Define effleurage ----------
add(1, "Effleurage is the:", "Most commonly used Swedish stroke",
    ["Least used Swedish stroke", "Only stroke done without lubricant", "Most physically demanding stroke"],
    "Bold on the slide: mostly commonly used Swedish stroke.", "MA1-6, slide 2", True)
add(1, "Effleurage means:", "To flow or glide",
    ["To knead", "To rub", "To strike"],
    "Bold on the slide: means to FLOW or GLIDE. Knead = petrissage, rub = friction, strike = tapotement.", "MA1-6, slide 2", True)
add(1, "Effleurage is the application of repeated, unbroken gliding movements that follow the:", "Contour of the client's body",
    ["Direction of the muscle fibers only", "Path of the nerves", "Length of the spine only"],
    "CONTOUR is bold on the slide.", "MA1-6, slide 2", True)
add(1, "Effleurage pressure is applied:", "Centripetally",
    ["Centrifugally", "Randomly", "Only away from the heart"],
    "Underlined and bold on the slide: pressure is applied centripetally (toward the center/heart).", "MA1-6, slide 2", True)
add(1, "Which is NOT listed as a way to apply effleurage?", "Elbows",
    ["Palms of the hands", "Forearms", "Fists"],
    "Effleurage: palms, fingertips, forearms, fists. Elbows appear on the friction slide (and aren't allowed in school).", "MA1-6, slide 2")
add(1, "During effleurage you push the tissue:", "Down and away from the therapist",
    ["Up and toward the therapist", "Side to side only", "Straight down and hold"],
    "You will push the tissue down and away from the therapist.", "MA1-6, slide 2")
add(1, "Effleurage pressure may be:", "Superficial or deep",
    ["Superficial only", "Deep only", "None; it is always over the drape"],
    "Pressure may be superficial or deep; done with 1 or 2 hands.", "MA1-6, slide 2")

# ---------- 2. Effleurage variations ----------
add(2, "Which effleurage variation is applied centripetally on the limbs and can be superficial or deep?", "Linear",
    ["Raking", "Nerve/feather stroking", "Circular"],
    "Linear: push tissue down and away, centripetal on arms & legs, superficial or deep.", "MA1-6, slide 5", True)
add(2, "Circular effleurage is also called:", "Sun & Moon",
    ["Ocean waves", "C & V", "Ironing"],
    "Circular aka Sun & Moon; superficial; ball-and-socket joints and abdomen.", "MA1-6, slide 5")
add(2, "Circular (Sun & Moon) effleurage is used on:", "Ball-and-socket joints and the abdomen",
    ["Bony areas only, with no lubricant", "The face only", "The soles of the feet"],
    "Circular: superficial; ball & socket joints, abdomen.", "MA1-6, slide 5")
add(2, "Ironing effleurage is:", "Slow and deep, using larger tools like knuckles or forearms",
    ["Light and fast with the fingertips", "A percussive stroke", "Done only over the drape"],
    "Ironing: slow, deep; knuckles, forearms, etc.", "MA1-6, slide 5")
add(2, "Which effleurage variation is the slow, deep one?", "Ironing",
    ["Raking", "Nerve/feather stroking", "Circular"],
    "Raking, feather stroking and circular are all superficial; ironing is slow and deep.", "MA1-6, slide 5")
add(2, "Nerve/feather stroking is:", "Superficial",
    ["Deep", "Percussive", "Done without contact"],
    "Nerve/feather stroking: superficial.", "MA1-6, slide 5")
add(2, "Which list contains ONLY effleurage variations?", "Linear, raking, feather stroking, circular, ironing",
    ["C & V, ocean waves, fulling, skin rolling", "Chucking, cross-fiber, circular", "Hacking, cupping, pounding, clapping"],
    "The other lists are petrissage, deep friction and tapotement variations.", "MA1-6, slide 5")

# ---------- 3. Purpose of effleurage ----------
add(3, "Which is a purpose of effleurage?", "To introduce touch",
    ["To break down scar tissue", "To loosen mucus with suction", "To create minute muscle contractions"],
    "Purpose: introduce touch, move blood & lymph, prepare for/flush after deeper work, spread lubricant, transition, fall-back stroke.", "MA1-6, slide 3")
add(3, "Effleurage is used both before and after deeper work to:", "Prepare tissue first, then flush it afterward",
    ["Numb the tissue", "Pinch the tissue", "Stretch the joint capsule"],
    "Prepare for deeper work; flush tissue after deeper work.", "MA1-6, slide 3")
add(3, "Effleurage is described as a 'fall-back' stroke and a:", "Transition stroke",
    ["Corrective stroke", "Percussion stroke", "Ancillary stroke"],
    "Transition stroke; fall-back stroke.", "MA1-6, slide 3")
add(3, "Which stroke is used to apply and spread the lubricant?", "Effleurage",
    ["Friction", "Tapotement", "Skin rolling"],
    "Apply lubricant / spread is a purpose of effleurage. Friction and skin rolling use little or no lubricant.", "MA1-6, slide 3")
add(3, "Effleurage moves which fluids?", "Blood and lymph",
    ["Synovial fluid only", "Cerebrospinal fluid", "Bile"],
    "Purpose: move blood & lymph.", "MA1-6, slide 3")
add(3, "Which is NOT a purpose of effleurage?", "Breaking down adhesions with cross-fiber work",
    ["Introducing touch", "Flushing tissue after deeper work", "Transitioning between strokes"],
    "Breaking adhesions is a friction benefit.", "MA1-6, slide 3; MA1-7, slide 4")

# ---------- 4. Direction on limbs ----------
add(4, "On the limbs, effleurage is performed:", "Centripetally, toward the heart (distal to proximal)",
    ["Centrifugally, away from the heart", "Only side to side", "In any direction; it doesn't matter"],
    "Linear effleurage is applied centripetally on the arms & legs.", "MA1-6, slide 5", True)
add(4, "Why is effleurage applied toward the heart on the limbs?", "It follows the direction of venous and lymphatic circulation",
    ["It follows the direction of arterial flow", "It stretches the nerves", "It is easier on the therapist's wrists"],
    "Direction slide: centripetal = toward the center/heart, in the direction of venous & lymphatic circulation.", "MA1-5, slide 5")
add(4, "'Centripetal' means:", "Toward the center/heart",
    ["Away from the center", "Across the muscle fibers", "Along the spine"],
    "Centripetal = toward the center/heart.", "MA1-5, slide 5")
add(4, "On the arm, centripetal effleurage moves from:", "Hand toward the shoulder",
    ["Shoulder toward the hand", "Elbow toward the wrist", "Across the forearm only"],
    "Toward the heart = distal to proximal.", "MA1-5, slide 5; MA1-6, slide 5")
add(4, "On the leg, centripetal effleurage moves from:", "Foot toward the hip",
    ["Hip toward the foot", "Knee toward the ankle", "Side to side on the thigh"],
    "Toward the heart = distal to proximal.", "MA1-5, slide 5; MA1-6, slide 5")
add(4, "Applying effleurage toward the heart helps:", "Venous return and lymph flow",
    ["Arterial pressure rise", "Nerve conduction stop", "Bone growth"],
    "It works with venous & lymphatic circulation; a purpose of effleurage is moving blood & lymph.", "MA1-5, slide 5; MA1-6, slide 3")

# ---------- 5. Benefits of effleurage ----------
add(5, "Effleurage can calm or stimulate depending on:", "Speed",
    ["The lubricant used", "The time of day", "Whether the client is prone"],
    "Calms or stimulates depending on speed (slow = relaxing, rapid = stimulating).", "MA1-6, slide 4; MA1-5, slide 6")
add(5, "Which is a benefit of effleurage?", "Relieves insomnia",
    ["Loosens chest mucus", "Breaks down scar tissue", "Stimulates synovial fluid production"],
    "Benefits: warms, relaxes, calms or stimulates, prepares, soothes & flushes, lengthens muscle, soothes achy muscles, relieves insomnia.", "MA1-6, slide 4")
add(5, "Which pair are both effleurage benefits?", "Warms tissue and lengthens muscle",
    ["Tones atrophied muscle and aids lung decongestion", "Dilates capillaries and breaks down adhesions", "Creates minute contractions and moves gas"],
    "The other pairs are tapotement, friction and vibration benefits.", "MA1-6, slide 4")
add(5, "Fast effleurage is:", "Stimulating",
    ["Always sedating", "Contraindicated", "The same as friction"],
    "Speed: rapid = stimulating; slow = relaxing.", "MA1-5, slide 6")
add(5, "Effleurage soothes and:", "Flushes",
    ["Pinches", "Strikes", "Compresses ischemically"],
    "Soothes & flushes.", "MA1-6, slide 4")
add(5, "Which is NOT an effleurage benefit?", "Tones atrophied muscles",
    ["Relaxes the client", "Soothes tired, achy muscles", "Prepares tissue for deeper work"],
    "Toning atrophied muscle is a tapotement benefit.", "MA1-6, slide 4; MA1-7, slide 11")

# ---------- 6. Stance for effleurage ----------
add(6, "Which stance do you use for effleurage?", "Bow / archer / lunge stance",
    ["Horse / warrior stance", "Feet together", "Kneeling"],
    "Bow-Archer-Lunge = long strokes, down and away from the therapist, which is how effleurage is applied.", "MA1-4, slide 5")
add(6, "The bow stance is used for:", "Long strokes, down and away from the therapist",
    ["Short, multidirectional strokes", "Percussion only", "Turning the client"],
    "Bow-Archer-Lunge stance: long strokes, down and away.", "MA1-4, slide 5")
add(6, "Why does effleurage use the archer (lunge) stance?", "It is a long gliding stroke, and the lunge lets you shift weight from back foot to front",
    ["It keeps both feet parallel for short strokes", "It lets you sit down", "It keeps your hands off the skin"],
    "Long strokes = bow/archer; weight transfers from trail foot to lead foot on the stroke.", "MA1-4, slide 5")
add(6, "In the bow stance used for effleurage, the lead foot:", "Points in the direction of the stroke",
    ["Points back toward the therapist", "Is parallel to the table", "Stays behind the trail foot"],
    "Lead foot points in the direction of the stroke.", "Body Mechanics & Effleurage notes")

# ---------- 7. Define petrissage ----------
add(7, "Petrissage comes from the French 'pétrir', meaning:", "To mash or to knead",
    ["To flow or glide", "To rub", "To pluck"],
    "Speaker notes: petrir means to mash or to knead; like milking the tissue.", "MA1-6, slide 6")
add(7, "Petrissage is:", "Rhythmic lifting of muscle tissue away from the bone, squeezing and releasing",
    ["Gliding along the contour of the body", "Rubbing one surface over another", "Staccato striking with loose wrists"],
    "Definition on the Petrissage slide.", "MA1-6, slide 6")
add(7, "Petrissage is applied to the:", "Muscle belly",
    ["Tendon only", "Bony landmarks", "Joint capsule"],
    "Applied to the muscle belly (middle of the muscle).", "MA1-6, slide 6")
add(7, "Petrissage pressure must be applied:", "Rhythmically, usually in a circular motion",
    ["Randomly", "In one sustained hold", "Only in straight lines"],
    "RHYTHMICALLY is bold on the slide.", "MA1-6, slide 6", True)
add(7, "During petrissage you should:", "Lift, don't pinch the tissue",
    ["Pinch the tissue firmly", "Break contact between squeezes", "Use your elbows"],
    "DON'T is in red on the slide: lift, don't pinch; don't lose contact with the skin.", "MA1-6, slide 6", True)
add(7, "Petrissage is often compared to:", "Milking the tissue",
    ["Ironing a shirt", "Bowing a violin", "Pushing a swing"],
    "Speaker notes: it is like milking the tissue. Bowing = cross-fiber friction; swing = rocking.", "MA1-6, slide 6")
add(7, "Petrissage can be done with:", "1 or 2 hands",
    ["2 hands only", "Elbows only", "A mechanical device only"],
    "Can be done 1 or 2 handed.", "MA1-6, slide 6")

# ---------- 8. What petrissage follows ----------
add(8, "In Swedish massage, petrissage typically follows:", "Effleurage",
    ["Friction", "Tapotement", "Vibration"],
    "Typically follows effleurage.", "MA1-6, slide 6")
add(8, "The Swedish stroke sequence is:", "Effleurage, petrissage, friction, tapotement, vibration, ancillary",
    ["Petrissage, effleurage, tapotement, friction, vibration", "Friction, effleurage, petrissage, vibration", "Tapotement, vibration, friction, effleurage"],
    "Sequence slide.", "MA1-5, slide 8")
add(8, "Which stroke comes right before petrissage in the sequence?", "Effleurage",
    ["Friction", "Compression", "Cupping"],
    "Effleurage warms and prepares tissue for petrissage.", "MA1-6, slide 6; MA1-5, slide 8")
add(8, "Which stroke comes right after petrissage in the sequence?", "Friction",
    ["Effleurage", "Vibration", "Tapotement"],
    "Friction follows petrissage.", "MA1-7, slide 2; MA1-5, slide 8")

# ---------- 9. Petrissage variations ----------
add(9, "In C & V petrissage, the hands:", "Start in a C, lift the belly from the bone, compress, and release in a V without breaking contact",
    ["Tap in a V shape", "Glide in a C along the spine", "Roll the skin between the fingertips"],
    "C & V: rhythmic circle pattern, 1 or 2 handed.", "MA1-6, slide 9")
add(9, "Ocean waves petrissage:", "Rolls/pushes the muscle against the bone, then squeezes and lifts; good on thighs",
    ["Lifts skin with no lubricant", "Is one-handed on the face", "Glides superficially toward the heart"],
    "Ocean waves: fingers point medially, broadens the tissue, 2 handed.", "MA1-6, slide 9")
add(9, "In ocean waves petrissage, the fingers point:", "Medially",
    ["Laterally", "Toward the floor", "Toward the head"],
    "Fingers pointed medially.", "MA1-6, slide 9")
add(9, "Fulling (broadening):", "Grips with both hands, lifts and spreads the tissue laterally from the center",
    ["Rolls skin between thumb and fingers", "Taps with the fingertips", "Is done with one hand on bony areas"],
    "Fulling: used on limbs and back; 2 handed.", "MA1-6, slide 9")
add(9, "Skin rolling is done with:", "Little to NO lubricant and no downward force",
    ["Lots of oil and deep pressure", "The forearm", "A loose fist"],
    "Grasp & lift skin between fingertips and thumbs, compress & roll.", "MA1-6, slide 10")
add(9, "Which petrissage variation can be done on bony areas?", "Skin rolling",
    ["Ocean waves", "Fulling", "C & V"],
    "Skin rolling: no downward force, can be done on bony areas.", "MA1-6, slide 10")
add(9, "Skin rolling stimulates endorphins, producing:", "Analgesia (the absence of pain)",
    ["Anesthesia of the whole body", "Hyperemia only", "Peristalsis"],
    "Will stimulate the release of endorphins & produce analgesia.", "MA1-6, slide 10")
add(9, "Skin rolling is essential to Bindegewebsmassage (connective tissue massage), developed by:", "Elizabeth Dicke",
    ["James Cyriax", "Per Henrik Ling", "Johann Mezger"],
    "BINDEGEWEBSMASSAGE is bold on the slide. Cyriax = cross-fiber friction.", "MA1-6, slide 10", True)

# ---------- 10. Benefits of petrissage ----------
add(10, "Petrissage draws what into the tissue?", "New blood and oxygen",
    ["Lactic acid", "Lymph out of the tissue only", "Lubricant"],
    "Bold on the Purpose slide: draws NEW blood & oxygen to the tissue, improving circulation.", "MA1-6, slide 7", True)
add(10, "Petrissage reduces swelling that is:", "Local",
    ["Systemic", "Caused by a blood clot", "In the lungs"],
    "Reduces LOCAL swelling.", "MA1-6, slide 8")
add(10, "Which is a benefit of petrissage?", "Softens superficial fascia",
    ["Aids lung decongestion", "Moves gas in the GI tract", "Desensitizes a hypersensitive area"],
    "Petrissage benefits include softening superficial fascia; the others are tapotement/vibration benefits.", "MA1-6, slide 8")
add(10, "Petrissage reduces soreness and stiffness by:", "Increasing fresh blood to muscles and soft tissue",
    ["Numbing the nerves", "Blocking circulation", "Breaking bones down"],
    "By increasing fresh blood to the muscles and soft tissues.", "MA1-6, slide 8")
add(10, "Petrissage relieves:", "'Knots' and muscle spasms, improving muscular function",
    ["Fractures", "Contagious skin conditions", "Low blood sugar"],
    "Bold on the Purpose slide.", "MA1-6, slide 7", True)
add(10, "Which pair are both petrissage benefits?", "Removes waste products and stimulates the nervous system",
    ["Dilates capillaries and promotes scar formation", "Tones atrophied muscle and loosens mucus", "Moves gas and stimulates synovial fluid"],
    "Petrissage: ↑ blood flow, removes waste, reduces local swelling and fatigue, relaxes/lengthens, stimulates the nervous system, softens fascia.", "MA1-6, slide 8")
add(10, "Petrissage works through which techniques?", "Stretching, kneading and squeezing",
    ["Gliding, raking and ironing", "Striking, cupping and hacking", "Shaking, rocking and jostling"],
    "Bold on the Purpose slide.", "MA1-6, slide 7", True)

# ---------- 11. Stance for petrissage ----------
add(11, "Which stance is typically used for petrissage?", "Horse / warrior stance",
    ["Bow / archer stance", "Feet together", "Single-leg stance"],
    "Horse-Warrior = short, multidirectional strokes, which is how kneading works.", "MA1-4, slide 5")
add(11, "The horse (warrior) stance is used for:", "Short, multidirectional strokes",
    ["Long strokes down the length of the leg", "Lifting the client", "Turning the client"],
    "Horse-Warrior: short strokes, multidirectional strokes.", "MA1-4, slide 5")
add(11, "In the warrior (horse) stance:", "Feet are wider than the hips and toes point forward",
    ["One foot is far behind the other", "Feet are together", "You kneel on the table"],
    "Warrior: feet wider than hips, toes forward; used for short strokes like petrissage and friction.", "Body Mechanics & Effleurage notes")
add(11, "Which two strokes are best done in the warrior stance?", "Petrissage and friction",
    ["Effleurage and ironing", "Linear effleurage and raking", "Feather stroking and rocking"],
    "Short-distance strokes such as petrissage and friction use warrior stance.", "Body Mechanics & Effleurage notes")

# ================= Study guide "MA1-8" (deck MA1-7) =================

# ---------- 12. Describe friction ----------
add(12, "Friction means:", "To rub",
    ["To knead", "To glide", "To shake"],
    "Friction means to RUB: moving one surface over another.", "MA1-7, slide 2")
add(12, "Friction is done with:", "Little or NO lubricant",
    ["Lots of oil", "Lotion only", "Hot stones"],
    "Bold on the slide: done with little or NO lubricant.", "MA1-7, slide 2", True)
add(12, "Which friction tool can you NOT use while in school?", "Elbows",
    ["Palms", "Thumbs", "Fingers"],
    "Bold on the slide: elbows (that you can not use while in school!!!).", "MA1-7, slide 2", True)
add(12, "Friction is especially beneficial in areas that have:", "Little blood supply, such as around joints, ligaments and tendons",
    ["The most blood supply, like the muscle belly", "Major nerves", "Lymph nodes"],
    "Beneficial in areas with little or no blood supply: around joints, ligaments, tendons.", "MA1-7, slide 2")
add(12, "Friction pressure is:", "NOT gentle or light",
    ["Always feather-light", "Applied over the drape only", "Rhythmic pumping"],
    "Is NOT a gentle or light pressure.", "MA1-7, slide 2")
add(12, "The purpose of friction is to:", "Increase circulation, create heat and loosen stuck tissue",
    ["Introduce touch and spread lubricant", "Loosen mucus with suction", "End the massage"],
    "Purpose: increase circulation, create heat; superficial & deep friction help loosen stuck tissue.", "MA1-7, slide 3")
add(12, "Friction is best described as:", "Moving one surface over another",
    ["Lifting tissue off the bone", "Striking with loose wrists", "Rhythmic pumping into the bone"],
    "Move one surface over another.", "MA1-7, slide 2")

# ---------- 13. What friction follows ----------
add(13, "Friction typically follows:", "Petrissage",
    ["Effleurage", "Tapotement", "Vibration"],
    "Follows petrissage.", "MA1-7, slide 2")
add(13, "In the Swedish sequence, which stroke comes immediately before friction?", "Petrissage",
    ["Tapotement", "Vibration", "Compression"],
    "Sequence: effleurage → petrissage → friction → tapotement → vibration → ancillary.", "MA1-5, slide 8")
add(13, "Why does friction come after petrissage?", "Petrissage has already warmed and loosened the tissue for more specific work",
    ["Friction needs lots of oil from petrissage", "Friction ends the massage", "Petrissage numbs the area"],
    "Sequence goes from general to specific; friction follows petrissage.", "MA1-7, slide 2; MA1-5, slide 8")
add(13, "Which order is correct?", "Effleurage → petrissage → friction",
    ["Friction → petrissage → effleurage", "Petrissage → friction → effleurage → petrissage", "Tapotement → friction → petrissage"],
    "Sequence slide.", "MA1-5, slide 8")

# ---------- 14. What follows friction ----------
add(14, "After friction, follow with:", "Effleurage",
    ["Tapotement", "Skin rolling", "Ischemic compression"],
    "Bold on the slide: when done with friction, follow with effleurage.", "MA1-7, slide 2", True)
add(14, "Why follow friction with effleurage?", "To flush and soothe the area",
    ["To add heat", "To break up adhesions", "To stimulate the nerves"],
    "Bold on the slide: to flush & soothe area.", "MA1-7, slide 2", True)
add(14, "Effleurage after friction flushes the tissue. Which effleurage purpose does this match?", "Flush tissue after deeper work",
    ["Introduce touch", "Apply lubricant", "Prepare for deeper work"],
    "Effleurage purpose: flush tissue after deeper work.", "MA1-6, slide 3; MA1-7, slide 2")
add(14, "A therapist finishes cross-fiber friction on a tendon. What should come next?", "Effleurage over the area",
    ["More friction with elbows", "Pounding", "Nothing; move to the next area"],
    "Follow friction with effleurage to flush & soothe.", "MA1-7, slide 2", True)

# ---------- 15. Superficial vs. deep friction ----------
add(15, "In superficial friction, the hands:", "Slide back and forth over the client's skin to generate heat",
    ["Do NOT slide over the skin", "Strike the skin", "Lift the skin off the bone"],
    "Bold on the slide: back and forth over the SKIN.", "MA1-7, slide 5", True)
add(15, "In deep friction, the therapist's hands:", "Do NOT slide over the skin",
    ["Slide quickly over the skin", "Tap the skin", "Use lots of oil"],
    "DO NOT is bold: skin and superficial fascia move across deeper layers.", "MA1-7, slide 7", True)
add(15, "Deep friction moves:", "The skin and superficial fascia across the deeper layers of tissue",
    ["The hands across the skin's surface", "Only the bone", "Lymph toward the heart"],
    "Definition of deep friction.", "MA1-7, slide 7")
add(15, "Which friction is general and more vague?", "Superficial friction",
    ["Deep friction", "Cross-fiber friction", "Chucking"],
    "Superficial: general, more vague. Deep: more precise.", "MA1-7, slide 5")
add(15, "Superficial friction on the limbs works:", "Distal to proximal (wrist → elbow, ankle → knee)",
    ["Proximal to distal", "Across the joint only", "In random circles"],
    "Work distal to proximal.", "MA1-7, slide 5")
add(15, "Deep friction softens hyperplasia, which means:", "Thickening of tissue",
    ["Loss of tissue", "Bleeding under the skin", "Nerve damage"],
    "Softens hyperplasia (thickening of tissue).", "MA1-7, slide 7")
add(15, "Deep friction rearranges muscle and collagen fibers into a:", "More biofunctional pattern",
    ["Random pattern", "Tighter scar", "Shorter muscle"],
    "Breaks down scar tissue & adhesions; rearranges fibers in a more biofunctional pattern.", "MA1-7, slide 7")
add(15, "What do superficial and deep friction have in common?", "Both use little or no lubricant",
    ["Both slide over the skin", "Both are percussive", "Both are only done over the drape"],
    "Little or NO lubricant appears on both slides.", "MA1-7, slides 5 and 7")

# ---------- 16. Benefits of friction ----------
add(16, "Which is a benefit of friction?", "Breaks down adhesions",
    ["Aids lung decongestion", "Stimulates peristalsis", "Relieves insomnia"],
    "Friction benefits: heat, dilates capillaries, ↑ circulation, breaks adhesions, proper scar formation, reduces trigger/tender points.", "MA1-7, slide 4")
add(16, "Friction dilates the:", "Capillaries",
    ["Pupils", "Bronchi", "Lymph nodes"],
    "Dilates capillaries.", "MA1-7, slide 4")
add(16, "Friction promotes:", "Proper scar formation",
    ["Thicker scars", "Muscle atrophy", "Fluid retention"],
    "Promotes proper scar formation.", "MA1-7, slide 4")
add(16, "Friction reduces:", "Trigger and tender point formation and activity",
    ["Circulation", "Heat in the tissue", "Range of motion"],
    "Reduces trigger & tender point formation & activity.", "MA1-7, slide 4")
add(16, "Which is NOT a friction benefit?", "Tones atrophied muscles",
    ["Generates heat", "Increases circulation", "Breaks down adhesions"],
    "Toning atrophied muscles is a tapotement benefit.", "MA1-7, slides 4 and 11")
add(16, "Friction generates:", "Heat",
    ["Cold", "Suction", "Numbness"],
    "Generates heat; purpose: creates heat.", "MA1-7, slides 3–4")

# ---------- 17. Superficial friction types ----------
add(17, "The 3 types of superficial friction are:", "Superficial warming (SWF), rolling, wringing",
    ["Chucking, cross-fiber, circular", "Tapping, hacking, cupping", "Fine, coarse, rocking"],
    "Superficial variations slide. Chucking/XFF/circular are deep friction.", "MA1-7, slide 6")
add(17, "Superficial warming friction (SWF) is:", "General, longitudinal, light pressure that heats the surface",
    ["Perpendicular to the fibers on an injury", "Two hands moving in opposite directions", "Rolling tissue around the bone"],
    "SWF: general, longitudinal, 1 or 2 hands, light pressure, lots of heat only to the surface.", "MA1-7, slide 6")
add(17, "In rolling friction, the palms:", "Roll the tissue around the bone, mostly on the forearms",
    ["Strike with a cupped hand", "Lift skin between fingertips", "Move in opposite directions vigorously"],
    "Rolling: 2 handed, arms & legs (mostly forearms), palmar surface, consistent pressure.", "MA1-7, slide 6")
add(17, "Which superficial friction has the hands moving in opposite directions, like a brush burn?", "Wringing",
    ["Rolling", "Superficial warming", "Chucking"],
    "Wringing: 2 handed, very vigorous, pushing & pulling in opposite directions.", "MA1-7, slide 6")
add(17, "Wringing on the fingers and toes is done with:", "The index finger and thumb",
    ["The forearm", "A loose fist", "The heel of the hand"],
    "Wringing: arms & legs; fingers & toes with index finger and thumb.", "MA1-7, slide 6")
add(17, "Which superficial friction uses light pressure?", "Superficial warming friction (SWF)",
    ["Wringing", "Cross-fiber friction", "Chucking"],
    "SWF: light pressure. Wringing is very vigorous.", "MA1-7, slide 6")

# ---------- 18. Deep friction types ----------
add(18, "The 3 types of deep friction are:", "Chucking, cross-fiber friction, circular",
    ["SWF, rolling, wringing", "Tapping, pincement, clapping", "Compression, rocking, jostling"],
    "Deep friction variations slide.", "MA1-7, slide 8")
add(18, "Chucking is also called linear, parallel or longitudinal friction because it goes:", "In the direction of the muscle fibers",
    ["Perpendicular to the fibers", "In tiny circles", "Across the skin only"],
    "Chucking: in the direction of muscle fibers; fingertips or thumbs.", "MA1-7, slide 8")
add(18, "Chucking is very effective on or between:", "Bony areas such as the metatarsals and metacarpals",
    ["The abdomen", "Large muscles like the glutes", "Lymph nodes"],
    "Very effective on or between bony areas: metatarsals/metacarpals.", "MA1-7, slide 8")
add(18, "Cross-fiber friction (XFF) is applied:", "Perpendicular to the muscle fibers",
    ["Parallel to the muscle fibers", "In large circles", "With a cupped hand"],
    "XFF: work perpendicular to muscle fiber, like a bow across a stringed instrument.", "MA1-7, slide 8", True)
add(18, "Cross-fiber friction is also called:", "Deep transverse friction",
    ["Superficial warming friction", "Longitudinal friction", "Palmar friction"],
    "XFF aka deep transverse friction.", "MA1-7, slide 8", True)
add(18, "Cross-fiber friction is a rehabilitative/corrective stroke that is more effective on:", "Newer scar tissue",
    ["Old, mature scars only", "Healthy muscle bellies", "Bones"],
    "XFF: used on injured or contracted tissue; more effective on newer scar tissue; communicate with the client.", "MA1-7, slide 8")
add(18, "Circular deep friction is often described as:", "'Filling in a Scantron': tiny circles around joints and bony areas",
    ["'Karate chops' on the back", "'Like a bow across strings'", "'Like pushing a swing'"],
    "Circular: thumbs or fingertips, tiny circles; heel of the hand on the muscle belly.", "MA1-7, slide 8")
add(18, "Cross-fiber friction should be:", "Done on just the spot, with lighter pressure on injuries as tolerated",
    ["Done all over the muscle with heavy pressure", "Done over the drape only", "Painless, so no need to check in"],
    "Rub just the spot, not all over; moderate-heavy in general, lighter on injured tissue; can be sore, communicate.", "MA1-7, slide 8")

# ---------- 19. Define tapotement ----------
add(19, "Tapotement is also known as:", "Percussion",
    ["Compression", "Vibration", "Friction"],
    "Bold on the slide: aka Percussion.", "MA1-7, slide 9", True)
add(19, "Tapotement is:", "Repetitive staccato striking movements of the hands with loose wrists and fingers",
    ["Rhythmic lifting of tissue off the bone", "Unbroken gliding along the contour", "Rapid shaking without breaking contact"],
    "Definition; 'with loose wrists and fingers' is bold.", "MA1-7, slide 9", True)
add(19, "The purpose of tapotement is:", "Stimulating underlying tissue",
    ["Spreading lubricant", "Breaking down scar tissue", "Holding pressure on a trigger point"],
    "Bold: for the PURPOSE of stimulating underlying tissue.", "MA1-7, slide 9", True)
add(19, "How should tapotement build?", "Start soft and slow, build to forceful and quick, then soften and slow to finish",
    ["Start at full power and stay there", "Start fast and stop abruptly", "Stay the same throughout"],
    "You don't have to get to full power.", "MA1-7, slide 10")
add(19, "Tapotement is often used to:", "Finish an area or end the massage",
    ["Introduce touch", "Spread lubricant", "Begin the session"],
    "Often used to finish an area or end the massage.", "MA1-7, slide 10")
add(19, "Tapotement can be applied:", "Directly to the skin or over the drape, with no lubricant",
    ["Only with heavy oil", "Only on bare skin", "Only on the face"],
    "Applied directly to the skin or over the drape; NO lubricant is necessary.", "MA1-7, slide 10")

# ---------- 20. Avoid tapotement ----------
add(20, "Tapotement should be avoided:", "Over endangerment sites",
    ["Over large muscles", "On the back", "Over the drape"],
    "Bold: Avoid over endangerment sites.", "MA1-7, slide 10", True)
add(20, "Tapotement should be avoided:", "Immediately after exercise",
    ["Before the massage ends", "On the soles of the feet", "After effleurage"],
    "Bold: Avoid immediately after exercise.", "MA1-7, slide 10", True)
add(20, "For a client with a history of abuse trauma, tapotement:", "May be avoided; maybe don't 'hit' them",
    ["Should always be done at full force", "Is required to finish the session", "Should only be pounding"],
    "People who have abuse trauma, maybe don't 'hit' them.", "MA1-7, slide 10")
add(20, "Which tapotement is 'definitely NOT' for someone who has experienced trauma?", "Pounding",
    ["Raindrops", "Tapping", "Pincement"],
    "Bold on the slide under pounding.", "MA1-7, slide 14", True)
add(20, "Clapping (slapping) can be negative because:", "The client may have experienced trauma; know your client",
    ["It requires oil", "It numbs the area", "It is too light to feel"],
    "Bold: can be NEGATIVE, KNOW your client; may have experienced trauma.", "MA1-7, slide 14", True)
add(20, "Which is NOT listed as a reason to avoid tapotement?", "The client is lying prone",
    ["Over endangerment sites", "Immediately after exercise", "Abuse trauma history"],
    "Prone is fine; cupping for drainage is done prone.", "MA1-7, slides 10 and 13")

# ---------- 21. 7 types of percussion ----------
add(21, "Which list is the 7 types of tapotement?", "Tapping, pincement, hacking, cupping, pounding, diffused, clapping",
    ["Tapping, raking, hacking, cupping, rocking, jostling, clapping", "Chucking, wringing, rolling, hacking, cupping, pounding, clapping", "Fine, coarse, rocking, mechanical, hacking, cupping, clapping"],
    "Variations of tapotement slides.", "MA1-7, slides 12–14")
add(21, "Tapping is also called:", "Punctuation",
    ["Plucking", "Beating", "Slapping"],
    "Bold: Tapping aka Punctuation. Plucking = pincement; beating = pounding; slapping = clapping.", "MA1-7, slide 12", True)
add(21, "Pincement is also called:", "Plucking",
    ["Punctuation", "Beating", "Slapping"],
    "Bold: Pincement aka Plucking; a mini petrissage.", "MA1-7, slide 12", True)
add(21, "Pulsing, a type of tapping, is done:", "With one hand to the rhythm of a heartbeat (lub-dub)",
    ["With two fists on the glutes", "With a cupped hand on the chest", "With the ulnar border on the back"],
    "Tapping: regular tapping, pulsing (heartbeat), raindrops (random fingertips, nice on face & scalp).", "MA1-7, slide 12")
add(21, "Which tapping technique is very nice on the face and scalp?", "Raindrops",
    ["Hacking", "Pounding", "Cupping"],
    "Raindrops: fingertips falling randomly.", "MA1-7, slide 12")
add(21, "Hacking is done with:", "The ulnar border of the hand, like karate chops",
    ["A cupped palm", "The fingertips only", "The palmar surface"],
    "Hacking: mainly on the back; usually 2 handed; fingers slightly apart, come together on impact.", "MA1-7, slide 13")
add(21, "Hacking ALONG the muscle fibers is ___, and ACROSS the fibers is ___.", "Relaxing; stimulating",
    ["Stimulating; relaxing", "Relaxing; relaxing", "Painful; numbing"],
    "Bold on the slide.", "MA1-7, slide 13", True)
add(21, "Cupping is used over the thoracic region to:", "Loosen congestion, mucus and phlegm in the chest",
    ["Stimulate peristalsis", "Tone atrophied glutes", "Release trigger points"],
    "Cupping: suction, hollow sound, very vigorous, may induce coughing; helps clear a lingering cold.", "MA1-7, slide 13")
add(21, "Cupping is combined with postural drainage, in which the client is:", "Prone with the head lower than the chest and a pillow under the hips",
    ["Supine with the head raised", "Seated upright", "Side-lying with knees bent"],
    "Gravity-assisted drainage.", "MA1-7, slide 13")
add(21, "Pounding (beating) is done with the ulnar side of an open/relaxed fist on:", "Large muscles like the glutes, quads and hamstrings",
    ["The face and scalp", "The abdomen", "Bony areas"],
    "OPEN/RELAXED and LARGE are bold.", "MA1-7, slide 14", True)
add(21, "Diffused tapotement is mostly used on the abdomen to:", "Stimulate peristalsis",
    ["Loosen mucus", "Tone the quads", "Calm the scalp"],
    "Diffused: one hand rests loosely as a buffer, the other taps its dorsal surface.", "MA1-7, slide 14")
add(21, "Clapping (slapping) is done with the palmar surface and is good on:", "The bottom of the feet",
    ["The face", "Endangerment sites", "The abdomen"],
    "Gentle slapping, firm patting, 'like a cat bats'.", "MA1-7, slide 14")

# ---------- 22. Benefits of tapotement ----------
add(22, "Tapotement affects nerve endings by:", "Stimulating them first, then sedating them if continued",
    ["Only stimulating them", "Only sedating them", "Having no effect"],
    "Becomes more sedative if continued with consistent pressure and rhythm.", "MA1-7, slide 11")
add(22, "Which is a benefit of tapotement?", "Aids decongestion of the lungs",
    ["Breaks down scar tissue", "Relieves insomnia", "Softens superficial fascia"],
    "Tapotement benefits: stimulates then sedates, lung decongestion, tones atrophied muscles, ↑ local blood flow, relieves pain, desensitizes.", "MA1-7, slide 11")
add(22, "Tapotement tones:", "Atrophied muscles",
    ["Scar tissue", "Tendons only", "Bones"],
    "Tones atrophied muscles.", "MA1-7, slide 11")
add(22, "Tapotement increases blood flow that is:", "Local",
    ["Systemic", "Arterial only", "In the brain"],
    "LOCAL is bold.", "MA1-7, slide 11", True)
add(22, "After a few minutes, tapotement can:", "Desensitize a hypersensitive area",
    ["Make an area more sensitive", "Cause scar tissue", "Raise blood pressure permanently"],
    "Desensitizes a hypersensitive area after a few minutes of stimulation.", "MA1-7, slide 11")
add(22, "To make tapotement sedating rather than stimulating, keep it:", "Consistent in pressure and rhythm, and continue it",
    ["Random and short", "As forceful as possible", "Under 5 seconds"],
    "Stimulates initially, then more sedative if continued with consistent pressure and rhythm.", "MA1-7, slide 11")

# ---------- 23. Cross-fiber friction credit ----------
add(23, "Who is credited with cross-fiber friction (XFF)?", "James Cyriax",
    ["Elizabeth Dicke", "Per Henrik Ling", "Johann Mezger"],
    "Highlighted in green and underlined on the slide (spelled 'Cryiax'). Dicke = Bindegewebsmassage.", "MA1-7, slide 8", True)
add(23, "James Cyriax developed which technique?", "Cross-fiber (deep transverse) friction",
    ["Skin rolling", "Swedish effleurage", "Bindegewebsmassage"],
    "XFF aka deep transverse friction, discovered by James Cyriax.", "MA1-7, slide 8", True)
add(23, "Cyriax's technique works:", "Perpendicular to the muscle fibers, like a bow across strings",
    ["Parallel to the fibers", "Only on the skin's surface", "With suction"],
    "Cross-fiber = perpendicular.", "MA1-7, slide 8", True)
add(23, "Match: Elizabeth Dicke is to Bindegewebsmassage as James Cyriax is to:", "Cross-fiber friction",
    ["Skin rolling", "Tapotement", "Ischemic compression"],
    "Dicke: connective tissue massage (skin rolling). Cyriax: XFF.", "MA1-6, slide 10; MA1-7, slide 8", True)

# ================= Deck MA1-8 Vibration & Ancillary Strokes (11/11, on Quiz #4 per the calendar) =================

# ---------- 24. Vibration: definition and effects ----------
add(24, "Vibration is:", "Rapid shaking, quivering, trembling or rocking movements",
    ["Staccato striking with loose wrists", "Rhythmic pumping into the bone", "Gliding along the contour"],
    "Applied with the fingertips, full hand or an appliance.", "MA1-8, slide 2")
add(24, "During vibration you must:", "Not break contact with the skin",
    ["Lift your hands between each movement", "Use lots of oil", "Strike the skin"],
    "Bold: DO NOT BREAK CONTACT WITH THE SKIN!", "MA1-8, slide 2", True)
add(24, "Which is the most physically demanding stroke?", "Vibration",
    ["Effleurage", "Petrissage", "Compression"],
    "Bold on the slide: vibration is the most physically demanding stroke.", "MA1-8, slide 2", True)
add(24, "The effects of vibration depend on:", "Intensity, speed and duration",
    ["Lubricant, music and lighting", "Table height only", "The client's age only"],
    "The effects depend on intensity, speed, duration.", "MA1-8, slide 2")
add(24, "The 3 physiological stages of vibration are:", "Stimulation, relaxation, numbing (if applied longer)",
    ["Ischemia, hyperemia, blanching", "Warming, cooling, warming", "Pain, spasm, pain"],
    "Physiological effects: 3 stages.", "MA1-8, slide 2")
add(24, "If vibration is applied for a long time, it can cause:", "Numbing",
    ["Bruising", "Scar tissue", "Muscle atrophy"],
    "Third stage: numbing (if applied longer).", "MA1-8, slide 2")

# ---------- 25. Benefits of vibration ----------
add(25, "Which is a benefit of vibration?", "Moves gas in the gastrointestinal tract",
    ["Breaks down scar tissue", "Promotes proper scar formation", "Softens superficial fascia"],
    "Vibration benefits slide.", "MA1-8, slide 3")
add(25, "Vibration creates:", "Minute muscle contractions",
    ["Large muscle spasms", "Ischemia that lasts", "Adhesions"],
    "Creates minute muscle contractions.", "MA1-8, slide 3")
add(25, "Vibration (mostly jostling) stimulates the production of:", "Synovial fluid",
    ["Bile", "Red blood cells", "Mucus"],
    "Stimulates synovial fluid production: jostling mostly.", "MA1-8, slide 3")
add(25, "Vibration relieves which kind of congestion?", "Chest and sinus congestion",
    ["Lymph node congestion", "Liver congestion", "Kidney congestion"],
    "Relieves chest & sinus congestion.", "MA1-8, slide 3")
add(25, "Regarding trigger and tender points, vibration:", "Reduces their activity; not a cure, but helps",
    ["Cures them permanently", "Creates them", "Has no effect"],
    "Reduces trigger & tender point activity: not cure, but helps.", "MA1-8, slide 3")
add(25, "Which benefit do vibration and diffused tapotement share?", "Stimulating peristalsis",
    ["Breaking adhesions", "Toning atrophied muscle", "Loosening mucus with suction"],
    "Vibration stimulates peristalsis; diffused tapotement is used on the abdomen to stimulate peristalsis.", "MA1-8, slide 3; MA1-7, slide 14")
add(25, "Vibration accesses:", "Deeper structures",
    ["Only the skin", "Only the drape", "Bone marrow"],
    "Accesses deeper structures.", "MA1-8, slide 3")

# ---------- 26. 4 variations of vibration ----------
add(26, "The 4 variations of vibration are:", "Fine, coarse (jostling), rocking, mechanical devices",
    ["Tapping, hacking, cupping, clapping", "Chucking, cross-fiber, circular, wringing", "Active, latent, primary, satellite"],
    "Bold on the slide: 4 variations of vibration.", "MA1-8, slide 4", True)
add(26, "Fine vibration is done with:", "Fingertips, with stiff fingers and wrist; small movements",
    ["The whole limb grasped and shaken", "A loose fist", "A cupped palm"],
    "Fine: small movements, any direction, alternating fingertips like pistons; on the abdomen to increase peristalsis.", "MA1-8, slide 4", True)
add(26, "Coarse vibration is also called:", "Jostling",
    ["Rocking", "Raindrops", "Pincement"],
    "Coarse/Jostling: bigger movements; grasp and shake the muscle belly or the whole limb.", "MA1-8, slide 4", True)
add(26, "When jostling a whole limb, you:", "Grab the limb, apply slight traction and shake it",
    ["Strike it with the ulnar border", "Press it into the bone and hold", "Glide toward the heart only"],
    "Used at the shoulder & hip to loosen the muscles around the joint.", "MA1-8, slide 4", True)
add(26, "Before jostling a limb, make sure:", "There are no joint problems",
    ["The client is hungry", "You've used plenty of oil", "The client is standing"],
    "MAKE SURE THERE ARE NO JOINT PROBLEMS.", "MA1-8, slide 4")
add(26, "Rocking vibration:", "Is more relaxing and uses a pitch-and-catch motion, like pushing someone on a swing",
    ["Is the most stimulating vibration", "Uses stiff fingertips like pistons", "Requires a mechanical device"],
    "Rocking: eyes closed, it feels like the table is swaying.", "MA1-8, slide 4", True)
add(26, "Use caution with mechanical vibration devices because:", "You take the vibrations back up your own arm",
    ["They require oil", "They cannot be used on muscle", "They are only for the face"],
    "Mechanical devices: CAUTION when using.", "MA1-8, slide 4", True)

# ---------- 27. Compression ----------
add(27, "Compression is:", "Rhythmic pumping performed perpendicular to the muscle belly",
    ["Gliding parallel to the fibers", "Striking with a cupped hand", "Lifting skin between fingers"],
    "Bold: RHYTHMIC PUMPING.", "MA1-8, slide 5", True)
add(27, "Compression is applied:", "On the skin or over the drape or clothing, with no lubricant",
    ["Only with heavy oil", "Only on bare skin", "Only with a mechanical device"],
    "NO lubricant required; great for pre-event sports massage.", "MA1-8, slide 5")
add(27, "Compression is great for:", "Pre-event sports massage",
    ["Post-surgical scar tissue only", "Facial massage", "Lung decongestion"],
    "Great for pre-event sport massage.", "MA1-8, slide 5")
add(27, "When you press and hold during compression, the tissue blanches because of:", "Ischemia: reduced blood flow; cool to the touch",
    ["Hyperemia: increased blood flow", "Inflammation", "Bruising"],
    "Blanching = ischemia (lack of blood flow).", "MA1-8, slide 5")
add(27, "On release of compression, hyperemia means:", "Increased blood flow; warm to the touch",
    ["Decreased blood flow; cool to the touch", "A trigger point has formed", "A bruise is forming"],
    "Hyperemia created on release. If it stays warm/pink a long time, it might need more work.", "MA1-8, slide 5")
add(27, "Ischemic compression is held for:", "8–12 seconds",
    ["1–2 seconds", "30–60 seconds", "5 minutes"],
    "Ischemic compression: hold 8–12 seconds.", "MA1-8, slides 5 and 12")
add(27, "Which is a benefit of compression?", "Interrupts the pain–spasm–pain cycle",
    ["Breaks down scar tissue", "Loosens mucus", "Moves gas in the GI tract"],
    "Compression benefits: capillary flush, ↑ cellular nutrition, spreads/broadens fibers, vasodilation, interrupts pain–spasm–pain.", "MA1-8, slide 6")
add(27, "Compression creates a:", "Capillary flush",
    ["Lymph blockage", "Muscle tear", "Scar"],
    "Compression benefits slide.", "MA1-8, slide 6")

# ---------- 28. Muscle cramps / spasms ----------
add(28, "To treat a muscle cramp or spasm you must use:", "Even, sustained compression",
    ["Rapid tapotement", "Cross-fiber friction", "Skin rolling"],
    "Bold on the slide: even, sustained compression.", "MA1-8, slide 7", True)
add(28, "Which is on the list for treating a muscle cramp or spasm?", "Golgi tendon release",
    ["Pounding", "Ice and dehydration", "Cupping"],
    "Treatment: even sustained compression, stretch, effleurage, Golgi tendon release, heat, hydration.", "MA1-8, slide 7")
add(28, "Which list is ALL treatments for a muscle cramp?", "Stretch, effleurage, heat, hydration",
    ["Hacking, cupping, pounding, clapping", "Chucking, wringing, rolling", "Ice, rest, tapotement"],
    "Cramp treatment list.", "MA1-8, slide 7")
add(28, "Which is NOT on the cramp/spasm treatment list?", "Tapotement",
    ["Heat", "Stretch", "Hydration"],
    "Tapotement is stimulating; the list is compression, stretch, effleurage, Golgi tendon release, heat, hydration.", "MA1-8, slide 7")

# ---------- 29. Trigger points: definition & classifications ----------
add(29, "A trigger point is a:", "Hyperirritable focus in a taut band of skeletal muscle or fascia that refers pain when compressed",
    ["Local tender spot that never refers pain", "Bony landmark", "Bruise from deep pressure"],
    "HYPERIRRITABLE is bold.", "MA1-8, slide 8", True)
add(29, "Trigger points are:", "Always tender when compressed",
    ["Never tender", "Only found in bone", "Only found in tendons"],
    "Bold: always tender when compressed; can be any tissue ('landmines').", "MA1-8, slide 8", True)
add(29, "Trigger points can cause autonomic phenomena such as:", "Sweating, tearing, goosebumps and skin temperature changes",
    ["Fractures and dislocations", "Fever and rash", "Hair loss"],
    "Examples listed in the definition.", "MA1-8, slide 8")
add(29, "Active trigger points are:", "Symptomatic: they hurt with or without pressure and refer pain",
    ["Asymptomatic and hidden", "Painful only with pressure", "Always harmless"],
    "Active: symptomatic, very sensitive, refer pain, cause weakness, stop muscles lengthening.", "MA1-8, slide 9", True)
add(29, "Latent trigger points are:", "Asymptomatic, more common, painful only with pressure, and do NOT refer pain",
    ["Symptomatic and constantly painful", "Rare and always referring pain", "Found only in the referral zone"],
    "Latent: the ones that are hiding.", "MA1-8, slide 9", True)
add(29, "Which type of trigger point is more common?", "Latent",
    ["Active", "Primary", "Satellite"],
    "Latent: more common.", "MA1-8, slide 9", True)
add(29, "A primary trigger point is:", "The original or main trigger point, activated by acute or chronic overload",
    ["One found in the referral zone", "One caused by overcompensation in a synergist", "Always isolated"],
    "Primary: rarely an isolated TP.", "MA1-8, slide 10", True)
add(29, "A satellite trigger point is found:", "In the referral pattern/zone of another trigger point",
    ["In the synergist muscle from overcompensation", "Only in the original muscle", "In bone"],
    "Associated TPs: secondary (synergist, overcompensation) and satellite (in the referral zone).", "MA1-8, slide 10", True)
add(29, "A secondary trigger point is activated by:", "Overcompensation, and can be found in a synergist",
    ["Being in the referral zone", "Cold only", "Direct trauma to the bone"],
    "Secondary: synergist = a muscle that supports or aids the first muscle's action.", "MA1-8, slide 10", True)
add(29, "The 2 types of associated trigger points are:", "Secondary and satellite",
    ["Active and latent", "Primary and secondary", "Fine and coarse"],
    "Associated = result of the main trigger point.", "MA1-8, slide 10", True)

# ---------- 30. Big Six causes & treatment ----------
add(30, "The 'Big Six' causes of trigger points spell:", "CRIOTS: Cold, Referral, Ischemia, Overload, Trauma, Stress",
    ["RICE: Rest, Ice, Compression, Elevation", "SOAP: Subjective, Objective, Assessment, Plan", "SUDS: Subjective Units of Distress Scale"],
    "In red on the slide: The Big Six.", "MA1-8, slide 11", True)
add(30, "Which is one of the Big Six causes of trigger points?", "Ischemia",
    ["Hydration", "Heat", "Effleurage"],
    "C-Cold, R-Referral, I-Ischemia, O-Overload, T-Trauma, S-Stress.", "MA1-8, slide 11", True)
add(30, "Which is NOT one of the Big Six?", "Hydration",
    ["Cold", "Overload", "Stress"],
    "Hydration is a cramp treatment, not a cause.", "MA1-8, slides 7 and 11", True)
add(30, "Trigger point treatment should be:", "Polymodal: use different strokes",
    ["Only one stroke repeated", "Tapotement only", "Avoided entirely"],
    "Bold: should be polymodal.", "MA1-8, slide 12", True)
add(30, "Which is part of trigger point treatment?", "Ischemic compression held 8–12 seconds",
    ["Pounding for 5 minutes", "Avoiding any stretching", "Using lots of oil"],
    "Treatment: polymodal, lengthen the muscle, ischemic compression 8–12 s, adjust lifestyle/habits.", "MA1-8, slide 12", True)
add(30, "To eliminate a trigger point's symptoms, the client has to:", "Eliminate the cause",
    ["Avoid all massage", "Take a hot bath only", "Exercise immediately after"],
    "In red: you can treat trigger points, but they have to eliminate the cause to eliminate the symptoms.", "MA1-8, slide 12", True)
add(30, "When a trigger point releases, it might:", "Start to vibrate like a really fast pulse",
    ["Turn cold and blanch", "Bruise immediately", "Spread to the whole limb"],
    "In red on the slide.", "MA1-8, slide 12", True)
add(30, "Besides hands-on work, trigger point treatment includes:", "Adjusting lifestyle/habits and lengthening the muscle",
    ["Avoiding water", "Only rest", "Only medication"],
    "Bold on the slide.", "MA1-8, slide 12", True)

# ---------- 31. Tender points, LTR, jump sign ----------
add(31, "A tender point is:", "Local: in one spot, does not move anywhere else",
    ["Always refers pain elsewhere", "Found only in the referral zone", "A bony landmark"],
    "Bold: is local, in one spot. A knot in a muscle is a tender point.", "MA1-8, slide 13", True)
add(31, "The key difference between a trigger point and a tender point is:", "A trigger point refers pain; a tender point stays local",
    ["A tender point refers pain; a trigger point stays local", "They are identical", "Tender points are only in bone"],
    "TPs give rise to referred pain; tender points are local.", "MA1-8, slides 8 and 13")
add(31, "Use less pressure on tender points for clients on:", "High-dose blood thinners, since they bruise more easily",
    ["Antihistamines", "Vitamins", "No medication"],
    "Cautions on tender points.", "MA1-8, slide 13")
add(31, "Tender point work should NOT be used:", "In the acute stage of an injury",
    ["After the intake", "On a knot in the muscle", "With relative pressure"],
    "Do not use in an acute stage of an injury.", "MA1-8, slide 13")
add(31, "A local twitch response (LTR) is:", "A reflexive twitch of the affected or adjacent muscle; a good sign the body is settling in",
    ["The client wincing or jumping in pain", "Bruising after pressure", "A sign to stop massage permanently"],
    "Bold heading; firing results from a summation of sensory nerve information.", "MA1-8, slide 14", True)
add(31, "A jump sign is:", "A spontaneous reaction of pain or discomfort: the client winces, jumps or speaks up on pressure",
    ["A reflexive muscle twitch that is a good sign", "Increased blood flow on release", "Blanching of the tissue"],
    "Jump sign vs. local twitch response.", "MA1-8, slide 14", True)
add(31, "Which is described as 'a good sign'?", "Local twitch response",
    ["Jump sign", "Blanching that stays", "Active trigger point"],
    "LTR: when this happens you know the body is settling in. It is a good sign.", "MA1-8, slide 14", True)

c = {}
for q in Q:
    c[q["topic"]] = c.get(q["topic"], 0) + 1
for t in TOPICS:
    assert c.get(t, 0) >= 4, (t, c.get(t, 0))

QUIZ = {"id": "q4", "title": "MA1 Quiz #4", "lectures": "Classes 6–8 (week 4, quiz 11/16)",
        "blurb": "Effleurage and petrissage (definitions, variations, purpose, benefits, direction, stances), friction (superficial and deep types, Cyriax), tapotement (7 types, when to avoid, benefits), vibration, compression, muscle cramps, trigger points and tender points.",
        "sgNote": "1–11 are the \"MA1-7\" study guide (Effleurage, Petrissage), 12–23 are the \"MA1-8\" study guide (Friction, Tapotement). The guides are numbered one ahead of the decks, so slides cited are decks MA1-6 and MA1-7. Per the program calendar, 24–31 cover the MA1-8 Vibration & Ancillary Strokes deck (11/11), also on this quiz.",
        "studyGuideTopics": STUDY_GUIDE_TOPICS, "topics": TOPICS, "questions": Q}
