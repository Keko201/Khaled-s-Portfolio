import sys

def intro():
    print("Welcome to the Dungeon Adventure!")
    print("You find yourself in a dark and musty dungeon.")
    print("Your goal is to find the treasure and escape.")
    print("Good luck!")
    print()

def show_options():
    print("What would you like to do?")
    print("1. Go North")
    print("2. Go South")
    print("3. Go East")
    print("4. Go West")
    print("5. Check Inventory")
    print("6. Quit Game")
    print()

def process_choice(choice):
    if choice == '1':
        print("You go North and find a treasure chest!")
        print("Congratulations! You've won the game!")
        sys.exit()
    elif choice == '2':
        print("You go South and encounter a fearsome monster!")
        print("You have been defeated. Game over.")
        sys.exit()
    elif choice == '3':
        print("You go East and find a hidden passage.")
        print("You are now in a maze with many twists and turns.")
    elif choice == '4':
        print("You go West and find a locked door.")
        print("You need a key to open it.")
    elif choice == '5':
        print("You check your inventory. You have: Nothing.")
    elif choice == '6':
        print("Thanks for playing! Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please choose a number between 1 and 6.")

def main():
    intro()
    while True:
        show_options()
        choice = input("Enter your choice (1-6): ")
        process_choice(choice)

if __name__ == "__main__":
    main()

#Welcome to the Dungeon Adventure!
#You find yourself in a dark and musty dungeon.
#Your goal is to find the treasure and escape.
#Good luck!

#What would you like to do?
#1. Go North
#2. Go South
#3. Go East
#4. Go West
#5. Check Inventory
#6. Quit Game

#Enter your choice (1-6)
