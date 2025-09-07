# Ask the player for their name.
player_name = input("Enter your name: ")

# Display a message that greets them and introduces them to the game world.
print("Hello ",player_name," welcome to the D&D world!")

has_sword = False

# Present them with a choice between two doors.
while True:
    door_choice = input("You see two doors. Choose a door ('left' or 'right'): ")

    # If they choose the left door, they'll see an empty room.
    if door_choice == "left":
        print("You enter a quiet, empty-looking room.")
        room_choice = input("Stay and look around ('look') or return to the doors ('return')? ")

        if room_choice == "return":
            print("You step back to the doors.")
            continue

        # When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
        if room_choice == "look":
            if not has_sword:
                sword_choice = input("You find a magical sword! Take it ('take') or leave it ('leave')? ")
                if sword_choice == "take":
                    has_sword = True
                    print("You take the sword.")
                else:
                    print("You leave the sword behind.")
            else:
                print("You've already taken the sword. Nothing else here.")
        # In both cases, they have the option to return to the previous room or interact further.
        input("Press Enter to return to the doors.")
        continue

    # If they choose the right door, then they encounter a dragon.
    elif door_choice == "right":
        print("A huge dragon is in the room!")
        dragon_choice = input("Do you fight ('fight') or return to the doors ('return')? ")

        if dragon_choice == "return":
            print("You close the door and back away.")
            continue
        # When encountering the dragon, they have the choice to fight it.
        if dragon_choice == "fight":
            # If they have the sword from the other room, then they will be able to defeat it and win the game.
            if has_sword:
                print("With your magic sword, you slay the dragon. YOU WIN!")
                break
            # If they don't have the sword, then they will be eaten by the dragon and lose the game.
            else:
                print("You have no weapon. The dragon eats you - GAME OVER.")
                break
        
    else:
        print("Not a valid choice. Try again.")