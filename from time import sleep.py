from time import sleep
name = input("hello! what is your name?")
print("hi", name)
age = int(input("how old are you?"))


sleep(2)

print("""
 
               _                            _                                  _           
              | |                          | |                                | |          
 __      _____| | ___ ___  _ __ ___   ___  | |_ ___    _ __ ___  _   _ _ __ __| | ___ _ __ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | '_ ` _ \| | | | '__/ _` |/ _ \ '__|
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | | | | |_| | | | (_| |  __/ |   
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_| |_| |_|\__,_|_|  \__,_|\___|_|   
                     | |                                                                   
  _ __ ___  _   _ ___| |_ ___ _ __ _   _                                                   
 | '_ ` _ \| | | / __| __/ _ \ '__| | | |                                                  
 | | | | | | |_| \__ \ ||  __/ |  | |_| |                                                  
 |_| |_| |_|\__, |___/\__\___|_|   \__, |                                                  
             __/ |                  __/ |                                                  
            |___/                  |___/                                                   
                                                                                                                                                                                                 
""")

sleep(2)

print("this morning, you found a body in the livingroom")
sleep(1)
print("12 people live in the mansion, in rooms labled 1-12 plus the living room, dining room, kitchen and garden")
sleep(1)
print("to investigate a room say 'investigate ___' do not use capitals")
sleep(1)

print("the answers will never be longer than 5 words")

# Helper function for 3 attempts per question, ends game if out of attempts
import sys
def get_attempted_input(prompt, valid_answers):
    attempts = 0
    while attempts < 3:
        answer = input(prompt).strip()
        for valid in valid_answers:
            if answer == valid:
                return answer
        attempts += 1
        if attempts < 3:
            print(f"Try again. Attempts left: {3 - attempts}")
    print("Out of attempts! You have failed and died.")
    sys.exit()

choice = get_attempted_input("look places to add to your score, where will you investigate first?", ["investigate living room", "investigate the living room"])

while True:
    if choice in ["investigate living room", "investigate the living room"]:
        print("you creep around the living room. you see the body.")
        investigatescene = get_attempted_input("what should you do?", ["investigate body", "investigate the body"])
        if investigatescene:
            print("the body is one of the person who lives in room 4")
            sleep(2)
            print("their name was Clair, your cousin")
            sleep(2)
            wherenext = get_attempted_input("where do you want to investigate next?", ["investigate room 4", "investigate 4", "investigat clair's room"])
            if wherenext:
                print("""you enter room 4 and you see:
                      - a closet
                      - a door
                      - a bed
                      - a suspicious rug
                      - a balcony
                      - a dressing table (mirror)      """)
                sleep(5)
                pick = get_attempted_input(
                    "where do you want to look?",
                    [
                        "look in closet", "investigate the closet", "investigate closet",
                        "look under bed", "investigate bed",
                        "look under rug", "investigate rug",
                        "open door", "go to balcony",
                        "look in mirror", "investigate dressing table",
                        "read note", "search drawers", "check balcony floor", "inspect window", "listen at door"
                    ]
                )
                if pick in ["look in closet", "investigate the closet", "investigate closet"]:
                    print("""Inside you see a red cloth, stained perhaps, with the initials 'C.D.' on it. It looks like it was torn from a dress.""")
                    sleep(1)
                    print("You feel uneasy. As you look closer, you notice a faint perfume scent—one you remember from the kitchen earlier.")
                elif pick in ["look under bed", "investigate bed"]:
                    print("You find a dusty box. Inside is a photo of Clair with another person, their face scratched out.")
                    sleep(1)
                    print("Who could it be? On the back, a date is written: 'Midnight, last Friday.'")
                elif pick in ["look under rug", "investigate rug"]:
                    print("You lift the rug and find a trapdoor. It's locked, but there are muddy footprints leading to it.")
                    sleep(1)
                    print("Maybe someone used this recently. You also spot a small golden key nearby.")
                elif pick in ["open door"]:
                    print("The door leads to a small bathroom. Nothing seems out of place, but the window is open.")
                    sleep(1)
                    print("Did someone escape? On the windowsill, you find a single red thread.")
                elif pick in ["go to balcony"]:
                    print("On the balcony, you see a scarf caught on the railing. It matches the red cloth from the closet.")
                    sleep(1)
                    print("The garden is just below. You also notice a muddy handprint on the balcony door.")
                elif pick in ["look in mirror", "investigate dressing table"]:
                    print("You find a hidden drawer in the dressing table. Inside is a note: 'Meet me at midnight. -R'")
                    sleep(1)
                    print("Who is 'R'? This could be a clue. Next to the note is a small locket with a faded photo of Clair and a mysterious figure.")
                elif pick == "read note":
                    print("You read the note again: 'Meet me at midnight. -R'. On the back, you notice a faint map of the garden.")
                elif pick == "search drawers":
                    print("You search all the drawers and find a broken necklace clasp and a small scrap of red fabric.")
                elif pick == "check balcony floor":
                    print("You check the balcony floor and find a muddy footprint and a cigarette butt with lipstick on it.")
                elif pick == "inspect window":
                    print("You inspect the bathroom window and see scratch marks, as if someone climbed out in a hurry.")
                elif pick == "listen at door":
                    print("You listen at the door and hear faint footsteps in the hallway. Someone might be watching you.")
                else:
                    print("You don't find anything unusual, but you can't shake the feeling that you're being watched.")
                # After exploring, ask where to go next
                next_room = get_attempted_input("Where do you want to go now? (e.g., 'investigate garden', 'investigate kitchen', 'investigate room 5')", [
                    "investigate garden", "investigate kitchen", "investigate room 5", "investigate room 6", "investigate room 7", "investigate room 8", "investigate room 9", "investigate room 10", "investigate room 11", "investigate room 12"])
                if next_room == "investigate garden":
                    print("You step into the garden. The grass is wet and you see muddy footprints leading to a shed.")
                    sleep(1)
                    print("The shed is locked, but you hear a faint noise inside.")
                    shed_choice = get_attempted_input("Do you want to try to open the shed? (yes/no/knock)", ["yes", "no", "knock"])
                    if shed_choice == "yes":
                        print("You force the door open and find muddy boots and a torn piece of paper.")
                        sleep(1)
                        print("The paper reads: 'Room 9. Midnight.' This could be the culprit's room!")
                        sleep(1)
                        print("You hurry back to the mansion to investigate room 9.")
                        print("You enter room 9. It's empty, but you find a diary under the pillow.")
                        sleep(1)
                        print("The diary confesses to the crime and mentions jealousy over Clair's inheritance.")
                        print("You have found the culprit's room: Room 9! Congratulations, you solved the mystery.")
                        sys.exit()
                    elif shed_choice == "knock":
                        print("You knock on the shed door. After a moment, a frightened maid opens it. She confesses she saw someone sneaking out of room 7 last night.")
                        sleep(1)
                        print("You decide to investigate room 7.")
                        print("Inside room 7, you find a blood-stained glove and a threatening letter addressed to Clair.")
                        print("It seems the resident of room 7 is the real culprit! You alert the authorities. Justice is served.")
                        print("Ending: The True Culprit in Room 7.")
                        sys.exit()
                    else:
                        print("You decide not to open the shed. The mystery remains unsolved. Maybe some secrets are best left hidden.")
                        print("Ending: The Case Goes Cold.")
                        sys.exit()
                elif next_room == "investigate kitchen":
                    print("In the kitchen, you find a knife missing from the rack and a half-eaten apple on the counter.")
                    sleep(1)
                    print("Someone left in a hurry.")
                    kitchen_choice = get_attempted_input("Do you want to search the trash or check the back door? (search/check/leave)", ["search", "check", "leave"])
                    if kitchen_choice == "search":
                        print("You search the trash and find a torn piece of a letter: '...meet in the garden at midnight. -R'")
                        print("You realize the kitchen and garden are connected in this mystery, but the trail goes cold.")
                        print("Ending: The Mystery Remains.")
                        sys.exit()
                    elif kitchen_choice == "check":
                        print("You check the back door and see muddy footprints leading away from the house. You follow them to the road, but the culprit is gone.")
                        print("Ending: The Suspect Escapes.")
                        sys.exit()
                    else:
                        print("You leave the kitchen, feeling like you missed something important.")
                        print("Ending: Unsolved, for now.")
                        sys.exit()
                elif next_room and next_room.startswith("investigate room"):
                    room_num = next_room.replace('investigate room ', '').strip()
                    print(f"You enter room {room_num}. It's quiet. You notice a diary on the desk.")
                    sleep(1)
                    if room_num == "9":
                        print("The diary confesses to the crime and mentions jealousy over Clair's inheritance.")
                        print("You have found the culprit's room: Room 9! Congratulations, you solved the mystery.")
                        print("Ending: The Jealous Heir.")
                        sys.exit()
                    elif room_num == "7":
                        print("You find a blood-stained glove and a threatening letter addressed to Clair.")
                        print("It seems the resident of room 7 is the real culprit! You alert the authorities. Justice is served.")
                        print("Ending: The True Culprit in Room 7.")
                        sys.exit()
                    elif room_num == "4":
                        print("You find Clair's belongings, but nothing new. The room is eerily quiet.")
                        print("Ending: The Victim's Silence.")
                        sys.exit()
                    else:
                        print("The diary mentions secret meetings in the garden at night.")
                        print("Ending: The Mystery Remains.")
                        sys.exit()
                else:
                    print("You wander the halls, but find nothing new at all.")
                    print("Ending: Lost in the Mansion.")
                    sys.exit()