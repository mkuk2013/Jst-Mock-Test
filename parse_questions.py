import json
import re

user_text = r"""
ENGLISH (1–10)
======================

1. Which sentence uses correct punctuation?
A) We need to buy several items: milk, bread, and eggs.
B) We need to buy several items; milk, bread, and eggs.
C) We need to buy several items, milk, bread, and eggs.
D) We need to buy: several items, milk, bread, and eggs.
Correct Answer: A

2. Identify the abstract noun:
A) Storm
B) Crew
C) Bravery
D) Saved
Correct Answer: C

3. Present Perfect tense:
A) has finish
B) have finished
C) has finished
D) finishes
Correct Answer: C

4. Apostrophe:
A) bus'
B) bus's
C) buses'
D) bus'es
Correct Answer: B

5. While I ______ dinner, phone rang:
A) am cooking
B) was cooking
C) cooked
D) have cooked
Correct Answer: B

6. Collective noun:
A) Flowers
B) Bouquet
C) Petals
D) Garden
Correct Answer: B

7. Compound sentence:
A) comma only
B) and only
C) ; and
D) , and
Correct Answer: D

8. Past continuous:
A) were playing
B) was playing
C) are playing
D) played
Correct Answer: A

9. Direct speech:
A) no comma
B) comma correct
C) capital error
D) wrong format
Correct Answer: B

10. Future simple:
A) going to
B) will go
C) will going
D) present
Correct Answer: B
🌍 General Knowledge (11–20)

11. Who is the current Governor of the State Bank of Pakistan?
A) Reza Baqir
B) Jameel Ahmad
C) Yaseen Anwar
D) Ashraf Mahmood Wathra
👉 ✅ Correct Answer: B

12. The main feature distinguishing the Constitution of 1962 from that of 1956 was:
A) Federal system
B) Parliamentary system
C) Presidential system
D) Islamic provisions
👉 ✅ Correct Answer: C

13. How many seats are allocated to Sindh in the Senate of Pakistan?
A) 20
B) 23
C) 25
D) 30
👉 ✅ Correct Answer: B

14. The Warsak Dam (KPK) is built on which river?
A) Indus River
B) Kabul River
C) Chenab River
D) Hub River
👉 ✅ Correct Answer: B

15. Who is the current Chairman of (NADRA)?
A) Tariq Malik
B) Khalid Latif
C) Lieutenant General Muhammad Munir Afsar
D) Ahsan Iqbal
👉 ✅ Correct Answer: C

16. Poverty in Pakistan is most directly caused by:
A) High foreign exchange reserves
B) Lack of skilled education and unemployment
C) Excessive tourism revenue
D) Surplus agricultural production
👉 ✅ Correct Answer: B

17. The largest natural freshwater lake in Pakistan is:
A) Keenjhar Lake
B) Saif-ul-Maluk Lake
C) Manchar Lake
D) Hanna Lake
👉 ✅ Correct Answer: C

18. Which Article of the Constitution of 1973 of Pakistan defines the fundamental rights of citizens?
A) Article 8–28
B) Article 25–40
C) Article 50–60
D) Article 10–20
👉 ✅ Correct Answer: A

19. On a map, the symbols that show roads, trees, and buildings are called:
A) Grid lines
B) Map legends
C) Scale bars
D) Compass roses
👉 ✅ Correct Answer: B

20. The people of the Stone Age used which of the following tools for hunting?
A) Steel spear
B) Wooden clubs
C) Stone hand axes
D) Bronze knives
👉 ✅ Correct Answer: C

🎓 Pedagogy (21–22)

21. The idea that knowledge comes from experience is:
A) Rationalism
B) Deductive reasoning
C) Logic
D) Empiricism
👉 ✅ Correct Answer: D

22. Which type of evaluation is carried out at the end of a course of study?
A) Summative
B) Assessment
C) Formative
D) Both (a) and (b)
👉 ✅ Correct Answer: A
🎓 Pedagogy (23–40)

23. The most significant approach of evaluation is:
A) Continuous and comprehensive evaluation
B) Conducting objective term end examination
C) Maintaining cumulative records of students
D) Semester system evaluation
👉 ✅ Correct Answer: A

24. When some students are deliberately attempting to disturb the discipline of the class by making mischief, what will be your role as a teacher?
A) Expelling those students
B) Isolate those students
C) Reform the group with your authority
D) Giving them no opportunity for introspection and improve their behavior
👉 ✅ Correct Answer: C

25. Those teachers are popular among students who:
A) Develop intimacy with them
B) Help them solve their problems
C) Award good grades
D) Take classes for extra tuition fee
👉 ✅ Correct Answer: B

26. The essence of an effective classroom environment is:
A) A variety of teaching instructional facilities
B) Pin-drop silence
C) Lively student–teacher interaction and effective learning
D) Strict discipline
👉 ✅ Correct Answer: C

27. In order to modify the undesirable behavior of a student, the most effective and pragmatic method is:
A) To punish the student and expel from school
B) To bring it to the notice of parents and impose fines
C) To find out the reasons for the undesirable behavior and provide remedies
D) All of the above
👉 ✅ Correct Answer: C

28. If students pass remarks on you while you are working as a teacher, you should:
A) Punish them
B) Expel them from the college
C) Take revenge while evaluating internal test copies
D) Be impartial at the time of evaluation
👉 ✅ Correct Answer: D

29. The ability to locate, evaluate, and effectively use information is an important trait known as:
A) Critical thinking
B) Information processing
C) Hearing
D) Selective attention
👉 ✅ Correct Answer: A

30. With smaller and inclusive classes, teachers are much more able to:
A) Identify learning problems
B) Provide individual attention
C) Adapt instruction to individual differences among students
D) All the above
👉 ✅ Correct Answer: D

31. 'Individual differences' in the learning process are given the maximum importance in:
A) Naturalism
B) Essentialism
C) Idealism
D) Pragmatism
👉 ✅ Correct Answer: D

32. While teaching in the classroom, any kind of work that involves two or more students, is a form of:
A) Collaborative learning
B) Collaborative project
C) Collaborative work
D) Collaborative effort
👉 ✅ Correct Answer: A

33. An assessment used to identify difficulties in the learning process is called:
A) Initial assessment
B) Diagnostic assessment
C) Formative assessment
D) Summative assessment
👉 ✅ Correct Answer: B

34. Anything that causes a reaction is called:
A) Learning
B) Stimulus
C) Connectionism
D) Physical objects
👉 ✅ Correct Answer: B

35. A scoring guide used to evaluate the quality of students is called:
A) Rubrics
B) Checklists
C) Inventories
D) Rating scales
👉 ✅ Correct Answer: A

36. The teacher wants students to practice by repetition of some learning content, he normally uses a teaching method:
A) Drill method
B) Recitation
C) Skill
D) None of these
👉 ✅ Correct Answer: A

37. Providing temporary support and encouragement to students until help is no longer needed is called:
A) Scaffolding
B) Criticizing
C) Appreciating
D) None of these
👉 ✅ Correct Answer: A

38. Validity of an assessment relates to the ___________ of an assessment:
A) Usefulness
B) Quality
C) Consistency
D) Relevance
👉 ✅ Correct Answer: D

39. Bloom’s taxonomy is a set of ……….. learning domains:
A) Two
B) Three
C) Four
D) Five
👉 ✅ Correct Answer: B

40. Which of the following is a key characteristic of microteaching?
A) Large group instructions and learning
B) Mastering multiple skills at once
C) Scaled-down teaching in multiple teachers
D) Lack of feedback mechanism
👉 ✅ Correct Answer: C
41. Ribosomes are mainly composed of:
A) Lipid & protein
B) DNA & lipid
C) RNA & protein
D) Carbohydrates
👉 ✅ Correct Answer: C

42. Which organelle modifies and packages proteins?
A) Endoplasmic Reticulum
B) Golgi apparatus
C) Lysosome
D) Nucleus
👉 ✅ Correct Answer: B

43. Chromosomes become visible during:
A) Prophase
B) Interphase
C) Telophase
D) Cytokinesis
👉 ✅ Correct Answer: A

44. During meiosis, if crossing over fails to occur, which of the following will be most affected?
A) Chromosome number
B) DNA replication
C) Genetic variation
D) Spindle formation
👉 ✅ Correct Answer: C

45. Diploid number is represented by:
A) n
B) 2n
C) n²
D) 4n
👉 ✅ Correct Answer: B

46. G2 phase prepares cell for:
A) DNA replication
B) Cell division
C) Protein digestion
D) Respiration
👉 ✅ Correct Answer: B

47. Interphase includes:
A) Cytokinesis only
B) Prophase, Metaphase
C) Anaphase, Telophase
D) G1, S, G2
👉 ✅ Correct Answer: D

48. Chromosomes align at equator in:
A) Metaphase
B) Prophase
C) Anaphase
D) Telophase
👉 ✅ Correct Answer: A

49. Synapsis occurs in:
A) Leptotene
B) Zygotene
C) Diplotene
D) Diakinesis
👉 ✅ Correct Answer: B

50. Meiosis II is similar to:
A) Meiosis I
B) Cytokinesis
C) Interphase
D) Mitosis
👉 ✅ Correct Answer: D

51. Chromosome number reduces from 2n to n in:
A) Prophase I
B) Anaphase I
C) Telophase II
D) Metaphase II
👉 ✅ Correct Answer: B

52. A cell has 2n = 8 chromosomes. After meiosis II, each daughter cell will have:
A) 8 chromosomes with 2 chromatids each
B) 4 chromosomes with 2 chromatids each
C) 4 chromosomes with 1 chromatid each
D) 8 chromosomes with 1 chromatid each
👉 ✅ Correct Answer: C

⚗️ Chemistry (53–64)

53. Which of the following compounds is formed by ionic bonding?
A) CH₄
B) H₂O
C) NaCl
D) CO₂
👉 ✅ Correct Answer: C

54. In a covalent bond, atoms share electrons to:
A) Lose electrons
B) Gain electrons
C) Complete their valence shells
D) Form ions
👉 ✅ Correct Answer: C

55. Which molecule contains a coordinate covalent (dative) bond?
A) NH₃
B) NH₄⁺
C) H₂
D) Cl₂
👉 ✅ Correct Answer: B

56. Hydrogen bonding occurs when hydrogen is bonded to:
A) Any metal
B) Carbon only
C) Highly electronegative atoms like N, O, or F
D) Noble gases
👉 ✅ Correct Answer: C

57. Which of the following has hydrogen bonding?
A) CH₄
B) H₂O
C) CO₂
D) NaCl
👉 ✅ Correct Answer: B

58. Which of the following is a strong electrolyte?
A) Glucose
B) NaCl
C) Urea
D) Ethanol
👉 ✅ Correct Answer: B

59. In electrochemistry, oxidation is defined as:
A) Gain of electrons
B) Loss of electrons
C) Gain of protons
D) Loss of neutrons
👉 ✅ Correct Answer: B

60. A true solution is characterized by:
A) Particle size greater than 1000 nm
B) Settling of particles on standing
C) Homogeneous mixture
D) Visible particles
👉 ✅ Correct Answer: C

61. Which of the following is an example of a suspension?
A) Salt in water
B) Sugar in water
C) Sand in water
D) Vinegar
👉 ✅ Correct Answer: C

62. The electrode where reduction occurs is called:
A) Anode
B) Cathode
C) Salt bridge
D) Electrolyte
👉 ✅ Correct Answer: B

63. Which gas is primarily responsible for global warming?
A) Oxygen
B) Nitrogen
C) Carbon dioxide
D) Hydrogen
👉 ✅ Correct Answer: C

64. Acid rain is mainly caused by the presence of:
A) CO₂ and O₂
B) SO₂ and NO₂
C) H₂ and Cl₂
D) CH₄ and NH₃
👉 ✅ Correct Answer: B
⚡ Physics (65–76)

65. Which Newton's law suggests the relation between force and acceleration?
A) 2nd law
B) 3rd law
C) 1st law
D) None of these
👉 ✅ Correct Answer: A

66. When current flows in a conductor, the velocity of electrons is known as:
A) Thermal Velocity
B) Uniform Velocity
C) Drift Velocity
D) Constant Velocity
👉 ✅ Correct Answer: C

67. Which of the following is degree temperature scales?
A) Kelvin
B) Celsius
C) Fahrenheit
D) Both B and C
👉 ✅ Correct Answer: D

68. According to Boyle’s law, which quantity remains constant?
A) Volume
B) Pressure
C) Number of moles
D) Temperature
👉 ✅ Correct Answer: D

69. The unit of radioactivity is:
A) Gray
B) Sievert
C) Becquerel
D) Tesla
👉 ✅ Correct Answer: C

70. In alpha decay, the atomic number decreases by:
A) 1
B) 2
C) 3
D) 4
👉 ✅ Correct Answer: B

71. In Bohr's model, electrons revolve in:
A) Random path
B) Elliptical Orbits
C) Fixed Circular Path
D) Straight lines
👉 ✅ Correct Answer: C

72. The energy of an electron in nth orbit is proportional to:
A) n
B) 1/n
C) 1/n²
D) n²
👉 ✅ Correct Answer: C

73. Doping a semiconductor means:
A) Heating
B) Adding impurities
C) Removing Electrons
D) Cooling it
👉 ✅ Correct Answer: B

74. A P.N Junction diode conducts in:
A) Reverse Bias only
B) Forward Bias only
C) Both directions
D) No direction
👉 ✅ Correct Answer: B

75. The speed of light in vacuum is:
A) 3 × 10⁸ m/s
B) 3 × 10⁶ m/s
C) 3 × 10⁴ m/s
D) 3 × 10² m/s
👉 ✅ Correct Answer: A

76. Total internal reflection occurs when:
A) Light goes from rarer to denser
B) Light goes from denser to rarer
C) Angle is zero
D) Speed increases
👉 ✅ Correct Answer: B

📊 Mathematics (77–88)

77. The ability of all observations in a data set to cluster around a central point is called:
A) Probability
B) Ratio proportion
C) Central Tendency
D) Variance
👉 ✅ Correct Answer: C

78. If A (3, 0) and B (0, 3) are any two points in the plane, then |AB| = ?
A) 6 Units
B) 6√2 Units
C) 3√2 Units
D) 2√3 Units
👉 ✅ Correct Answer: C

79. The simple interest on Rs 5000 at 8% per annum for 3 years is:
A) Rs 1000
B) Rs 1100
C) Rs 1200
D) Rs 1500
👉 ✅ Correct Answer: C

80. For any set of positive numbers, the correct relationship among Arithmetic Mean (AM), Geometric Mean (GM), and Harmonic Mean (HM) is:
A) AM < GM < HM
B) AM > GM > HM
C) GM > AM > HM
D) HM > GM > AM
👉 ✅ Correct Answer: B

81. Find the compound amount on Rs 10,000 at 10% per annum for 2 years:
A) Rs 11,000
B) Rs 12,100
C) Rs 12,700
D) Rs 13,000
👉 ✅ Correct Answer: B

82. A bag contains 5 red, 3 green, and 2 blue balls. One ball is drawn at random. What is the probability that it is not blue?
A) 2/10
B) 8/10
C) 5/10
D) 3/10
👉 ✅ Correct Answer: B

83. A train is moving at a speed of 90 km/h. What distance will it cover in 20 minutes?
A) 30 km
B) 25 km
C) 20 km
D) 15 km
👉 ✅ Correct Answer: A

84. Find the distance between points P(-2, 3) and Q(4, -1):
A) √40
B) √36
C) √50
D) √52
👉 ✅ Correct Answer: A

85. The smallest number divisible by 12, 15, and 20 is:
A) 60
B) 120
C) 180
D) 240
👉 ✅ Correct Answer: A

86. A TV is sold for Rs 23,000 at a profit of 15%. What was the original cost price of the TV?
A) Rs 19,500
B) Rs 20,000
C) Rs 21,000
D) Rs 22,000
👉 ✅ Correct Answer: B

87. Find 20% of 450:
A) 80
B) 90
C) 100
D) 120
👉 ✅ Correct Answer: B

88. A man walks 12 km in 2 hours. His speed is:
A) 4 km/h
B) 5 km/h
C) 6 km/h
D) 8 km/h
👉 ✅ Correct Answer: C

💻 Computer (89–100)

89. Which of the following best describes the "Von Neumann Bottleneck" in computer architecture?
A) The limitation of processing speed due to heat dissipation in CPUs
B) The throughput limitation caused by the shared bus between the CPU and memory
C) The inability of an Operating System to handle multi-threaded processes
D) The physical space constraint of transistors on a silicon wafer
👉 ✅ Correct Answer: B

90. In the context of computer generations, which technology was the primary catalyst for the transition from the Third to the Fourth Generation?
A) The replacement of magnetic cores with semiconductor memory
B) The invention of the Integrated Circuit (IC)
C) The development of Very Large Scale Integration (VLSI) allowing for microprocessors
D) The introduction of COBOL and FORTRAN high-level languages
👉 ✅ Correct Answer: C

91. In a Preemptive Multitasking Operating System, what happens when the "time slice" (quantum) of a process expires?
A) The process is moved to the "Blocked" state until I/O is ready
B) The process is terminated to free up system resources
C) The kernel triggers a context switch to move the process back to the "Ready" queue
D) The process remains in the "Running" state but with lower priority
👉 ✅ Correct Answer: C

92. When implementing Office Automation in a distributed environment, which protocol is primarily responsible for ensuring the reliable delivery of email between mail servers?
A) POP3
B) IMAP
C) SMTP
D) SNMP
👉 ✅ Correct Answer: C

93. Within the OSI Model, which layer is responsible for "Dialog Control" and "Token Management" between two communicating applications?
A) Transport Layer
B) Session Layer
C) Presentation Layer
D) Data Link Layer
👉 ✅ Correct Answer: B

94. In Web Development, which CSS property is used to create a "Flexible Box" layout that can automatically adjust its dimensions to fill available space?
A) display: grid;
B) position: relative;
C) display: flex;
D) float: left;
👉 ✅ Correct Answer: C

95. A "Man-in-the-Middle" (MitM) attack that specifically targets the resolution of domain names to IP addresses on a local network is known as:
A) SQL Injection
B) DNS Spoofing / Poisoning
C) Cross-Site Scripting (XSS)
D) Brute Force Attack
👉 ✅ Correct Answer: B

96. In a Database Management System (DBMS), which property of ACID ensures that a transaction remains committed even in the event of a system failure or power loss?
A) Atomicity
B) Consistency
C) Isolation
D) Durability
👉 ✅ Correct Answer: D

97. Which of the following is a "Type 1" Hypervisor used in modern cloud computing environments?
A) VMware Workstation
B) Oracle VirtualBox
C) Xen or Microsoft Hyper-V
D) Adobe Creative Cloud
👉 ✅ Correct Answer: C

98. What is the primary difference between a "Hub" and a "Switch" in Computer Networking?
A) A Hub operates at the Network Layer, while a Switch operates at the Physical Layer
B) A Hub broadcasts data to all ports, while a Switch uses MAC addresses to unicast data
C) A Hub provides encryption, while a Switch does not
D) A Hub is used for WANs, while a Switch is strictly for LANs
👉 ✅ Correct Answer: B

99. In Ethical Hacking, "Fuzzing" is a technique primarily used for:
A) Cracking complex WPA2 Wi-Fi passwords
B) Sending massive amounts of random data to an application to find memory leaks or crashes
C) Social engineering users into revealing their credentials
D) Mapping the physical topology of a remote network
👉 ✅ Correct Answer: B

100. Which SQL clause is used to filter the results of an aggregate function (like SUM or AVG) in a database query?
A) WHERE
B) ORDER BY
C) HAVING
D) GROUP BY
👉 ✅ Correct Answer: C
"""

# Improved parsing script
import json
import re

def remove_emojis(text):
    # This regex matches common emojis but keeps math symbols and other useful non-ASCII chars
    # We'll just define what we want to keep or explicitly remove emojis.
    # A safer way to remove emojis while keeping superscripts like ²
    emoji_pattern = re.compile("["
        u"\U0001f600-\U0001f64f"  # emoticons
        u"\U0001f300-\U0001f5ff"  # symbols & pictographs
        u"\U0001f680-\U0001f6ff"  # transport & map symbols
        u"\U0001f1e0-\U0001f1ff"  # flags (iOS)
        u"\u2702-\u27b0"
        u"\u24c2-\U0001f251"
        u"\uD83C[\uDF00-\uDFFF]"
        u"\uD83D[\uDC00-\uDDFF]"
        u"\uD83E[\uDE00-\uDEFF]"
        u"\uD83D[\uDE00-\uDE4F]"
        u"\uD83D[\uDE80-\uDEFF]"
        u"\U00002100-\U0000214F" # letterlike symbols
        u"\U00002300-\U000023FF" # misc technical
        u"\U00002B00-\U00002BFF" # misc symbols and arrows
        "]+", flags=re.UNICODE)
    # Also explicitly remove specific emojis/symbols from user text
    text = re.sub(r'[🌍🎓⚗️⚡📊💻👉✅]', '', text)
    return emoji_pattern.sub(r' ', text)

def parse_questions(text):
    # Standardize headers
    text = re.sub(r'ENGLISH\s?\(110\)', '\nSECTION: English\n', text)
    text = re.sub(r'General Knowledge\s?\(1120\)', '\nSECTION: General Knowledge\n', text)
    text = re.sub(r'Pedagogy\s?\(2122\)', '\nSECTION: Teaching and Learning Pedagogies\n', text)
    text = re.sub(r'Pedagogy\s?\(2340\)', '\nSECTION: Teaching and Learning Pedagogies\n', text)
    text = re.sub(r'Biology\s?\(4152\)', '\nSECTION: Biology\n', text)
    text = re.sub(r'Chemistry\s?\(5364\)', '\nSECTION: Chemistry\n', text)
    text = re.sub(r'Physics\s?\(6576\)', '\nSECTION: Physics\n', text)
    text = re.sub(r'Mathematics\s?\(7788\)', '\nSECTION: Mathematics\n', text)
    text = re.sub(r'Computer\s?\(89100\)', '\nSECTION: Computer\n', text)

    text = remove_emojis(text)
    
    questions = []
    current_section = "General Knowledge"
    
    # Split text by question numbers
    q_blocks = re.split(r'\n(\d+)\.\s+', text)
    
    # Section tracking
    def get_section(n):
        if 1 <= n <= 10: return "English"
        if 11 <= n <= 20: return "General Knowledge"
        if 21 <= n <= 40: return "Teaching and Learning Pedagogies"
        if 41 <= n <= 52: return "Biology"
        if 53 <= n <= 64: return "Chemistry"
        if 65 <= n <= 76: return "Physics"
        if 77 <= n <= 88: return "Mathematics"
        if 89 <= n <= 100: return "Computer"
        return "General Knowledge"

    # q_blocks[0] is the text before question 1
    for i in range(1, len(q_blocks), 2):
        q_num = int(q_blocks[i])
        content = q_blocks[i+1]
        
        # Split content into question text, options, and answer
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        q_text = ""
        options = []
        correct_letter = ""
        
        # The first lines are the question text (until an option start)
        j = 0
        while j < len(lines) and not re.match(r'^[A-D]\)', lines[j]):
            if "Correct Answer" not in lines[j]:
                q_text += " " + lines[j]
            j += 1
        
        q_text = q_text.strip()
        
        # Parse options
        while j < len(lines) and re.match(r'^[A-D]\)', lines[j]):
            opt_text = re.sub(r'^[A-D]\)\s*', '', lines[j])
            options.append(opt_text)
            j += 1
            
        # Parse answer
        for line in lines[j:]:
            ans_match = re.search(r'(?:Correct Answer|Correct Answer):\s*([A-D])', line)
            if ans_match:
                correct_letter = ans_match.group(1)
                break
        
        if not correct_letter:
            # Check the whole block for answer if not found in trailing lines
            ans_match = re.search(r'(?:Correct Answer|Correct Answer):\s*([A-D])', content)
            if ans_match:
                correct_letter = ans_match.group(1)

        # Map letter to text
        answer_text = ""
        if correct_letter:
            idx = ord(correct_letter) - ord('A')
            if idx < len(options):
                answer_text = options[idx]
            else:
                answer_text = correct_letter
        
        questions.append({
            "question": f"{q_num}. {q_text}",
            "options": options,
            "answer": answer_text,
            "section": get_section(q_num)
        })

    return questions

qs = parse_questions(user_text)

# Validation
if len(qs) != 100:
    print(f"ERROR: Only parsed {len(qs)} questions instead of 100.")
    # Identify missing
    existing = {int(re.match(r'(\d+)\.', q['question']).group(1)) for q in qs}
    missing = [n for n in range(1, 101) if n not in existing]
    print(f"Missing: {missing}")
else:
    print("SUCCESS: Parsed all 100 questions.")

with open('/tmp/questions.json', 'w', encoding='utf-8') as f:
    json.dump(qs, f, indent=4, ensure_ascii=False)
