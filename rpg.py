'''
Description:
<A role playing game with a fighter (user defined class) in combat against another fighter. 
The two will try to hit eachother until one is left standing>
'''

import random

class Fighter: #User defined class, Fighter, that can attack and take damage.
    def __init__(self, name): #init, self explanitory
        self.name = name
        self.hit_points = 10
    
    def __repr__(self): #repr, how to print
        return ( self.name + " (HP: " + str(self.hit_points) + ")" )
        
    def take_damage(self, damage_amount): #reduces damage points
        self.hit_points = self.hit_points - damage_amount
        if self.hit_points <= 0:        
            print("Alas, " + self.name + " has fallen!")
        elif self.hit_points == 1:
            print(self.name + " has 1 hit point remaining.")
        else:
            print(self.name + " has " + str(self.hit_points) + " hit points remaining.")
    
    def attack(self, other): #brings on the pain for the other Fighter, or just misses
        print(self.name + " attacks " + other.name + "!")
        strike = random.randint(1,20)
        if strike > 11:
            damage = random.randint(1,6)
            if damage == 1:            
                print("Hits for " + str(damage) + " hit point!")
            else:
                print("Hits for " + str(damage) + " hit points!")
            other.take_damage(damage)
        else:
            print("Misses!") 
    

def combat_round(fighter1, fighter2): #this will make run a simulated fight sequence. The two fighters will get random numbers to find out who strikes first, or they might just go simultaneously

    f1_roll = random.randint(1,6) #simulates tolling a 6 sided die
    f2_roll = random.randint(1,6)
    if f1_roll == f2_roll:
        print("Simultaneous!") #attack at the same time
        fighter1.attack(fighter2)
        fighter2.attack(fighter1)
    else:
        if f1_roll > f2_roll:
            fighter1.attack(fighter2)
        if fighter2.hit_points > 0:
            fighter2.attack(fighter1)
        if f2_roll > f1_roll:
            fighter2.attack(fighter1)
            if fighter1.hit_points > 0:
                fighter1.attack(fighter2)

def main():
    little_brother = Fighter("Little Brother")
    big_brother = Fighter("Big Brother")
    ''' This program will simulate a fight between two siblings. The while loop will keep them in combat until one loses all their hit points.
    '''
    count = 1
    while True: #makes the game keep running
        print("{:=^52}".format(" ROUND " + str(count) + " "))
        count += 1
        print(little_brother)
        print(big_brother)
        raw_input = input("Enter to Fight!")
        combat_round(little_brother, big_brother)
        if little_brother.hit_points < 1 or big_brother.hit_points < 1:
            print("The battle is over!")
            print(little_brother)
            print(big_brother)
            break



if __name__ == '__main__':
    main()
