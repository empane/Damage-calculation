
class Player():             #Klassen, som beskriver spelaren.
    def __init__(self, name, hp, attack, magic_attack, armor, magical_res, damage):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.magic_attack = magic_attack
        self.armor = armor
        self.magical_res = magical_res
        self.damage = damage

                #Tar fysisk skada
    def take_damage(self, opponent_attack):
        dammut = self.calc_multiplier(self.armor)
        self.damage = opponent_attack * dammut
        return self.damage

                    #Tar magiskt skada
    def take_damage_mr(self, opponent_attack_mr):
        dam = self.calc_multiplier_mr(self.magical_res)
        self.damage = opponent_attack_mr * dam
        return self.damage
        
            #Räknar ut den fysiska skada och motstånd 
    def calc_multiplier(self, armor):
        if self.armor > 0:
            dan = 100 + self.armor
            print("dan:", dan)
            damage_multiplier = 100/dan
            print("mul:", damage_multiplier)
            return damage_multiplier

        else:
            damage_multiplier = 2 - (100/(100 - self.armor))
            return damage_multiplier

            #Räknar ut den magiska skada och motstånd
    def calc_multiplier_mr(self, magical_res):
        if self.magical_res > 0:
            damage_multi = 100/(100 + self.magical_res)
            return damage_multi

        else:
            damage_multi = 2 - (100/(100 - self.magical_res))
            return damage_multi

    

p1 = Player("Alex", 0, 0, 0, 0, 0, 0)
p2 = Player("Will", 0, 0, 0, 0, 0, 0)

print("E-delen:")
print("You´re player 1") 
p1.attack = 200
p2.armor = 120
p1.magic_attack = 160
p2.magical_res = 100

print(p1.name, "attacks", p2.name)
opponent_attack = p1.attack
print("Attack points:", opponent_attack)
p2.take_damage(opponent_attack)
print("Total damage:", round(p2.damage, 2))


print("C-delen")
        #Väljer vilka värden jag vill ha, hur mycket skada och motstånd, etc.
p1.attack = 100 
p2.armor = 100
p1.magic_attack = 160
p2.magical_res = 100

            #Frågar spelaren om de vill göra magiskt eller fysikst skada
def choice():
    val = input("Would you want to do magical or physical attack? Type m for magical attack, type a for physical attack\n")
    if val == "a":
        p2.take_damage(p1.attack)
                            #Avrundar skadan och skriver ut den.
        print("Total damage:", round(p2.damage, 2))
        p2.hp -= p2.damage
    elif val == "m":
        p2.take_damage_mr(p1.magic_attack)
        print("Total magical damage:", round(p2.damage, 2))
        p2.hp -= p2.damage

        #Om man inte skriver m eller a så säger den till, och börjar om.
    else:
        print("Invalid input, try again.")
        choice()


    #Funktionen körs.
choice()





        
#class Opponent():
    #def __init__(self, name, hp, attack, magic_attack, armor, mr):
     #   self.name = name
      #  self.hp = hp
       # self.attack = attack
        #self.magic_attack = magic_attack
        #self.armor = armor
        #self.mr = magical_res
