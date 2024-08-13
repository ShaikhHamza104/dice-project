import random

# ASCII art representations of dice faces
# Each variable (one, two, three, etc.) holds a string that visually represents a dice face.
one = '''
┌─────────┐
│         │
│    ●    │
│         │
└─────────┘
'''
two = '''
┌─────────┐
│  ●      │
│         │
│      ●  │
└─────────┘
'''
three = '''
┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘
'''
four = '''
┌─────────┐
│  ●   ●  │
│         │
│  ●   ●  │
└─────────┘
'''
five = '''
┌─────────┐
│  ●   ●  │
│    ●    │
│  ●   ●  │
└─────────┘
'''
six = '''
┌─────────┐
│  ●   ●  │
│  ●   ●  │
│  ●   ●  │
└─────────┘
'''

# Mapping numbers to their respective dice faces for easy lookup
die_faces = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six
}

def get_user_choice():
    # Prompt the user to choose a dice option and return their choice
    user_choice = int(input('''Choose your dice option:
1. For a 6-sided die, you must pay 10 Rs
2. For a 5-sided die, you must pay 5 Rs
3. For not paying money 
Enter your choice (1, 2, or 3): '''))
    return user_choice

def process_payment(user_choice:int):
    # Determine the cost based on user choice and process the payment
    if user_choice == 1:
        cost = 10
    elif user_choice == 2:
        cost = 5
    elif user_choice == 3:
        cost = 0
    else:
        print("Invalid choice.")
        exit()

    payment = int(input(f"Enter your payment (minimum {cost} Rs): "))
    if payment < cost:
        print("Insufficient payment. Exiting the game.")
        exit()
    elif payment > cost:
        print("Take back your change:", payment - cost)

def roll_dice(user_choice):
    # Roll the dice based on the user's choice and return the result
    if user_choice == 1:
        return random.randint(5, 6)
    elif user_choice == 2:
        return random.randint(4, 5)
    elif user_choice == 3:
        return random.randint(1, 6)

def main():
    # Main function to run the game loop
    user_choice = get_user_choice()
    process_payment(user_choice)
    while True:
        die_face = roll_dice(user_choice)
        user_input = input("Roll the dice? (yes/no): ").lower()
        if user_input == 'yes':
            print(die_faces[die_face])
        elif user_input == 'no':
            print("Exiting the game.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()