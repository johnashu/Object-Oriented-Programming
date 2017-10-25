
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
            print(self.name, ' Is DeeD!!!\n')
        elif dmgAmount > 0:
            print("\nOuch..", self.name, "Took ", dmgAmount, "of Damage\n\n" +
                  self.name + '\'s New Health is: ', self.health, '\n')


class Human(LivingThing):

    def __init__(self, name, legs, age, health, languages, city):
        self.name = name
        self.legs = 2
        self.age = age
        self.health = health
        self.hunger = 0
        self.languages = [languages]
        self.city = city

    def addLanguage(self, language):
        self.languages.append(language)

    def wearsGlasses(self, wears):
        if wears is True:
            print('\n' + self.name, 'Wears Glasses')
        else:
            print('\n' + self.name, "Does not wear glasses")

    def hasChildren(self, haschild, gender=None, age=0):
        gender = gender.upper()
        if haschild is True:
            print(self.name, "has children")
        else:
            print(self.name, "Has Zero Children")

        if gender == "MALE":
            print("The child is a Boy")
        elif gender == "FEMALE":
            print("The child is a Girl")

        try:
            age == int(age)
            if age != 0:
                print(self.name + '\'s', gender, 'is {} years old'.format(age))
            else:
                print("no age given")
        except ValueError:
            if age is not None:
                print(age, "is not an integer")

    def shoeSize(self, ss):
        if ss == int(ss):
            print(self.name, "shoe size is {}".format(ss))


class Canine(LivingThing):

    def __init__(self, furType, wild, name, legs, age, health):
        self.name = name
        self.legs = 4
        self.age = age
        self.health = health
        self.hunger = 0
        self.furType = furType
        self.wild = wild

    def FurType(self):
        if self.furType == self.furType:
            return self.furType

    def isWild(self):
        if self.wild is True:
            return "Be Careful, This is a Wild Animal!!\n"
        else:
            return 'Feel Free To Pet My Dog!!\n'


class Feline(LivingThing):

    def __init__(self, furType, wild, name, legs, age, health):
        self.name = name
        self.legs = 4
        self.age = age
        self.health = health
        self.hunger = 0
        self.furType = furType
        self.wild = wild

    def FurType(self):
        if self.furType == self.furType:
            return self.furType

    def isWild(self):
        if self.wild is True:
            return "Be Careful, This is a Wild Animal!!\n"
        else:
            return 'Feel Free To Pet My Cat!!\n'


john = Human('John', 2, 36, 65, 'English', 'Rosmalen')
john.DamageHealth(15)
john.addLanguage('Dutch')
print("LAnguages spoken by ", john.name, john.languages)

john.wearsGlasses(False)


john.shoeSize(9)

john.hasChildren(True, 'MALE', 'beans')
john.hasChildren(True, 'MALE', 1)
john.hasChildren(True, 'MALE')


dog = Canine('Long-Haired', True, 'Fido', 4, 5, 86)
cat = Feline('Short-Haired', False, 'Gotham', 4, 5, 86)

print('\nThe Dog\'s fur is ', dog.FurType())
print(dog.isWild())

print('\nThe Cat\'s fur is ', cat.FurType())
print(cat.isWild())

# print(john.legs)
# print(dog.legs)
# print(cat.legs)
