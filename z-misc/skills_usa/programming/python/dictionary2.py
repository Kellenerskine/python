prompt = "add"

employees = []

while prompt != "exit":
    if prompt == "add":
        name = input("Enter employee name: " )
        age = input("Enter employee age: ")
        dept = input("Enter employee department: ")
        salary = input("Enter employee salary: ")

        employee = {}
        employee["name"] = name
        employee["age"] = age
        employee["dept"] = dept
        employee["salary"] = salary
        employees.append(employee)

    elif prompt == "print":
        print(employees)
#        for key, value in employee.items():
#            print(f"Username: {key}, Favorite food: {value}")
    
    prompt = input("What would you like to do next? (add, print, exit): ")


#        for employee in employees:
#            for i in range(len(employee)):
#                if i == 0: # first item
#                    print("Name:", employee[i])
#                elif i == 1:
#                    print("Age:", employee[i])
#                elif i == 2:
#                    print("Department:", employee[i])
#                elif i == 3:
#                    print("Salary:", employee[i])
#            print()