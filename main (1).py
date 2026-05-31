import datetime
import json
import random

# Function to save the generated results to a text file as required
def save_to_file(action_name, content):
    with open("output.txt", "a") as file:
        file.write(f"[{datetime.datetime.now()}] {action_name}:\n{content}\n")
        file.write("-" * 40 + "\n")

# Load the tips and quotes from the JSON file (Bonus requirement)
try:
    with open("tips.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: tips.json file not found! Please create it first.")
    exit()

# Step 1: Ask the user for their name
user_name = input("Enter your name: ")

# Step 2: Display a personalized greeting
print(f"\nHello, {user_name}! Welcome to your Smart Student Assistant.")

# Step 3: Provide menu options inside a loop
while True:
    print("\n=== MENU OPTIONS ===")
    print("1. Generate Study Tips")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit Program")
    
    choice = input("\nPlease select an option (1-4): ")
    
    if choice == "1":
        # Pull a random tip from the JSON data
        random_tip = random.choice(data["study_tips"])
        result = f"Study Tip: {random_tip}"
        print(f"\n[RESULT] {result}")
        save_to_file("Study Tip Generated", result)
        
    elif choice == "2":
        # Pull a random quote from the JSON data
        random_quote = random.choice(data["motivation_quotes"])
        result = f"Quote: {random_quote}"
        print(f"\n[RESULT] {result}")
        save_to_file("Motivation Quote Generated", result)
        
    elif choice == "3":
        # Fetch the exact current live date and time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = f"Current Date & Time: {current_time}"
        print(f"\n[RESULT] {result}")
        save_to_file("Date & Time Checked", result)
        
    elif choice == "4":
        print(f"\nGoodbye, {user_name}! Have a productive day ahead.")
        break
        
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")