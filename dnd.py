import random

class Character:
    def __init__(self,hp,prof,str,dex,con,int,wis,cha):
        self.hp = hp
        self.prof = prof
        self.stats = [str,dex,con,int,wis,cha]
        #checks the integer of the stat, assigns a modifier based on integer.
        for i in range(len(self.stats)):
            stat = self.stats[i]
            if stat == 1:
                stat = -5
            elif stat <= 3:
                stat = -4
            elif stat <= 5:
                stat = -3
            elif stat <= 7:
                stat = -2
            elif stat <= 9:
                stat = -1
            elif stat <= 11:
                stat = 0
            elif stat <= 13:
                stat = 1
            elif stat <= 15:
                stat = 2
            elif stat <= 17:
                stat = 3
            elif stat <= 19:
                stat = 4
            elif stat <= 21:
                stat = 5
            elif stat <= 23:
                stat = 6
            elif stat <= 25:
                stat = 7
            elif stat <= 27:
                stat = 8
            elif stat <= 29:
                stat = 9
            elif stat == 30:
                stat = 10
            self.stats[i] = stat
        #sets each stat as the associated modifier
        self.str = self.stats[0]
        self.dex = self.stats[1]
        self.con = self.stats[2]
        self.int = self.stats[3]
        self.wis = self.stats[4]
        self.cha = self.stats[5]
        self.modstats = {'str':self.str,'dex':self.dex,'con':self.con,'int':self.int,'wis':self.wis,'cha':self.cha}
    #ass_stat can only be str,dex,con,int,wis,cha

    #function chooses a number between 1-20, and adds the roll to the given stat as a string
    def check(self,stat_string):
        ass_stat = self.modstats[stat_string]
        d20 = random.randrange(1,21)
        if d20 == 1:
            print("natural 1")
        elif d20 == 20:
            print("natural 20")
        return d20 + ass_stat

    #function chooses a number between 1-20, and adds the roll to the given stat as a string
    #with the character objects proficiency integer
    def prof_check(self,ass_stat):
        d20 = [1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,18,19,20]
        roll = random.choices(20,1) + self.prof
        return roll + self.ass_stat
    
    def take_dmg(self,dmg):
        self.hp -= dmg

#goblin character object, 300 health, 5 strength, 20 dexterity, 10 constitution
# 10 wisdom, 10 charisma. 
goblin = Character(300,1,1,10,10,10,10,10)

print(goblin.check('str'))

goblin.take_dmg(40)
print(goblin.hp)
goblin.take_dmg(40)
print(goblin.hp)
        
print(goblin.check('str'))
