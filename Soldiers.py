from random import *

class Soldiers:
# Býr til vopn fyrir hermenina
    def weaponstats(self):
         return ["Vibro-blade","Electrostaff","Blaster","Sniper","Lightsaber","Heavy Blaster pistol","Bowcaster","Wrist rockets","Disruptor","Force pike","Vibro-az","Ion Blaster","Minigun","Thermal detonator"][self.weapon-1]
    #setur líf, kraft og vopn fyrir hermenina
    def __init__(self, name, live=0, weapon=1, power=0):
        self.name = name
        self.live = live
        self.weapon = weapon
        self.power = power
        self.weaponname = self.weaponstats()

    def printsoldier(self):
        return self.name + ' Weapon: ' + self.weaponname + ' Power: ' + str(self.power) + ' Live:  ' + str(self.live)