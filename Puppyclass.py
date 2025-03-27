class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
class GuardDog(Dog):
    def rrr(self):
        print("Stay away")

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
        
    def __str__(self):
        return f"Puppy name is {self.name} the breed is {self.breed} "
    def test(self):
        return f"Puppy name is {self.name}"
    def woof_woof(self):
        print("Woof Woof")
    def introduce(self):
        self.woof_woof()
        
    
bibi = Puppy(name="bibi",breed="Dalmatian")

bigDog = GuardDog(name="BullDog", breed="Bull", age=5)

print(bigDog.rrr())

print(bibi)

print(bibi.test())

bibi.woof_woof()   

bibi.introduce() 