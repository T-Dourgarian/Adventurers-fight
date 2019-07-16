# This is the same as HW9A until the tournament function

class Adventurer(object):

    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = level * 6
        self.hidden = False

    def __repr__(self):
        return self.name + ' - HP: ' + str(self.HP)

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getStrength(self):
        return self.strength
    
    def getSpeed(self):
        return self.speed
    
    def getPower(self):
        return self.power
    
    def getHP(self):
        return self.HP

    def getHidden(self):
        return self.hidden

    def setStrength(self,NewStrength):
        self.strength = NewStrength

    def setHP(self,NewHP):
        self.HP = NewHP

    def setHidden(self,newHidden):
        self.hidden = newHidden
    

    def attack(self,target):
        if target.getHidden() == True:
            return self.name + ' can''t see ' + target.getName()
        else:
            target.setHP(target.getHP() - (self.strength + 4))
            print(self.name + ' attacks ' + target.getName() + ' for ' + str(self.strength + 4) + ' damage')


class Fighter(Adventurer):

    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = level * 12
        self.hidden = False
        
            
    def attack(self,target):
        if target.getHidden() == True:
            print(self.name + ' can''t see ' + target.getName())
        else:
            target.setHP(target.getHP() - (2*self.strength + 6))
            print(self.name + ' attacks ' + target.getName() + ' for ' + str(2*self.strength + 6) + ' damage')
    

class Thief(Adventurer):

    def __init__(self,name = '', level = 0, strength = 0, speed = 0, power = 0):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = level * 8
        self.hidden = True

    def attack(self,target):
        if self.hidden == False:
            super(Thief,self).attack(target)
        elif self.hidden == True and target.getHidden() == True and self.speed < target.getSpeed():
            print(self.name + ' can''t see ' + target.getName())
        else:
            self.hidden = False
            target.setHidden(False)
            target.setHP(target.getHP() - ((self.speed + self.level) * 5))
            print(self.name + ' sneak attacks ' + target.getName() + ' for ' + str((self.speed + self.level) * 5) + ' damage')



class Wizard(Adventurer):

    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = level * 6
        self.hidden = False
        self.fireballs_left = power

    def attack(self,target):
        if self.fireballs_left == 0:
            super(Wizard,self).attack(target)
        else:
            target.setHidden(False)
            target.setHP(target.getHP() - (self.level * 3))
            self.fireballs_left -= 1
            print(self.name + ' casts fireball on ' + target.getName() + ' for ' + str(self.level * 3) + ' damage')



def duel(adv1, adv2):
    print(adv1)
    print(adv2)
    while adv1.getHP() > 0 and adv2.getHP() > 0:
        adv1.attack(adv2)
        if adv2.getHP() <= 0 and adv1 != adv2:
            print(adv1.getName() + ' wins!')
            return True
            
        adv2.attack(adv1)
        if adv1.getHP() <= 0 and adv1 != adv2:
            print(adv1)
            print(adv2)
            print(adv2.getName() + ' wins!')
            return False
                
        print(adv1)
        print(adv2)
        
    if not(max([adv1.getHP(),adv2.getHP()]) == adv1.getHP() and adv1.getHP() != adv2.getHP() and max([adv1.getHP(),adv2.getHP()]) == adv2.getHP()) and not(adv1.getHP() != adv2.getHP()):
        print('Everyone loses!')
        return False

# same as HW 9A until here

def tournament(advList):
    if len(advList) == 0:
        return None
    elif len(advList) == 1:
        return advList[0]
    else:
        # Duel until the list length is 1
        while len(advList) != 1:
            # sorting
            advList = sorted(advList, key=lambda Adventurer:Adventurer.getHP(),reverse = True)
            # adv1 wins
            if duel(advList[1],advList[0]) == True:
                del advList[0]
            # adv2 wins
            else:
                del advList[1]
        return advList[0]
            
        
    
                         
                  
        
