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
                pick = get_attempted_input("where do you want to look?", ["look in closet", "investigate the closet", "investigate closet", "look under bed", "investigate bed", "look under rug", "investigate rug", "open door", "go to balcony", "look in mirror", "investigate dressing table"])
                if pick in ["look in closet", "investigate the closet", "investigate closet"]:
                    print("""Inside you see a red cloth, stained perhaps, with the initials 'C.D.' on it. It looks like it was torn from a dress.""")
                    sleep(1)
                    print("You feel uneasy. Where next?")
                elif pick in ["look under bed", "investigate bed"]:
                    print("You find a dusty box. Inside is a photo of Clair with another person, their face scratched out.")
                    sleep(1)
                    print("Who could it be?")
                elif pick in ["look under rug", "investigate rug"]:
                    print("You lift the rug and find a trapdoor. It's locked, but there are muddy footprints leading to it.")
                    sleep(1)
                    print("Maybe someone used this recently.")
                elif pick in ["open door"]:
                    print("The door leads to a small bathroom. Nothing seems out of place, but the window is open.")
                    sleep(1)
                    print("Did someone escape?")
                elif pick in ["go to balcony"]:
                    print("On the balcony, you see a scarf caught on the railing. It matches the red cloth from the closet.")
                    sleep(1)
                    print("The garden is just below.")
                elif pick in ["look in mirror", "investigate dressing table"]:
                    print("You find a hidden drawer in the dressing table. Inside is a note: 'Meet me at midnight. -R'")
                    sleep(1)
                    print("Who is 'R'? This could be a clue.")
                else:
                    print("You don't find anything unusual.")
                # After exploring, ask where to go next
                next_room = get_attempted_input("Where do you want to go now? (e.g., 'investigate garden', 'investigate kitchen', 'investigate room 5')", [
                    "investigate garden", "investigate kitchen", "investigate room 5", "investigate room 6", "investigate room 7", "investigate room 8", "investigate room 9", "investigate room 10", "investigate room 11", "investigate room 12"])
                if next_room == "investigate garden":
                    print("You step into the garden. The grass is wet and you see muddy footprints leading to a shed.")
                    sleep(1)
                    print("The shed is locked, but you hear a faint noise inside.")
                elif next_room == "investigate kitchen":
                    print("In the kitchen, you find a knife missing from the rack and a half-eaten apple on the counter.")
                    sleep(1)
                    print("Someone left in a hurry.")
                elif next_room and next_room.startswith("investigate room"):
                    print(f"You enter {next_room.replace('investigate ', '')}. It's quiet. You notice a diary on the desk.")
                    sleep(1)
                    print("The diary mentions secret meetings in the garden at night.")
                else:
                    print("You wander the halls, but find nothing new.")