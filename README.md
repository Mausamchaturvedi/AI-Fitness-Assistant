# 🏋️ AI Fitness Assistant

**AI Fitness Assistant** is a Python-based fitness application designed to help users manage their basic fitness goals. It provides BMI calculation, daily calorie estimation, and personalized workout recommendations based on the user's fitness objectives.

The project uses Core Python concepts such as functions, conditional statements, loops, dictionaries, and user input to create a simple interactive fitness assistant.

## 🚀 Features

- **User Registration:** Create a new account using a username and password.
- **User Login:** Secure login verification using registered credentials during the running session.
- **BMI Calculator:** Calculate Body Mass Index based on weight and height.
- **BMI Classification:** Identify fitness categories:
  - Underweight
  - Normal Weight
  - Overweight
  - Obese
- **Calorie Calculator:** Estimate daily calorie requirements using a formula based on weight, height, age, and a male-specific BMR equation.
- **Workout Recommendations:** Get workout suggestions according to fitness goals:
  - Weight Loss
  - Muscle Gain
  - Maintain Fitness
- **Logout:** Safely return to the main menu after logging out.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Dictionaries | Store user credentials |
| Functions | Organize application modules |
| Conditional Statements | Implement decision-making |
| Loops | Manage application menus |
| User Input | Collect user information |

## 📂 Project Structure

```text
AI-Fitness-Assistant/
│
├── main.py          # Main Python application
├── README.md        # Project documentation
└── LICENSE          # Project license (optional)
```

## ⚙️ Installation & Setup

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Fitness-Assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Fitness-Assistant
```

### 3. Run the Application

```bash
python main.py
```

**Note:** Python 3.x must be installed on your system. No external libraries are required.

## 💻 How to Use

### Step 1: Welcome Screen

When you run the application, the following menu appears:

```text
===== WELCOME TO AI FITNESS ASSISTANT =====
1. Register
2. Login
3. Exit

Enter Choice:
```

### Step 2: Register an Account

Select option 1 and create your username and password.

### Step 3: Login

Enter your registered username and password to access the fitness dashboard.

### Step 4: Select a Fitness Feature

```text
===== AI FITNESS ASSISTANT =====
1. BMI Calculator
2. Calorie Calculator
3. Workout Recommendation
4. Logout
```

### Step 5: Calculate BMI

Enter your weight in kilograms and height in meters to calculate your BMI.

### Step 6: Calculate Daily Calories

Enter your weight, height in centimeters, and age to estimate your daily calorie requirements.

### Step 7: Get Workout Recommendations

Choose your fitness goal:

- Weight Loss
- Muscle Gain
- Maintain Fitness

The application displays a workout plan based on your selection.

## 🧮 Formulas Used

### 1. Body Mass Index (BMI)

```text
BMI = Weight (kg) / Height (m)²
```

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25 – 29.9 | Overweight |
| 30 or above | Obese |

### 2. Basal Metabolic Rate (BMR)

The application uses the following Mifflin-St Jeor equation for males:

```text
BMR = 10 × Weight + 6.25 × Height - 5 × Age + 5
```

**Note:** This equation estimates BMR, not total daily calorie expenditure. Actual daily calorie needs also depend on activity level and other individual factors.

## 🎯 Project Objectives

- To develop a simple and interactive fitness application using Python.
- To understand the practical implementation of Python functions.
- To perform BMI and calorie calculations.
- To provide goal-based workout recommendations.
- To demonstrate user registration and login functionality.
- To apply programming concepts to a real-world fitness-related problem.

## 🔮 Future Enhancements

The project can be enhanced with the following features:

- Database integration using MySQL or SQLite.
- Password hashing and improved authentication.
- Personalized diet recommendations.
- AI-powered fitness chatbot.
- Daily water intake calculator.
- Fitness progress tracking.
- Graphical User Interface (GUI) using Tkinter.
- Personalized calorie targets based on activity level.
- Workout schedules and reminder notifications.

## ⚠️ Limitations

- User credentials are stored in memory and are lost when the application closes.
- The calorie formula currently uses the male BMR equation.
- Workout recommendations are predefined rather than generated using machine learning.
- BMI is a screening measure and does not independently determine overall health.

## 📚 Learning Outcomes

Through this project, I learned:

- Python programming fundamentals.
- Functions and modular programming.
- Dictionary-based data handling.
- Conditional statements and loops.
- Mathematical calculations using Python.
- Building interactive console-based applications.
- Applying programming concepts to real-world problems.

## 👨‍💻 Author

**Mausam Chaturvedi**

Python Developer | BCA Graduate

## 📄 License

This project is developed for educational and academic purposes. You are welcome to explore and modify the source code.

---

⭐ **If you like this project, don't forget to star the repository!**

