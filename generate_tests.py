import json
import random
import re

english_bank = [
    {"question": "Choose the correct synonym for 'Diligent':", "options": ["Lazy", "Hardworking", "Careless", "Quick"], "answer": "Hardworking", "section": "English"},
    {"question": "Identify the part of speech of the word 'quickly' in the sentence: 'She ran quickly.'", "options": ["Noun", "Verb", "Adverb", "Adjective"], "answer": "Adverb", "section": "English"},
    {"question": "Which sentence is correctly punctuated?", "options": ["Its raining today.", "It's raining, today.", "Its' raining today.", "It's raining today."], "answer": "It's raining today.", "section": "English"},
    {"question": "Change to Active Voice: 'The cake was eaten by John.'", "options": ["John eating the cake.", "John ate the cake.", "John eats the cake.", "John has eaten the cake."], "answer": "John ate the cake.", "section": "English"},
    {"question": "Change to Indirect Speech: He said, 'I am happy.'", "options": ["He said that he was happy.", "He said he is happy.", "He says he was happy.", "He told me he is happy."], "answer": "He said that he was happy.", "section": "English"},
    {"question": "Identify the tense: 'They have been playing for two hours.'", "options": ["Present Continuous", "Present Perfect Continuous", "Past Continuous", "Future Perfect"], "answer": "Present Perfect Continuous", "section": "English"},
    {"question": "Choose the correct antonym for 'Abundant':", "options": ["Plentiful", "Scarce", "Rich", "Heavy"], "answer": "Scarce", "section": "English"},
    {"question": "Which of the following is a preposition?", "options": ["And", "But", "Under", "Quickly"], "answer": "Under", "section": "English"},
    {"question": "Select the correct spelling:", "options": ["Accomodation", "Accommodation", "Acommodation", "Acomodation"], "answer": "Accommodation", "section": "English"},
    {"question": "Fill in the blank: She is good ___ Mathematics.", "options": ["in", "at", "with", "on"], "answer": "at", "section": "English"},
    {"question": "Change into passive voice: 'She writes a letter.'", "options": ["A letter is written by her.", "A letter was written by her.", "A letter is writing by her.", "A letter wrote by her."], "answer": "A letter is written by her.", "section": "English"},
    {"question": "Identify the noun in the sentence: 'The quick brown fox jumps.'", "options": ["quick", "brown", "fox", "jumps"], "answer": "fox", "section": "English"},
    {"question": "Which is a complex sentence?", "options": ["I like tea.", "I like tea, and he likes coffee.", "Because I was tired, I went to bed.", "She ran fast."], "answer": "Because I was tired, I went to bed.", "section": "English"},
    {"question": "Choose the correct article: 'He is ___ honest man.'", "options": ["a", "an", "the", "none"], "answer": "an", "section": "English"},
    {"question": "What is the past participle of 'Break'?", "options": ["Broke", "Breaks", "Breaking", "Broken"], "answer": "Broken", "section": "English"},
]

gk_bank = [
    {"question": "When did Pakistan become an Islamic Republic?", "options": ["1947", "1956", "1962", "1973"], "answer": "1956", "section": "General Knowledge"},
    {"question": "Complete the name of the highest mountain in Pakistan:", "options": ["Nanga Parbat", "K2", "Broad Peak", "Tirich Mir"], "answer": "K2", "section": "General Knowledge"},
    {"question": "Who was the first Prime Minister of Pakistan?", "options": ["Quaid-e-Azam", "Allama Iqbal", "Liaquat Ali Khan", "Sir Syed Ahmed Khan"], "answer": "Liaquat Ali Khan", "section": "General Knowledge"},
    {"question": "Which is the largest province of Pakistan by area?", "options": ["Punjab", "Sindh", "Balochistan", "KPK"], "answer": "Balochistan", "section": "General Knowledge"},
    {"question": "The national animal of Pakistan is:", "options": ["Markhor", "Snow Leopard", "Lion", "Tiger"], "answer": "Markhor", "section": "General Knowledge"},
    {"question": "Mohenjo-Daro is located in which province?", "options": ["Punjab", "Sindh", "Balochistan", "KPK"], "answer": "Sindh", "section": "General Knowledge"},
    {"question": "The longest river in Pakistan is:", "options": ["Ravi", "Chenab", "Indus", "Sutlej"], "answer": "Indus", "section": "General Knowledge"},
    {"question": "Who wrote the national anthem of Pakistan?", "options": ["Allama Iqbal", "Hafeez Jalandhari", "Faiz Ahmed Faiz", "Ahmed Faraz"], "answer": "Hafeez Jalandhari", "section": "General Knowledge"},
    {"question": "What is the capital of Sindh?", "options": ["Hyderabad", "Sukkur", "Karachi", "Mirpurkhas"], "answer": "Karachi", "section": "General Knowledge"},
    {"question": "Which sea lies to the south of Pakistan?", "options": ["Caspian Sea", "Red Sea", "Arabian Sea", "Mediterranean Sea"], "answer": "Arabian Sea", "section": "General Knowledge"},
    {"question": "Who was the founder of the Mughal Empire?", "options": ["Akbar", "Humayun", "Babur", "Shah Jahan"], "answer": "Babur", "section": "General Knowledge"},
    {"question": "The Pakistan Resolution was passed in which year?", "options": ["1930", "1940", "1947", "1948"], "answer": "1940", "section": "General Knowledge"},
    {"question": "What is the national flower of Pakistan?", "options": ["Rose", "Jasmine", "Sunflower", "Lotus"], "answer": "Jasmine", "section": "General Knowledge"},
    {"question": "In which city is the Faisal Mosque located?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad", "section": "General Knowledge"},
    {"question": "Which mountain range is located in the north of Pakistan?", "options": ["Karakoram", "Himalayas", "Hindu Kush", "All of these"], "answer": "All of these", "section": "General Knowledge"},
]

pedagogy_bank = [
    {"question": "VARK learning style stands for:", "options": ["Visual, Aural, Read/Write, Kinesthetic", "Visual, Audio, Rote, Kinetic", "Verbal, Audio, Read, Kinesthetic", "Visual, Active, Reading, Kinetic"], "answer": "Visual, Aural, Read/Write, Kinesthetic", "section": "Teaching and Learning Pedagogies"},
    {"question": "Which level of Bloom's Taxonomy involves creating something new?", "options": ["Remembering", "Analyzing", "Evaluating", "Creating"], "answer": "Creating", "section": "Teaching and Learning Pedagogies"},
    {"question": "Which teaching method involves students working in groups to solve an open-ended problem?", "options": ["Lecture Method", "Project-Based Learning", "Demonstration", "Rote Learning"], "answer": "Project-Based Learning", "section": "Teaching and Learning Pedagogies"},
    {"question": "What is the main purpose of formative feedback?", "options": ["To grade the student", "To rank the student", "To improve learning during the process", "To punish mistakes"], "answer": "To improve learning during the process", "section": "Teaching and Learning Pedagogies"},
    {"question": "ICT integration in the classroom means:", "options": ["Using computers to teach the same way", "Replacing teachers with computers", "Using tech tools to enhance learning", "Only using digital textbooks"], "answer": "Using tech tools to enhance learning", "section": "Teaching and Learning Pedagogies"},
    {"question": "Reflective practice for a teacher means:", "options": ["Looking in the mirror", "Thinking about their teaching to improve", "Making students reflect", "Copying other teachers"], "answer": "Thinking about their teaching to improve", "section": "Teaching and Learning Pedagogies"},
    {"question": "A strategy to handle a disruptive student is part of:", "options": ["Lesson Planning", "Classroom Management", "Curriculum Design", "Assessment"], "answer": "Classroom Management", "section": "Teaching and Learning Pedagogies"},
    {"question": "Brainstorming is used primarily to:", "options": ["Evaluate knowledge", "Generate many ideas", "Discipline students", "Test memory"], "answer": "Generate many ideas", "section": "Teaching and Learning Pedagogies"},
    {"question": "Which of these is a 21st-century skill?", "options": ["Memorization", "Critical Thinking", "Copying notes", "Silence"], "answer": "Critical Thinking", "section": "Teaching and Learning Pedagogies"},
    {"question": "What is the lowest level of Bloom's Cognitive Domain?", "options": ["Understanding", "Applying", "Remembering", "Analyzing"], "answer": "Remembering", "section": "Teaching and Learning Pedagogies"},
    {"question": "Which of the following describes a 'Kinesthetic' learner?", "options": ["Learns by listening", "Learns by reading", "Learns by doing/moving", "Learns by watching video"], "answer": "Learns by doing/moving", "section": "Teaching and Learning Pedagogies"},
    {"question": "Summative assessment is usually conducted:", "options": ["At the beginning of the lesson", "During the lesson", "At the end of a unit/course", "Randomly"], "answer": "At the end of a unit/course", "section": "Teaching and Learning Pedagogies"},
    {"question": "Team teaching involves:", "options": ["Students teaching each other", "Two or more teachers teaching together", "Teaching a sports team", "Teachers grading together"], "answer": "Two or more teachers teaching together", "section": "Teaching and Learning Pedagogies"},
    {"question": "A case study method is most effectively used to:", "options": ["Teach historical dates", "Analyze complex real-world situations", "Memorize formulas", "Assess physical fitness"], "answer": "Analyze complex real-world situations", "section": "Teaching and Learning Pedagogies"},
    {"question": "Formative assessment is described as assessment:", "options": ["Of learning", "For learning", "As learning", "By learning"], "answer": "For learning", "section": "Teaching and Learning Pedagogies"},
]

biology_bank = [
    {"question": "The powerhouse of the cell is:", "options": ["Nucleus", "Ribosome", "Mitochondria", "Golgi Body"], "answer": "Mitochondria", "section": "Biology"},
    {"question": "Which process is used by plants to make food?", "options": ["Respiration", "Digestion", "Photosynthesis", "Transpiration"], "answer": "Photosynthesis", "section": "Biology"},
    {"question": "Enzymes are biologically categorized as:", "options": ["Carbohydrates", "Lipids", "Proteins", "Nucleic Acids"], "answer": "Proteins", "section": "Biology"},
    {"question": "Viruses are composed of:", "options": ["Nucleic acid and protein", "Carbohydrates", "Only lipids", "Cells"], "answer": "Nucleic acid and protein", "section": "Biology"},
    {"question": "The basic structural and functional unit of life is:", "options": ["Tissue", "Organ", "Cell", "System"], "answer": "Cell", "section": "Biology"},
    {"question": "Which blood cells fight diseases?", "options": ["RBC", "WBC", "Platelets", "Plasma"], "answer": "WBC", "section": "Biology"},
    {"question": "The process by which a cell divides into two identical daughter cells is:", "options": ["Meiosis", "Mitosis", "Fertilization", "Osmosis"], "answer": "Mitosis", "section": "Biology"},
    {"question": "Digestion of carbohydrates begins in the:", "options": ["Stomach", "Mouth", "Small Intestine", "Large Intestine"], "answer": "Mouth", "section": "Biology"},
    {"question": "Which of the following is an abiotic component of an ecosystem?", "options": ["Plants", "Animals", "Sunlight", "Fungi"], "answer": "Sunlight", "section": "Biology"},
    {"question": "Bacteria reproduce primarily through?", "options": ["Meiosis", "Binary Fission", "Budding", "Spore formation"], "answer": "Binary Fission", "section": "Biology"},
    {"question": "An adaptation of a cactus for desert survival is:", "options": ["Broad leaves", "Deep taproot", "Thin bark", "Many stomata"], "answer": "Deep taproot", "section": "Biology"},
    {"question": "Respiration in humans primarily occurs in:", "options": ["Kidneys", "Liver", "Lungs", "Heart"], "answer": "Lungs", "section": "Biology"},
    {"question": "The human stomach produces which acid to help with digestion?", "options": ["Sulfuric acid", "Hydrochloric acid", "Citric acid", "Nitric acid"], "answer": "Hydrochloric acid", "section": "Biology"},
    {"question": "A disease causing agent is known as a:", "options": ["Pathogen", "Antibody", "Antigen", "Enzyme"], "answer": "Pathogen", "section": "Biology"},
    {"question": "Which organ is heavily involved in filtering blood and excreting urea?", "options": ["Liver", "Kidney", "Stomach", "Heart"], "answer": "Kidney", "section": "Biology"},
    {"question": "Chloroplasts contain a green pigment called:", "options": ["Hemoglobin", "Melanin", "Chlorophyll", "Carotene"], "answer": "Chlorophyll", "section": "Biology"},
    {"question": "The largest organ of the human body is:", "options": ["Liver", "Brain", "Skin", "Heart"], "answer": "Skin", "section": "Biology"},
    {"question": "Which vitamin deficiency causes scurvy?", "options": ["A", "B", "C", "D"], "answer": "C", "section": "Biology"},
]

chemistry_bank = [
    {"question": "The atomic number is equal to the number of:", "options": ["Neutrons", "Protons", "Electrons", "Nucleons"], "answer": "Protons", "section": "Chemistry"},
    {"question": "Water is considered a:", "options": ["Element", "Mixture", "Compound", "Ion"], "answer": "Compound", "section": "Chemistry"},
    {"question": "Which type of bond involves sharing of electrons?", "options": ["Ionic", "Covalent", "Metallic", "Hydrogen"], "answer": "Covalent", "section": "Chemistry"},
    {"question": "An acid is a substance with a pH:", "options": ["Equal to 7", "Greater than 7", "Less than 7", "Equal to 14"], "answer": "Less than 7", "section": "Chemistry"},
    {"question": "The study of carbon-containing compounds is:", "options": ["Inorganic Chemistry", "Organic Chemistry", "Biochemistry", "Physical Chemistry"], "answer": "Organic Chemistry", "section": "Chemistry"},
    {"question": "A solution that conducts electricity is called an:", "options": ["Insulator", "Electrolyte", "Solvent", "Precipitate"], "answer": "Electrolyte", "section": "Chemistry"},
    {"question": "Which gas is most abundant in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Nitrogen", "section": "Chemistry"},
    {"question": "In a reaction at equilibrium:", "options": ["Reactants are used up", "Products stop forming", "Forward and reverse rates are equal", "Heat is absorbed"], "answer": "Forward and reverse rates are equal", "section": "Chemistry"},
    {"question": "The process of a solid turning directly into a gas is:", "options": ["Evaporation", "Condensation", "Sublimation", "Melting"], "answer": "Sublimation", "section": "Chemistry"},
    {"question": "The rows in the periodic table are called:", "options": ["Groups", "Families", "Periods", "Columns"], "answer": "Periods", "section": "Chemistry"},
    {"question": "An exothermic reaction:", "options": ["Absorbs heat", "Releases heat", "Requires a catalyst", "Produces cold"], "answer": "Releases heat", "section": "Chemistry"},
    {"question": "Sulfuric acid is:", "options": ["H2SO4", "HCl", "HNO3", "CH3COOH"], "answer": "H2SO4", "section": "Chemistry"},
    {"question": "The smallest unit of a chemical compound is a:", "options": ["Atom", "Molecule", "Electron", "Mixture"], "answer": "Molecule", "section": "Chemistry"},
    {"question": "Which branch of chemistry deals with the study of heat changes?", "options": ["Thermochemistry", "Electrochemistry", "Biochemistry", "Kinetics"], "answer": "Thermochemistry", "section": "Chemistry"},
    {"question": "A mixture of sand and water is an example of a:", "options": ["Solution", "Suspension", "Compound", "Element"], "answer": "Suspension", "section": "Chemistry"},
    {"question": "Which particle has a negative charge?", "options": ["Proton", "Neutron", "Electron", "Nucleus"], "answer": "Electron", "section": "Chemistry"},
    {"question": "What is the pH of pure water?", "options": ["0", "7", "14", "5.5"], "answer": "7", "section": "Chemistry"},
    {"question": "Kinetics is the study of:", "options": ["Chemical bonding", "Reaction rates", "Atomic mass", "Energy levels"], "answer": "Reaction rates", "section": "Chemistry"},
]

physics_bank = [
    {"question": "Newton's second law is articulated by the formula:", "options": ["F = m/a", "F = m-a", "F = m*a", "F = a/m"], "answer": "F = m*a", "section": "Physics"},
    {"question": "The SI unit of force is:", "options": ["Joule", "Watt", "Newton", "Pascal"], "answer": "Newton", "section": "Physics"},
    {"question": "Energy of motion is called:", "options": ["Potential energy", "Kinetic energy", "Thermal energy", "Nuclear energy"], "answer": "Kinetic energy", "section": "Physics"},
    {"question": "Which principle states that an object submerged experiences an upward force equal to the weight of the fluid displaced?", "options": ["Newton's Law", "Archimedes' Principle", "Pascal's Law", "Boyle's Law"], "answer": "Archimedes' Principle", "section": "Physics"},
    {"question": "The time it takes for half of a radioactive substance to decay is its:", "options": ["Lifespan", "Decay constant", "Half-life", "Isotope time"], "answer": "Half-life", "section": "Physics"},
    {"question": "The splitting of a massive nucleus into smaller fragments is:", "options": ["Fusion", "Fission", "Radioactivity", "Beta decay"], "answer": "Fission", "section": "Physics"},
    {"question": "Sound waves cannot travel through:", "options": ["Water", "Steel", "Air", "Vacuum"], "answer": "Vacuum", "section": "Physics"},
    {"question": "What lens is thicker at the center than at the edges?", "options": ["Concave", "Convex", "Plano-concave", "Cylindrical"], "answer": "Convex", "section": "Physics"},
    {"question": "The opposite of electrical resistance is:", "options": ["Voltage", "Current", "Conductance", "Capacitance"], "answer": "Conductance", "section": "Physics"},
    {"question": "Coulomb's Law describes:", "options": ["Gravity between masses", "Electrostatic force between charges", "Magnetic field strength", "Nuclear forces"], "answer": "Electrostatic force between charges", "section": "Physics"},
    {"question": "Which is a vector quantity?", "options": ["Speed", "Distance", "Mass", "Velocity"], "answer": "Velocity", "section": "Physics"},
    {"question": "The rate of doing work is:", "options": ["Force", "Power", "Momentum", "Impulse"], "answer": "Power", "section": "Physics"},
    {"question": "Which logic gate outputs true ONLY if both inputs are true?", "options": ["OR", "NOT", "AND", "XOR"], "answer": "AND", "section": "Physics"},
    {"question": "Temperature determines the direction of flow of:", "options": ["Light", "Heat", "Sound", "Electricity"], "answer": "Heat", "section": "Physics"},
    {"question": "A device that converts mechanical energy into electrical energy is:", "options": ["Motor", "Generator", "Transformer", "Battery"], "answer": "Generator", "section": "Physics"},
    {"question": "Momentum is the product of mass and:", "options": ["Acceleration", "Velocity", "Force", "Time"], "answer": "Velocity", "section": "Physics"},
    {"question": "Which of the following describes torque?", "options": ["Linear force", "Rotational force", "Energy over time", "Mass in motion"], "answer": "Rotational force", "section": "Physics"},
    {"question": "The base unit of thermodynamic temperature is:", "options": ["Celsius", "Fahrenheit", "Kelvin", "Rankine"], "answer": "Kelvin", "section": "Physics"},
]

math_bank = [
    {"question": "What is 15% of 200?", "options": ["15", "20", "30", "45"], "answer": "30", "section": "Mathematics"},
    {"question": "Solve for x: 3x - 5 = 10", "options": ["3", "5", "15", "2"], "answer": "5", "section": "Mathematics"},
    {"question": "The perimeter of a rectangle with length 5 and width 3 is:", "options": ["15", "8", "16", "34"], "answer": "16", "section": "Mathematics"},
    {"question": "Sum of angles in a triangle is:", "options": ["90°", "180°", "360°", "270°"], "answer": "180°", "section": "Mathematics"},
    {"question": "What is the median of 3, 5, 8, 2, 7?", "options": ["3", "5", "7", "8"], "answer": "5", "section": "Mathematics"},
    {"question": "Which is a prime number?", "options": ["15", "21", "29", "33"], "answer": "29", "section": "Mathematics"},
    {"question": "What is the area of a circle with radius r?", "options": ["πr", "2πr", "πr²", "2πr²"], "answer": "πr²", "section": "Mathematics"},
    {"question": "If 1 meter = 100 cm, how many cm in 2.5 meters?", "options": ["25", "250", "205", "2500"], "answer": "250", "section": "Mathematics"},
    {"question": "What is 2^3?", "options": ["6", "8", "9", "12"], "answer": "8", "section": "Mathematics"},
    {"question": "The ratio 4:12 simplified is:", "options": ["1:2", "1:3", "2:6", "1:4"], "answer": "1:3", "section": "Mathematics"},
    {"question": "The probability of flipping a coin and getting heads is:", "options": ["0", "0.25", "0.5", "1"], "answer": "0.5", "section": "Mathematics"},
    {"question": "If a shirt costs $50 and is discounted by 20%, the new price is:", "options": ["$30", "$40", "$45", "$35"], "answer": "$40", "section": "Mathematics"},
    {"question": "Which logical gate returns '0' if all inputs are '0'?", "options": ["OR", "AND", "NOT", "All of these except NOT"], "answer": "All of these except NOT", "section": "Mathematics"},
    {"question": "The average of 10, 20, and 30 is:", "options": ["15", "20", "25", "30"], "answer": "20", "section": "Mathematics"},
    {"question": "Find the next number in the series: 2, 4, 8, 16, ___", "options": ["24", "30", "32", "64"], "answer": "32", "section": "Mathematics"},
    {"question": "Which of these is a composite number?", "options": ["11", "13", "15", "17"], "answer": "15", "section": "Mathematics"},
    {"question": "The LCM of 4 and 6 is:", "options": ["10", "12", "24", "2"], "answer": "12", "section": "Mathematics"},
    {"question": "What is 5! (5 factorial)?", "options": ["15", "60", "120", "25"], "answer": "120", "section": "Mathematics"},
    {"question": "A quadrilateral has how many sides?", "options": ["3", "4", "5", "6"], "answer": "4", "section": "Mathematics"},
    {"question": "1 km is equal to how many meters?", "options": ["100", "10", "1000", "10000"], "answer": "1000", "section": "Mathematics"},
    {"question": "Simplify: 5(x + 2)", "options": ["5x + 2", "5x + 10", "x + 10", "5x + 7"], "answer": "5x + 10", "section": "Mathematics"},
    {"question": "Volume of a cube with side 3 cm is:", "options": ["9 cm³", "27 cm³", "18 cm³", "6 cm³"], "answer": "27 cm³", "section": "Mathematics"},
    {"question": "Pie chart is a form of:", "options": ["Algebra", "Data Presentation", "Geometry", "Calculus"], "answer": "Data Presentation", "section": "Mathematics"},
    {"question": "Calculate the mode: 2, 2, 3, 4, 5", "options": ["2", "3", "4", "5"], "answer": "2", "section": "Mathematics"},
    {"question": "Sum of interior angles of a quadrilateral is:", "options": ["180°", "270°", "360°", "720°"], "answer": "360°", "section": "Mathematics"},
]

computer_bank = [
    {"question": "Which is an operating system?", "options": ["Microsoft Word", "Google Chrome", "Linux", "Intel"], "answer": "Linux", "section": "Computer"},
    {"question": "The brain of the computer is the:", "options": ["RAM", "Hard Drive", "CPU", "Motherboard"], "answer": "CPU", "section": "Computer"},
    {"question": "HTML stands for:", "options": ["Hyper Text Markup Language", "High Tech Machine Logic", "Hyper Tabular Markup List", "Home Tool Markup Language"], "answer": "Hyper Text Markup Language", "section": "Computer"},
    {"question": "Which of these is a network topology?", "options": ["Star", "Square", "Triangle", "Circle"], "answer": "Star", "section": "Computer"},
    {"question": "First generation computers used:", "options": ["Transistors", "Integrated Circuits", "Vacuum Tubes", "Microprocessors"], "answer": "Vacuum Tubes", "section": "Computer"},
    {"question": "Which is an example of Office Automation software?", "options": ["Adobe Photoshop", "Microsoft Excel", "AutoCAD", "Visual Studio"], "answer": "Microsoft Excel", "section": "Computer"},
    {"question": "A collection of related data is called a:", "options": ["Database", "Web page", "Network", "Virus"], "answer": "Database", "section": "Computer"},
    {"question": "Phishing is a type of:", "options": ["Hardware issue", "Network protocol", "Cyber-Attack", "Programming Language"], "answer": "Cyber-Attack", "section": "Computer"},
    {"question": "What does LAN stand for?", "options": ["Local Area Node", "Large Area Network", "Local Area Network", "Logical Area Network"], "answer": "Local Area Network", "section": "Computer"},
    {"question": "Which of the following is an input device?", "options": ["Monitor", "Printer", "Keyboard", "Speaker"], "answer": "Keyboard", "section": "Computer"},
    {"question": "SQL stands for:", "options": ["Structured Query Language", "Simple Question Language", "System Query Logic", "Standard Quotation Lingo"], "answer": "Structured Query Language", "section": "Computer"},
    {"question": "A malicious software designed to disrupt or damage a computer system is:", "options": ["Malware", "Firewall", "Router", "Compiler"], "answer": "Malware", "section": "Computer"},
    {"question": "Which layer is NOT in the OSI model?", "options": ["Physical", "Transport", "Internet", "Application"], "answer": "Internet", "section": "Computer"},
    {"question": "Ethical hacking is also known as:", "options": ["Black hat hacking", "White hat hacking", "Grey hat hacking", "Cracking"], "answer": "White hat hacking", "section": "Computer"},
    {"question": "What does a DBMS do?", "options": ["Manages networks", "Compiles code", "Manages databases", "Tests hardware"], "answer": "Manages databases", "section": "Computer"},
    {"question": "CSS is used for:", "options": ["Styling web pages", "Creating databases", "Building operating systems", "Network routing"], "answer": "Styling web pages", "section": "Computer"},
    {"question": "What kind of memory is RAM?", "options": ["Non-volatile", "Volatile", "Optical", "Magnetic"], "answer": "Volatile", "section": "Computer"},
    {"question": "Which of these is used for web development?", "options": ["JavaScript", "BIOS", "Ethernet", "VGA"], "answer": "JavaScript", "section": "Computer"},
]

def generate_test_questions():
    questions = []
    
    # Needs: English:10, GK:10, Ped:10, Bio:12, Chem:12, Phy:12, Math:22, Comp:12 = 100
    # Our banks might not have exactly this many if I didn't write enough. Let's make sure we pad them if needed.
    
    def get_q(bank, count):
        # Allow repetition if bank is smaller than count
        if len(bank) >= count:
            selection = random.sample(bank, count)
        else:
            selection = bank.copy()
            while len(selection) < count:
                selection.append(random.choice(bank).copy())
        return selection
    
    questions.extend(get_q(english_bank, 10))
    questions.extend(get_q(gk_bank, 10))
    questions.extend(get_q(pedagogy_bank, 10))
    questions.extend(get_q(biology_bank, 12))
    questions.extend(get_q(chemistry_bank, 12))
    questions.extend(get_q(physics_bank, 12))
    questions.extend(get_q(math_bank, 22))
    questions.extend(get_q(computer_bank, 12))
    
    # Format the numbering
    for i, q in enumerate(questions):
        # remove old numbering like "1. ", "51. "
        q_text = re.sub(r'^\d+\.\s*', '', q['question'])
        q['question'] = f"{i+1}. {q_text}"
        
    return questions

import os

for i in range(1, 10):
    filename = f"jst-quiz{i}.html"
    filepath = os.path.join(r"C:\Users\Hon3y Chauhan\Desktop\Jst-Mock-Test", filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Generate new questions
        new_q = generate_test_questions()
        qs_json = json.dumps(new_q, indent=4)
        
        # Replace the `const questions = [ ... ];` block
        # We need to find `const questions = [` and the corresponding ending `];`
        pattern = r"const questions = \[\s*//.*?\];"
        
        # In jst-quiz1.html it starts with:
        # const questions = [
        #    // =======================
        #    // SCIENCE – BIOLOGY (Q1–20)
        
        # We can use a simpler approach. Find `const questions = [` and the next `];` after the `]`
        # Using regex to replace the array
        content = re.sub(r'const questions = \[\s*.*?\s*\];', f"const questions = {qs_json};", content, flags=re.DOTALL)
        
        # Wait, the end of the array is `];`, but there might be other `];` in the file.
        # Let's inspect the file structure in python.
        
        # A safer approach:
        start_idx = content.find("const questions = [")
        if start_idx != -1:
            end_idx = content.find("];", start_idx) + 2
            
            # double check we are not matching a nested array closing
            # we should look for "    const questions = [\n" or similar
            # simpler method: replace from `const questions = [` up to the next `];\n`
            
            # Let's write the new content
            new_content = content[:start_idx] + f"const questions = {qs_json};\n" + content[end_idx:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
    else:
        print(f"File {filename} not found.")
