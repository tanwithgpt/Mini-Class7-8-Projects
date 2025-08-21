class Boss:
    def __init__(self, level, healthb, attackb, healb, rewardb,usingb):
        self.level = level
        self.healthb = healthb
        self.attackb = attackb
        self.healb = healb
        self.rewardb = rewardb
        self.usingb = usingb

Level1 = Boss(1,50,20,0,20,'N')
Level2 = Boss(2,70,50,30,50,'N')
Level3 = Boss(3,100,100,50,100,'N')