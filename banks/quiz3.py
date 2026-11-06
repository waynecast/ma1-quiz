# MA1 Quiz #3 question bank (Week 3). Built by build.py.
# Study guides: "MA1-5 Body Mechanics, Tools of Trade, Draping, Assisting on/off Table" and
# "MA1-6 Stroke Elements, Draping Review". The study guides are numbered by class; the matching slide decks are
# MA1-4 (Body Mechanics, Draping, Assisting) and MA1-5 (Stroke Elements & Draping Review).
# Per question: topic, q, a, w (3 wrong), e (explanation), s (source), f (flagged).
# f=True when the point is underlined, or set apart in bold body text on the slide (not just a slide heading).
# Sources: MA1-4 / MA1-5 / MA1-14 = slide decks; handouts by name:
#   "Body Mechanics & Effleurage notes" = MA1 Body Mechanics, Stroke Elements & Effleurage Notes (class handout)
#   "Draping Policy handout" = NYIM Draping Policy MA1-02
#   "Swedish Guidelines handout" = General Guidelines for Swedish Massage MA1-02
#   "Basic Timing handout" = Basic Timing for a Massage Session

TOPICS = {
    # Study guide page 1 - "MA1-5" Body Mechanics, Tools of Trade, Draping, Assisting (deck MA1-4)
    1: "Define body mechanics and why it matters",
    2: "Components of body mechanics",
    3: "The two foot stances",
    4: "Table mechanics",
    5: "Principles of body mechanics",
    6: "5 things you need to do your job",
    7: "Define draping",
    8: "What draping does",
    9: "What warmth provides",
    10: "Rules of draping",
    # Study guide page 2 - "MA1-6" Stroke Elements, Draping Review (deck MA1-5)
    11: "What the stroke elements are",
    12: "#1 reason people leave the industry, and why",
    13: "What must always stay covered",
    14: "Intention",
    15: "Direction",
    16: "Excursion",
    17: "Continuity",
    18: "Sequence",
    19: "Where your pressure comes from",
    20: "Routine: all the elements together",
    # Also on the slides / handouts
    21: "Touch, pressure and depth",
    22: "Speed and rhythm",
    23: "Duration and session timing",
    24: "General guidelines for Swedish massage",
    25: "NYIM draping policy",
    26: "Sheet draping, turning and assisting on/off the table",
    27: "Repetitive strain injuries: causes and prevention",
    28: "Effleurage",
}
STUDY_GUIDE_TOPICS = list(range(1, 21))  # 1-10 = "MA1-5" study guide, 11-20 = "MA1-6" study guide

from banks.common import Bank
B = Bank()
add = B.add
Q = B.Q

# ================= Study guide "MA1-5" (deck MA1-4) =================

# ---------- 1. Define body mechanics ----------
add(1, "Body mechanics is defined as:",
    "The proper use of postural techniques to deliver massage with the utmost efficiency and least trauma to the therapist",
    ["The study of how a client walks", "The arrangement of strokes in a routine", "Adjusting the table for the client's comfort only"],
    "Definition on the first Body Mechanics slide.", "MA1-4, slide 2")
add(1, "Why are good body mechanics important?", "They let you work efficiently and reduce the risk of injury to the therapist",
    ["They make the client fall asleep faster", "They replace the need for draping", "They let you skip the intake"],
    "Efficiency plus least trauma to the therapist; the notes add that they reduce repetitive strain injuries.", "Body Mechanics & Effleurage notes")
add(1, "Good body mechanics reduce which type of injury?", "Repetitive strain injuries (RSIs)",
    ["Contagious skin conditions", "Sprains in the client", "Allergic reactions to oil"],
    "Notes: 2. Reduces repetitive strain injuries (RSIs).", "Body Mechanics & Effleurage notes")
add(1, "Body mechanics is also called:", "Biomechanics",
    ["Table mechanics", "Kinesiology taping", "Ergonomic draping"],
    "Notes heading: Body Mechanics (Biomechanics).", "Body Mechanics & Effleurage notes")
add(1, "Per the notes, Western culture's approach to body mechanics focuses on:", "Strength and stamina",
    ["Being grounded and balanced", "Breath only", "Flexibility only"],
    "Western = strength and stamina; Eastern = balance and being grounded, which translates into strength and stamina.", "Body Mechanics & Effleurage notes")
add(1, "Per the notes, Eastern culture's approach to body mechanics focuses on:", "Balance and being grounded",
    ["Speed and force", "Heavy resistance training", "Table height"],
    "Eastern focus on balance and being grounded translates into strength and stamina.", "Body Mechanics & Effleurage notes")
add(1, "Which TWO things does the notes handout say are needed for proper body mechanics?", "Proper foot placement and weight distribution",
    ["Long nails and strong wrists", "A heated table and music", "Fast strokes and deep pressure"],
    "Notes point 5: proper foot placement and weight distribution needed.", "Body Mechanics & Effleurage notes")

# ---------- 2. Components of body mechanics ----------
add(2, "Which is one of the factors involved in maintaining proper body mechanics?", "Leverage",
    ["Lubricant choice", "Client intake", "Music volume"],
    "Factors: table mechanics, foot stance, leverage, body posture, strength, stamina, breathing, stability, groundedness/centering, balance & flexibility.", "MA1-4, slide 2")
add(2, "Which is NOT one of the listed components of body mechanics?", "Draping policy",
    ["Foot stance", "Breathing", "Groundedness/centering"],
    "Draping is part of table mechanics, but 'draping policy' is not on the body mechanics factor list.", "MA1-4, slide 2")
add(2, "Table mechanics, foot stance, leverage and body posture are all:", "Factors involved in proper body mechanics",
    ["Elements of a stroke", "Rules of draping", "Endangerment sites"],
    "The body mechanics slide lists these as factors.", "MA1-4, slide 2")
add(2, "Which list contains ONLY components of body mechanics?", "Strength, stamina, breathing, stability",
    ["Intention, touch, excursion, routine", "Genitals, gluteal cleft, breasts", "Effleurage, petrissage, friction, tapotement"],
    "Intention/touch/excursion are stroke elements; the last list is the stroke sequence.", "MA1-4, slide 2")
add(2, "Balance & flexibility and groundedness/centering are both:", "Components of body mechanics",
    ["Types of draping", "Stroke speeds", "Contraindications"],
    "Both are on the body mechanics factor list.", "MA1-4, slide 2")
add(2, "How many factors does the MA1-4 Body Mechanics slide list?", "10",
    ["4", "6", "13"],
    "Table mechanics, foot stance, leverage, body posture, strength, stamina, breathing, stability, groundedness/centering, balance & flexibility.", "MA1-4, slide 2")

# ---------- 3. Foot stances ----------
add(3, "The Bow / Archer / Lunge stance is used for:", "Long strokes, down and away from the therapist",
    ["Short, multidirectional strokes", "Turning the client", "Sitting at the head of the table"],
    "Bow-Archer-Lunge = long strokes, down and away.", "MA1-4, slide 5")
add(3, "The Horse / Warrior stance is used for:", "Short, multidirectional strokes",
    ["Long strokes down the length of the leg", "Lifting the client", "Draping the abdomen"],
    "Horse-Warrior = short, multidirectional strokes.", "MA1-4, slide 5")
add(3, "In the bow (lunge) stance, the lead foot:", "Points in the direction of the stroke",
    ["Points toward the therapist", "Is parallel to the trail foot", "Is lifted off the floor"],
    "Lead foot points in the direction of the stroke; trail foot points off to the side.", "Body Mechanics & Effleurage notes")
add(3, "In the bow stance, weight moves:", "From the trail foot to the lead foot on the stroke, and back on the return",
    ["Only onto the trail foot", "Evenly on both feet with no shift", "Onto the toes of both feet"],
    "Weight transfers from trail foot to lead foot when performing the stroke, back to trail foot on the return.", "Body Mechanics & Effleurage notes")
add(3, "In the warrior (horse) stance:", "Feet are wider than the hips and the toes point forward",
    ["One foot is far behind the other", "Feet are together", "The trail foot points off to the side"],
    "Warrior: feet wider than hips, toes forward; used for short-distance strokes like petrissage and friction.", "Body Mechanics & Effleurage notes")
add(3, "Which stance is best for petrissage and friction?", "Warrior (horse) stance",
    ["Bow (archer) stance", "Seated stance only", "Single-leg stance"],
    "Short-distance strokes such as petrissage and friction use warrior stance.", "Body Mechanics & Effleurage notes")
add(3, "Which stance is used for covering larger areas or when using effleurage?", "Bow (archer, lunge) stance",
    ["Horse (warrior) stance", "Feet-together stance", "Kneeling stance"],
    "Bow stance: covering larger areas or effleurage.", "Body Mechanics & Effleurage notes")

# ---------- 4. Table mechanics ----------
add(4, "Table mechanics is:", "Anything that has to do with equipment and client",
    ["The therapist's foot stance", "The order of massage strokes", "Cleaning the table between clients"],
    "Bold on the slide: anything that has to do with equipment & client.", "MA1-4, slide 3", True)
add(4, "Which list is table mechanics?", "Table height, client positioning, bolstering, draping",
    ["Strength, stamina, breathing, stability", "Intention, touch, pressure, depth", "Look away, re-drape, stay composed"],
    "Table mechanics involves table height, client positioning, bolstering and draping.", "MA1-4, slide 3", True)
add(4, "Bolstering falls under:", "Table mechanics",
    ["Stroke elements", "Foot stances", "Repetitive motion injuries"],
    "Table height, client positioning, bolstering and draping.", "MA1-4, slide 3")
add(4, "Table height is part of:", "Table mechanics",
    ["Excursion", "Continuity", "Intention"],
    "Table mechanics = equipment & client.", "MA1-4, slide 3")
add(4, "Which is NOT part of table mechanics?", "Rhythm",
    ["Client positioning", "Draping", "Table height"],
    "Rhythm is a stroke element.", "MA1-4, slide 3")
add(4, "Draping is listed as part of:", "Table mechanics",
    ["Principles of body mechanics", "Foot stances", "Physical fitness"],
    "Table mechanics: table height, client positioning, bolstering, draping.", "MA1-4, slide 3")

# ---------- 5. Principles of body mechanics ----------
add(5, "Which is one of the principles of body mechanics?", "Groundedness & centeredness",
    ["Intention", "Excursion", "Diaper draping"],
    "Principles: strength & stamina, breath, stability, balance & flexibility, groundedness & centeredness.", "MA1-4, slide 4")
add(5, "Per the slide, breath:", "Paces you, fuels you, centers you and connects you with the client",
    ["Should be held during deep strokes", "Only matters for the client", "Is part of table mechanics"],
    "Breath: paces you, fuels, centers you, connects you w/client.", "MA1-4, slide 4")
add(5, "Groundedness & centeredness:", "Stop you from giving your energy away",
    ["Increase the speed of your strokes", "Raise the table height", "Replace stretching"],
    "Groundedness & centeredness: stops from giving your energy away.", "MA1-4, slide 4")
add(5, "Balance & flexibility is the ability of muscle and nerve to:", "Take you from a stable static position to a dynamic one and back",
    ["Lift a client off the table", "Keep the sheet in contact with the client", "Increase blood pressure"],
    "Slide definition of balance & flexibility.", "MA1-4, slide 4")
add(5, "Per the notes, lack of strength results in:", "Early fatigue and increased risk of injury",
    ["Better palpation", "Faster strokes", "Deeper breathing"],
    "Lack of strength = early fatigue, more risk of injury, harder to assist physically challenged clients.", "Body Mechanics & Effleurage notes")
add(5, "Per the notes, stamina (endurance) is improved with:", "Cardiovascular training about 3 times a week",
    ["Push-ups only", "Longer sessions", "Holding your breath"],
    "Stamina: enough for all your clients in a day; improve with CV training 3x a week.", "Body Mechanics & Effleurage notes")
add(5, "The notes compare stability to:", "A pogo stick vs. a tripod",
    ["A hammer vs. a nail", "A river vs. a lake", "A bow vs. an arrow"],
    "Need a stable base to work from: compare a pogo stick and a tripod.", "Body Mechanics & Effleurage notes")
add(5, "Per the notes, balance is the:", "Ability to work against gravity",
    ["Order of the strokes", "Distance traveled into the tissue", "Length of the stroke"],
    "Balance: ability to work against gravity.", "Body Mechanics & Effleurage notes")

# ---------- 6. Tools of the trade ----------
add(6, "Which is one of the things you need to do your job?", "A massage table",
    ["A blood pressure prescription", "A stethoscope", "A gait belt"],
    "What do you need to do your job: massage table, face cradle/bolsters/pillows, stool, oils/lotions/creams, linens, music & lighting, storage etc.", "MA1-14, slide 3")
add(6, "Which list is ALL tools of the trade?", "Face cradle, bolsters, linens, massage oil, stool",
    ["Scalpel, gauze, splint, ice, cast", "Gait belt, cane, walker, crutches, brace", "Microscope, slides, gloves, mask, gown"],
    "Tools of the trade slide.", "MA1-14, slide 3")
add(6, "Linens should be twin sheets, blankets and towels in quantities:", "Enough to change between clients",
    ["One set per day", "Only when visibly dirty", "One set per week"],
    "Linens: enough to change between clients.", "MA1-14, slide 3")
add(6, "Music and lighting are listed as tools for:", "Ambiance",
    ["Draping", "Body mechanics", "Assessment"],
    "Music & lighting (ambiance).", "MA1-14, slide 3")
add(6, "The stool on the tools list is for:", "You to sit on",
    ["The client to step up on", "Holding oils", "Elevating the client's feet"],
    "Stool: for you to sit on (sit when appropriate is also an element of proper body mechanics).", "MA1-14, slide 3")
add(6, "Besides buying linens, the tools slide asks you to plan:", "How you will wash your linens, towels and blankets",
    ["Which client gets the newest sheets", "How to avoid using towels", "Where to buy disposable sheets"],
    "How are you going to wash your linens, towels, blankets.", "MA1-14, slide 3")
add(6, "Which item is on the 'what do you need to do your job' list?", "Massage oils, lotions and creams",
    ["Muscle relaxant pills", "Heating pads only", "A treadmill"],
    "Oils, lotions & creams.", "MA1-14, slide 3")

# ---------- 7. Define draping ----------
add(7, "Draping is defined as:", "To cover the body with cloth",
    ["To wrap a joint for support", "To position the client with bolsters", "To change the sheets between clients"],
    "Draping: 'To cover the body with cloth.'", "MA1-4, slide 10")
add(7, "'To cover the body with cloth' is the definition of:", "Draping",
    ["Bolstering", "Table mechanics", "Continuity"],
    "Draping definition.", "MA1-4, slide 10")
add(7, "Which are the 2 types of draping?", "Sheet draping and towel draping",
    ["Diaper draping and swaddle draping", "Top draping and side draping", "Wet draping and dry draping"],
    "2 types of draping: sheet and towel.", "MA1-4, slide 16")
add(7, "The NYIM Draping Policy defines draping as being:", "Covered with sheets",
    ["Covered with towels only", "Left uncovered to stay cool", "Covered with blankets only"],
    "Policy item 1: draped (covered) with sheets at all times.", "Draping Policy handout")
add(7, "Draping covers the client's body with cloth so that:", "Only the area being massaged is exposed",
    ["The whole body is exposed for assessment", "The therapist can work through the sheet only", "The client stays fully clothed"],
    "Expose only the area being massaged.", "MA1-4, slide 15")

# ---------- 8. What draping does ----------
add(8, "Draping gives:", "Therapist professionalism, client modesty and boundaries",
    ["Deeper pressure and faster strokes", "A diagnosis and treatment plan", "Lubrication and warmth only"],
    "Draping gives: therapist professionalism, client's modesty, boundaries.", "MA1-4, slide 10")
add(8, "Why drape? (3 reasons on the slide)", "Maintains privacy, offers warmth, establishes a boundary",
    ["Saves oil, keeps sheets clean, speeds the session", "Hides posture, prevents gait problems, lowers BP", "Required for chair massage only"],
    "Why DRAPE: privacy, warmth, boundary between client and therapist.", "MA1-4, slide 11")
add(8, "Draping establishes a boundary between:", "The client and the therapist",
    ["The table and the floor", "The front and back of the body", "The clinic and the school"],
    "Establishes a boundary between the client & therapist.", "MA1-4, slide 11")
add(8, "For the therapist, draping provides:", "Professionalism",
    ["Modesty", "Warmth", "Faster sessions"],
    "Therapist professionalism; client modesty.", "MA1-4, slide 10")
add(8, "For the client, draping provides:", "Modesty",
    ["Professionalism", "Stamina", "Leverage"],
    "Clients modesty.", "MA1-4, slide 10")
add(8, "Which is NOT a reason to drape?", "To let the therapist work faster",
    ["Maintains the client's privacy", "Offers warmth", "Establishes a boundary"],
    "Privacy, warmth, boundary.", "MA1-4, slide 11")

# ---------- 9. Warmth ----------
add(9, "The primary comfort consideration when draping is:", "Warmth",
    ["Sheet color", "Speed of the session", "Music"],
    "Primary comfort consideration is warmth.", "MA1-4, slide 12")
add(9, "Why does warmth matter more as the session goes on?", "The relaxed client shifts to a parasympathetic state, and body temperature and BP may drop",
    ["The client becomes sympathetic and starts sweating", "The oil cools the table", "Blood pressure rises sharply"],
    "As the client relaxes into parasympathetic, body temperature and BP may drop.", "MA1-4, slide 12")
add(9, "As a client relaxes during massage, they shift into a:", "Parasympathetic state",
    ["Sympathetic state", "Fight-or-flight state", "Hypertensive state"],
    "Parasympathetic = rest and digest.", "MA1-4, slide 12")
add(9, "When should you check the client's comfort with warmth?", "Before and during the therapy",
    ["Only after the session", "Only if they complain", "Never; it interrupts the massage"],
    "Check with the client before & during the therapy for comfort.", "MA1-4, slide 12")
add(9, "Warmth provides the client with:", "Comfort",
    ["Modesty", "A diagnosis", "Deeper pressure"],
    "Warmth is the primary comfort consideration.", "MA1-4, slide 12")
add(9, "In a parasympathetic state, which may drop?", "Body temperature and blood pressure",
    ["Heart rate only rises", "Muscle tone rises", "Breathing speeds up"],
    "Body temperature & blood pressure may drop.", "MA1-4, slide 12")

# ---------- 10. Rules of draping ----------
add(10, "Local laws regarding draping are:", "The minimum draping standard; you CANNOT use less",
    ["The maximum allowed", "Optional if the client agrees", "Only for clinic shifts"],
    "Bold: you CANNOT use less than local law.", "MA1-4, slide 14", True)
add(10, "Which is a rule of draping?", "Don't lift, fluff or move sheets away from the client",
    ["Lift the sheet high to check the client", "Fluff the sheet to warm it", "Remove the sheet for back work"],
    "Bold on the slide: don't lift, fluff, or move sheets away from the client.", "MA1-4, slide 15", True)
add(10, "If you accidentally expose a client:", "Look away, re-drape, stay composed",
    ["Stop the massage and apologize at length", "Pretend it didn't happen and keep going", "Ask the client to fix the sheet"],
    "If you expose: look away, re-drape, STAY COMPOSED.", "MA1-4, slide 15")
add(10, "Which rule is about the sheet itself?", "Keep the sheet in contact with the client",
    ["Keep the sheet tucked under the table", "Hold the sheet above the client", "Use a different sheet for each body part"],
    "Keep the sheet in contact with the client.", "MA1-4, slide 14")
add(10, "Whose comfort and requests do the draping rules say to honor?", "The client's requests and the therapist's comfort level",
    ["Only the clinic supervisor's", "Only the client's family", "Neither; follow the routine"],
    "Honor client's request; respect therapist's comfort level.", "MA1-4, slide 14")
add(10, "Which part of the body is exposed during massage?", "Only the area being massaged",
    ["The whole back and glutes", "Anything the therapist chooses", "Both legs at once"],
    "Expose only the area being massaged.", "MA1-4, slide 15")
add(10, "Which is NOT a rule of draping?", "Use less draping than local law if the client asks",
    ["Follow local laws", "Expose only the area being massaged", "Keep the sheet in contact with the client"],
    "Local law is the minimum; you cannot use less.", "MA1-4, slide 14", True)

# ================= Study guide "MA1-6" (deck MA1-5) =================

# ---------- 11. Stroke elements ----------
add(11, "The elements of strokes are:", "The blend of body mechanics, intention, touch, pressure, depth, direction, excursion, speed, rhythm, continuity, duration, sequence and routine",
    ["Effleurage, petrissage, friction, tapotement and vibration", "Table height, positioning, bolstering and draping", "Strength, stamina, breath and stability"],
    "Giving a massage is more than rubbing skin; it is a blend of these elements.", "MA1-5, slide 2")
add(11, "Which is a stroke element?", "Excursion",
    ["Effleurage", "Bolstering", "Diaper draping"],
    "Effleurage is a stroke in the sequence, not an element.", "MA1-5, slide 2")
add(11, "Per the slides, giving a massage is:", "More than just putting your hands on someone and rubbing their skin",
    ["Mainly about pressure", "Only about the routine", "The same for every client"],
    "Opening line of Elements of Strokes.", "MA1-5, slide 2")
add(11, "Which list contains ONLY stroke elements?", "Intention, touch, depth, rhythm",
    ["Effleurage, friction, vibration, tapotement", "Privacy, warmth, boundaries, modesty", "Strength, stamina, balance, stability"],
    "Stroke elements list.", "MA1-5, slide 2")
add(11, "Which is NOT one of the elements of strokes?", "Bolstering",
    ["Speed", "Continuity", "Duration"],
    "Bolstering is table mechanics.", "MA1-5, slide 2")
add(11, "The notes say massage is:", "An art and a science, and application of the elements varies session to session",
    ["Purely a science with fixed elements", "Purely an art with no rules", "The same routine every time"],
    "Elements of a Stroke: massage is an art and a science.", "Body Mechanics & Effleurage notes")
add(11, "Which element is listed FIRST in the blend?", "Body mechanics",
    ["Routine", "Touch", "Sequence"],
    "The list begins with body mechanics and ends with routine.", "MA1-5, slide 2")

# ---------- 12. #1 reason people leave ----------
add(12, "What is the number 1 reason people leave the massage therapy industry?", "Repetitive motion injuries",
    ["Low pay", "Difficult clients", "Failing the licensing exam"],
    "Repetitive motion injuries: the number 1 reason people leave the industry.", "MA1-4, slide 7")
add(12, "Why do repetitive motion injuries happen?", "They are self-inflicted from POOR body mechanics",
    ["Clients pass them to therapists", "They come from using too much oil", "They are caused by draping"],
    "Self-inflicted injuries related to POOR body mechanics.", "MA1-4, slide 7")
add(12, "Repetitive strain injuries are described as:", "Overuse injuries that are cumulative in nature",
    ["Sudden one-time traumas", "Contagious conditions", "Allergic reactions"],
    "Notes: overuse injuries, cumulative in nature.", "Body Mechanics & Effleurage notes")
add(12, "Which is a repetitive motion injury listed on the slide?", "Carpal tunnel syndrome",
    ["Plantar wart", "Sciatica from sitting", "Scoliosis"],
    "Carpal tunnel, tennis elbow, thoracic outlet syndrome, rotator cuff strain, tendonitis.", "MA1-4, slide 7")
add(12, "Which is NOT listed as a repetitive motion injury?", "Ankle sprain",
    ["Tennis elbow", "Thoracic outlet syndrome", "Rotator cuff strain"],
    "List: carpal tunnel, tennis elbow, TOS, rotator cuff strain, tendonitis.", "MA1-4, slide 7")
add(12, "The best way to stay in the field long-term is to:", "Use good body mechanics",
    ["Work faster to see more clients", "Use only deep pressure", "Skip stretching to save time"],
    "Poor body mechanics cause the RSIs that drive people out.", "MA1-4, slide 7")

# ---------- 13. What must stay covered ----------
add(13, "Which areas MUST always stay draped?", "Genital region, gluteal cleft and breast area",
    ["Feet, hands and face", "Back, shoulders and neck", "Abdomen and thighs only"],
    "Underlined: MUST stay draped.", "MA1-4, slide 13", True)
add(13, "In the NYIM clinic, the breast area stays draped for:", "BOTH men and women",
    ["Women only", "Men only", "Only clients who ask"],
    "Bold: in clinic breast area of BOTH men & women WILL STAY DRAPED.", "MA1-4, slide 13", True)
add(13, "Which is one of the 3 areas that must always remain covered?", "Gluteal cleft",
    ["Lower back", "Upper thigh", "Abdomen"],
    "Genital region, gluteal cleft, breast area.", "MA1-4, slide 13", True)
add(13, "When draping the abdomen, what is added over the breasts?", "A towel or pillowcase",
    ["Nothing; the sheet is folded down", "A bolster", "The client's own clothing"],
    "Use a towel or pillowcase over the breasts when draping the abdomen.", "MA1-4, slide 16")
add(13, "A male client in the NYIM clinic asks to leave his chest uncovered. You:", "Keep the chest draped; clinic rule covers both men and women",
    ["Uncover it since he asked", "Ask the supervisor to uncover it", "Drape only the abdomen"],
    "In clinic the breast area of both men and women stays draped.", "MA1-4, slide 13", True)
add(13, "Which area is NOT on the 'must stay draped' list?", "Upper back",
    ["Genital region", "Gluteal cleft", "Breast area"],
    "Only genitals, gluteal cleft and breast area.", "MA1-4, slide 13", True)

# ---------- 14. Intention ----------
add(14, "Intention means:", "The consciously sought goal or desired end of the massage",
    ["The order of the strokes", "The length of the stroke", "The force applied to the body"],
    "Intention: consciously sought GOAL or desired end; what is your PURPOSE.", "MA1-5, slide 3")
add(14, "Intention underlies:", "All components of the massage session",
    ["Only the first stroke", "Only draping", "Only the intake"],
    "Underlies all components of the massage session.", "MA1-5, slide 3")
add(14, "Which question captures intention?", "What is your purpose?",
    ["How long is the stroke?", "How fast are you moving?", "Which stroke comes next?"],
    "What is your PURPOSE.", "MA1-5, slide 3")
add(14, "Per the notes, intention is based on:", "A plan of action that meets the wants and needs of the client",
    ["The therapist's favorite routine", "The time left in the session", "The table height"],
    "Intention: based on a plan of action; should meet the wants/needs of the client.", "Body Mechanics & Effleurage notes")
add(14, "Per the notes, all other stroke elements are dependent on:", "Intention",
    ["Speed", "Duration", "Sequence"],
    "All other elements are dependent on intention.", "Body Mechanics & Effleurage notes")
add(14, "'Consciously sought goal or desired end' describes:", "Intention",
    ["Routine", "Continuity", "Touch"],
    "Intention definition.", "MA1-5, slide 3")

# ---------- 15. Direction ----------
add(15, "Massage movements should move:", "Centripetally, toward the center/heart",
    ["Centrifugally, away from the heart", "Side to side only", "In whatever direction feels best"],
    "Direction: centripetal, toward the center/heart.", "MA1-5, slide 5")
add(15, "Centripetal strokes follow the direction of:", "Venous and lymphatic circulation",
    ["Arterial flow away from the heart", "Nerve impulses to the fingers", "Hair growth"],
    "In the direction of venous & lymphatic circulation.", "MA1-5, slide 5")
add(15, "On the arm, a centripetal stroke moves from:", "The hand toward the shoulder",
    ["The shoulder toward the hand", "Side to side across the forearm", "The elbow outward in both directions"],
    "Toward the heart = distal to proximal on a limb.", "MA1-5, slide 5")
add(15, "'Centripetal' means:", "Toward the center",
    ["Away from the center", "In circles", "Across the fibers"],
    "Centripetal = toward the center/heart.", "MA1-5, slide 5")
add(15, "Per the notes, effleurage on the extremities is applied:", "Centripetally (toward the heart)",
    ["Centrifugally (away from the heart)", "Only across the muscle", "Only at the joints"],
    "Effleurage is applied on the extremities centripetally.", "Body Mechanics & Effleurage notes")
add(15, "Why do strokes move toward the heart?", "To follow venous and lymphatic flow",
    ["To push blood into the fingers", "To keep the sheet in place", "To make the stroke shorter"],
    "Direction of venous & lymphatic circulation.", "MA1-5, slide 5")

# ---------- 16. Excursion ----------
add(16, "Which stroke element is related to stance, foot placement and the length of the stroke?", "Excursion",
    ["Rhythm", "Intention", "Duration"],
    "Excursion: length of the massage stroke; related to stance & foot placement.", "MA1-5, slide 5")
add(16, "Excursion is:", "The length of the massage stroke, the distance traveled",
    ["The time spent on an area", "The force applied", "The order of the strokes"],
    "Length of the massage stroke / distance traveled.", "MA1-5, slide 5")
add(16, "Excursion is dependent on:", "Proper foot placement",
    ["The type of lubricant", "The client's blood pressure", "The music"],
    "Notes: excursion is dependent on proper foot placement.", "Body Mechanics & Effleurage notes")
add(16, "A long stroke from ankle to hip has a large:", "Excursion",
    ["Depth", "Duration", "Intention"],
    "Excursion = distance covered.", "MA1-5, slide 5")
add(16, "Which stance gives you a long excursion?", "Bow / lunge stance",
    ["Horse / warrior stance", "Feet together", "Sitting on the stool"],
    "Bow = long strokes; excursion is tied to stance.", "MA1-4, slide 5")
add(16, "'Distance covered with a massage stroke' defines:", "Excursion",
    ["Depth", "Pressure", "Sequence"],
    "Depth is distance INTO the tissue; excursion is distance ALONG the body.", "Body Mechanics & Effleurage notes")

# ---------- 17. Continuity ----------
add(17, "Continuity is:", "The uninterrupted flow of strokes and unbroken transitions between them",
    ["The repetition or regularity of strokes", "The order of strokes", "The time spent on an area"],
    "Continuity: uninterrupted flow, unbroken transitions.", "MA1-5, slide 7")
add(17, "To keep continuity as you flow around the body, you:", "Keep contact with the client",
    ["Lift your hands between each body part", "Stop to add oil often", "Change speed with every stroke"],
    "Flow around the body: KEEPING CONTACT.", "MA1-5, slide 7")
add(17, "Rhythm vs. continuity:", "Rhythm = regularity of strokes; continuity = unbroken transitions between strokes",
    ["Rhythm = order of strokes; continuity = length of strokes", "They mean the same thing", "Rhythm = pressure; continuity = depth"],
    "Notes: rhythm is repetition/regularity; continuity is the unbroken transition from one stroke to another.", "Body Mechanics & Effleurage notes")
add(17, "'Uninterrupted flow' describes:", "Continuity",
    ["Excursion", "Duration", "Touch"],
    "Continuity definition.", "MA1-5, slide 7")
add(17, "Taking your hands off the client between strokes breaks:", "Continuity",
    ["Direction", "Depth", "Intention"],
    "Continuity means keeping contact.", "MA1-5, slide 7")
add(17, "Overlapping your strokes over joints to connect one body part to the next supports:", "Continuity",
    ["Excursion only", "Duration only", "Draping"],
    "Swedish guideline 5: connect body parts by overlapping strokes over joints.", "Swedish Guidelines handout")

# ---------- 18. Sequence ----------
add(18, "Sequence refers to:", "The order of the massage strokes",
    ["The length of the stroke", "The speed of the stroke", "The combination of all elements"],
    "Sequence: order of the massage strokes.", "MA1-5, slide 8")
add(18, "The stroke sequence on the slide is:", "Effleurage, petrissage, friction, tapotement, vibration, ancillary movements",
    ["Petrissage, effleurage, tapotement, friction, vibration", "Friction, vibration, effleurage, petrissage", "Tapotement, friction, petrissage, effleurage"],
    "Strokes in order: effleurage, petrissage, friction, tapotement, vibration, ancillary.", "MA1-5, slide 8")
add(18, "Which stroke usually goes first?", "Effleurage",
    ["Petrissage", "Tapotement", "Friction"],
    "Notes: effleurage usually goes first, then petrissage.", "Body Mechanics & Effleurage notes")
add(18, "Which stroke comes right after effleurage?", "Petrissage",
    ["Vibration", "Tapotement", "Ancillary movements"],
    "Effleurage, then petrissage.", "MA1-5, slide 8")
add(18, "Which comes LAST in the stroke sequence?", "Ancillary movements",
    ["Effleurage", "Friction", "Petrissage"],
    "Sequence ends with vibration, then ancillary movements.", "MA1-5, slide 8")
add(18, "'The arrangement of massage strokes' is:", "Sequence",
    ["Routine", "Rhythm", "Continuity"],
    "Notes: sequence = arrangement of massage strokes.", "Body Mechanics & Effleurage notes")

# ---------- 19. Where pressure comes from ----------
add(19, "Where does your pressure come from?", "Your own body weight, leaning in from the hara",
    ["Your thumbs and wrists", "Pushing with your shoulders", "Squeezing with your fingers"],
    "Use your own body weight. Lean in: pressure from the hara.", "MA1-5, slide 4")
add(19, "To get depth, the slide says to:", "Lean in and use your own body weight",
    ["Lock your elbows and push with your arms", "Raise the table", "Speed up the stroke"],
    "Use your own body weight; lean in.", "MA1-5, slide 4")
add(19, "The hara (dan-tien) is the body's:", "Center of gravity, near L4-L5 in front of the spine",
    ["Highest point of the shoulder", "Base of the skull", "Arch of the foot"],
    "Notes: center of gravity called the dan-tien, at L4-L5 anterior to the spine; center of physical and spiritual balance.", "Body Mechanics & Effleurage notes")
add(19, "'Work from hara' is listed as:", "An element of proper body mechanics",
    ["A rule of draping", "A type of stroke", "A contraindication"],
    "Elements of proper body mechanics include work from hara.", "MA1-4, slide 8")
add(19, "Which is the WRONG way to create pressure?", "Muscling it with your hands and thumbs",
    ["Leaning in with body weight", "Moving from the hara", "Shifting weight onto the lead foot"],
    "Pressure comes from body weight and hara, not hand strength.", "MA1-5, slide 4")
add(19, "Per the notes, who ultimately controls depth?", "The client, by guarding/tensing or relaxing and letting you in",
    ["The therapist alone", "The clinic supervisor", "The table height"],
    "Ultimately the client controls depth.", "Body Mechanics & Effleurage notes")

# ---------- 20. Routine ----------
add(20, "What is it called when you put all the elements together?", "The routine",
    ["The sequence", "Continuity", "Intention"],
    "Bold: Routine = combination of all these ELEMENTS!!!", "MA1-5, slide 8", True)
add(20, "Routine is:", "The combination of all the stroke elements",
    ["The order of strokes only", "The time spent on one area", "The length of one stroke"],
    "Routine: combination of all these elements.", "MA1-5, slide 8", True)
add(20, "Per the notes, routines:", "Can change with every massage",
    ["Must be identical every session", "Never include effleurage", "Only apply to chair massage"],
    "Routine: the union of all other elements; routines can change with every massage.", "Body Mechanics & Effleurage notes")
add(20, "Sequence vs. routine:", "Sequence = order of strokes; routine = all elements combined",
    ["They mean the same thing", "Routine = order of strokes; sequence = all elements", "Sequence = pressure; routine = speed"],
    "Don't mix these up on the quiz.", "MA1-5, slide 8", True)
add(20, "'The union of all the other elements' describes:", "Routine",
    ["Rhythm", "Excursion", "Depth"],
    "Notes: the routine is the union of all the other elements.", "Body Mechanics & Effleurage notes")
add(20, "Which stroke element is listed LAST?", "Routine",
    ["Sequence", "Duration", "Intention"],
    "Routine is last because it combines everything.", "MA1-5, slide 2")

# ================= Also on the slides / handouts =================

# ---------- 21. Touch, pressure, depth ----------
add(21, "Touch is described as:", "The medium of the massage; your opening and ending move",
    ["The order of the strokes", "The force applied to the body", "The length of the stroke"],
    "Touch: the medium of the massage; to begin & end the session.", "MA1-5, slide 3")
add(21, "Pressure is:", "Force applied to the surface of the body",
    ["Distance traveled into the tissue", "Length of the stroke", "Time spent on an area"],
    "Pressure definition.", "MA1-5, slide 4")
add(21, "Depth is:", "Distance traveled into the body's tissue",
    ["Force applied to the skin", "Length of the stroke", "Number of strokes"],
    "Depth: distance traveled into the tissue; achieved by level of pressure.", "MA1-5, slide 4")
add(21, "The pressure pattern through a session is:", "Begin light, gradually increase, deeper specific work, gradually decrease",
    ["Deep from start to finish", "Begin deep, then light", "Light the whole time"],
    "Pressure progression on the slide.", "MA1-5, slide 4")
add(21, "Depth varies from:", "Light, medium, deep",
    ["Fast, slow, still", "Short, long, circular", "Supine, prone, side-lying"],
    "Light, medium, deep.", "MA1-5, slide 4")
add(21, "Per the notes, it's usually good to begin a session at the:", "Head, feet or back",
    ["Abdomen", "Gluteals", "Inner thigh"],
    "Touch: usually good to begin at the head, feet or back; a physical introduction.", "Body Mechanics & Effleurage notes")

# ---------- 22. Speed and rhythm ----------
add(22, "Speed is based on:", "The purpose of the massage",
    ["The client's height", "The table width", "The type of oil"],
    "Bold on the slide: based on the purpose.", "MA1-5, slide 6", True)
add(22, "Rapid strokes are:", "Stimulating",
    ["Relaxing", "Sedating", "Always contraindicated"],
    "Rapid = stimulating; slow = relaxing.", "MA1-5, slide 6", True)
add(22, "Slow strokes are:", "Relaxing",
    ["Stimulating", "Alarming", "Only for athletes"],
    "Slow = relaxing.", "MA1-5, slide 6", True)
add(22, "Rhythm is:", "The repetition or regularity of massage movements",
    ["The unbroken transition between strokes", "The order of strokes", "The distance into the tissue"],
    "Rhythm definition.", "MA1-5, slide 7")
add(22, "Rhythm is affected by:", "Excursion, speed, pressure and intention",
    ["Table height, sheets, bolsters and music", "Gluteal cleft, genitals and breasts", "Only the client's mood"],
    "Affected by excursion, speed, pressure, intention/purpose.", "MA1-5, slide 7")
add(22, "Per the notes, strokes that are too fast:", "Can alarm and fatigue the client, and you can't palpate well",
    ["Always relax the client", "Improve palpation", "Are required at NYIM"],
    "Too quick can alarm; fast strokes can fatigue; can't palpate if too fast or too slow.", "Body Mechanics & Effleurage notes")

# ---------- 23. Duration and timing ----------
add(23, "Duration is:", "Length of time spent on an area or the whole massage",
    ["The order of the strokes", "The length of a stroke", "The force of a stroke"],
    "Duration definition.", "MA1-5, slide 8")
add(23, "Per the Basic Timing handout, head, neck and shoulders get:", "10-15 minutes",
    ["5 minutes", "30 minutes", "2 minutes"],
    "Supine: head, neck & shoulders 10-15 min.", "Basic Timing handout")
add(23, "Per the Basic Timing handout, the back gets:", "10-15 minutes",
    ["5 minutes each side", "20-25 minutes", "3 minutes"],
    "Prone: back 10-15 min.", "Basic Timing handout")
add(23, "Arms and hands, legs and feet, and legs and glutes each get:", "5 minutes on each side",
    ["10-15 minutes each side", "1 minute each side", "15 minutes total"],
    "5 minutes on each side.", "Basic Timing handout")
add(23, "In the basic timing order, the client starts:", "Supine, then turns prone",
    ["Prone, then turns supine", "Seated the whole time", "Side-lying"],
    "Supine: head/neck/shoulders, arms, legs. Turn prone: legs & glutes, back.", "Basic Timing handout")
add(23, "What decides how much time a body part gets?", "The discomfort or condition of the muscle tissue; more time on one area means less elsewhere",
    ["The therapist's favorite area", "Always equal time everywhere", "The order on the intake form"],
    "Handout note under the timing table.", "Basic Timing handout")

# ---------- 24. Swedish guidelines ----------
add(24, "General Swedish massage guideline: work from:", "General to specific, then back to general",
    ["Specific to general only", "The feet to the head always", "Deep to light"],
    "Guideline 1.", "Swedish Guidelines handout")
add(24, "Swedish guideline on pressure: work from:", "Light stroking to gradually deeper work, then back to lighter",
    ["Deep work first, then light", "Light only", "Deep only"],
    "Guideline 2.", "Swedish Guidelines handout")
add(24, "'Be thorough. Be complete.' means:", "Cover every square inch",
    ["Repeat each stroke 10 times", "Spend most time on the back", "Use every stroke on every body part"],
    "Guideline 3.", "Swedish Guidelines handout")
add(24, "Swedish guidelines say to work with your own:", "Weight and breath",
    ["Hand strength", "Speed", "Thumbs"],
    "Guideline 4: work with your own weight and breath.", "Swedish Guidelines handout")
add(24, "How deep should you work, per the guidelines?", "Deeply enough to contact and release tension",
    ["As deep as possible", "Only on the surface", "Until the client says stop"],
    "Guideline 6.", "Swedish Guidelines handout")
add(24, "The last Swedish guideline is:", "Stay with yourself. Stay centered. Stay grounded.",
    ["Finish with tapotement", "Always end at the feet", "Ask for feedback every minute"],
    "Guideline 7.", "Swedish Guidelines handout")

# ---------- 25. NYIM draping policy ----------
add(25, "Per the NYIM Draping Policy, students receiving massage are draped:", "With sheets at all times",
    ["Only on the back", "Only when the instructor is present", "With towels only"],
    "Policy item 1.", "Draping Policy handout")
add(25, "Walking from the dressing room to the table, the student wraps a sheet:", "Horizontally around the trunk for minimum exposure",
    ["Over the shoulders like a cape", "Around the waist only", "Not at all; robes are used"],
    "Policy item 3.", "Draping Policy handout")
add(25, "Once the client is on the table, draping responsibility shifts to:", "The student acting as the therapist",
    ["The client", "The clinic supervisor", "The front desk"],
    "Policy item 4.", "Draping Policy handout")
add(25, "When the massage is over, the student therapist should:", "Help the client stay fully covered while getting off the table",
    ["Leave the room immediately", "Remove the sheet for the client", "Ask the client to fold the sheets"],
    "Policy item 6.", "Draping Policy handout")
add(25, "The policy box stresses developing an attitude of:", "Non-judgment of physical appearance; treat every body the same",
    ["Strict silence during the session", "Speed and efficiency", "Correcting clients' posture"],
    "Box at the bottom of the policy.", "Draping Policy handout")
add(25, "To prepare, students receiving massage disrobe:", "In a bathroom or dressing room",
    ["On the massage table", "In the classroom", "Behind the therapist"],
    "Policy item 2.", "Draping Policy handout")

# ---------- 26. Sheet draping, turning, assisting ----------
add(26, "Which draping method MUST be used at NYIM?", "Diaper draping",
    ["Towel-only draping", "Top-sheet-only draping", "No draping"],
    "Underlined: DIAPER DRAPING must be used at NYIM.", "MA1-4, slide 16", True)
add(26, "Which sheets are best for draping?", "Twin size; 2 sheets required (fitted & top, or top & top)",
    ["King size; 1 sheet", "Any towel", "Full size; 3 sheets"],
    "Twin size best; 2 sheets required; fold down top sheet.", "MA1-4, slide 16")
add(26, "When turning a client at NYIM, the client turns:", "Toward you",
    ["Away from you", "Off the table first", "Without the sheet"],
    "Have client turn toward you (NYIM).", "MA1-4, slide 17")
add(26, "When turning, you anchor the sheet with your:", "Thighs, and lift the sheet on the opposite side at the shoulder and hip",
    ["Hands, lifting the whole sheet", "Elbows, pinning both sides", "Feet, on the floor"],
    "Anchor sheet with your thighs, elevate on the opposite side.", "MA1-4, slide 17")
add(26, "First step when turning a client either way:", "Remove all positioning equipment",
    ["Ask them to move into the face cradle", "Place the ankle bolster", "Remove the top sheet"],
    "Both directions start by removing positioning equipment.", "MA1-4, slide 17")
add(26, "Turning prone to supine, before the turn the client:", "Moves DOWN out of the face cradle",
    ["Moves up into the face cradle", "Sits up", "Gets a bolster under the ankles"],
    "Prone to supine: move down out of the face cradle.", "MA1-4, slide 17")
add(26, "Assisting a client on/off the table, you:", "Lift with your legs, keep boundaries, maintain modesty and ensure safety",
    ["Lift with your back to move quickly", "Let the client manage alone", "Remove the drape to see their footing"],
    "Assisting slide.", "MA1-4, slide 18")

# ---------- 27. RSIs ----------
add(27, "Which is a way to avoid RSIs?", "Use a variety of strokes",
    ["Use the same stroke all session", "Book clients back to back", "Keep sustained pressure"],
    "Avoid RSIs: vary strokes, stretch, proper table height, space clients, avoid sustained pressure, stay fit, get massages.", "Body Mechanics & Effleurage notes")
add(27, "Which does NOT help prevent RSIs?", "Sustained pressure",
    ["Stretching between sessions", "Proper table height", "Spacing out clients"],
    "Avoid sustained pressure.", "Body Mechanics & Effleurage notes")
add(27, "Which is an element of proper body mechanics?", "Brace your digits",
    ["Lock your knees", "Hold your breath", "Lift with your back"],
    "Also: check table height, warm up, vary strokes, work from hara, breathe, stretch, sit when appropriate, lift with legs, honor your limits.", "MA1-4, slide 8")
add(27, "'Honor your limits' and 'find your rhythm' are:", "Elements of proper body mechanics",
    ["Rules of draping", "Stroke sequence steps", "Swedish timing rules"],
    "Elements of proper body mechanics slide.", "MA1-4, slide 8")
add(27, "Physical fitness is:", "The ability to carry out daily tasks with enough energy left to enjoy leisure and meet emergencies",
    ["Being able to lift the table alone", "Having no body fat", "Running a mile a day"],
    "Physical fitness definition.", "MA1-4, slide 6")
add(27, "Per the notes, receiving massages regularly helps the therapist:", "Avoid RSIs",
    ["Skip warming up", "Use less draping", "Work faster"],
    "One of the ways to avoid RSIs.", "Body Mechanics & Effleurage notes")

# ---------- 28. Effleurage ----------
add(28, "Effleurage is a:", "Gliding stroke",
    ["Kneading stroke", "Percussive stroke", "Shaking stroke"],
    "Effleurage: a gliding stroke, one or two hands.", "Body Mechanics & Effleurage notes")
add(28, "Effleurage is used for:", "Introducing touch, applying lubricant, and assessing tissue",
    ["Breaking up scar tissue", "Waking the client with percussion", "Range of motion testing"],
    "Introducing touch, applying lubricant, assessing and exploring tissues.", "Body Mechanics & Effleurage notes")
add(28, "Light effleurage used to finish a body part or the session is called:", "Nerve strokes",
    ["Ironing", "Cupping", "Hacking"],
    "Nerve strokes are a light effleurage.", "Body Mechanics & Effleurage notes")
add(28, "Deep effleurage is also called:", "Ironing",
    ["Nerve strokes", "Wringing", "Tapping"],
    "Deep effleurage = ironing.", "Body Mechanics & Effleurage notes")
add(28, "With effleurage on the extremities, you work:", "Proximal, then distal",
    ["Distal only", "Across the joint only", "Away from the heart"],
    "Work proximal then distal on the extremities; strokes go toward the heart.", "Body Mechanics & Effleurage notes")
add(28, "During effleurage, pressure on the return (dragging hands back) is:", "Less than on the applied stroke",
    ["More than the applied stroke", "Equal to the applied stroke", "Zero, with hands lifted off"],
    "Less pressure when dragging hands back.", "Body Mechanics & Effleurage notes")
add(28, "Which is a benefit of effleurage?", "Increases blood and lymph flow",
    ["Raises blood pressure", "Causes insomnia", "Increases congestion"],
    "Benefits: warms tissues, relaxing, soothing, flushes congestion, passive stretch, blood & lymph flow, relieves insomnia.", "Body Mechanics & Effleurage notes")

c = {}
for q in Q:
    c[q["topic"]] = c.get(q["topic"], 0) + 1
for t in TOPICS:
    assert c.get(t, 0) >= 4, (t, c.get(t, 0))

QUIZ = {"id": "q3", "title": "MA1 Quiz #3", "lectures": "Class 5–6 (week 3)",
        "blurb": "Body mechanics, foot stances, table mechanics, tools of the trade, draping and the draping policy, stroke elements, Swedish guidelines and session timing, effleurage.",
        "sgNote": "1–10 are the \"MA1-5\" study guide (Body Mechanics, Tools, Draping), 11–20 are the \"MA1-6\" study guide (Stroke Elements, Draping Review). Slides cited are decks MA1-4 and MA1-5.",
        "studyGuideTopics": STUDY_GUIDE_TOPICS, "topics": TOPICS, "questions": Q}
