# Imports
import re # Import the regular expressions module for pattern matching

# Definitions
def get_valid_name():
    """
    Prompts the user to enter a valid name. The name can only contain english letters (A-Z/a-z) and spaces.
    The input is validated using a regular expression to make sure only valid characters pass.
    I decided to restrict the input rather than deleting non-English letter characters afterwards
    to prevent getting wrong results. For example would be using leetspeak get another sum than plain text.
    """
    pattern = r'^[A-Za-z ]+$'


    while True:
        name = input().strip() #Remove white space at the beginning and the end

        if not name: #Check if input is empty after stripping.
            print("Your input can't be empty.")

        elif not re.match(pattern, name): #Check if input matches pattern
            print("Your input can only contain letters from A-Z.")

        else:
            return name #exit loop

def calculate_sum(name):
    """
    Calculates the sum of the letter values in the input name.
    Each letter gets assigned to a value (A=1, B=2,..., Z=26).
    Changes every character to lower case and deletes whitespace.
    Returns the sum of the name.
    """
    name = name.lower()
    name = name.replace(" ","")
    return sum(ord(char) - ord('a') + 1 for char in name)
    """Translates every single letter of the input in unicode.
    Subtracts the uni code number of "a" (which is 97) from every unicode number of the letters and adds +1 each time.
    Returns the sum of the name by adding the value of every single letter."""

# Main program
if __name__ == "__main__":
    print("Hello, please enter your name. Please use A-Z only.")
    name = get_valid_name() # prompt user for valid name input
    total = calculate_sum(name) # Calculate the sum of the letter values
    print("The sum of the letters in your name is " + str(total) + ".") # Output the result






