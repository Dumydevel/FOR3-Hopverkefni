#Kaj Arnar Jorgensen &Hrannar Örn Eyþórsson
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
        while val != 3:
            print("Do you what to add a player?")
            print("Or do you what to watch cumputer vs cumputer")
            print("press 1 to add a player")
            print("press 2 for cumputer vs cumputer")
            print("press 3 to quit")
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
                if team == 1:
                    print("pick a class")
                    print("press 1 to pick Bounty Hunter ")
                    print("press 2 to pick Sith Assasin")
                    print("press 3 to pick Sith Lord")
                    print("press 4 to pick Imperial Agent")
                    empclass = int(input("pick a class: "))
                    print()
                    if empclass == 1:
                        print("you have chosen Bounty hunter")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Blaster")
                        print("press 3 for Wrist Rockets")
                        print("press 4 for sniper")
                        weapon = int(input("pick a weapon: "))
                        if weapon == 1:
                            s = Soldiers('Bounty hunnter ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 3
                           s = Soldiers('Bounty hunnter ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                            weapon = 8
                            s = Soldiers('Bounty hunnter ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 4:
                            s = Soldiers('Bounty hunnter ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        else:
                            print("this weapon is not available")

                    elif empclass == 2:
                        print("you have chosen Sith Assassin")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Light Saber")
                        print("press 3 for Double Bladed Light Saber")
                        weapon = int(input("pick a weapon: "))
                        if weapon == 1:
                            s = Soldiers('Sith Assassin ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 5
                           s = Soldiers('Sith Assassin ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                            weapon = 15
                            s = Soldiers('Sith Assassin ' + str(cnt), randint(1, 5), weapon, randint(1, 5))

                    elif empclass == 3:
                        print("you have chosen Sith Lord")
                        print("choose a weapon")
                        print("press 1 for Light Saber")
                        print("press 2 for Double Bladed Light Saber")
                        weapon = int(input("pick a weapon: "))
                        if weapon == 1:
                            weapon = 5
                            s = Soldiers('Sith Lord ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 15
                           s = Soldiers('Sith Lord ' + str(cnt), randint(1, 5), weapon, randint(1, 5))

                    elif empclass == 4:
                        print("you have chosen Imperial Agent")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Sniper")
                        print("press 3 for Blaster")
                        print("press 4 for Ion Blaster")
                        print("press 5 for Thermal detonator")
                        print("press 6 for Disruptor")
                        weapon = int(input("pick a weapon: "))
                        if weapon == 1:
                            s = Soldiers('Imperial Agent ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 4
                           s = Soldiers('Imperial Agent ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                           s = Soldiers('Imperial Agent ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 4:
                           weapon = 12
                           s = Soldiers('Imperial Agent ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 5:
                           weapon = 14
                           s = Soldiers('Imperial Agent ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 6:
                           weapon = 9
                           s = Soldiers('Imperial Agent ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                    elif empclass == 25:
                        s = Soldiers('Darth Vader ' + str(cnt), 10, 5, 10)
                    print()
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

                elif team == 2:
                    print("press 1 to pick Jedi knight")
                    print("press 2 to pick Commando")
                    print("press 3 to pick Smuggler")
                    print("press 4 to pick Pod Racer")
                    reblclass = int(input("Pick a class: "))
                    s = Soldiers('Rebel ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                    s.weaponstats()
                    rebels.append(s)
                    empire.append(Soldiers('Empire ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5)))
                    for x in range(4):
                        cnt += 1
                        s = Soldiers('Rebel ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5))
                        s.weaponstats()
                        rebels.append(s)
                        empire.append(Soldiers('Rebel ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5)))

                    print("Team Rebels")
                    for s in rebels:
                        print(s.printsoldier())

                    print()

                    print("Team Empire")
                    for s in empire:
                        print(s.printsoldier())

                print()

                print('Fight!' + str(len(rebels)) + ' ' + str(len(empire)))
                print()
                while len(rebels) > 0 and len(empire) > 0:
                    print("Next Round!")
                    if len(rebels) == 1:
                        rebeltroop = rebels[0]
                    else:
                        rebeltroop = rebels[randint(0, len(rebels) - 1)]
                    if len(empire) == 1:
                        empiretroop = empire[0]
                    else:
                        empiretroop = empire[randint(0, len(empire) - 1)]
                    fight(rebeltroop, empiretroop)
                    print(rebeltroop.printsoldier())
                    print(empiretroop.printsoldier())
                    print()
                    if rebeltroop.live <= 0:
                        rebels.remove(rebeltroop)
                    if empiretroop.live <= 0:
                        empire.remove(empiretroop)
                    print('Empire has', len(empire), 'soldiers left')
                    print('Rebels has', len(rebels), 'soldiers left')
                    print()
                if len(rebels) < len(empire):
                    print("Empire wins")
                    print()
                    for s in empire:
                        print(s.printsoldier(self.name))
                    print("Survived")
                    print()
                elif len(empire) < len(rebels):
                    print("Rebels wins")
                    for s in rebels:
                        print(s.printsoldier(self.name))
                    print()
                else:
                    print("The dark lord Sauron joined the game out of nowhere and killed everyone with ease! ")
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

                print()

                print("Team Empire")
                for s in empire:
                    print(s.printsoldier())

                print('Fight!' + str(len(rebels))+ ' ' +  str(len(empire)))
                print()
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
                    print()
                    if rebeltroop.live <= 0:
                        rebels.remove(rebeltroop)
                    if empiretroop.live <= 0:
                        empire.remove(empiretroop)
                    print('Empire has', len(empire), 'soldiers left')
                    print('Rebels has', len(rebels), 'soldiers left')
                    print()
                if len(rebels) < len(empire):
                    print("Empire wins")
                    print()
                    for s in empire:
                        print(s.printsoldier())
                    print("survived")
                elif len(empire) < len(rebels):
                    print("Rebels wins")
                    print()
                else:
                    print("Out of nowhere the dark lord Sauron joined the game and killed everyone with ease! ")
