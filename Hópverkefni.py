#skilaverkefni6
#kaj arnar jorgensen
#31.3.17

from random import *
from Soldiers import *

def fight(troop1, troop2):
    troop1.live -= troop2.power
    troop2.live -= troop1.power

rebels = []
empire = []
val = 0
while val != 2:
    print("welcome to Rebels vs the Empire\n ")
    print("Rules:")
    print("each team has 5 soldiers with random weapons, life, and power")
    print("first team to eliminate each other wins\n")
    print("press 1 to start the war ")
    print("press 2 to quit ")
    val = int(input("press the number here: "))
    print()

    if val == 1:
        while val != 2:
            print("Do you what to add a player?")
            print("Or do you what to watch cumputer vs cumputer")
            print("press 1 to add a player")
            print("press 2 for cumputer vs cumputer")
            val = int(input("press the number here: "))
            print()
# striðið byrjar
            if val == 1:
                cnt = 1
                print("Do you want to be the Empire or the Rebel")
                print("Press 1 to select the Empire")
                print("Press 2 to select the Rebels")
                team = int(input("press the number here: "))
                print()
                weapon = int(input("Choose your weapon: "))
                if team == 1:
                    s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                    s.weaponstats()
                    empire.append(s)
                    rebels.append(Soldiers('Rebel ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5)))
                    for x in range(4):
                        cnt += 1
                        s = Soldiers('Empire ' + str(cnt),randint(1,5),randint(1,14),randint(1,5))
                        s.weaponstats()
                        empire.append(s)
                        rebels.append(Soldiers('Rebel ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5)))

                print("Team Empire")
                for s in empire:
                    print(s.printsoldier())

                print()

                print("Team Rebels")
                for s in rebels:
                    print(s.printsoldier())

                print()

            elif val == 2:
                cnt = 1
                for x in range(5):
                    s = Soldiers('Rebel ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5))
                    s.weaponstats()
                    rebels.append(s)
                    empire.append(Soldiers('Empire ' + str(cnt), randint(1, 5), randint(1, 11), randint(1, 5)))
                    cnt += 1

                print("Team Rebels")
                for s in rebels:
                    print(s.printsoldier())

                print("Team Empire")
                for s in empire:
                    print(s.printsoldier())

                print('Fight!' + str(len(rebels))+ ' ' +  str(len(empire)))
                while len(rebels) > 0 and len(empire) > 0:
                    print("Next Round!")
                    if len(rebels) == 1:
                        rebeltroop = rebels[0]
                    else:
                        rebeltroop = rebels[randint(0,len(rebels)-1)]
                    if len(empire) == 1:
                        empiretroop = empire[0]
                    else:
                        empiretroop = empire[randint(0,len(empire)-1)]
                    fight(rebeltroop, empiretroop)
                    print(rebeltroop.printsoldier())
                    print(empiretroop.printsoldier())
                    if rebeltroop.live <= 0:
                        rebels.remove(rebeltroop)
                    if empiretroop.live <= 0:
                        empire.remove(empiretroop)
                    print('Empire has', len(empire), 'soldiers left')
                    print('Rebels has', len(rebels), 'soldiers left')
                if len(rebels) < len(empire):
                    print("Empire wins")
                elif len(empire) < len(rebels):
                    print("Rebels wins")
                else:
                    print("Every one died the Dark Lord Sauron takes over ")
