#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
List of choices for room and objects
"""

def RoomChoices():
    """
    List of choices that a player can do in a room
    """
    print("\nList of choices you can do in a room\n")
    print("(i, info)                Displays description of the room.")
    print("(h, help)                Displays available commands")
    print("(fr, fram)               Move to next room if unlocked")
    print("(ba, bak)                Move to previous room")
    print("(se)                     Look around in the room")
    print("(l, ledtråd)             Gives a clue on how to solve the problem")
    print("(ans, answer) <answer>   Right answer will unlock the next room")
    print("(q, quit)                Quit the game")


def ObjectChoices():
    """
    List of choices that a player can interact with objects
    """
    print("\nList of choices you can interact with objects\n")
    print("(o, objekt)              Displays list of objects in a room")
    print("(t, titta) <objekt>      Displays description about the object")
    print("(ö, öppna) <objekt>      Open the object if possible")
    print("(s, sparka) <objekt>     Kick the object if possible")
    print("(f, flytta) <objekt>     Move the object if possible")


def game_completed():
    """
    Display congratulations message once game is completed.
    """
    game = r"""

                                                    
 / ____|                          | |       | |     | | (_)                
| |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
| |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
| |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \
 \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                    __/ |                                                  
                   |___/                                               
\ \   / /                                     | |        | | | |
 \ \_/ /__  _   _   ___ _   _  ___ ___ ___  __| | ___  __| | | |
  \   / _ \| | | | / __| | | |/ __/ __/ _ \/ _` |/ _ \/ _` | | |
   | | (_) | |_| | \__ \ |_| | (_| (_|  __/ (_| |  __/ (_| | |_|
   |_|\___/ \__,_| |___/\__,_|\___\___\___|\__,_|\___|\__,_| (_)
    """
    return game
