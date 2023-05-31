#Activity 5: Python - Object Oriented Programming Game Character
#Name: Fernandez, John Marvin D.
#Name: Florendo, Edrian E.
#Section: BSIS-NS-2C

from asyncio.windows_events import NULL


class character1:
    def __init__(self, Class, weapon, ability, ability2):
        self.Class = Class
        self.weapon = weapon
        self.ability = ability
        self.ability2 = ability2
        
    #Function for the user to choose a class
    def setClass(self):
        temp = 5
        print("----------------------------------------")
        print("Classes:")
        print("1. Wizard")
        print("2. Knight")
        print("3. Archer")
        print("4. Assassin")
        while temp > 4:
            self.Class = int(input("Enter your pick (1-4): "))
            temp = self.Class
            if (self.Class == 1):
                self.Class = "Wizard"
            elif (self.Class == 2):
                self.Class = "Knight"
            elif (self.Class == 3):
                self.Class = "Archer"
            elif (self.Class == 4):
                self.Class = "Assassin"
            else:
                print("Error! Not in the choices!")
    
    #function for the user to choose a weapon
    def setWeapon(self):
        temp = 5
        print("Weapons: ")
        print("1. Wizard Staff")
        print("2. Sword")
        print("3. Bow & Arrow")
        print("4. Katar")
        while temp > 4:
            self.weapon = int(input("Enter your pick (1-4): "))
            temp = self.weapon
            if (self.weapon == 1):
                self.weapon = "Wizard Staff"
            elif (self.weapon == 2):
                self.weapon = "Sword"
            elif (self.weapon == 3):
                self.weapon = "Bow & Arrow"
            elif (self.weapon == 4):
                self.weapon = "Katar"
            else:
                print("Error! Not in the choices!")
    
    #Function for the user to choose an ability
    def setAbility(self):
        temp = 5
        
        #Function for the Wizard class
        if (self.Class == "Wizard"):
            print("Abilities of a Wizard: ")
            print("1. Energy Ball")
            print("2. Dragons Breath")
            print("3. Crown of Flame")
            print("4. Hail Storm")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4): "))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Energy Ball"
                elif (self.ability == 2):
                    self.ability = "Dragons Breath"
                elif (self.ability == 3):
                    self.ability = "Crown of Flame"
                elif (self.ability == 4):
                    self.ability = "Hail Storm"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4): "))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Energy Ball"
                elif (self.ability2 == 2):
                    self.ability2 = "Dragons Breath"
                elif (self.ability2 == 3):
                    self.ability2 = "Crown of Flame"
                elif (self.ability2 == 4):
                    self.ability2 = "Hail Storm"
                else:
                    print("Error! Not in the choices!")
                    
        #Function for the Knight class
        if (self.Class == "Knight"):
            print("Abilities of a Knight: ")
            print("1. Fire Slash")
            print("2. Power Slash")
            print("3. Gigantic Storm")
            print("4. Chaotic Disaster")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4):"))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Fire Slash"
                elif (self.ability == 2):
                    self.ability = "Power Slash"
                elif (self.ability == 3):
                    self.ability = "Gigantic Storm"
                elif (self.ability == 4):
                    self.ability = "Chaotic Disaster"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4):"))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Fire Slash"
                elif (self.ability2 == 2):
                    self.ability2 = "Power Slash"
                elif (self.ability2 == 3):
                    self.ability2 = "Gigantic Storm"
                elif (self.ability2 == 4):
                    self.ability2 = "Chaotic Disaster"
                else:
                    print("Error! Not in the choices!")
                    
        #Function for the Archer class
        if (self.Class == "Archer"):
            print("Abilities of a Archer: ")
            print("1. Take Aim")
            print("2. Quick Shot")
            print("3. Blazing Arrow")
            print("4. Frost Arrow")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4):"))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Take Aim"
                elif (self.ability == 2):
                    self.ability = "Quick Shot"
                elif (self.ability == 3):
                    self.ability = "Blazing Arrow"
                elif (self.ability == 4):
                    self.ability = "Frost Arrow"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4):"))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Take Aim"
                elif (self.ability2 == 2):
                    self.ability2 = "Quick Shot"
                elif (self.ability2 == 3):
                    self.ability2 = "Blazing Arrow"
                elif (self.ability2 == 4):
                    self.ability2 = "Frost Arrow"
                else:
                    print("Error! Not in the choices!")
                    
        #Function for the Assassin class
        if (self.Class == "Assassin"):
            print("Abilities of a Assassin: ")
            print("1. Cloaking")
            print("2. Enchant Poison")
            print("3. Sonic Acceleration")
            print("4. Meteor Assault")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4): "))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Cloaking"
                elif (self.ability == 2):
                    self.ability = "Enchant Poison"
                elif (self.ability == 3):
                    self.ability = "Sonic Acceleration"
                elif (self.ability == 4):
                    self.ability = "Meteor Assault"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4): "))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Cloaking"
                elif (self.ability2 == 2):
                    self.ability2 = "Enchant Poison"
                elif (self.ability2 == 3):
                    self.ability2 = "Sonic Acceleration"
                elif (self.ability2 == 4):
                    self.ability2 = "Meteor Assault"
                else:
                    print("Error! Not in the choices!")
    
    #Function to show the summary of the character
    def showResult(self):
        print("----------------------------------------")
        print("Character 1: ")
        print("Character's Class: " + self.Class)
        print("Character's Weapon: " + self.weapon)
        print("Character's Abilities: ")
        print("Ability 1: " + self.ability)
        print("Ability 2: " + self.ability2)

# Class for the second character
class character2:
    def __init__(self, Class, weapon, ability, ability2):
        self.Class = Class
        self.weapon = weapon
        self.ability = ability
        self.ability2 = ability2
        
    def setClass(self):
        temp = 5
        print("----------------------------------------")
        print("Classes:")
        print("1. Wizard")
        print("2. Knight")
        print("3. Archer")
        print("4. Assassin")
        while temp > 4:
            self.Class = int(input("Enter your pick (1-4): "))
            temp = self.Class
            if (self.Class == 1):
                self.Class = "Wizard"
            elif (self.Class == 2):
                self.Class = "Knight"
            elif (self.Class == 3):
                self.Class = "Archer"
            elif (self.Class == 4):
                self.Class = "Assassin"
            else:
                print("Error! Not in the choices!")
        
    def setWeapon(self):
        temp = 5
        print("Weapons: ")
        print("1. Wizard Staff")
        print("2. Sword")
        print("3. Bow & Arrow")
        print("4. Katar")
        while temp > 4:
            self.weapon = int(input("Enter your pick (1-4): "))
            temp = self.weapon
            if (self.weapon == 1):
                self.weapon = "Wizard Staff"
            elif (self.weapon == 2):
                self.weapon = "Sword"
            elif (self.weapon == 3):
                self.weapon = "Bow & Arrow"
            elif (self.weapon == 4):
                self.weapon = "Katar"
            else:
                print("Error! Not in the choices!")
        
    def setAbility(self):
        temp = 5
        if (self.Class == "Wizard"):
            print("Abilities of a Wizard: ")
            print("1. Energy Ball")
            print("2. Dragons Breath")
            print("3. Crown of Flame")
            print("4. Hail Storm")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4): "))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Energy Ball"
                elif (self.ability == 2):
                    self.ability = "Dragons Breath"
                elif (self.ability == 3):
                    self.ability = "Crown of Flame"
                elif (self.ability == 4):
                    self.ability = "Hail Storm"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4): "))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Energy Ball"
                elif (self.ability2 == 2):
                    self.ability2 = "Dragons Breath"
                elif (self.ability2 == 3):
                    self.ability2 = "Crown of Flame"
                elif (self.ability2 == 4):
                    self.ability2 = "Hail Storm"
                else:
                    print("Error! Not in the choices!")
        if (self.Class == "Knight"):
            print("Abilities of a Knight: ")
            print("1. Fire Slash")
            print("2. Power Slash")
            print("3. Gigantic Storm")
            print("4. Chaotic Disaster")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4):"))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Fire Slash"
                elif (self.ability == 2):
                    self.ability = "Power Slash"
                elif (self.ability == 3):
                    self.ability = "Gigantic Storm"
                elif (self.ability == 4):
                    self.ability = "Chaotic Disaster"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4):"))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Fire Slash"
                elif (self.ability2 == 2):
                    self.ability2 = "Power Slash"
                elif (self.ability2 == 3):
                    self.ability2 = "Gigantic Storm"
                elif (self.ability2 == 4):
                    self.ability2 = "Chaotic Disaster"
                else:
                    print("Error! Not in the choices!")
        if (self.Class == "Archer"):
            print("Abilities of a Archer: ")
            print("1. Take Aim")
            print("2. Quick Shot")
            print("3. Blazing Arrow")
            print("4. Frost Arrow")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4):"))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Take Aim"
                elif (self.ability == 2):
                    self.ability = "Quick Shot"
                elif (self.ability == 3):
                    self.ability = "Blazing Arrow"
                elif (self.ability == 4):
                    self.ability = "Frost Arrow"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4):"))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Take Aim"
                elif (self.ability2 == 2):
                    self.ability2 = "Quick Shot"
                elif (self.ability2 == 3):
                    self.ability2 = "Blazing Arrow"
                elif (self.ability2 == 4):
                    self.ability2 = "Frost Arrow"
                else:
                    print("Error! Not in the choices!")
        if (self.Class == "Assassin"):
            print("Abilities of a Assassin: ")
            print("1. Cloaking")
            print("2. Enchant Poison")
            print("3. Sonic Acceleration")
            print("4. Meteor Assault")
            print("Only choose 2 abilities:")
            while temp > 4:
                self.ability = int(input("Enter your first pick (1-4): "))
                temp = self.ability
                if (self.ability == 1):
                    self.ability = "Cloaking"
                elif (self.ability == 2):
                    self.ability = "Enchant Poison"
                elif (self.ability == 3):
                    self.ability = "Sonic Acceleration"
                elif (self.ability == 4):
                    self.ability = "Meteor Assault"
                else:
                    print("Error! Not in the choices!")
            temp = 5
            while temp > 4:
                self.ability2 = int(input("Enter your second pick (1-4): "))
                temp = self.ability2
                if (self.ability2 == 1):
                    self.ability2 = "Cloaking"
                elif (self.ability2 == 2):
                    self.ability2 = "Enchant Poison"
                elif (self.ability2 == 3):
                    self.ability2 = "Sonic Acceleration"
                elif (self.ability2 == 4):
                    self.ability2 = "Meteor Assault"
                else:
                    print("Error! Not in the choices!")
                    
    def showResult(self):
        print("----------------------------------------")
        print("Character 2: ")
        print("Character's Class: " + self.Class)
        print("Character's Weapon: " + self.weapon)
        print("Character's Abilities: ")
        print("Ability 1: " + self.ability)
        print("Ability 2: " + self.ability2)

#main
Class, weapon, ability, ability2 = NULL, NULL, NULL, NULL
print("Activity 5: Python - Object Oriented Programming Game Character")
print("Create A Character: ")
c1 = character1(Class, weapon, ability, ability2)
c2 = character2(Class, weapon, ability, ability2)
c1.setClass()
c1.setWeapon()
c1.setAbility()
c2.setClass()
c2.setWeapon()
c2.setAbility()
c1.showResult()
c2.showResult()