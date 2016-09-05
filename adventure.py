#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adventure In Minervavägen
"""
import choices as choices
import images as images
import sys
import os
import getopt

PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Ishaq Jound"
VERSION = "1.0"
USAGE = """{program} - Projekt By {author}, version {version}.

Usage:
  {program} [options] name

Options:
  -h, --help                         Display this help message.
  -v, --version                      Print version and exit.
  -i, --info                         Display description of the game 
  -a, --about                        Display about the developer of this game
  -c, --cheat                        Display cheat for this game.
""".format(program=PROGRAM, author=AUTHOR, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(
    program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)


# Global variables
EXIT_SUCCESS = 0
EXIT_USAGE = 1


def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)


def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)


def info():
    """
    info about the game
    """
    print("--------------------------")
    print("\nADVENTURE IN MINERVAVÄGEN")
    print("--------------------------\n")
    print("This game has 7 rooms, your job is to go to each room and unlock the rooms and \nfinish the game.")
    print("\nIn each room there are objects you have to interact with in order to solve \nthe problems.")
    print("\nOnce you are asked a question then you have to answer the question in order to \ngoto next room")
    print("\nYou can always type 'help' or 'h' to see which commands are available in the game.")
    print("\nGood Luck!")
    sys.exit(EXIT_SUCCESS)


def about():
    """
    About me
    """
    print("---------------")
    print("\nABOUT ME")
    print("---------------\n")
    print("My name is Ishaq Jound and I study at BTH and I'm the developer of this game.")
    sys.exit(EXIT_SUCCESS)


def cheat():
    """
    Game cheat
    """
    print("---------------")
    print("\nGAME CHEAT")
    print("---------------\n")
    print("To skip each room below are the answers for all the rooms\n")
    print("In each room you can type ans <room code> or answer <room code>")
    print("\nRoom 1: shoes\nRoom 2: canberra\nRoom 3: pippi långstrump")
    print("Room 4: myself\nRoom 5: sun\nRoom 6: no\nRoom 7: 12554\n")
    print("To jump directly to last room type: cheat room7 in the game")
    sys.exit(EXIT_SUCCESS)


def main():
    """
    Display game info when game starts
    """
    print("--------------------------")
    print("\nADVENTURE IN MINERVAVÄGEN")
    print("--------------------------\n")
    print("This game has 7 rooms, your job is to go to each room and unlock the rooms and \nfinish the game.")
    print("\nIn each room there are objects you have to interact with in order to solve \nthe problems.")
    print("\nOnce you are asked a question then you have to answer the question in order to \ngoto next room")
    print("\nYou can always type 'help' or 'h' to see which commands are available in the game.")
    print("\nGood Luck!")
    input("\nPress enter to start the game")


def gameStatus():
    """
    Show current room info
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(rooms[currentRoom]["image"]())
    print(rooms[currentRoom]["info"])
    print("---------------------------")
    print("You are in the " + rooms[currentRoom]["name"])


def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """
    # Switch through all options
    try:

        opts, args = getopt.getopt(sys.argv[1:], "hvsd:r:o:", [
            "help",
            "version",
            "info",
            "about",
            "cheat"
        ])

        for opt, args in opts:
            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("-i", "--info"):
                info()

            elif opt in ("-a", "--about"):
                about()

            elif opt in ("-c", "--cheat"):
                cheat()

            else:
                assert False, "Unhandled option"

        if len(args) != 1:
            assert False, "Missing name"

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        # traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)


rooms = {

    1: {"name": "Room 1",
        "info": "You have entered the first room.This room is more like a guide.\
        \nThe task is very simple, you have to guess what's inside the wardrobe\
        \nOnce you see the object inside the wardrobe then just type\
        \nans <object> to unlock the next room.\
        \nYou can always type h or help to see available commands!",
        "look": "There is wardrobe in the room and the door is closed.",
        "clue": "In wardrobe i have something that i need to wear so i can go outside.",
        "item": "wardrobe",
        "open_item": "You have opened the wardrobe and you see shoes that i need to wear.",
        "kick_item": "You don't need to kick the wardrobe, you can open it instead!",
        "move_item": "You can't move the wardrobe it's too heavy, you can open it instead!",
        "answer": "shoes".split(),
        "image": images.Room1,
        "room_key": 0},

    2: {"name": "Room 2",
        "info": "You have entered the second room, this room is smaller than the previous one.\
        \nFrom this room and onwards when you are asked a question\
        \nyou have to answer a question\nto unlock next room.",
        "look": "There is a locked box in the room.",
        "clue": ["The box is locked so there must be something in it", "The capital starts with 'C'"],
        "item": "box",
        "open_item": "You can't open the box because it's locked.",
        "kick_item": "You kicked the box few times and it opened and you can see a note saying\
        \n'What is the capital of Australia?' type 'l or ledtråd' for clue.",
        "move_item": "You can't move the box because it's heavy",
        "answer": "canberra".split(),
        "image": images.Room2,
        "clue_key": 0,
        "room_key": 0},

    3: {"name": "Room 3",
        "info": "You are in room 3 and it's dark with no lights",
        "look": {"torch": "There is torch in the room that can light up the room.",
                 "book": "There is a book that is lying on the floor."},
        "clue": ["Since there is no light in the room maybe you will need to turn on torch?",
                 "The book was published in 1945–1948"],
        "item": {"torch": "torch", "book": "book"},
        "open_item": {"torch": "The torch is turned on and there is light in the room,\
                       \nyou can interact with the book now",
                      "book": "You opened the book, it's written by Astrid Lindgren and it's the most popular\
                      \nbook published by her, what's the book name? type l for the clue",
                      3: "You can't open book when there is no light in the room."},
        "kick_item": {"torch": "There is no reason to kick the torch.",
                      "book": "Why would you kick the book when you can open it? Seriously!"},
        "move_item": {"torch": "There is no point in moving the torch.",
                      "book": "There is no bookshelf in the room, so it lies fine on the floor."},
        "answer": "Pippi Långstrump".lower().split(),
        "image": images.Room3,
        "item_key": 0,
        "clue_key": 0,
        "room_key": 0},

    4: {"name": "Room 4",
        "info": "You have entered fourth room, this room also have a toilet",
        "look": {"door": "There is a toilet in the room but the door is locked.",
                 "mirror": "there is a locked mirror in the toilet."},
        "clue": ["Find out how to get inside the toilet",
                 "Who do you see in the mirror?"],
        "item": {"door": "door", "mirror": "mirror"},
        "open_item": {"door": "You can't open the door, it's locked",
                      "mirror": "You opened the mirror and who do you see in the mirror?",
                      4: "You can't open mirror when you are not inside the toilet"},
        "kick_item": {"door": "You kicked the door and it opened, there is a mirror in the toilet",
                      "mirror": "You can't kick the mirror"},
        "move_item": {"door": "You can't move the door", "mirror": "You can't move the mirror"},
        "answer": "myself".split(),
        "image": images.Room4,
        "item_key": 0,
        "clue_key": 0,
        "room_key": 0},

    5: {"name": "Room 5",
        "info": "You have entered the fifth room, it's very dark in the room but sunny outside",
        "look": {"desk": "There is a desk is infront of the window.",
                 "curtain": "there is a closed curtain in the room."},
        "clue": ["The desk is blocking the way",
                 "It's dark in the room, the room needs lights from outside,\
                 \nsomething needs to be done with the curtain"],
        "item": {"desk": "desk", "curtain": "curtain"},
        "open_item": {"desk": "You can't open the desk",
                      "curtain": "You opened the curtain, where is the light coming from?",
                      5: "You can't open the curtain, the desk is blocking the way"},
        "kick_item": {"desk": "You can't kick the desk", "curtain": "You can't kick the curtain"},
        "move_item": {"desk": "You moved the desk to the right place", "curtain": "You can't move the curtain"},
        "answer": "sun".split(),
        "image": images.Room5,
        "item_key": 0,
        "clue_key": 0,
        "room_key": 0},

    6: {"name": "Room 6",
        "info": "You have entered the sixth room, this room have space for many objects",
        "look": {"box1": "Box1 lies on the floor.", "box2": "Box2 lies on top of the box1."},
        "clue": ["Box2 is empty and is just waste of space",
                 "There is light coming from box1 so there must be something in it"],
        "item": {"box1": "box1", "box2": "box2"},
        "open_item": {"box1": "You opened the box1, You see a latop that is turned on and it has a question for you:\
        \nCan a man and a woman ever just be friends?",
                      "box2": "You don't need to open the box2 because there is nothing in it.",
                      6: "You can't open the Box1 because Box2 lies on the Box1"},
        "kick_item": {"box1": "You can't kick Box1 because there is something in it", "box2": "You can't kick Box2"},
        "move_item": {"box1": "You can't move the Box1 because Box2 lies on the Box1",
                      "box2": "You moved the box2 to correct place."},
        "answer": "no".split(),
        "image": images.Room6,
        "item_key": 0,
        "clue_key": 0,
        "room_key": 0},

    7: {"name": "Room 7",
        "info": "You have entered the last seventh room, the door is locked.\
        \nThis room is very small and something big will happen in the room!",
        "look": {"machine": "There is a machine in the room, you don't know what it is for.",
                 "electroniclock": "The room door is locked and it has a electronic lock with pin code."},
        "clue": ["You must be wondering what the machine does, try to play around with it",
                 "Try to interact with electroniclock and answer the result"],
        "item": {"machine": "machine", "electroniclock": "electroniclock"},
        "open_item": {"machine": "You opened the machine and it displays a timer that is counting down from 1 minute\
        \nand has WARNING sound effect, you need to get out of the room as soon as possible!,\
        \nyou realize that the room is about to explode",
                      "electroniclock": "You opened the Electronic lock and it's asking for a pin code\
                      \nthe pin code is result of 112*112",
                      7: "You have to interact with the machine first"},
        "kick_item": {"machine": "There is no point in kicking the machine",
                      "electroniclock": "Why would you kick the electronic lock?"},
        "move_item": {"machine": "You can't move the machine it's too heavy",
                      "electroniclock": "It's not possible to move the electronic lock"},
        "answer": "12554",
        "image": images.Room7,
        "item_key": 0,
        "clue_key": 0,
        "room_key": 0}

}

currentRoom = 1

main()

gameStatus()



while True:

    if currentRoom == 0:
        currentRoom = 1
        gameStatus()

    choice = input(">").lower().split()

    # ROOM STUFF
    if (choice[0] == "fram") or (choice[0] == "fr"):
        if rooms[currentRoom]["room_key"] == 0:
            print("Sorry but the room is locked!")

        else:
            currentRoom += 1
            gameStatus()

    elif(choice[0] == "bak") or (choice[0] == "ba"):
        if currentRoom == 1:
            currentRoom -= 1
            main()
        else:
            currentRoom -= 1
            gameStatus()

    elif choice[0] == "se":
        if isinstance(rooms[currentRoom]["look"], dict):
            for items in rooms[currentRoom]["look"].values():
                print(items)

        else:
            print(rooms[currentRoom]["look"])

    elif (choice[0] == "info") or (choice[0] == "i"):
        print(rooms[currentRoom]["info"])

    elif (choice[0] == "help") or (choice[0] == "h"):
        choices.RoomChoices()
        choices.ObjectChoices()

    elif (choice[0] == "ledtråd") or (choice[0] == "l"):
        if isinstance(rooms[currentRoom]["clue"], list):
            if rooms[currentRoom]["clue_key"] == 0:
                print(rooms[currentRoom]["clue"][0])
            else:
                print(rooms[currentRoom]["clue"][1])
        else:
            print(rooms[currentRoom]["clue"])

    # OBJECT STUFF

    elif (choice[0] == "objekt") or (choice[0] == "o"):
        print("Following objects are in this room:")
        if isinstance(rooms[currentRoom]["item"], str):
            print(rooms[currentRoom]["item"])

        else:
            for items in rooms[currentRoom]["item"].keys():
                print(items)

    elif (choice[0] == "t") or (choice[0] == "titta"):
        if isinstance(rooms[currentRoom]["item"], str):
            if choice[1] in rooms[currentRoom]["item"]:
                print(rooms[currentRoom]["look"])
            else:
                print("There is no such object")
        else:
            if choice[1] in rooms[currentRoom]["item"]:
                print(rooms[currentRoom]["look"][choice[1]])
            else:
                print("There is no such object")

    elif (choice[0] == "ö") or (choice[0] == "öppna"):
        if isinstance(rooms[currentRoom]["open_item"], dict):
            if choice[1] in rooms[currentRoom]["open_item"]:
                if (currentRoom == 3) and (choice[1] == "book"):
                    if rooms[currentRoom]["item_key"] == 0:
                        print(rooms[currentRoom]["open_item"][3])
                    else:
                        print(rooms[currentRoom]["open_item"][choice[1]])

                elif (currentRoom == 4) and (choice[1] == "mirror"):
                    if rooms[currentRoom]["item_key"] == 0:
                        print(rooms[currentRoom]["open_item"][4])
                    else:
                        print(rooms[currentRoom]["open_item"][choice[1]])

                elif (currentRoom == 5) and (choice[1] == "curtain"):
                    if rooms[currentRoom]["item_key"] == 0:
                        print(rooms[currentRoom]["open_item"][5])
                    else:
                        print(rooms[currentRoom]["open_item"][choice[1]])

                elif (currentRoom == 6) and (choice[1] == "box1"):
                    if rooms[currentRoom]["item_key"] == 0:
                        print(rooms[currentRoom]["open_item"][6])
                    else:
                        print(rooms[currentRoom]["open_item"][choice[1]])

                elif (currentRoom == 7) and (choice[1] == "electroniclock"):
                    if rooms[currentRoom]["item_key"] == 0:
                        print(rooms[currentRoom]["open_item"][7])
                    else:
                        print(rooms[currentRoom]["open_item"][choice[1]])

                else:
                    if choice[1] in rooms[currentRoom]["open_item"][choice[1]]:
                        print(rooms[currentRoom]["open_item"][choice[1]])

                        if currentRoom == 3:
                            rooms[currentRoom]["clue_key"] = 1
                            rooms[currentRoom]["item_key"] = 1

                        if (currentRoom == 7) and (choice[1] == "machine"):
                            rooms[currentRoom]["clue_key"] = 1
                            rooms[currentRoom]["item_key"] = 1
            else:
                print("There is no such object")
        else:
            if choice[1] in rooms[currentRoom]["item"]:
                print(rooms[currentRoom]["open_item"])
            else:
                print("There is no such object")

    elif (choice[0] == "s") or (choice[0] == "sparka"):
        if isinstance(rooms[currentRoom]["kick_item"], dict):
            if choice[1] in rooms[currentRoom]["item"]:
                print(rooms[currentRoom]["kick_item"][choice[1]])

                if currentRoom == 4:
                    rooms[currentRoom]["clue_key"] = 1
                    rooms[currentRoom]["item_key"] = 1
            else:
                print("There is no such object")
        else:
            if choice[1] in rooms[currentRoom]["item"]:
                print(rooms[currentRoom]["kick_item"])
                if currentRoom == 2:
                    rooms[currentRoom]["clue_key"] = 1
            else:
                print("There is no such object")

    elif (choice[0] == "f") or (choice[0] == "flytta"):
        if isinstance(rooms[currentRoom]["move_item"], dict):
            if choice[1] in rooms[currentRoom]["item"]:
                print(rooms[currentRoom]["move_item"][choice[1]])

                if currentRoom == 5:
                    rooms[currentRoom]["clue_key"] = 1
                    rooms[currentRoom]["item_key"] = 1

                elif (currentRoom == 6) and (choice[1] == "box2"):
                    rooms[currentRoom]["clue_key"] = 1
                    rooms[currentRoom]["item_key"] = 1
            else:
                print("There is no such object")
        else:
            if choice[1] in rooms[currentRoom]["item"]:
                print(rooms[currentRoom]["move_item"])

            else:
                print("There is no such object")

    elif (choice[0] == "ans") or (choice[0] == "answer"):
        if choice[1] in rooms[currentRoom]["answer"]:
            if currentRoom == 7:
                print(
                    "Your answer is right, You managed to get out the room before it exploded")
                print(choices.game_completed())
                print("Play again?", "y/n")
                game = input(">").lower().split()
                if game[0] == "y":
                    main()
                    gameStatus()
                elif game[0] == "n":
                    print("Good bye!")
                    break

            else:
                print("Your answer is right and Room",
                      currentRoom + 1, "is unlocked!")
                rooms[currentRoom]["room_key"] = 1
        else:
            print("Sorry it's not the right answer!")

    elif (choice[0] == "q") or (choice[0] == "quit"):
        print("Good bye!")
        break

    elif choice[0] == "cheat":
        if choice[1] == "room7":
            currentRoom = 7
            gameStatus()

        else:
            print("Wrong cheat.")
parseOptions()