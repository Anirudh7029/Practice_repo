# Get user input to find probability of a specific die roll
def pmf_user_choice():
    die_faces = range(1, 7)  # Possible outcomes (1 to 6)
    pmf_values = [1/6] * 6  # Each outcome has 1/6 probability
    
    try:
        user_choice = int(input("Enter a number between 1 and 6 to find its probability: "))
        if user_choice in die_faces:
            print(f"P(X={user_choice}) = {pmf_values[user_choice - 1]:.2f}")
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 6.")

# Call the function to allow user input
pmf_user_choice()
