import random

class Character:
    def __init__(self,hp,ac,prof,str,dex,con,int,wis,cha):
        self.hp = hp
        self.ac = ac
        self.prof = prof
        self.stats = [str,dex,con,int,wis,cha]
        for i in range(len(self.stats)):
            stat = self.stats[i]
            if stat == 1:
                stat = -5
            elif stat > 1 and stat <= 3:
                stat = -4
            elif stat >= 4 and stat <= 5:
                stat = -3
            elif stat >= 6 and stat <= 7:
                stat = -2
            elif stat >= 8 and stat <= 9:
                stat = -1
            elif stat >= 10 and stat <= 11:
                stat = 0
            elif stat >= 12 and stat <= 13:
                stat = 1
            elif stat >= 14 and stat <= 15:
                stat = 2
            elif stat >= 16 and stat <= 17:
                stat = 3
            elif stat >= 18 and stat <= 19:
                stat = 4
            elif stat >= 20 and stat <= 21:
                stat = 5
            elif stat >= 22 and stat <= 23:
                stat = 6
            elif stat >= 24 and stat <= 25:
                stat = 7
            elif stat >= 26 and stat <= 27:
                stat = 8
            elif stat >= 28 and stat <= 29:
                stat = 9
            elif stat == 30:
                stat = 10
            self.stats[i] = stat
        self.str = self.stats[0]
        self.dex = self.stats[1]
        self.con = self.stats[2]
        self.int = self.stats[3]
        self.wis = self.stats[4]
        self.cha = self.stats[5]
        self.modstats = {'str':self.str,'dex':self.dex,'con':self.con,'int':self.int,'wis':self.wis,'cha':self.cha}
    #ass_stat can only be str,dex,con,int,wis,cha
    def check(self,stat_string):
        ass_stat = self.modstats[stat_string]
        d20 = random.randrange(1,21)
        if d20 == 1:
            print("natural 1")
        elif d20 == 20:
            print("natural 20")
        return d20 + ass_stat
    def prof_check(self,ass_stat):
        d20 = [1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,18,19,20]
        roll = random.choices(20,1) + self.prof
        return roll + self.ass_stat

goblin = Character(300,18,5,20,10,10,10,10,10)

print(goblin.check('str'))
    

        
