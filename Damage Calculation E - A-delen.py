
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
            damage_multiplier = 100/dan
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

    
#Spelarna:
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


print("C-delen:")
        #Väljer vilka värden jag vill ha, hur mycket skada och motstånd, etc.
p1.attack = 100 
p2.armor = 100
p1.magic_attack = 160
p2.magical_res = 100
p2.hp = 100

            #Frågar spelaren om de vill göra magiskt eller fysikst skada
def choice():
    val = input("Would you want to do magical or physical attack? Type m for magical attack, type a for physical attack\n")
    if val == "a":
        p2.take_damage(p1.attack)
                            #Avrundar skadan och skriver ut den.
        print("Total damage:", round(p2.damage, 2))
        p2.hp -= p2.damage
        print(p2.hp)
        
    elif val == "m":
        p2.take_damage_mr(p1.magic_attack) #Anropar funktionen
        print("Total magical damage:", round(p2.damage, 2))
        p2.hp -= p2.damage
        print(p2.hp)

        #Om man inte skriver m eller a så säger den till, och börjar om.
    else:
        print("Invalid input, try again.")
        choice()


    #Funktionen körs.
choice()


print("A-delen")
#Funktion till listan av val.
def main():
    p1.attack = 0 
    p2.armor = 0
    p1.magic_attack = 0 #Från början är alla värden noll, så att inget blir fel, med nästa omgång
    p2.magical_res = 0
    p2.hp = 200
    
    print("\n1. Do attack:")
    print("2. Do magic attack:")
    print("3. Do mixed attack")
    print("4. Exit program")

    choice = input("What choice?\n")
#Om du trycker 1 så blir det denna if-sats.
    if choice == "1":
        p1.attack = input("How much attack?\n")
        p2.armor = input("How much armor?\n")

        p1.attack = int(p1.attack) #Gör om str till int
        p2.armor = int(p2.armor)


        p2.take_damage(p1.attack) #Anropar för att attackera
        p2.hp -= p2.damage #Subtraherar bort skadan på hp

        print("\nTotal damage:", round(p2.damage,2)) #Skriver ut svaren och avrundar
        print("Opponents HP:", round(p2.hp, 2))

    elif choice == "2":
        p1.magic_attack = input("How much magic attack?\n") #Frågar användaren hur mycket de olika värdena ska vara.
        p2.magical_res = input("How much magic resistance?\n")

        p1.magic_attack = int(p1.magic_attack) #str till int
        p2.magical_res = int(p2.magical_res)

        p2.take_damage_mr(p1.magic_attack) #Anropar att attackera
        p2.hp -= p2.damage

        print("\nTotal damage:", round(p2.damage,2))#Skriver ut svaren
        print("Opponents HP:", round(p2.hp, 2))

#Mixad attack
    elif choice == "3": 
        p1.attack = input("How much attack?\n")
        p2.armor = input("How much armor?\n")       #Frågar användaren, för att få värdena
        p1.magic_attack = input("How much magic attack?\n")
        p2.magical_res = input("How much magic resistance?\n")

        p1.attack = int(p1.attack)
        p2.armor = int(p2.armor)
        p1.magic_attack = int(p1.magic_attack)
        p2.magical_res = int(p2.magical_res)

        p2.take_damage(p1.attack) #Anropar första attacken
        p2.hp -= p2.damage          # Subtraherar bort skadan från HP
        p2.take_damage_mr(p1.magic_attack) #Anropar andra attacken
        p2.hp -= p2.damage

        print("\nTotal damage:", round(p2.damage,2)) #Skriver ut svaren
        print("Opponents HP:", round(p2.hp, 2))


    elif choice == "4":
        print("Exiting programme") # Stänger av programmet
        exit()

#Om den får ett annat nummer så kommer den säga till och gå tillbaka.
    else:
        print("Undentified number, try again") 
        main()

#Efter funktionen är avklarad så frågar den om man vill gå tillbaka.
    while choice != "5":
        go_back = input("Do you want to go back? Press enter or if you dont want to type no.\n")
        while go_back != "no":
            main()


#Funktionen körs.        
main()

        
        
        
        

    
        
        
        

