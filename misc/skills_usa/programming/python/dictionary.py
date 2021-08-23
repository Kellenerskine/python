#my_dict = {
#    "my_key": 13,
#    "another_key": 19,
#    18: "string",
#    "some_new_key": 15,
#}

#my_new_var = my_dict["my_key"]
#my_dict["some_new_key"] = 15
#my_keys = my_dict.keys()
#my_values = my_dict.values()

#for key, value in my_dict.items():
#    print(key)
#    print(value)

#users = {}

#user_name = input("please enter your username: ")
#user_favorite_food = input("enter your favorite food: ")
#users[user_name] = user_favorite_food

#for key, value in users.items():
#    print(f"Username: {key}, Favorite food: {value}")





prompt = "add"

employees = []

while prompt != "exit":
    if prompt == "add":
        name = input("Enter your name: " )
        age = input("Enter you age: ")
        dept = input("Enter you department: ")
        salary = input("Enter your salary: ")

        employee = {}
        employee["name"] = name
        employee["age"] = age
        employee["dept"] = dept
        employee["salary"] = salary

        for key, value in employee.items():
            print(f"Username: {key}, Favorite food: {value}")

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