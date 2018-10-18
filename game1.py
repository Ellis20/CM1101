#!/usr/bin/python3

from map1 import rooms
import string


def remove_punct(text):

    no_punct = ""
    for char in text:
        if not(char in string.punctuation):
            no_punct = no_punct + char

    return no_punct
    
def remove_spaces(text):
    
    return text.replace(" ","")
    
def normalise_input(user_input):

    no_punct = remove_punct(user_input)

    no_spaces = remove_spaces(no_punct)


    return no_spaces.lower()

       
def display_room(room):

    Name = (room["name"])
    Name_Capital = Name.upper()

    print (" ")   
    print (Name_Capital)
    print (" ")
    print (room["description"])
    print (" ")

   
def exit_leads_to(exits, direction):

    for key, val in exits.items():
        if key == direction:
            return val


def print_menu_line(direction, leads_to):

    print("Go " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits):

    print(" ")
    print("You can:")

    for key,val in exits.items():
        print_menu_line(key,val)

    print("Where do you want to go?")


def is_valid_exit(exits, user_input):

    if user_input in exits:
        return True
    else:
        return False
        
def menu(exits):
    

    # Repeat until the player enter a valid choice
    while True:
        
        # Display menu
        print_menu(exits)
        
        # Read player's input
        chosen_exit = input("What exit would you like to take?: ")
        
        # Normalise the input
        chosen_exit_checked = normalise_input(chosen_exit)
        
        # Check if the input makes sense (is valid exit)
            # If so, return the player's choice
            
        if is_valid_exit(exits,chosen_exit_checked) == True:
            return chosen_exit_checked

def move(exits, direction):
 
    return rooms[exit_leads_to(exits,direction)]


        
# This is the entry point of our program
def main():
    # Start game at the reception
    current_room = rooms["Reception"]
    
    # Main game loop
    while True:
        # Display game status (room description etc.)
        display_room(current_room)
        
        # What are the possible exits from the current room?
        exits = current_room["exits"]

        # Show the menu with exits and ask the player
        direction = menu(exits)

        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)
        

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
    


