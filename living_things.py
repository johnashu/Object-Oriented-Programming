
class LivingThing:

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
        elif dmgAmount > 0:
            print("Ouch..", self.name, "Took ", dmgAmount, "of Damage\n\n", self.name, 'New Health is: ', self.health)


class Canine(LivingThing):

    def __init__(self, furType, wild, name, legs, age, health):
        self.name = name
        self.legs = 4
        self.age = age
        self.health = health
        self.hunger = 0
        self.furType = furType
        self.wild = wild

    def FurType(self, furType):
        if self.furType == self.furType:
            print(furType)

    def isWild(self, wild):
        if self.wild is True:
            print("Be CAreful, This is a Wild Animal!!")
        else:
            print('Feel Free To Pet My Pet Dog!!')


john = LivingThing('John', 2, 36, 65)
john.DamageHealth(15)
dog = Canine('Long-Haired', True, 'fido', 4, 5, 86)

print(dog.FurType)
print(dog.isWild)

print(john.legs)
print(dog.legs)
