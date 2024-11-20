def quiz_beginner():
    score = 0
    print("\n1. What is a block in programming?")
    print("a) A set of statements that belong together as a group")
    print("b) A boolean variable that signals when some condition exists in a program")
    print("c) A set of statements that execute in order in which they appear")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "a":
        print("Correct")
        score+= 2
    else:
        print("Incorrect, the correct answer is a")

    print("\n2. What is a flag in programming?")
    print("a) A piece of cloth attached to a pole ")
    print("b) A boolean variable that signals when some condition exists in a program")
    print("c) A decision structure that has only one alternative path execution")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "b":
         print("Correct")
         score+= 1
    else:
        print("Incorrect, the correct answer is b")

    print("\n3. Which answer choice defines control structure in programming")
    print("a) A logical design that controls the order in which a set of statements execute")
    print("b) The structure of something that is controlled")
    print("c) The operator that connects two values and determines whether a specific relationship exists between them")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "a":
        print("Correct")
        score+= 1
    else:
        print("Incorrect, the correct answer is a")

    print(f"\nYou scored {score}/4.")
    if score == 4:
        print("Awsome!!! You're on a roll.")
    elif score == 2:
        print("Nice job! keep studying.")
    else:
        print("Don't worry, keep practicing.")
quiz_beginner()

        
