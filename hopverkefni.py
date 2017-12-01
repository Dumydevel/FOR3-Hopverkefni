from random import *





class Soldiers:
# Býr til vopn fyrir hermenina
    def weaponstats(self):
        return ["Vibro-blade","Electrostaff","Blaster","Sniper","Lightsaber","Heavy Blaster pistol","Bowcaster","Wrist rockets","Disruptor","Force pike","Vibro-ax","Ion Blaster","Minigun","Thermal detonator","Double Bladed Lightsaber"][self.weapon-1]
        return "Unknown"
    #setur líf, kraft og vopn fyrir hermenina
    def __init__(self, name, live=0, weapon=1, power=0):
        self.name = name
        self.live = live
        self.weapon = weapon
        self.power = power
        self.weaponname = self.weaponstats()

    def printsoldier(self):
        return self.name + ' Weapon: ' + self.weaponname + ' Power: ' + str(self.power) + ' Live:  ' + str(self.live)



def fight(troop1, troop2):
    troop1.live -= troop2.power
    troop2.live -= troop1.power

rebels = []
empire = []
val = 0
while val != 2:
    print("welcome to Rebels vs the Empire ")
    print("Rules")
    print("each team has 5 soldiers with random weapons, life, and power")
    print("first team to eliminate each other wins")
    print("press 1 to start the war ")
    print("press 2 to quit ")
    val = int(input("press the number here"))

    if val == 1:
        while val != 2:
            print("Do you what to add a player?")
            print("Or do you what to watch cumputer vs cumputer")
            print("press 1 to add a player")
            print("press 2 for cumputer vs cumputer")
            val = int(input("press the number here"))
# striðið byrjar
            if val == 1:

                cnt = 1
                print("Do you want to be the Empire or the Rebel")
                print("Press 1 to select the Empire")
                print("Press 2 to select the Rebels")
                team = int(input("press the number here: "))
                if team == 1:
                    print("pick a class")
                    print("press 1 to pick Bounty Hunter ")
                    print("press 2 to pick Sith Assasin")
                    print("press 3 to pick Sith Lord")
                    print("press 4 to pick Imperial Agent")
                    empclass = int(input("pick a class"))

                    if empclass == 1:
                        print("you have chosen Bounty hunter")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Blaster")
                        print("press 3 for Wrist Rockets")
                        print("press 4 for sniper")
                        weapon = int(input("pick a weapon"))
                        if weapon == 1:
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 3
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                            weapon = 8
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 4:
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        else:
                            print("this weapon is not available")

                    if empclass == 2:
                        print("you have chosen Sith Assasin")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Light Saber")
                        print("press 3 for Double Bladed Light Saber")
                        weapon = int(input("pick a weapon"))
                        if weapon == 1:
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 5
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                            weapon = 15
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))

                    if empclass == 3:
                        print("you have chosen Sith Lord")
                        print("choose a weapon")
                        print("press 1 for Light Saber")
                        print("press 2 for Double Bladed Light Saber")
                        weapon = int(input("pick a weapon"))
                        if weapon == 1:
                            weapon = 5
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 15
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))

                    if empclass == 4:
                        print("you have chosen Imperial Agent")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Sniper")
                        print("press 3 for Blaster")
                        print("press 4 for Ion Blaster")
                        print("press 5 for Thermal detonator")
                        print("press 6 for Disruptor")
                        weapon = int(input("pick a weapon"))
                        if weapon == 1:
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 4
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 4:
                           weapon = 12
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 5:
                           weapon = 14
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 9
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))





                if team == 2:
                    print("pick a class")
                    print("press 1 to pick Jedi knight")
                    print("press 2 to pick Commando")
                    print("press 3 to pick Smuggler")
                    print("press 4 to pick Pod Racer")
                    rebclass = int(input("pick a class"))

                    if rebclass == 1:
                        print("you have chosen Jedi Knight")
                        print("choose a weapon")
                        print("press 1 for Light Saber")
                        print("press 2 for Double Blader Lightsaber")

                        weapon = int(input("pick a weapon"))
                        if weapon == 1:
                            weapon = 5
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 15
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        else:
                            print("this weapon is not available")
                    if rebclass == 2:
                        print("you have chosen Comando")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Blaster")
                        print("press 3 for Heavy Blaster Pistol")
                        print("press 4 for Bowcaster")
                        print("press 5 for Vibro-Ax")
                        print("press 6 for Minigun")
                        weapon = int(input("pick a weapon"))
                        if weapon == 1:
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 3
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                            weapon = 6
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 4:
                            weapon = 7
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 5:
                            weapon = 11
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 6:
                            weapon = 13
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        else:
                            print("this weapon is not available")
                    if rebclass == 3:
                        print("you have chosen Smuggler")
                        print("choose a weapon")
                        print("press 1 for Vibro-Blade")
                        print("press 2 for Blaster")
                        print("press 3 for Thermal detonator")
                        print("press 4 for Bowcaster")
                        weapon = int(input("pick a weapon"))
                        if weapon == 1:
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 2:
                           weapon = 3
                           s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 3:
                            weapon = 14
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        elif weapon == 4:
                            weapon = 7
                            s = Soldiers('Empire ' + str(cnt), randint(1, 5), weapon, randint(1, 5))
                        else:
                            print("this weapon is not available")
                    



            if val == 2:
                cnt = 1
                for x in range(5):
                    s = Soldiers('Rebel ' + str(cnt), randint(1, 5), randint(1, 15), randint(1, 5))
                    s.weaponstats()
                    rebels.append(s)
                    empire.append(Soldiers('Empire ' + str(cnt), randint(1, 5), randint(1, 15), randint(1, 5)))
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
