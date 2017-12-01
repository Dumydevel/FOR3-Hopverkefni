from random import *





class Soldiers:
# Býr til vopn fyrir hermenina
    def weaponstats(self):
        return ["Vibro-blade","Electrostaff","Blaster","Sniper","Lightsaber","Heavy Blaster pistol","Bowcaster","Wrist rockets","Disruptor","Force pike","Vibro-az","Ion Blaster","Minigun","Thermal detonator"][self.weapon-1]
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
                    print("press 5 to pick Imperial Agent")
                    empclass = int(input("pick a class"))

                if team == 2:
                    print("pick a class")
                    print("press 1 to pick Jedi knight")
                    print("press 2 to pick Commando")
                    print("press 3 to pick Smuggler")
                    print("press 4 to pick Pod Racer")



            if val == 2:
                cnt = 1
                for x in range(5):
                    s = Soldiers('Rebel ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5))
                    s.weaponstats()
                    rebels.append(s)
                    empire.append(Soldiers('Empire ' + str(cnt), randint(1, 5), randint(1, 14), randint(1, 5)))
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
