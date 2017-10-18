
class LivingThing():

    def __init__(self, name, legs, age, health):
        self.name = name
        self.legs = legs
        self.age = age
        self.health = health
        self.hunger = 0

    def DamageHealth(self, dmgAmount):
        self.health = self.health - dmgAmount
        if self.health == 0:
            print(self.name, ' Is DeeD!!!')


class Canine(LivingThing):

    def __init__(self, furType, wild):
        self.furType = furType
        self.wild = wild

    def FurType(self):
        self.furType = self.furType
        print(self.furType)

    def isWild(self, wild):
        if self.wild is True:
            print("Be CAreful, This is a Wild Animal!!")
        else:
            print('Feel Free To Pet My Pet Dog!!')


john = LivingThing('john', 2, 36, 65)
john.DamageHealth(65)
dog = LivingThing('fido', 4, 5, 86 )
dog = Canine('Long-Haired', True)

print(dog.FurType)
print(dog.isWild)

print(john.legs)
print(john.health)
