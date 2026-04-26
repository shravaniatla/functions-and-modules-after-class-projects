try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid age entered. Please enter a realistic age")
    else:
        print("Valid age entered.")
        if age % 2 == 0:
            print("Age is Even.")
        else:
            print("Age is Odd.")

except ValueError:
    print("Error: Please enter a valid integer value for age.")