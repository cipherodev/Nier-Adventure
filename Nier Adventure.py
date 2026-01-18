# MADE IN 8TH GRADE, MRS.MATTICKS CLASS | 2023


### Nier:Adventure demo
###Imports
import random
import time
import math
start = time.time()
health = 10
score = 10
credits2 = "Made by Timothy Cox"
#Player If bad 
doggo_kill_list = ["The dog blows up and you DO too", 
                   "You faint and pass out due from shock", 
                   "THE DOG OFFENDS YOU DIE FROM SHOCK", 
                   "YOU CHOKE ON A TURKEY LEG AND DIED, ", 
                   "YOU FORGOT TO BREATHE"]
###Endings
Death_Ending = ["The world was [O]verrun by monsters, ENDING O", 
                "The monsters had a [R]ampage, ENDING R", 
                "The demon lord rules the ENT[I]RE WORLD! ENDING I", 
                "EVERY THING IS ON [F]IRE!!! ENDING F", 
                "THE WORLD BLOWS [U]P!!! ENDING U", 
                "A BLACK HOLE SWALLOWS THE ENTIRE [S]OLAR SYSTEM!!! ENDING S", 
                "The [W]orld Is Saved By Other People No Thanks To You! ENDING W", 
                "Your [G]ood for nothing, ENDING G", 
                "[H]alf of the entire universe is GONE, ENDING H", 
                "The World was a bad [J]udgement, ENDING J", 
                "Your not a [K]now it all, ENDING K", 
                "Your a [L]oser to the world, ENDING L", 
                "[M]onsters big meal, ENDING M", 
                "[N]ot helpful, ENDING N", 
                "[P]rotest of lives, ENDING P", 
                "[Q]uestionable actions, ENDING Q", 
                "[S]crewed over humanity, ENDING S", 
                "[T]ruth be told, ENDING T", 
                "humanity's e[X]tinction, ENDING X", 
                "opened [V]ent of time, ENDING V", 
                "what does the fox say, not a [W]in, ENDING W", 
                "[Y]our doing awful, ENDING Y", 
                "over[Z]jealous, ENDING Z" ]

true_ending = ["the [E]nd of yorha, ENDING E", 
               "One man's c[A]n, ENDING A", 
               "[B]ridge of hope, ENDING B", 
               "meaningless [C]ode, ENDING C", 
               "chil[D]hood's end, ENDING D"]

###Class for the player
class Creature:
    def __init__(self, pname, hp, xp,):
        self.pname = pname
        self.hp = hp
        self.xp = xp
        return

    def hpcalc(self, hp):
        self.hp += hp
        return

    def xpcalc(self, xp):
        self.xp += xp
        return
        
###Welcome Screen
print("V 1.0")
time.sleep(1)
print("Welcome to Nier Adventure demo".title())
print(credits2)
time.sleep(1)
print("This is a text based RPG game")
time.sleep(1)
print("This game was very inspired by the game NieR:Automata")
time.sleep(1)
print("There are easter eggs from other games and animes")
time.sleep(1)
print("all responses are lowercase")
time.sleep(1)
print("If you make a bad choice and die don't worry")
time.sleep(1)
print("After you get one of the 26 different endings it will print the input again forever")
time.sleep(1)
for i in range(4):
      print(".")
time.sleep(1)

#Player inputs
if input ("Type Start"):    
    Name = input ("What is your first name?> ")
    Player = Creature(Name, 10, 0)
    time.sleep(1)
    lastname = input("What is your last name?> ")
    time.sleep(1)
    adventurer = input("What is your class, (EX) Mage, warrior, Healer, etc?> ")
    time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    
    ###Beginning Screen
    print ("The", adventurer, "known as,", Name, "is in the country known as the Kingdom of Lugunica") 
    time.sleep(2)
    #Player HP
    print("You're a kind person and")
    time.sleep(1)
    
    #First Quest
    if input("You found a quest to save a haunted house, do you accept?> ") == "yes":
      time.sleep(1)
      print("good the house is in your hands")
      time.sleep(1)
    
    #Quest if no
    else:
      for i in range(4):
          print(".")  
      print("NEXT DAY")
      time.sleep(2)
      print(random.choice(Death_Ending))
      time.sleep(1)
      print(credits2)
      print("You should always help people in need")
      time.sleep(3)
      while input("You found a quest to save a haunted house, do you accept?> ") is not "yes":
        if input("You found a quest to save a haunted house, do you accept?> ") == "yes":
          break
    for i in range(4):
          print(".")
    
    #Story start
    print("You set out to go to a haunted house")
    time.sleep(2)
    print("The client (Who is an old lady) told you that there is a dog inside of her house")
    time.sleep(2)
    print("What could a dog do to make a lady say that her house is haunted, you think in your head")
    time.sleep(2)
    print("You open up her door to find the small, white, yet harmless little dog")
    time.sleep(2)
    #Input if dog
    if input("Do you, capture or play with the dog?> ") is not "capture":
      print("your not really going to get side tracked are you?")
      print("You get near the dog...")
      time.sleep(1)
      for i in range(4):
            print(".")
      time.sleep(1)
      print(random.choice(doggo_kill_list))
      print(random.choice(Death_Ending))
      print(credits2)
      time.sleep(5)
      while input("Do you, capture or play with the dog?> ") is not "capture":
        if input("Do you, capture or play with the dog?> ") == "capture":
          break
    for i in range(4):
          print(".")
    time.sleep(1)
    print("you are attempting to capture the dog")
    time.sleep(1)
    print("right when you thought you had him you didn't   ")
    time.sleep(1)
    print("At this moment you figured out why the old lady posted the quest  ")
    time.sleep(1)
    print("it's not that the house itself was haunted, it was the dog, A MONSTER DOG")
    time.sleep(1)
    print("The cute, little dog isn't so little now")
    time.sleep(1)
    print("the dog became 6 FEET TALL AND YOU THINK YOUR DONE FOR")
    time.sleep(2)
    for i in range(4):
          print(".")
    time.sleep(1)
    if input("DO YOU RUN OR FIGHT?> ") == "run":
      print("You run as fast as you can out of that house")
      time.sleep(2)
      print(random.choice(doggo_kill_list))
      print(random.choice(Death_Ending))
      print(credits2)
      time.sleep(5)
      while input("DO YOU RUN OR FIGHT?> ") is not "fight":
        print(input("DO YOU RUN OR FIGHT?> "))
        if input("DO YOU RUN OR FIGHT?> ") == "fight":
          break
    for i in range(4):
          print(".")
    time.sleep(1)
    print("You stand your ground to fight")
    print("ready?")
    for i in range(4):
          print(".")
    time.sleep(2)
    print("FIGHT!")
    print("You have hp:", Player.hp)
    for i in range(4):
          print(".")
    time.sleep(1)
    if input("The dog does a downward slash, do you dodge left or right> ") is not "right":
      print("you tripped on a rock...")
      time.sleep(1)
      print(random.choice(Death_Ending))
      time.sleep(1)
      print(credits2)
      time.sleep(3)
      while input("The dog does a downward slash, do you dodge left or right> ") is not "right":
        print(input("The dog does a downward slash, do you dodge left or right> "))
        if input("The dog does a downward slash, do you dodge left or right> ") == "right":
          break
    for i in range(4):
          print(".")
    time.sleep(1)
    print("You dodge the attack safely")
    time.sleep(1)
    print("Just than something unexpected happened")
    time.sleep(1)
    print("The monster Dog jump out of the house, and ran away")
    time.sleep(1)
    print("Well that was scary")
    time.sleep(1)
    print("at least I gained some XP and the enemy dropped somthing")
    level = 1
    XP = 0
    WHAT_LEVEL = "Your level", level
    if XP >= 10:
      XP = XP - 10
      level = level + 1
      
    for i in range(4):
          print(".")
    time.sleep(1)
    XP = XP + 7
    print("Your current XP is", XP)
    if input("Should I pick up the items?> ") == "yes":
      print("You picked up the items...")
      time.sleep(2)
      print("It was a XP item, you gained some XP")
      XP = XP + 4
      print("Your current XP is", XP)
    else:
      print("You leave the item alone, Maybe for the better")
    print("You walk out of the non-haunted house")
    time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    print("Peter Griffin walk up to you and says ")
    time.sleep(1)
    print("Where's my dog BRIAN?!")
    time.sleep(1)
    print("You run away fearing for your life")
    if input("where to now? Your house or old lady> ") is not "old lady":
      print("You went to your small house and laid down  on your bed")
      time.sleep(1)
      print("You went to sleep...")
      time.sleep(1)
      print("FOREVER!!!")
      time.sleep(2)
      print(random.choice(Death_Ending))
      time.sleep(4)
      while input("where to now? Your house or old lady> ") is not "old lady":
        print(input("where to now? Your house or old lady> "))
        if input("where to now? Your house or old lady> ") == "old lady":
          break
    print("You start heading to where the old lady is and on your way you spot something on the ground")
    if input("Should you pick it up> ") is not "no":
      time.sleep(1)
      print("you pick it up...")
      time.sleep(1)
      print("IT BLEW UP IN YOUR FACE always stay on track")
      time.sleep(2)
      print(random.choice(Death_Ending))
      time.sleep(4)
      while input("Should you pick it up> ") is not "no":
        print(input("Should you pick it up> "))
        if input("Should you pick it up> ") == "no":
          break
    print("Probably for the best anyway")
    time.sleep(1)
    print("You get to the old lady and you tell her what happend")
    time.sleep(2)
    print("she was happy that the dog was gone and paid you 50 silver coins")
    
    money = 50
    buy = -20
    if money < 0:
        print("You don't have enough money")
        
    time.sleep(2)
    print("With this quest complete,", Name, "sets out to go to a new town looking for work")
    print("But before you leave you head to a black smith to get a weapon")
    for i in range(4):
          print(".")
    time.sleep(1)
    print(Player.hp, "You currently have", money, "silver coins")
    Weapon = input("You decided to buy a low-level weapon for 20 silvers, what did you buy: ")
    time.sleep(1)
    print("You bought a " + Weapon)
    time.sleep(1)
    money = money + buy
    print("You have a remaining balence of", money)
    for i in range(4):
          print(".")
    time.sleep(1)
    #armor
    choice = input("Should you buy armor before leaving town? yes/no > ")
    if choice.lower() == "yes":   
        print("You go to the nearest blacksmith you could find...")
        time.sleep(1)
        print("There are (2) low level suits of armor that fit your current budget")
        time.sleep(1)
        print("overlord and yorha")
        time.sleep(1)
        print("the overlord set cost 30 silver and gives you an extra 10 health")
        print("The yorha set cost 20 and gives you an extra 5 health")
        time.sleep(1)
        armorpick = ""
        choice = False
        
        while choice == False:
            armorpick = input("Pick your armor:")
            if armorpick == "overlord" or armorpick == "yorha":
                choice = True
    
        
        def pickedarmor(armor):
            print("You bought the {} armor set".format, (armor))
            print("You currently have a max health of", Player.hp)
            print("Your current balence is", money)
            return
        if  armorpick == "overlord":
            Player.hpcalc(10)
            money = money + -30
            pickedarmor(armorpick)
        elif  armorpick == "yorha":
            Player.hpcalc(5)
            money = money + -30
            pickedarmor(armorpick)
            print("Also there is an engraving inside the armor that reads...")
            time.sleep(1)
            print("Glory To Mankind")
        else:
            print("That was not a choice")
    else:
        print("You decided not to buy armor before leaving")
            
    
    for i in range(4):
          print(".")
    time.sleep(1)
    #Continue of the game
    print("You leave the current place and enter the Nether")
    time.sleep(1)
    print("It's still in the Kingdom of Lugunica")
    print("Your current health is,", Player.hp)
    print("Your current balence is,", money)
    for i in range(4):
          print(".")
    time.sleep(1)
    print("You enter the dungeon called the Nether")
    time.sleep(1)
    print("You use your", Weapon, "and kill some low level monsters" )
    print("You gained XP")
    XP = XP + 8
    print("You now have", XP, "XP")
    time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    wtd = input ("Should you continue fighting in the dungeon, yes/no > ")
    if wtd == "yes":
        print("You continue to fight the monsters...")
        XP = XP + 10
        time.sleep(1)
        for i in range(4):
          print(".")
        time.sleep(1)
        print("Your gaining a lot of XP", XP, "but your starting to get tired...")
        
        tired = input ("Are you going to still fight?> ")
        
        if tired == "yes":
            print("You keep fighting...")
            time.sleep(1)
            print("You fall to the ground due to tiredness... ")
            print(random.choice(Death_Ending))
            time.sleep(1)
            print(credits2)
            time.sleep(3)
        if tired is not "yes":
            print("You're done with the dungeon for today because you are tired")
    
    elif wtd is not "yes":
        print("You're done with the dungeon for today")
    for i in range(4):
          print(".")
    time.sleep(1)
    print("You decided to leave the dungeon and camp out")
    time.sleep(1)
    print("Your current xp is", XP)
    print("Your current money is", money)
    time.sleep(1)
    print("you look to your right and see a girl")
    time.sleep(1)
    print("The girl casts a a spell")
    time.sleep(1)
    print("The girls says, EXPLOSION!")
    time.sleep(1)
    print("Just than a massive mushroom cloud is high up in the sky. The Explosion is powerful, the Explosion is scary")
    time.sleep(2)
    print("You do what any normal person would do and leave without saying a word")
    time.sleep(1)
    time.sleep(1)
    print("Well that was out of the normal, you think to yourself")
    time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    print("You re-enter the dungeon the next day")
    time.sleep(1)
    print("Time to battle for REAL!")
    print("Your health is", Player.hp)
    time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    ###Battle for real
    monster = ["Slime", "Cabbage", "Elder Lich", "Snufaluffagus", "Machine", "Rock", "Creeper"]
    print("You encounter a...")
    time.sleep(1)
    monster = (random.choice(monster))
    print(monster)
    time.sleep(1)
    print("You whip out your trusty,", Weapon)
    print("You are ready to fight")
    time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    print("The monster attacks you and it hurts")
    Player.hp = Player.hp + -1
    print("Your hp is", Player.hp)
    print("The fight is over you won because the monster took a nap")
    time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    
    end = input("Should you talk to the mysterious girl? yes/no > ")
    if end.lower() == "yes":   
        print("You go to the girl and she introduces herself as Megumin")
        time.sleep(1)
        print("You leave because after she casted the exsplosion she fell and won't get up")
        time.sleep(2)
        print("You are kind of worried but its not your problem so...")
        time.sleep(2)
        for i in range(4):
          print(".")
        time.sleep(1)
        print("You eventally go on in life and go to the of demon King of the world...")
        time.sleep(1)
        print("YOU BEAT THE DEMON KING!")
        time.sleep(1)   
    if end.lower() =="no":
        print ("You leave the girl be")
        time.sleep(1)
        print("You eventually go on in life and beat the demon King")
        time.sleep(1)
        print("YOU BEAT THE DEMON KING")
        time.sleep(1)
    for i in range(4):
          print(".")
    time.sleep(1)
    print("You beat Nier Adventure")
    end = time.time()
    time.sleep(2)
    print(random.choice(true_ending))
    time.sleep(2)
    print(credits2)
    time.sleep(2)
    print("You saved the entire world! Aqua is your new best friend. Here are your states of as beating the demo")
    for i in range(4):
          print(".")
    time.sleep(2)
    print("You full name was", lastname + " " + Player.pname)
    time.sleep(2)
    print("Your class was", adventurer)
    time.sleep(2)
    print("Your max health was", Player.hp)
    time.sleep(2)
    print("Your current balence is,", money)
    time.sleep(2)
    print("your xp was", XP)
    time.sleep(2)
    print("Your weapon was",Weapon)
    time.sleep(2)
    print("Your time was",(end - start))
    time.sleep(2)
    for i in range(4):
          print(".")
    time.sleep(1)
    print("The end...")
    time.sleep(1)
    print("This game is just a demo, full game coming soon")
    time.sleep(2)
    print("Thanks For Playing Nier Adventure")