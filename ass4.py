knowledgeBase = [ 
    ({"Files are not syncing", "Internet is disconnected"}, "Network issue"), 
    ({"Network issue"}, "Reconnect to the internet"), 
    ({"Files are not syncing", "OneDrive storage is full"}, "Storage issue"), 
    ({"Storage issue"}, "Free up OneDrive storage"), 
    ({"Files are not syncing", "OneDrive account is signed out"}, "Account issue"), 
    ({"Account issue"}, "Sign in to OneDrive"), 
    ({"Files are not syncing", "OneDrive is not responding"}, "Application issue"), 
    ({"Application issue"}, "Restart OneDrive"), 
    ({"Files are not syncing", "OneDrive sync is disabled"}, "Sync settings issue"), 
    ({"Sync settings issue"}, "Enable OneDrive sync") 
] 
 
def forwardChaining(knowledgeBase, initialFacts): 
    knownFacts = list(initialFacts) 
    addedNewFact = True 
 
    while addedNewFact: 
        addedNewFact = False 
 
        for rule in knowledgeBase: 
            consequent = rule[1] 
 
            if consequent not in knownFacts: 
                if rule[0] <= set(knownFacts): 
                    knownFacts.append(consequent) 
                    addedNewFact = True 
 
    return knownFacts 
 
def backwardChaining(knowledgeBase, knownFacts, goal): 
    if goal in knownFacts: 
        return True 
 
    matchingRules = [] 
 
    for rule in knowledgeBase: 
        antecedents = rule[0] 
        consequent = rule[1] 
 
        if consequent == goal: 
            matchingRules.append(rule) 
 
    if not matchingRules: 
        return False 
 
    for rule in matchingRules: 
        antecedents = rule[0] 
        allAntecedentsProven = True 
 
        for antecedent in antecedents: 
            if not backwardChaining( 
                knowledgeBase, 
                knownFacts, 
                antecedent 
            ): 
                allAntecedentsProven = False 
                break 
 
        if allAntecedentsProven: 
            knownFacts.add(goal) 
            return True 
 
    return False 
 
def selectSymptoms(): 
    facts = [] 
 
    print("\nSelect the symptoms:") 
    print("1. Files are not syncing") 
    print("2. Internet is disconnected") 
    print("3. OneDrive storage is full") 
    print("4. OneDrive account is signed out") 
    print("5. OneDrive is not responding") 
    print("6. OneDrive sync is disabled") 
    print("0. Done") 
 
    while True: 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            facts.append("Files are not syncing") 
 
        elif choice == "2": 
            facts.append("Internet is disconnected") 
 
        elif choice == "3": 
            facts.append("OneDrive storage is full") 
 
        elif choice == "4": 
            facts.append("OneDrive account is signed out") 
 
        elif choice == "5": 
            facts.append("OneDrive is not responding") 
 
        elif choice == "6": 
            facts.append("OneDrive sync is disabled") 
 
        elif choice == "0": 
            break 
 
        else: 
            print("Invalid Value. Try Again.") 
 
    return facts 
 
while True: 
 
    print("\n========================================") 
    print("       ONEDRIVE TROUBLESHOOTING") 
    print("========================================") 
    print("1. Forward Chaining") 
    print("2. Backward Chaining") 
    print("3. Exit") 
 
    option = input("Enter your choice: ") 
 
    if option == "1": 
 
        print("\n--- Forward Chaining ---") 
 
        initialFacts = selectSymptoms() 
 
        knownFacts = forwardChaining( 
            knowledgeBase, 
            initialFacts 
        ) 
 
        newFacts = [ 
            fact for fact in knownFacts 
            if fact not in initialFacts 
        ] 
 
        print("\nInitial Facts:", initialFacts) 
        print("Known Facts:", knownFacts) 
        print("New Facts:", newFacts) 
 
        if newFacts: 
            print("Conclusion:", newFacts[-1]) 
        else: 
            print("Conclusion: No conclusion could be derived.") 
 
    elif option == "2": 
 
        print("\n--- Backward Chaining ---") 
 
        print("\nSelect the goal:") 
        print("1. Reconnect to the internet") 
        print("2. Free up OneDrive storage") 
        print("3. Sign in to OneDrive") 
        print("4. Restart OneDrive") 
        print("5. Enable OneDrive sync") 
 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            goal = "Reconnect to the internet" 
 
        elif choice == "2": 
            goal = "Free up OneDrive storage" 
 
        elif choice == "3": 
            goal = "Sign in to OneDrive" 
 
        elif choice == "4": 
            goal = "Restart OneDrive" 
 
        elif choice == "5": 
            goal = "Enable OneDrive sync" 
 
        else: 
            print("Invalid Value. Try Again.") 
            continue 
 
        initialFacts = selectSymptoms() 
        knownFacts = set(initialFacts) 
 
        result = backwardChaining( 
            knowledgeBase, 
            knownFacts, 
            goal 
        ) 
 
        print("\nInitial Facts:", initialFacts) 
        print("Goal:", goal) 
        print("Known Facts:", knownFacts) 
        print("Result:", result) 
 
        if result: 
            print("Conclusion: Goal reached") 
        else: 
            print("Conclusion: Goal cannot be proven.") 
 
    elif option == "3": 
 
        print("\nExiting...") 
        break 
 
    else: 
 
        print("Invalid Value. Try Again.")