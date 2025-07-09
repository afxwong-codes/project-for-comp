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


# Add more starting branches
first_choices = [
    "investigate living room", "investigate the living room",
    "investigate kitchen", "investigate garden",
    "investigate dining room", "investigate room 1", "investigate room 2", "investigate room 3", "investigate room 4", "investigate room 5", "investigate room 6", "investigate room 7", "investigate room 8", "investigate room 9", "investigate room 10", "investigate room 11", "investigate room 12"
]
choice = get_attempted_input(
    "look places to add to your score, where will you investigate first?",
    first_choices
)

while True:
    if choice in ["investigate living room", "investigate the living room"]:
        # ...existing code for living room branch...
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
                    print("You check the balcony floor and find a muddy footprint and a bottle with lipstick on it.")
                elif pick == "inspect window":
                    print("You inspect the bathroom window and see scratch marks, as if someone climbed out in a hurry.")
                elif pick == "listen at door":
                    print("You listen at the door and hear faint footsteps in the hallway. Someone might be watching you.")
                else:
                    print("You don't find anything unusual, but you can't shake the feeling that you're being watched.")
                # After exploring, ask where to go next
                next_room = get_attempted_input("Where do you want to go now? (e.g., 'investigate garden', 'investigate kitchen', 'investigate room 5')", [
                    "investigate garden", "investigate kitchen", "investigate room 5", "investigate room 6", "investigate room 7", "investigate room 8", "investigate room 9", "investigate room 10", "investigate room 11", "investigate room 12"])
                # ...existing code for next_room branches...
                if next_room == "investigate garden":
                    # ...existing code for garden branch...
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
                    # ...existing code for kitchen branch...
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
                    # ...existing code for room branches...
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
    elif choice in ["investigate kitchen"]:
        print("You head to the kitchen. The air smells of apples and something metallic.")
        print("You notice a knife missing from the rack and muddy footprints on the floor.")
        kitchen_choice = get_attempted_input("Do you want to search the trash, check the back door, or look in the fridge? (search/check/fridge/leave)", ["search", "check", "fridge", "leave"])
        if kitchen_choice == "search":
            print("You search the trash and find a torn piece of a letter: '...meet in the garden at midnight. -R'")
            print("You realize the kitchen and garden are connected in this mystery, but the trail goes cold.")
            print("Ending: The Mystery Remains.")
            sys.exit()
        elif kitchen_choice == "check":
            print("You check the back door and see muddy footprints leading away from the house. You follow them to the road, but the culprit is gone.")
            print("Ending: The Suspect Escapes.")
            sys.exit()
        elif kitchen_choice == "fridge":
            print("You open the fridge and find a bottle of expensive wine, half-empty, and a plate of untouched cheese. Someone was celebrating or hiding here.")
            print("You also find a red lipstick, the same shade as the one on the bottle from the balcony.")
            print("You sense a connection between the kitchen and the balcony.")
            print("Ending: A Tangled Web.")
            sys.exit()
        else:
            print("You leave the kitchen, feeling like you missed something important.")
            print("Ending: Unsolved, for now.")
            sys.exit()
    elif choice in ["investigate garden"]:
        print("You step into the garden. The grass is wet and you see muddy footprints leading to a shed.")
        print("The air is chilly and you hear distant birds. There are flowerbeds, a stone bench, and a small pond nearby.")
        garden_action = get_attempted_input("Do you want to examine the footprints, look at the pond, sit on the bench, or go to the shed? (footprints/pond/bench/shed)", ["footprints", "pond", "bench", "shed"])
        clues_found = []
        # Step 1: Garden exploration
        if garden_action == "footprints":
            print("You follow the muddy footprints. They circle the garden, pause at the pond, and then lead to the shed.")
            print("You notice a torn piece of red fabric caught on a rose bush.")
            clues_found.append("red fabric")
            print("You pocket the fabric and continue exploring the garden.")
            # Q1: Examine the rose bush more closely
            rose_choice = get_attempted_input("Do you want to examine the rose bush for more clues? (yes/no)", ["yes", "no"])
            if rose_choice == "yes":
                print("You find a small gold earring tangled in the thorns. It matches the locket from the pond.")
                clues_found.append("earring")
            else:
                print("You leave the rose bush alone.")
        elif garden_action == "pond":
            print("You kneel by the pond. The water is murky, but you spot something shiny at the bottom.")
            pond_choice = get_attempted_input("Do you want to reach in and grab it? (yes/no)", ["yes", "no"])
            if pond_choice == "yes":
                print("You reach into the cold water and pull out a golden locket. Inside is a photo of Clair and a mysterious person with the initial 'R'.")
                clues_found.append("locket")
                print("You dry your hands and continue exploring the garden.")
                # Q2: Open the locket
                locket_choice = get_attempted_input("Do you want to open the locket? (yes/no)", ["yes", "no"])
                if locket_choice == "yes":
                    print("Inside the locket, you find a tiny folded note: 'Trust no one in room 7.'")
                    clues_found.append("locket note")
                else:
                    print("You keep the locket closed for now.")
            else:
                print("You decide not to reach in. Maybe you'll come back later.")
        elif garden_action == "bench":
            print("You sit on the stone bench. Underneath, you find a crumpled note: 'Meet at the shed after midnight.'")
            clues_found.append("note")
            print("You feel a chill and continue exploring the garden.")
            # Q3: Inspect the bench further
            bench_choice = get_attempted_input("Do you want to look under the bench or check the ground nearby? (look/check/leave)", ["look", "check", "leave"])
            if bench_choice == "look":
                print("You find a muddy handkerchief with the initials 'R.D.'")
                clues_found.append("handkerchief")
            elif bench_choice == "check":
                print("You find a set of muddy footprints leading away from the bench toward the pond.")
                clues_found.append("bench footprints")
            else:
                print("You leave the bench and shiver in the cold.")
        else:
            print("You walk directly to the shed, the footprints squishing beneath your feet.")
            # Q4: Listen at the shed door
            listen_choice = get_attempted_input("Do you want to listen at the shed door before acting? (yes/no)", ["yes", "no"])
            if listen_choice == "yes":
                print("You hear muffled voices and the sound of something being dragged inside.")
                clues_found.append("voices")
            else:
                print("You don't hear anything unusual.")
        # Step 2: Must find at least 2 clues before shed
        if len(clues_found) < 2:
            print("You feel like you're missing something. Maybe you should look around the garden more before going to the shed.")
            # Let the player choose again
            garden_action2 = get_attempted_input("Where next in the garden? (footprints/pond/bench/shed)", ["footprints", "pond", "bench", "shed"])
            if garden_action2 == "footprints" and "red fabric" not in clues_found:
                print("You follow the muddy footprints again and find a torn piece of red fabric on a rose bush.")
                clues_found.append("red fabric")
                # Q5: Examine the rose bush again
                rose_choice2 = get_attempted_input("Do you want to examine the rose bush for more clues? (yes/no)", ["yes", "no"])
                if rose_choice2 == "yes" and "earring" not in clues_found:
                    print("You find a small gold earring tangled in the thorns. It matches the locket from the pond.")
                    clues_found.append("earring")
            elif garden_action2 == "pond" and "locket" not in clues_found:
                print("You kneel by the pond and spot something shiny at the bottom.")
                pond_choice2 = get_attempted_input("Do you want to reach in and grab it? (yes/no)", ["yes", "no"])
                if pond_choice2 == "yes":
                    print("You reach into the cold water and pull out a golden locket. Inside is a photo of Clair and a mysterious person with the initial 'R'.")
                    clues_found.append("locket")
                    # Q6: Open the locket
                    locket_choice2 = get_attempted_input("Do you want to open the locket? (yes/no)", ["yes", "no"])
                    if locket_choice2 == "yes" and "locket note" not in clues_found:
                        print("Inside the locket, you find a tiny folded note: 'Trust no one in room 7.'")
                        clues_found.append("locket note")
            elif garden_action2 == "bench" and "note" not in clues_found:
                print("You sit on the stone bench. Underneath, you find a crumpled note: 'Meet at the shed after midnight.'")
                clues_found.append("note")
                # Q7: Inspect the bench further
                bench_choice2 = get_attempted_input("Do you want to look under the bench or check the ground nearby? (look/check/leave)", ["look", "check", "leave"])
                if bench_choice2 == "look" and "handkerchief" not in clues_found:
                    print("You find a muddy handkerchief with the initials 'R.D.'")
                    clues_found.append("handkerchief")
                elif bench_choice2 == "check" and "bench footprints" not in clues_found:
                    print("You find a set of muddy footprints leading away from the bench toward the pond.")
                    clues_found.append("bench footprints")
            else:
                print("You wander the garden but find nothing new.")
        # Step 3: Now allow shed
        print("You approach the shed, clues in hand. The shed is locked, but you hear a faint noise inside.")
        shed_choice = get_attempted_input("Do you want to try to open the shed? (yes/no/knock)", ["yes", "no", "knock"])
        if shed_choice == "yes":
            print("You force the door open and find muddy boots and a torn piece of paper.")
            print("The paper reads: 'Room 9. Midnight.' This could be the culprit's room!")
            print("You hurry back to the mansion to investigate room 9.")
            print("You enter room 9. It's empty, but you find a diary under the pillow.")
            print("The diary confesses to the crime and mentions jealousy over Clair's inheritance.")
            print("You have found the culprit's room: Room 9! Congratulations, you solved the mystery.")
            sys.exit()
        elif shed_choice == "knock":
            print("You knock on the shed door. After a moment, a frightened maid opens it. She confesses she saw someone sneaking out of room 7 last night.")
            print("You decide to investigate room 7.")
            print("Inside room 7, you find a blood-stained glove and a threatening letter addressed to Clair.")
            print("you are sure that the culprit must be them, but you need more evidence.")
            print("It seems the resident of room 7 is the real culprit so You alert the authorities. Justice is served.")
            print("the resident of room 7 protests their innocence, and you are torn between believing them or not.")
            print("Ending: the unsure solution.")
            sys.exit()
        else:
            print("You decide not to open the shed. The mystery remains unsolved. Maybe some secrets are best left hidden.")
            print("Ending: The Case Goes Cold.")
            sys.exit()
    elif choice in ["investigate dining room"]:
        print("You enter the dining room. The table is set for breakfast, but no one is here.")
        print("You notice a spilled cup of tea and a napkin with a lipstick mark.")
        dining_choice = get_attempted_input("Do you want to check under the table, inspect the tea, or look at the painting? (under table/tea/painting/leave)", ["under table", "tea", "painting", "leave"])
        if dining_choice == "under table":
            print("You look under the table and find a dropped earring. It matches the locket from Clair's room.")
            print("You sense a secret relationship was hidden here.")
            print("Ending: Hidden Affairs.")
            sys.exit()
        elif dining_choice == "tea":
            print("You inspect the tea and smell a faint almond scent. Poison? You pocket the cup for evidence.")
            print("Ending: A Deadly Breakfast.")
            sys.exit()
        elif dining_choice == "painting":
            print("You look at the painting and discover a safe hidden behind it. It's locked, but you hear something moving inside.")
            print("Ending: Secrets Behind the Canvas.")
            sys.exit()
        else:
            print("You leave the dining room, feeling like you missed something important.")
            print("Ending: Unsolved, for now.")
            sys.exit()
    elif choice.startswith("investigate room"):
        room_num = choice.replace('investigate room ', '').replace('investigate ', '').strip()
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