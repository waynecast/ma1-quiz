# Builds questions.json for the MA1 Quiz #1 practice app.
# Per question: topic, q (prompt), a (correct answer), w (3 wrong answers), e (explanation), s (source), f (flagged on slides)
# f=True when the fact is starred, red, highlighted, or set apart on the slide. Flagged facts are drawn more often.
import json

TOPICS = {
    1: "Define pathogen",
    2: "Agent of disease most likely encountered",
    3: "What Universal Precautions are / who they protect",
    4: "When to wear gloves",
    5: "Disinfection vs. sterilization",
    6: "Primary source of cross-contamination",
    7: "Handwashing: key element and time",
    8: "Define hygiene",
    9: "Define massage",
    10: "Benefits of massage",
    11: "First culture to document massage",
    12: "Amma",
    13: "Shiatsu",
    14: "Symbol of medicine (Aesculapius)",
    15: "Father of Western medicine",
    16: "William Harvey",
    17: "Father of Swedish massage",
    18: "Describe Swedish massage",
    19: "Swedish stroke terminology (Mezger)",
    20: "Swedish massage comes to the U.S.",
    21: "3 types of professional communication",
    22: "Informed consent",
    23: "SOAP: the 4 record categories",
    24: "What is a symptom",
    25: "Short-term vs. long-term goals",
    26: "SUDS",
    27: "Where/when to review medical history",
    28: "Correcting a SOAP note mistake",
    29: "Systolic blood pressure",
    30: "Diastolic blood pressure",
    31: "Most honest form of communication",
    32: "Clinic BP cutoff and procedure",
    33: "Review: nails, soiled linens, lubricant",
    34: "Glove types and glove use",
    35: "Bacteria, viruses, protozoa, parasites",
    36: "Sanitation and safety guidelines",
    37: "More massage history",
    38: "OH PAIN, intake, and aftercare",
}
STUDY_GUIDE_TOPICS = list(range(1, 34))  # 1-32 = study guide questions in order, 33 = its review line

Q = []
def add(t, q, a, w, e, s, f=False):
    assert len(w) == 3, q
    assert a not in w, q
    assert len(set(w)) == 3, q
    Q.append({"topic": t, "q": q, "a": a, "w": w, "e": e, "s": s, "f": f})

# ---------- 1. Pathogen ----------
add(1, "A pathogen is defined as:", "A biological agent capable of causing disease",
    ["An inanimate object that carries disease", "The reproductive unit of a fungus", "A chemical used to disinfect surfaces"],
    "Pathogen = biological agent capable of causing disease.", "MA1-1, slide 25")
add(1, "Which of these is NOT a type of pathogen listed in the lecture?", "Fomites",
    ["Bacteria", "Fungi", "Viruses"],
    "Pathogens: bacteria, fungi, viruses, protozoa, animal parasites. A fomite is an object that carries them.", "MA1-1, slides 25, 26")
add(1, "Bacteria, fungi, viruses and animal parasites are all examples of:", "Pathogens",
    ["Fomites", "Spores", "Endangerment sites"],
    "These are the agents that cause disease (pathogens).", "MA1-1, slide 25")
add(1, "A massage table, a shared towel, or a door handle that carries disease is called a:", "Fomite",
    ["Pathogen", "Vector", "Spore"],
    "Fomite = inanimate object that transmits disease.", "MA1-1, slide 26")
add(1, "Which term means 'a biological agent capable of causing disease'?", "Pathogen",
    ["Antibody", "Antiseptic", "Fomite"],
    "Pathogen is the lecture's definition word.", "MA1-1, slide 25")

# ---------- 2. Most likely agent ----------
add(2, "Which agent of disease is a massage therapist MOST likely to be exposed to?", "Fungi (ringworm/tinea)",
    ["Viruses", "Bacteria", "Protozoa"],
    "Slide callout: fungi are the most common pathogen massage therapists will be exposed to.", "MA1-1, slide 27", True)
add(2, "The most common pathogen massage therapists will be exposed to is:", "Ringworm (tinea), a fungus",
    ["Herpes simplex, a virus", "Staph, a bacterium", "Scabies, a parasite"],
    "Fungi, especially tinea (ringworm).", "MA1-1, slide 27", True)
add(2, "Fungi thrive in which environment?", "Warm and moist",
    ["Cold and dry", "Hot and dry", "Cold and moist"],
    "Fungal agents (molds and yeast) thrive in warm, moist environments.", "MA1-1, slide 27")
add(2, "Fungal infections are generally transmitted by:", "A fomite (inanimate object)",
    ["Insect bites", "Contaminated water only", "Sexual contact only"],
    "Generally by a fomite; can also spread via touch.", "MA1-1, slide 27")
add(2, "Tinea pedis is commonly known as:", "Athlete's foot",
    ["Jock itch", "Ringworm of the scalp", "Ringworm of the nails"],
    "Pedis = foot.", "MA1-1, slide 27")
add(2, "Tinea capitis (ringworm of the head) is most common in:", "Children",
    ["Men and adolescent boys", "The elderly", "Pregnant women"],
    "Capitis is most common in children; cruris (jock itch) in men and adolescent boys.", "MA1-1, slide 27")
add(2, "Tinea unguium affects the:", "Nails (toenails more often than fingernails)",
    ["Beard and chin", "Groin", "Scalp"],
    "Unguium = nails.", "MA1-1, slide 27")
add(2, "Fungal infections are described as:", "Superficial, tenacious and difficult to eradicate",
    ["Deep, mild and easy to cure", "Only spread by blood", "Not contagious"],
    "Superficial, tenacious, hard to eradicate, very contagious, 2-3 week incubation.", "MA1-1, slide 27")

# ---------- 3. Universal Precautions ----------
add(3, "Universal Precautions protect:", "Both the client and the therapist",
    ["Only the client", "Only the therapist", "Only clients in medical settings"],
    "They protect client AND therapist from disease transmission.", "MA1-1, slides 24, 31")
add(3, "If standards and guidelines are NOT followed, who is at risk of disease or injury?", "Both the client and the therapist",
    ["Only the client", "Only the therapist", "Neither, massage is always safe"],
    "Slide 3 highlights 'DO NOT FOLLOW': both client and therapist are at risk.", "MA1-1, slide 3", True)
add(3, "Universal Precautions were established by:", "OSHA and the CDC in the early 1990s",
    ["The AMTA in 1856", "The FDA in the 1970s", "NYIM in 2000"],
    "OSHA & CDC, early 1990s.", "MA1-1, slide 31")
add(3, "The core assumption behind Universal Precautions is:", "Every individual has a potentially infectious condition",
    ["Only visibly ill clients are infectious", "Clients will disclose all infections on the intake form", "Infection only spreads through blood"],
    "Assume EVERY individual is potentially infectious.", "MA1-1, slide 24 · UP handout")
add(3, "Which is NOT one of the main principles of Universal Precautions for massage therapists?", "Prescribing medication",
    ["Sanitation", "Glove use", "Handwashing"],
    "Main principles: sanitation, hygiene, glove use, handwashing, careful handling of blood and body fluids.", "MA1-1, slide 32")
add(3, "Therapists working in which setting have a greater risk of exposure to pathogens?", "A medical setting",
    ["A spa", "A chair-massage event", "A home practice"],
    "Medical settings carry greater exposure risk.", "MA1-1, slides 24, 31")
add(3, "Which body fluid is listed as a concern under Universal Precautions?", "Synovial fluid",
    ["Tears from cutting onions", "Sweat on intact skin", "Massage oil"],
    "Listed: blood, saliva, mucus, semen, vaginal secretions, cerebrospinal, synovial, pleural, peritoneal, pericardial fluids.", "MA1-1, slide 31")

# ---------- 4. Gloves: when ----------
add(4, "A massage therapist should wear gloves when:", "The therapist or client has a break in the skin",
    ["The client has dry skin", "Using a cream instead of oil", "The client is new"],
    "Broken skin on either person calls for gloves (finger cot if only one fingertip).", "MA1-1, slide 35")
add(4, "If only the tip of one finger has a cut, the therapist can use a:", "Finger cot",
    ["Full pair of latex gloves only", "Bandage with no cover", "Hand sanitizer instead"],
    "Finger cot covers a single fingertip.", "MA1-1, slide 35")
add(4, "Gloves are recommended for hygiene reasons during:", "TMJ (intraoral) massage",
    ["Foot massage", "Back massage", "Scalp massage"],
    "TMJ work is the slide's hygiene example; the UP handout also lists examining the mouth.", "MA1-1, slide 35 · UP handout")
add(4, "Which situation calls for gloves?", "Removing linens and trash that may be contaminated with body fluids",
    ["Greeting the client", "Taking the intake history", "Adjusting the table height"],
    "Handling blood or body fluids includes possibly contaminated linens and trash.", "MA1-1, slide 35 · UP handout")
add(4, "If the client does not want you to use gloves when they are needed, you:", "Have the right to refuse the massage",
    ["Must massage without gloves", "Use extra oil instead", "Use gloves on one hand only"],
    "You may refuse to do the massage.", "MA1-1, slide 36")
add(4, "Which is TRUE about glove use?", "Wash hands before and after using gloves",
    ["Gloves replace handwashing", "Gloves improve palpation", "Gloves reduce friction on hairy skin"],
    "Wash before and after; gloves reduce palpation and add friction, especially over thick hair.", "MA1-1, slide 36 · UP handout")
add(4, "If a glove tears during a massage, you should:", "Wash your hands and put on a new glove",
    ["Finish the massage quickly", "Tape the tear", "Switch to the other hand"],
    "Damaged glove: wash hands, new glove.", "MA1-1, slide 36")

# ---------- 5. Disinfection vs sterilization ----------
add(5, "The difference between disinfection and sterilization is:", "Sterilization destroys all pathogens; disinfection may not remove spores",
    ["Disinfection destroys spores; sterilization does not", "They are the same process", "Sterilization uses only soap and water"],
    "Disinfection removes pathogens from a surface but does not always remove spores.", "MA1-1, slide 33", True)
add(5, "Which process does NOT always remove spores?", "Disinfection",
    ["Sterilization", "Autoclaving", "Baking at 350°F for 1 hour"],
    "Disinfection does not always remove spores (the reproductive unit).", "MA1-1, slide 33", True)
add(5, "Disinfection removes pathogens from a surface using:", "A chemical or mechanical agent",
    ["Steam at 15 psi", "Baking at 350°F", "Radiation only"],
    "Chemical or mechanical agent; heat/steam methods are sterilization.", "MA1-1, slide 33", True)
add(5, "Which is a method of STERILIZATION?", "Autoclave (steam) at 15 psi, 250°F for 30 minutes",
    ["Wiping with a disinfectant", "Rinsing with water", "Air drying"],
    "Sterilization: heat, water, chemicals or gases, e.g. autoclave or baking.", "MA1-1, slide 33", True)
add(5, "Dry-heat sterilization in the lecture is baking at:", "350°F for 1 hour",
    ["250°F for 10 minutes", "212°F for 5 minutes", "450°F for 3 hours"],
    "Bake at 350°F for 1 hour.", "MA1-1, slide 33", True)
add(5, "A spore is:", "The reproductive unit of a microorganism",
    ["A disinfecting chemical", "A type of glove", "A virus that causes colds"],
    "Spore = reproductive unit; may survive disinfection.", "MA1-1, slide 33")
add(5, "The UP handout says areas soiled with blood should be cleaned with disinfectant and rinsed with:", "1 part chlorine bleach to 10 parts water",
    ["1 part bleach to 100 parts water", "Plain hot water", "Rubbing alcohol only"],
    "Rinse with a 1:10 bleach solution.", "UP handout")
add(5, "'The application of measures to promote a healthful, disease-free environment' defines:", "Sanitation",
    ["Sterilization", "Hygiene", "Disinfection"],
    "Sanitation is the umbrella term.", "MA1-1, slide 33")

# ---------- 6. Primary source ----------
add(6, "The primary source of microorganism cross-contamination is:", "Human hands",
    ["Massage tables", "Air", "Linens"],
    "Contact with human hands.", "MA1-1, slide 38")
add(6, "The best way to control cross-contamination is:", "Handwashing",
    ["Wearing gloves at all times", "Using bar soap", "Changing linens weekly"],
    "Best control = HAND WASHING.", "MA1-1, slide 38", True)
add(6, "When should you wash your hands?", "Before AND after each massage",
    ["Only after each massage", "Only before the first massage of the day", "Only when hands look dirty"],
    "Slide callout: WASH HANDS BEFORE & AFTER EACH MASSAGE.", "MA1-1, slide 38", True)
add(6, "According to the UP handout, you should wash your hands:", "After removing disposable gloves",
    ["Only before putting gloves on", "Instead of wearing gloves", "Only at the end of the day"],
    "Also before/after eating, after the restroom, after any body-fluid contact.", "UP handout")

# ---------- 7. Handwashing ----------
add(7, "The most important aspect of handwashing is:", "Friction",
    ["Water temperature", "Type of towel", "Brand of soap"],
    "Friction emulsifies skin oil and removes microorganisms and dirt.", "MA1-1, slide 38", True)
add(7, "Friction during handwashing is essential because it:", "Emulsifies the oil on the skin and removes microorganisms and dirt",
    ["Warms the hands for massage", "Sterilizes the skin", "Removes the need to rinse"],
    "Friction emulsifies skin oil and lifts microbes and dirt.", "MA1-1, slide 38", True)
add(7, "The recommended time to rub soap up the forearms is:", "15-30 seconds (up to 2 minutes if needed)",
    ["5 seconds", "5 minutes", "1 hour"],
    "15-30 seconds, 2 minutes if needed.", "MA1-1, slide 38")
add(7, "When rinsing, water should run:", "From the fingers to the elbows",
    ["From the elbows to the fingers", "Only over the palms", "From the shoulders down"],
    "Fingers to elbows keeps the hands the cleanest area.", "MA1-1, slide 38")
add(7, "At the start of handwashing, the hands should be:", "Lower than the elbows",
    ["Higher than the elbows", "Level with the shoulders", "Behind the back"],
    "Start with hands lower than the elbows.", "MA1-1, slide 38")
add(7, "Which soap is preferred?", "Liquid soap",
    ["Bar soap", "Dish soap", "No soap, water only"],
    "Liquid soap is preferred over bar soap.", "MA1-1, slide 38 · UP handout")
add(7, "After drying your hands, the paper towel should be used to:", "Turn off the water and open door handles, then be discarded",
    ["Dry the massage table", "Wipe the client's feet", "Be saved for the next wash"],
    "Use the same towel for the faucet and door handles until you reach the massage area.", "MA1-1, slide 38")

# ---------- 8. Hygiene ----------
add(8, "Hygiene is best defined as:", "The science and practice of preserving health and preventing disease through cleanliness",
    ["Destroying all microorganisms with heat", "The removal of pathogens from a surface", "A biological agent capable of causing disease"],
    "Hygiene = practices that preserve health. (Not on slides; standard definition.)", "Textbook definition")
add(8, "Which is a personal hygiene guideline from the lecture?", "Keep nails short and clean",
    ["Wear rings for professionalism", "Wear a light perfume", "Chew gum to freshen breath"],
    "Short clean nails, no jewelry, no perfume, no gum.", "MA1-1, slide 39")
add(8, "Which should a massage therapist AVOID?", "Wearing perfumes and scented cosmetics",
    ["Tying back long hair", "Using mouthwash", "Showering daily"],
    "Avoid perfumes and scented cosmetics.", "MA1-1, slide 39")
add(8, "Which food does the lecture say to avoid before working with clients?", "Garlic and onions",
    ["Rice", "Bananas", "Bread"],
    "Avoid offensive foods: garlic, onions, etc.", "MA1-1, slide 39")
add(8, "Personal hygiene for therapists includes:", "No jewelry and no gum",
    ["Long nails for deeper pressure", "Smoking only before the massage", "Hair worn loose"],
    "No jewelry, no gum, no smoking around clients or before a massage.", "MA1-1, slide 39")

# ---------- 9. Definition of massage ----------
add(9, "Massage is defined as:", "Systematic and scientific manipulation of the soft tissues of the body for the purpose of obtaining or maintaining health",
    ["Random rubbing of the skin for relaxation only", "Manipulation of the bones to correct alignment", "Any touch that relieves pain"],
    "The highlighted definition on slide 4.", "MA1-1, slide 4", True)
add(9, "According to the definition, massage manipulates the:", "Soft tissues of the body",
    ["Bones of the body", "Internal organs only", "Nervous system directly"],
    "Soft tissues.", "MA1-1, slide 4", True)
add(9, "The purpose of massage in the definition is:", "Obtaining or maintaining health",
    ["Diagnosing disease", "Curing infection", "Correcting bone alignment"],
    "For the purpose of obtaining or maintaining health.", "MA1-1, slide 4", True)
add(9, "About how many types of massage and bodywork are used in the world today?", "Over 75",
    ["About 10", "Exactly 25", "Over 1,000"],
    "Over 75 types.", "MA1-1, slide 4")
add(9, "Which two words describe how massage manipulates tissue, per the definition?", "Systematic and scientific",
    ["Random and intuitive", "Fast and forceful", "Spiritual and energetic"],
    "Systematic and scientific manipulation.", "MA1-1, slide 4", True)

# ---------- 10. Benefits ----------
add(10, "Which is a general benefit of massage?", "Increases the oxygen capacity of blood",
    ["Raises blood pressure", "Cures infections", "Increases swelling"],
    "Benefits: reduce stress, enhance circulation, decrease pain, promote sleep, reduce swelling, enhance relaxation, increase blood oxygen capacity.", "MA1-1, slide 5")
add(10, "Which is NOT listed as a benefit of massage?", "Sterilizes the skin",
    ["Reduces stress", "Promotes sleep", "Reduces swelling"],
    "Sterilizing is not a massage effect.", "MA1-1, slide 5")
add(10, "Massage affects circulation by:", "Enhancing blood circulation",
    ["Stopping blood flow", "Thickening the blood", "Lowering oxygen in blood"],
    "Enhance blood circulation.", "MA1-1, slide 5")
add(10, "Which set lists only benefits of massage?", "Decrease pain, promote sleep, enhance relaxation",
    ["Decrease pain, increase swelling, raise stress", "Promote sleep, spread infection, decrease circulation", "Reduce stress, cure disease, increase swelling"],
    "All three are on the benefits slide.", "MA1-1, slide 5")
add(10, "Massage therapy is described as one of the healthcare field's:", "Safest and least obtrusive yet effective modalities",
    ["Most invasive treatments", "Least effective therapies", "Riskiest procedures"],
    "Safest, least obtrusive, yet effective.", "MA1-1, slide 3")

# ---------- 11. First culture ----------
add(11, "The first culture to DOCUMENT the use of massage was:", "China",
    ["Greece", "India", "Sweden"],
    "Documented use in China dates back to 3000 BC.", "MA1-1, slide 9", True)
add(11, "Documented use of massage in China dates back to about:", "3000 BC",
    ["15,000 BC", "460 BC", "1856 AD"],
    "3000 BC, about 5,000 years ago.", "MA1-1, slide 9", True)
add(11, "Which culture was the first to train blind therapists?", "The Chinese",
    ["The Greeks", "The Japanese", "The Swedes"],
    "Starred in red on slide 10.", "MA1-1, slide 10", True)
add(11, "Cave paintings from about 15,000 years ago:", "Imply that massage was used",
    ["Are the first written record of massage", "Show Swedish massage strokes", "Were made in China"],
    "They imply massage; China has the first documentation.", "MA1-1, slide 8")
add(11, "Acupuncture first appeared in Chinese medical writings around:", "90 BC",
    ["3000 BC", "6th century AD", "1856"],
    "90 BC; the precursor of all other manual or energetic therapies.", "MA1-1, slide 9", True)
add(11, "The Huang-ti nei-ching is:", "The classic scripture of Traditional Chinese Medicine",
    ["A Japanese finger-pressure technique", "The Hippocratic Oath", "The first American massage textbook"],
    "Compiled under the mythical Yellow Emperor.", "MA1-1, slide 10", True)
add(11, "Chinese therapies are called 'the grandparents of ALL techniques' because:", "They are the precursor of all other manual or energetic therapies",
    ["They were invented in Sweden", "They use only French terms", "They were written by Hippocrates"],
    "Precursor of all others.", "MA1-1, slide 9", True)

# ---------- 12. Amma ----------
add(12, "Amma is:", "A Chinese technique of rubbing, pressing and manipulating specific points",
    ["A Japanese finger-pressure technique", "An Indian code of life", "A Swedish movement cure"],
    "Amma (Amna, Ammo) comes from the classic scripture of TCM.", "MA1-1, slide 10", True)
add(12, "Amma originates from which culture?", "China",
    ["Japan", "India", "Greece"],
    "Chinese, from the classic scripture of TCM.", "MA1-1, slide 10", True)
add(12, "Which technique involves rubbing, pressing and manipulating specific points?", "Amma",
    ["Effleurage", "Ayurveda", "Gymnastics"],
    "Amma.", "MA1-1, slide 10", True)
add(12, "Amma comes from:", "The classic scripture of Traditional Chinese Medicine",
    ["The Hippocratic Oath", "The Ling System", "De Medicina"],
    "From the classic TCM scripture.", "MA1-1, slide 10")

# ---------- 13. Shiatsu ----------
add(13, "Shiatsu means:", "Finger pressure",
    ["Code of life", "Energy point", "Rubbing and pressing"],
    "Shiatsu = finger pressure.", "MA1-1, slide 11")
add(13, "Shiatsu comes from which country?", "Japan",
    ["China", "India", "Sweden"],
    "Japan, 6th century AD.", "MA1-1, slide 11")
add(13, "In Shiatsu, a tsubo is:", "An energy point",
    ["A type of stroke", "A massage tool", "A Japanese healer"],
    "Tsubo = energy point.", "MA1-1, slide 11")
add(13, "The goal of Shiatsu is to:", "Bring balance between mind and body",
    ["Break up scar tissue", "Increase muscle size", "Sterilize the skin"],
    "Balance between mind and body.", "MA1-1, slide 11")
add(13, "Shiatsu developed in the:", "6th century AD",
    ["3000 BC", "7th century BC", "1800s"],
    "Japan, 6th century AD.", "MA1-1, slide 11")
add(13, "In India, massage is an aspect of:", "Ayurveda, the 'code of life'",
    ["Shiatsu", "Amma", "The Ling System"],
    "Ayurveda took shape in the 6th-7th centuries BC.", "MA1-1, slide 11")

# ---------- 14. Symbol / Aesculapius ----------
add(14, "The current symbol of medicine, a snake and staff, is credited to:", "Aesculapius",
    ["Hippocrates", "Galen", "Pehr Henrik Ling"],
    "His holy snake and staff remain the symbol of the medical profession.", "MA1-1, slide 12")
add(14, "Aesculapius was a:", "Greek priest-physician",
    ["Roman emperor", "Swedish gymnast", "Chinese emperor"],
    "Greek priest-physician, 7th century BC.", "MA1-1, slide 12")
add(14, "Aesculapius combined exercise and massage to create:", "Gymnastics",
    ["Shiatsu", "The Hippocratic Oath", "Swedish massage"],
    "Exercise + massage = gymnastics.", "MA1-1, slide 12")
add(14, "Aesculapius was later revered as the:", "God of medicine",
    ["Father of Swedish massage", "Father of Western medicine", "First medical historian"],
    "Later revered as the god of medicine.", "MA1-1, slide 12")
add(14, "The symbol of the medical profession is:", "A snake coiled around a staff",
    ["A bowl and a mortar", "A red cross", "A pair of hands"],
    "Aesculapius' holy snake and staff.", "MA1-1, slide 12")

# ---------- 15. Hippocrates ----------
add(15, "The 'Father of Western Medicine' is:", "Hippocrates",
    ["Galen", "Aesculapius", "William Harvey"],
    "Hippocrates (460-375 BC).", "MA1-1, slide 13")
add(15, "Hippocrates' philosophy included:", "The healer should cause NO additional harm",
    ["Drugs are the first choice of treatment", "Treat the disease, not the patient", "Massage should be avoided"],
    "Emphasize the individual patient; do no additional harm.", "MA1-1, slide 13")
add(15, "Hippocrates was a proponent of massage, particularly:", "Friction",
    ["Tapotement", "Effleurage", "Vibration"],
    "Particularly friction.", "MA1-1, slide 13")
add(15, "The code of ethics associated with Hippocrates is the:", "Hippocratic Oath",
    ["Ling System", "De Medicina", "Huang-ti nei-ching"],
    "Hippocratic Oath.", "MA1-1, slide 13")
add(15, "Hippocrates emphasized:", "The individual patient",
    ["Surgery for every condition", "Treating groups, not individuals", "Gymnastics only"],
    "Emphasized the individual patient.", "MA1-1, slide 13")

# ---------- 16. William Harvey ----------
add(16, "William Harvey's discovery that helped establish massage as therapeutic was:", "Blood circulates through the arteries and veins by the beat of the heart",
    ["Arteries and veins contain blood", "Muscles contract when stimulated", "Bacteria cause disease"],
    "Circulation driven by the heartbeat enhanced acceptance of massage.", "MA1-1, slide 18")
add(16, "William Harvey was from:", "England",
    ["Sweden", "Greece", "France"],
    "England, 1578-1657.", "MA1-1, slide 18")
add(16, "Who discovered that arteries and veins CONTAIN blood (not that it circulates)?", "Galen",
    ["William Harvey", "Hippocrates", "Borelli"],
    "Galen: contain. Harvey: circulate via the heartbeat.", "MA1-1, slides 15, 18")
add(16, "Harvey's discovery affected massage by:", "Enhancing the acceptance of massage as therapeutic",
    ["Banning massage in hospitals", "Introducing French terms", "Creating Swedish massage"],
    "It enhanced the acceptance of massage as therapeutic.", "MA1-1, slide 18")

# ---------- 17. Ling ----------
add(17, "The 'Father of Swedish Massage' is:", "Pehr Henrik Ling",
    ["Johann Mezger", "John Harvey Kellogg", "George Henry Taylor"],
    "Ling (1776-1839), also father of physical therapy.", "MA1-1, slide 19")
add(17, "Pehr Henrik Ling's system of medical gymnastics is known as the:", "Ling System",
    ["Swedish Oath", "Taylor Method", "Kellogg Cure"],
    "Ling System → Swedish Movement → Swedish Movement Cure → Swedish Massage.", "MA1-1, slide 19")
add(17, "Besides Swedish massage, Ling is also considered the father of:", "Physical therapy",
    ["Chiropractic", "Acupuncture", "Sports medicine"],
    "Father of Swedish massage and physical therapy.", "MA1-1, slide 19")
add(17, "Ling was a:", "Swedish physiologist and gymnastics instructor",
    ["German physician", "Greek priest", "American author"],
    "Swedish physiologist and gymnastics instructor.", "MA1-1, slide 19")
add(17, "Which order shows how Ling's work evolved?", "Ling System → Swedish Movement → Swedish Movement Cure → Swedish Massage",
    ["Swedish Massage → Ling System → Swedish Movement", "Swedish Movement Cure → Ling System → Swedish Massage", "Amma → Shiatsu → Swedish Massage"],
    "The slide's sequence.", "MA1-1, slide 19")

# ---------- 18. Swedish massage ----------
add(18, "Swedish massage is described as:", "Massage strokes in tandem with movement",
    ["Finger pressure on energy points", "Rubbing and pressing specific points", "Joint manipulation only"],
    "Strokes in tandem with movement.", "MA1-1, slide 20")
add(18, "In Swedish massage, an ACTIVE movement is performed by the:", "Client",
    ["Therapist", "Client and therapist together", "Machine"],
    "Active = client; passive = therapist; duplicated = both.", "MA1-1, slide 20")
add(18, "In Swedish massage, a PASSIVE movement is performed by the:", "Therapist",
    ["Client", "Client and therapist together", "Neither"],
    "Passive = therapist.", "MA1-1, slide 20")
add(18, "A DUPLICATED movement is performed by:", "The client and therapist together",
    ["The client alone", "The therapist alone", "An assistant"],
    "Duplicated = both.", "MA1-1, slide 20")
add(18, "How many primary movements does Swedish massage have?", "3",
    ["2", "5", "7"],
    "Active, passive, duplicated.", "MA1-1, slide 20")
add(18, "Which is a stated effect of Swedish massage?", "Improves range of motion",
    ["Raises blood pressure", "Sterilizes tissue", "Increases muscle tension"],
    "Improves circulation, relieves tension, improves ROM, promotes relaxation.", "MA1-1, slide 20")

# ---------- 19. Mezger ----------
add(19, "Who is credited with much of the terminology for Swedish massage strokes?", "Johann Mezger",
    ["Pehr Henrik Ling", "John Harvey Kellogg", "Ambroise Paré"],
    "Mezger introduced French terminology.", "MA1-1, slide 21", True)
add(19, "The Swedish massage stroke terms originate from which language?", "French",
    ["Swedish", "Latin", "German"],
    "Effleurage, petrissage, tapotement are French.", "MA1-1, slide 21", True)
add(19, "Effleurage, petrissage and tapotement are examples of:", "French terms introduced by Johann Mezger",
    ["Swedish terms coined by Ling", "Greek terms from Hippocrates", "Chinese Amma techniques"],
    "Mezger's French terminology.", "MA1-1, slide 21", True)
add(19, "Johann Mezger made massage a fundamental component of:", "Physical rehabilitation",
    ["Spa relaxation", "Sports medicine", "Ayurveda"],
    "Physical rehabilitation; also promoted massage to the medical profession.", "MA1-1, slide 21")

# ---------- 20. Taylors ----------
add(20, "Who introduced Swedish massage (the Swedish Movement) to the United States?", "George Henry Taylor and Charles Fayette Taylor",
    ["John Harvey Kellogg", "Pehr Henrik Ling", "Johann Mezger"],
    "The Taylors; starred on the slide.", "MA1-1, slide 22", True)
add(20, "Swedish massage was introduced to the United States in:", "1856",
    ["1776", "1860", "1909"],
    "1856. The first American textbook followed in 1860.", "MA1-1, slide 22", True)
add(20, "The first American textbook on Swedish massage was published in:", "1860",
    ["1856", "1839", "1943"],
    "1860, by the Taylors.", "MA1-1, slide 22", True)
add(20, "John Harvey Kellogg is known for:", "Popularizing massage with the general public",
    ["Introducing Swedish massage to the U.S. in 1856", "Coining French stroke terms", "Founding the Ling System"],
    "Kellogg popularized it (Good Health magazine); the Taylors introduced it.", "MA1-1, slide 22")

# ---------- 21. Communication ----------
add(21, "The 3 types of professional communication are:", "Verbal, non-verbal, written",
    ["Verbal, electronic, legal", "Spoken, sung, signed", "Intake, SOAP, referral"],
    "Verbal, non-verbal, written.", "MA1-2a, slides 4-6")
add(21, "Professional communication with a client starts:", "When they call for an appointment",
    ["When they lie on the table", "After the first massage", "When they pay"],
    "Starts when they call for an appointment.", "MA1-2a, slide 2")
add(21, "Written communication should be:", "Checked with the client at each visit and updated",
    ["Filled out once and never changed", "Kept only by the front desk", "Optional for returning clients"],
    "Starred in red on the slide: always check with the client at each visit and update.", "MA1-2a, slide 6", True)
add(21, "Which is an example of WRITTEN communication?", "SOAP notes",
    ["Tracking", "Facial expressions", "Paraphrasing"],
    "Intake form, consent form, prescriptions, SOAP notes, correspondence, referral forms.", "MA1-2a, slide 6")
add(21, "'Speak it back to them in your own words and have them confirm' describes:", "Paraphrase, clarify, summarize",
    ["Tracking", "Power differential", "Informed consent"],
    "A verbal communication skill.", "MA1-2a, slide 4")
add(21, "'Sit if they sit, stand if they stand' describes:", "Power differential",
    ["Tracking", "Informed consent", "Open-ended questions"],
    "A non-verbal communication consideration.", "MA1-2a, slide 5")
add(21, "Good verbal communication with clients uses:", "Open-ended questions",
    ["Only yes/no questions", "Medical jargon", "Judgment of the client's habits"],
    "Open, safe, non-judgmental; open-ended questions; empathy.", "MA1-2a, slide 4")

# ---------- 22. Informed consent ----------
add(22, "Informed consent is:", "The client's authorization for professional services",
    ["A doctor's prescription for massage", "The therapist's treatment plan", "A referral from insurance"],
    "Starred on the slide.", "MA1-2a, slide 9", True)
add(22, "Informed consent can be:", "Written or verbal, but written is recommended",
    ["Verbal only", "Written only, by a doctor", "Assumed if the client shows up"],
    "Written or verbal; get it in writing.", "MA1-2a, slide 9", True)
add(22, "Massage therapists have 'direct access' to the public. This means:", "No prescription or referral is needed to receive massage",
    ["Insurance always pays", "A doctor must approve each session", "Clients may skip the intake form"],
    "Direct access = no prescription/referral needed.", "MA1-2a, slide 9")
add(22, "Most insurance companies require what before paying for massage?", "A prescription or referral",
    ["Informed consent only", "A SUDS rating", "Nothing"],
    "Insurance usually wants a prescription or referral.", "MA1-2a, slide 9")
add(22, "Informed consent is gained during the:", "Pre-massage interview",
    ["Post-massage recommendations", "Final SOAP note", "Billing process"],
    "Part of the pre-massage interview, after explaining services and benefits/side effects.", "MA1-2a, slide 3", True)

# ---------- 23. SOAP ----------
add(23, "The 4 categories of client treatment records are:", "Subjective, Objective, Action, Plan",
    ["Symptoms, Observations, Allergies, Prescriptions", "Subjective, Opinion, Assessment, Payment", "Systolic, Objective, Action, Pulse"],
    "SOAP. In medical settings A = Assessment.", "MA1-2a, slide 10")
add(23, "In SOAP notes, 'S' records:", "What the client tells you, in their words",
    ["What you see and feel", "The techniques you used", "Your recommendations"],
    "Subjective = client's words.", "MA1-2a, slide 10")
add(23, "In SOAP notes, 'O' records:", "Your findings: what you see, feel, hear, smell, sense",
    ["What the client tells you", "Home care recommendations", "The client's insurance"],
    "Objective = your findings.", "MA1-2a, slide 10")
add(23, "In SOAP notes, 'A' (Action) records:", "What you did during the session: strokes, techniques, ROM, stretching",
    ["The client's complaint", "Rescheduling", "Your visual observations"],
    "Action = what you did. (Medical: Assessment.)", "MA1-2a, slide 10")
add(23, "In SOAP notes, 'P' records:", "What you intend and recommend: rescheduling, home care",
    ["The client's pain description", "Blood pressure readings", "Strokes used"],
    "Plan.", "MA1-2a, slide 10")
add(23, "A client says, 'My neck hurts when I turn left.' This goes under:", "S (Subjective)",
    ["O (Objective)", "A (Action)", "P (Plan)"],
    "Client's own words = Subjective.", "MA1-2a, slide 10")
add(23, "You notice the client's right shoulder is elevated. This goes under:", "O (Objective)",
    ["S (Subjective)", "A (Action)", "P (Plan)"],
    "Your observation = Objective.", "MA1-2a, slide 10")
add(23, "You recommend neck stretches and a follow-up in one week. This goes under:", "P (Plan)",
    ["S (Subjective)", "O (Objective)", "A (Action)"],
    "Recommendations and rescheduling = Plan.", "MA1-2a, slide 10")

# ---------- 24. Symptom ----------
add(24, "A symptom is:", "A subjective change the client feels and reports",
    ["An objective finding the therapist measures", "A doctor's diagnosis", "A treatment goal"],
    "Symptom = subjective. Sign = objective. (Not on slides; standard definition.)", "Textbook definition")
add(24, "Symptoms are recorded in which part of the SOAP note?", "S (Subjective)",
    ["O (Objective)", "A (Action)", "P (Plan)"],
    "Client-reported, so Subjective.", "MA1-2a, slide 10")
add(24, "Which is a SYMPTOM rather than a sign?", "Numbness the client describes",
    ["Visible swelling", "A blood pressure reading", "Redness you observe"],
    "Symptoms are felt and reported by the client.", "Textbook definition")
add(24, "Something the therapist can observe or measure, like swelling, is called a:", "Sign",
    ["Symptom", "Goal", "Contraindication"],
    "Sign = objective.", "Textbook definition")

# ---------- 25. Goals ----------
add(25, "A short-term goal focuses on:", "The immediate problem, such as decreasing pain in the current session",
    ["Restoring normal function over months", "Changing the client's lifestyle", "Eliminating all symptoms permanently"],
    "Short-term = immediate problem, this session.", "MA1-2a, slide 11")
add(25, "A long-term goal focuses on:", "Restoring normal or enhanced function",
    ["Decreasing pain in the current session only", "Booking the next appointment", "Taking blood pressure"],
    "Long-term = restore function; decrease frequency and intensity of symptoms.", "MA1-2a, slide 11")
add(25, "'Decrease the frequency and intensity of symptoms' is a:", "Long-term goal",
    ["Short-term goal", "SOAP Subjective entry", "Contraindication"],
    "Long-term.", "MA1-2a, slide 11")
add(25, "'Decrease pain/discomfort in the current session' is a:", "Short-term goal",
    ["Long-term goal", "Plan entry for next month", "Informed consent"],
    "Short-term.", "MA1-2a, slide 11")

# ---------- 26. SUDS ----------
add(26, "SUDS stands for:", "Subjective Units of Discomfort Scale",
    ["Standard Units of Daily Stress", "Systolic Under Diastolic Score", "Subjective Under-Documented Symptoms"],
    "Subjective Units of Discomfort Scale.", "MA1-2a, slide 13")
add(26, "On the SUDS scale, 1 means:", "Best",
    ["Worst", "Moderate pain", "Not applicable"],
    "1 = best, 10 = worst.", "MA1-2a, slide 13")
add(26, "On the SUDS scale, 10 means:", "Worst",
    ["Best", "No pain", "Average"],
    "10 = worst.", "MA1-2a, slide 13")
add(26, "When should you ask the client for a SUDS rating?", "Before AND after EACH session",
    ["Only at the first visit", "Only after the massage", "Once a month"],
    "In red on the slide: before and after each therapy.", "MA1-2a, slide 13", True)
add(26, "The SUDS scale runs from:", "1 to 10",
    ["0 to 5", "1 to 100", "A to F"],
    "Scale 1 through 10.", "MA1-2a, slide 13")

# ---------- 27. Medical history ----------
add(27, "Where should you review a client's medical history?", "In a private, quiet area where others can't overhear",
    ["In the waiting room", "On the table during the massage", "At the front desk with other clients present"],
    "Confidentiality: private area, before the client undresses. (Location is not on slides.)", "Textbook practice · MA1-2a, slide 3")
add(27, "Reviewing the client's health history is part of the:", "Pre-massage interview",
    ["Post-massage recommendations", "Plan section of SOAP", "Clinic checkout"],
    "Bolded on the pre-massage interview slide.", "MA1-2a, slide 3", True)
add(27, "The medical history review should happen:", "Before the massage, while the client is still dressed",
    ["During the massage", "After the client leaves", "Only if the client asks"],
    "Pre-massage, clothed and seated.", "MA1-2a, slide 3", True)
add(27, "Which is part of the pre-massage interview?", "Orienting the client to the room",
    ["Applying cryotherapy", "Writing the Plan section", "Sending the client home"],
    "Includes greeting, explaining services, reviewing history, consent, orienting to the room.", "MA1-2a, slide 3")

# ---------- 28. SOAP corrections ----------
add(28, "If you make a mistake in SOAP notes, you should:", "Draw a single line through it, write the correction, and initial and date it",
    ["Use white-out and rewrite", "Scribble it out completely", "Tear out the page and start over"],
    "SOAP notes are legal records; the original must stay readable. (Not on slides; standard practice.)", "Textbook practice")
add(28, "Why should errors in SOAP notes NOT be erased?", "SOAP notes are legal documents and the original must stay readable",
    ["Erasers damage paper", "Clients prefer messy notes", "Insurance requires pencil"],
    "Legal record.", "Textbook practice")
add(28, "Which correction method is acceptable?", "Single line through the error, initialed and dated",
    ["Writing over the error in pencil", "Covering it with tape", "Blacking it out with marker"],
    "Single line, initial, date.", "Textbook practice")

# ---------- 29. Systolic ----------
add(29, "The systolic number is:", "The top number; where you HEAR the first beat",
    ["The bottom number; where the pulse disappears", "The pulse rate per minute", "Always the lower number"],
    "Systolic = top, first beat heard.", "MA1-2a, slide 15", True)
add(29, "The normal range for systolic blood pressure given in class is:", "80-140",
    ["50-88", "120-180", "60-100"],
    "Systolic 80-140; diastolic 50-88.", "MA1-2a, slide 15", True)
add(29, "Based on the class range, a systolic reading is considered HIGH above:", "140",
    ["88", "100", "200"],
    "Normal systolic tops out at 140.", "MA1-2a, slide 15", True)
add(29, "Normal blood pressure is considered:", "120/80",
    ["170/100", "140/50", "88/50"],
    "120/80.", "MA1-2a, slide 16", True)
add(29, "Blood pressure is a good indicator of:", "Overall health",
    ["Muscle strength", "Flexibility", "Infection"],
    "Highlighted: a good indicator of overall health.", "MA1-2a, slide 15", True)

# ---------- 30. Diastolic ----------
add(30, "The diastolic number is:", "The bottom number; where the pulse disappears",
    ["The top number; where you hear the first beat", "The heart rate", "The average of two readings"],
    "Diastolic = bottom ('D = Down'), pulse disappears.", "MA1-2a, slide 15", True)
add(30, "The normal range for diastolic blood pressure given in class is:", "50-88",
    ["80-140", "90-120", "100-170"],
    "Diastolic 50-88.", "MA1-2a, slide 15", True)
add(30, "Which BP number is believed to be the more important of the two?", "Diastolic",
    ["Systolic", "Both equally", "Neither"],
    "Diastolic is believed to be the more important number.", "MA1-2a, slide 15", True)
add(30, "Based on the class range, a diastolic reading is considered HIGH above:", "88",
    ["140", "50", "120"],
    "Normal diastolic tops out at 88.", "MA1-2a, slide 15", True)
add(30, "A memory aid for diastolic is:", "D = Down (bottom number)",
    ["D = Doctor", "D = Double the systolic", "D = Daily"],
    "D = Down.", "MA1-2a, slide 15", True)

# ---------- 31. Tracking ----------
add(31, "The MOST honest form of communication is:", "Tracking (watching the client's non-verbal cues)",
    ["The intake form", "Verbal answers to questions", "The SUDS rating"],
    "Tracking: keep an eye on your client.", "MA1-2a, slide 5", True)
add(31, "Tracking is considered the most honest form of communication because:", "The body reacts involuntarily and shows what the client may not say",
    ["Clients always tell the truth verbally", "It is written down", "It is required by law"],
    "Wincing, tensing and breath-holding happen without the client deciding to show them.", "MA1-2a, slide 5", True)
add(31, "Tracking falls under which type of communication?", "Non-verbal",
    ["Verbal", "Written", "Electronic"],
    "Non-verbal.", "MA1-2a, slide 5", True)
add(31, "Which is an example of tracking?", "Noticing the client tense up and hold their breath",
    ["Reading the intake form", "Asking an open-ended question", "Writing SOAP notes"],
    "Watching the client's body during the session.", "MA1-2a, slide 5", True)

# ---------- 32. Clinic cutoff ----------
add(32, "The blood pressure cutoff for massage in the student clinic is:", "170/100",
    ["120/80", "140/90", "200/120"],
    "In red and highlighted: 170/100.", "MA1-2a, slide 16", True)
add(32, "If either BP number reaches the clinic cutoff, you must:", "Have the CA check, and not do the therapy unless the CA approves",
    ["Do a shorter massage", "Take it again yourself and proceed", "Send the client home without telling anyone"],
    "DO NOT DO THE THERAPY UNLESS APPROVED BY THE CA.", "MA1-2a, slide 16", True)
add(32, "A client's BP is 150/100. In the student clinic you should:", "Get the CA to check before any massage",
    ["Proceed, since systolic is under 170", "Proceed with light pressure", "Ignore the diastolic number"],
    "Either number at the cutoff triggers a CA check.", "MA1-2a, slide 16", True)
add(32, "When taking BP, the stethoscope is placed over the artery in the:", "Antecubital area (inside of the elbow)",
    ["Wrist", "Neck", "Back of the knee"],
    "Antecubital area.", "MA1-2a, slide 16", True)
add(32, "When taking BP, the cuff is inflated to:", "180-200",
    ["100-120", "120-140", "250-300"],
    "180-200; you should not hear or feel a pulse.", "MA1-2a, slide 16", True)
add(32, "With a manual cuff, BP should be recorded as:", "An even number",
    ["An odd number", "A decimal", "A single number"],
    "Even number with a manual cuff.", "MA1-2a, slide 16", True)
add(32, "When placing the BP cuff, the bladder goes:", "Over the artery",
    ["Over the elbow bone", "Over the wrist", "Anywhere on the arm"],
    "Bladder over the artery.", "MA1-2a, slide 16", True)

# ---------- 33. Review line ----------
add(33, "Proper fingernail hygiene for a massage therapist is:", "Short, clean nails scrubbed with a nail brush; no polish or artificial nails",
    ["Long nails for deeper work", "Polished nails for a professional look", "Nails cleaned once a week"],
    "Study guide review answer.", "Study guide p.2 · MA1-1, slide 38")
add(33, "Soiled linens should be carried:", "Away from your body",
    ["Against your chest", "Over your shoulder", "Under your arm"],
    "UP handout: carry soiled linens away from your body; use a plastic-lined linen basket.", "UP handout")
add(33, "To prevent cross-contamination of a lubricant, you should:", "Keep it in a closed container (pump/squeeze) and never dip a used hand in",
    ["Use an open bowl of oil", "Share one jar among all clients", "Dip fingers in the jar between strokes"],
    "Closed containers for lubricants.", "MA1-1, slide 34")
add(33, "A lubricant that has been contaminated should be:", "Thrown out",
    ["Strained and reused", "Heated to sterilize it", "Saved for the next client"],
    "Study guide review answer: throw it out.", "Study guide p.2")
add(33, "Linens used by a client with a parasitic infestation should be:", "Kept separate, washed in HOT water with bleach, and HOT air dried",
    ["Shaken out and reused", "Washed in cold water", "Air dried outside"],
    "Treat parasites as 'HOT'.", "MA1-1, slide 30", True)
add(33, "How often should linens be changed?", "Clean linens for EACH client",
    ["Once a day", "Once a week", "Only when visibly soiled"],
    "Use clean linens for each therapy.", "MA1-1, slide 34")

# ---------- 34. Glove types ----------
add(34, "Which glove breaks down when used with oil-based lubricants?", "Latex",
    ["Nitrile", "Vinyl", "None of them"],
    "Latex breaks down with oil; many people are allergic.", "MA1-1, slide 37")
add(34, "Which glove is about 3x more puncture resistant than latex?", "Nitrile",
    ["Vinyl", "Cotton", "Latex"],
    "Nitrile: allergy-safe, high tactile sensitivity, durable, low friction.", "MA1-1, slide 37")
add(34, "Vinyl gloves are thicker, which:", "Reduces tactile sensitivity",
    ["Increases tactile sensitivity", "Makes them break down with oil", "Causes latex allergy"],
    "Thicker = less feel.", "MA1-1, slide 37")
add(34, "A client has a latex allergy. Which gloves are appropriate?", "Nitrile or vinyl",
    ["Latex only", "No gloves are allowed", "Latex with oil"],
    "Both vinyl and nitrile are allergy-safe.", "MA1-1, slide 37")
add(34, "Which glove offers high tactile sensitivity and resists oils and chemicals?", "Nitrile",
    ["Vinyl", "Latex", "Cotton"],
    "Nitrile.", "MA1-1, slide 37")

# ---------- 35. Other agents ----------
add(35, "The best prevention against viruses is:", "Good handwashing and avoidance",
    ["Antibiotics", "Massage with extra pressure", "Wearing perfume"],
    "In red and bold on the viruses slide.", "MA1-1, slide 29", True)
add(35, "Any parasitic infestation should be treated as:", "\"HOT\": separate sheets, hot water with bleach, hot air dry",
    ["Not contagious", "A virus", "Cold: wash in cold water"],
    "Bold callout on the parasites slide.", "MA1-1, slide 30", True)
add(35, "Herpes simplex is highly contagious during which stage?", "The acute (blistering) stage",
    ["After it heals", "Only in winter", "Never"],
    "At least locally contraindicated.", "MA1-1, slide 29")
add(35, "Scabies is caused by:", "Microscopic mites that burrow under the skin",
    ["A fungus", "A virus", "Bacteria"],
    "Mites; itchy especially at night, in warm creases.", "MA1-1, slide 30")
add(35, "Staph (boils), tuberculosis, strep throat and tetanus are caused by:", "Bacteria",
    ["Viruses", "Fungi", "Protozoa"],
    "Bacterial diseases.", "MA1-1, slide 26")
add(35, "Protozoa can only survive:", "In a living subject (host)",
    ["On dry surfaces", "In cold water only", "On massage tables"],
    "Single-celled; cause trichomoniasis, malaria, dysentery.", "MA1-1, slide 28")
add(35, "Nits are:", "White lice eggs that do not fall out easily",
    ["Scabies mites", "Fungal spores", "A type of bacteria"],
    "Head lice eggs.", "MA1-1, slide 30")
add(35, "Viruses are hard to treat because they:", "Mutate easily",
    ["Are too large", "Only live in water", "Are beneficial"],
    "Easily mutate; difficult to treat.", "MA1-1, slide 29")

# ---------- 36. Sanitation & safety ----------
add(36, "Which is a safety guideline from the lecture?", "Wipe lubricant from the client's feet",
    ["Leave oil on the feet for moisture", "Skip CPR certification", "Massage after one drink"],
    "Starred safety guidelines: CPR & first aid, first aid kit, wipe feet, know contraindications, never under the influence.", "MA1-1, slide 41", True)
add(36, "Massage therapists should maintain current certification in:", "CPR and First Aid",
    ["Phlebotomy", "Radiology", "Pharmacy"],
    "Starred on the safety slide.", "MA1-1, slide 41", True)
add(36, "Therapists must be able to identify:", "Endangerment sites and contraindications",
    ["Clients' insurance providers", "Every muscle's Latin name", "Blood types"],
    "Starred on the safety slide.", "MA1-1, slide 41", True)
add(36, "Which is a sanitation guideline?", "Use closed containers for lubricants",
    ["Reuse linens between clients", "Massage while ill if wearing gloves", "Clean the table once a week"],
    "Closed containers, clean linens each client, clean table each use.", "MA1-1, slide 34")
add(36, "If you are ill, the sanitation guidelines say:", "Do NOT massage",
    ["Massage with gloves", "Massage only regular clients", "Massage for half the time"],
    "Don't massage when ill; avoid massaging ill clients.", "MA1-1, slide 34")

# ---------- 37. More history ----------
add(37, "Who wrote the first book of sports medicine?", "Mercuriale",
    ["Borelli", "Ambroise Paré", "Galen"],
    "Highlighted on the Renaissance slide.", "MA1-1, slide 17", True)
add(37, "Galen was the personal physician to:", "Marcus Aurelius",
    ["Julius Caesar", "The Yellow Emperor", "King Gustav"],
    "Galen (130-200 AD); his text was used for over 1,000 years.", "MA1-1, slide 15")
add(37, "Aulus Celsus, author of De Medicina, is known as the:", "First important medical historian",
    ["Father of Western medicine", "God of medicine", "Father of physical therapy"],
    "Bridged the gap between Hippocrates and later times.", "MA1-1, slide 14")
add(37, "Ambroise Paré discussed the therapeutic effects of massage especially in:", "Orthopedic surgery cases",
    ["Childbirth", "Sports injuries", "Spa treatments"],
    "Also classified massage movements.", "MA1-1, slide 17")
add(37, "Cherokees and Navajos used massage for:", "Labor pains and colic",
    ["Broken bones", "Infections", "Headaches only"],
    "Americas slide.", "MA1-1, slide 16")
add(37, "Borelli (Renaissance) is associated with:", "Anatomical dissections and muscular contraction",
    ["The first sports medicine book", "Swedish massage", "Blood circulation"],
    "Borelli 1608-1679.", "MA1-1, slide 17")

# ---------- 38. OH PAIN & aftercare ----------
add(38, "In OH PAIN, the 'N' stands for:", "Neutralizers: what makes it less",
    ["Numbness", "Nerves involved", "Next appointment"],
    "Onset, How, Amount, Place, Interaction, Neutralizers.", "MA1-2a, slide 12")
add(38, "In OH PAIN, 'I' (Interaction) asks:", "What makes it worse",
    ["What makes it better", "Where it is", "How long you've had it"],
    "Interaction = worse; Neutralizers = better.", "MA1-2a, slide 12")
add(38, "Cryotherapy (cold) is used for:", "Acute conditions and inflammation",
    ["Chronic conditions and hypertonicity", "Relaxation only", "Stretching after surgery"],
    "Cold = acute; heat = chronic.", "MA1-2a, slide 20")
add(38, "Thermotherapy (moist heat) is used for:", "Chronic conditions and hypertonicity",
    ["Acute inflammation", "Fresh sprains", "Swelling right after injury"],
    "Heat = chronic, hypertonicity.", "MA1-2a, slide 20")
add(38, "Stretching is defined as:", "Passively positioning muscle attachments as far apart as possible to elongate the muscle",
    ["Contracting a muscle against resistance", "Rapid tapping of the muscle", "Applying ice to a muscle"],
    "Highlighted definition; increases ROM.", "MA1-2a, slide 22", True)
add(38, "Stretching is contraindicated:", "After surgery or a fracture",
    ["After a relaxing massage", "For chronic tension", "To increase ROM"],
    "Highlighted contraindications: disrupts healing, after surgery/fracture, joint inflammation, herniated disc, bone or muscle injury.", "MA1-2a, slide 22", True)
add(38, "Which is listed as a relaxation technique to recommend?", "Deep breathing",
    ["Heavy lifting", "Caffeine", "Skipping sleep"],
    "Highlighted list: deep breathing, meditation, yoga, tai chi, aromatherapy, music/art therapy, biofeedback, hydrotherapy.", "MA1-2a, slide 21", True)
add(38, "Which item is part of the intake form?", "Major complaint",
    ["SUDS after the massage", "Strokes used", "The CA's signature"],
    "Contact info, health/medical history, major complaint, daily activities.", "MA1-2a, slide 8")
add(38, "When applying cold packs or ice, you should:", "Place a barrier between the skin and the cold",
    ["Apply ice directly for 1 hour", "Use dry heat instead", "Rub ice firmly into the skin"],
    "Barrier between skin and cold.", "MA1-2a, slide 20")

from collections import Counter
c = Counter(q["topic"] for q in Q)
for t in TOPICS:
    assert c[t] >= 3, (t, c[t])
flagged_topics = sorted({q["topic"] for q in Q if q["f"]})
out = {"title": "MA1 Quiz #1 Practice", "topics": TOPICS, "studyGuideTopics": STUDY_GUIDE_TOPICS, "questions": Q}
json.dump(out, open("questions.json", "w"), ensure_ascii=False, indent=1)
print(len(Q), "questions;", sum(q["f"] for q in Q), "flagged; flagged topics:", flagged_topics)
