prompt = "add"

employees = []

while prompt != "exit":
    if prompt == "add":
        name = input("Enter your name: " )
        age = input("Enter you age: ")
        dept = input("Enter you department: ")
        salary = input("Enter your salary: ")
        employees.append([name, age, dept, salary])

    elif prompt == "print":
        for employee in employees:
            for i in range(len(employee)):
                if i == 0: # first item
                    print("Name:", employee[i])
                elif i == 1:
                    print("Age:", employee[i])
                elif i == 2:
                    print("Department:", employee[i])
                elif i == 3:
                    print("Salary:", employee[i])
            print()
    
    prompt = input("What would you like to do next? (add, print, exit): ")