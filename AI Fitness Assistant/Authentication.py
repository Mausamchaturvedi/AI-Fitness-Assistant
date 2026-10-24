# AI Fitness Assistant

users = {}

def calculate_bmi(weight, height):
    bmi = weight / (height * height)

    print("\nYour BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal Weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")


def calculate_calories(weight, height_cm, age):
    calories = 10 * weight + 6.25 * height_cm - 5 * age + 5
    print("\nEstimated Daily Calories Needed:", round(calories), "kcal")


def workout_recommendation():
    print("\nSelect Goal")
    print("1. Weight Loss")
    print("2. Muscle Gain")
    print("3. Maintain Fitness")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nWorkout Plan:")
        print("- 30 min Running")
        print("- Jump Rope")
        print("- Cycling")
        print("- HIIT Training")

    elif choice == "2":
        print("\nWorkout Plan:")
        print("- Bench Press")
        print("- Squats")
        print("- Deadlifts")
        print("- Pull Ups")

    elif choice == "3":
        print("\nWorkout Plan:")
        print("- Walking")
        print("- Push Ups")
        print("- Yoga")
        print("- Light Cardio")

    else:
        print("Invalid Choice")


def register():
    username = input("Create Username: ")
    password = input("Create Password: ")

    users[username] = password
    print("Registration Successful")


def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("\nLogin Successful")

        while True:
            print("\n===== AI FITNESS ASSISTANT =====")
            print("1. BMI Calculator")
            print("2. Calorie Calculator")
            print("3. Workout Recommendation")
            print("4. Logout")

            choice = input("Enter Choice: ")

            if choice == "1":
                weight = float(input("Enter Weight (kg): "))
                height = float(input("Enter Height (m): "))
                calculate_bmi(weight, height)

            elif choice == "2":
                weight = float(input("Enter Weight (kg): "))
                height_cm = float(input("Enter Height (cm): "))
                age = int(input("Enter Age: "))
                calculate_calories(weight, height_cm, age)

            elif choice == "3":
                workout_recommendation()

            elif choice == "4":
                print("Logged Out Successfully")
                break

            else:
                print("Invalid Choice")

    else:
        print("Invalid Username or Password")


while True:
    print("\n===== WELCOME TO AI FITNESS ASSISTANT =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    option = input("Enter Choice: ")

    if option == "1":
        register()

    elif option == "2":
        login()

    elif option == "3":
        print("Thank You For Using AI Fitness Assistant")
        break

    else:
        print("Invalid Choice")