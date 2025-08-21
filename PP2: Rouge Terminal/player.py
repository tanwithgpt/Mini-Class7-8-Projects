
class Player_c:
    def __init__(self,healthp,attackp,healpp,using):
        self.healthp = healthp
        self.attackp = attackp
        self.healpp = healpp
        self.using = using
class Player:
    def __init__(self,coins):
        self.coins = coins
mega = Player_c(50,30,50,'N')

ricop = Player_c(100,50,100,'N')
user = Player(0)
