import math
import random
i = 0
j = 0
lvlUp = ((3,2,2),(2,2,3),(2,3,2))

class player:   
# Some base stats.
    currentLocation = None
    enemiesDefeated = 0
    level = 1
    exp = 0
    totalGold = 0
    gold = 0
    turn = 0
    maxSkillPoints = 5
    skillPoints = 5
    #equiped[0] is bow/sword/shield, equiped[1] is armor/armour/I don't know, I'll just use armor.
    equipped = [None,None]
    inventory = [None,None,None,None,None,None,None,None,None,None]
    # Progress 0: Game hasn't been started yet.
    progress = 0
    # LOTS OF FOREST STUFF
    pos = None
    forestGrid = []
    mov = 2
    still = True
    goblins = 0
    def __move(self,direction,y=0,x=0,i=0):
        if str.lower(direction) == "up":
            if self.pos.up == True:
                self.still = False
                while y <= 4:
                    for tile in self.forestGrid[y]:
                        if tile == self.pos:
                            i = 1
                            break
                        else:
                            x = x + 1
                    if i == 1:
                        break
                    else:
                        x = 0
                        y = y + 1
                if y-1 == -1:
                    print("You reached the end\nof the forest!")
                    return 2
                else:
                    self.pos = self.forestGrid[y-1][x]
                    if enemy1:
                        self.goblins = self.goblins + random.randint(1,3)
                        if self.goblins >= 8:
                            self.goblins = 0
                            print("A goblin attacks!")
                            while True:
                                attacks = random.randint(1,8)
                                if self.level == 1:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                elif self.level == 2:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                elif self.level == 3:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                elif self.level >= 4:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                    elif attacks == 7:
                                        enemy1.newEnemy(1,"4")
                                        break
                                    elif attacks == 8:
                                        enemy1.newEnemy(2,"4")
                                        break
                            battle(self,enemy1)
                    return 0
            else:
                print("You can't go up!")
                if self.pos.left == True:
                    if self.pos.down == True:
                        if self.pos.right == True:
                            print("However, you can go left, down and right.")
                        else:
                            print("However, you can go left and down.")
                    elif self.pos.right == True:
                        print("However, you can go left and right.")
                    else:
                        print("However, you can go left.")
                elif self.pos.down:
                    if self.pos.right == True:
                        print("However, you can go down and right.")
                    else:
                        print("However, you can go down.")
                else:
                    print("However, you can go right.")
                return 0
        elif str.lower(direction) == "left":
            if self.pos.left == True:
                self.still = False
                while y <= 4:
                    for tile in self.forestGrid[y]:
                        if tile == self.pos:
                            i = 1
                            break
                        else:
                            x = x + 1
                    if i == 1:
                        break
                    else:
                        x = 0
                        y = y + 1
                self.pos = self.forestGrid[y][x-1]
                if enemy1:
                        self.goblins = self.goblins + random.randint(1,3)
                        if self.goblins >= 8:
                            self.goblins = 0
                            print("A goblin attacks!")
                            while True:
                                attacks = random.randint(1,8)
                                if self.level == 1:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                elif self.level == 2:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                elif self.level == 3:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                elif self.level >= 4:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                    elif attacks == 7:
                                        enemy1.newEnemy(1,"4")
                                        break
                                    elif attacks == 8:
                                        enemy1.newEnemy(2,"4")
                                        break
                            battle(self,enemy1)
                return 0
            else:
                print("You can't go left!")
                if self.pos.up == True:
                    if self.pos.down == True:
                        if self.pos.right == True:
                            print("However, you can go up, down and right.")
                        else:
                            print("However, you can go up and down.")
                    elif self.pos.right == True:
                        print("However, you can go up and right.")
                    else:
                        print("However, you can go up.")
                elif self.pos.down:
                    if self.pos.right == True:
                        print("However, you can go down and right.")
                    else:
                        print("However, you can go down.")
                else:
                    print("However, you can go right.")
                return 0
        elif str.lower(direction) == "down":
            if self.pos.down == True:
                self.still == False
                while y <= 4:
                    for tile in self.forestGrid[y]:
                        if tile == self.pos:
                            i = 1
                            break
                        else:
                            x = x + 1
                    if i == 1:
                        break
                    else:
                        x = 0
                        y = y + 1
                if y+1 == 5:
                    print("You decide to go back\nout of the deep forest...")
                    return 1
                else:
                    self.pos = self.forestGrid[y+1][x]
                    if enemy1:
                        self.goblins = self.goblins + random.randint(1,3)
                        if self.goblins >= 8:
                            self.goblins = 0
                            print("A goblin attacks!")
                            while True:
                                attacks = random.randint(1,8)
                                if self.level == 1:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                elif self.level == 2:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                elif self.level == 3:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                elif self.level >= 4:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                    elif attacks == 7:
                                        enemy1.newEnemy(1,"4")
                                        break
                                    elif attacks == 8:
                                        enemy1.newEnemy(2,"4")
                                        break
                            battle(self,enemy1)
                    return 0
            else:
                print("You can't go down!")
                if self.pos.up == True:
                    if self.pos.left == True:
                        if self.pos.right == True:
                            print("However, you can go up, left and right.")
                        else:
                            print("However, you can go up and left.")
                    elif self.pos.right == True:
                        print("However, you can go up and right.")
                    else:
                        print("However, you can go up.")
                elif self.pos.left:
                    if self.pos.right == True:
                        print("However, you can go left and right.")
                    else:
                        print("However, you can go left.")
                else:
                    print("However, you can go right.")
                return 0
        elif str.lower(direction) == "right":
            if self.pos.right == True:
                self.still = False
                while y <= 4:
                    for tile in self.forestGrid[y]:
                        if tile == self.pos:
                            i = 1
                            break
                        else:
                            x = x + 1
                    if i == 1:
                        break
                    else:
                        x = 0
                        y = y + 1
                self.pos = self.forestGrid[y][x+1]
                if enemy1:
                        self.goblins = self.goblins + random.randint(1,3)
                        if self.goblins >= 8:
                            self.goblins = 0
                            print("A goblin attacks!")
                            while True:
                                attacks = random.randint(1,8)
                                if self.level == 1:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                elif self.level == 2:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                elif self.level == 3:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                elif self.level >= 4:
                                    if attacks == 1:
                                        enemy1.newEnemy(1,"1")
                                        break
                                    elif attacks == 2:
                                        enemy1.newEnemy(2,"1")
                                        break
                                    elif attacks == 3:
                                        enemy1.newEnemy(1,"2")
                                        break
                                    elif attacks == 4:
                                        enemy1.newEnemy(2,"2")
                                        break
                                    elif attacks == 5:
                                        enemy1.newEnemy(1,"3")
                                        break
                                    elif attacks == 6:
                                        enemy1.newEnemy(2,"3")
                                        break
                                    elif attacks == 7:
                                        enemy1.newEnemy(1,"4")
                                        break
                                    elif attacks == 8:
                                        enemy1.newEnemy(2,"4")
                                        break
                            battle(self,enemy1)
                return 0
            else:
                print("You can't go right!")
                if self.pos.up == True:
                    if self.pos.left == True:
                        if self.pos.down == True:
                            print("However, you can go up, left and down.")
                        else:
                            print("However, you can go up and left.")
                    elif self.pos.down == True:
                        print("However, you can go up and down.")
                    else:
                        print("However, you can go up.")
                elif self.pos.left:
                    if self.pos.down == True:
                        print("However, you can go left and down.")
                    else:
                        print("However, you can go left.")
                else:
                    print("However, you can go down.")
                    return 0
        else:
            print("That isn't a valid direction!")
            print("Valid directions are up, down, left and right.")
            if self.pos.up == True:
                if self.pos.left == True:
                    if self.pos.down == True:
                        if self.pos.right == True:
                            ways = "up, left, down and right."
                        else:
                            ways = "up, left and down."
                    elif self.pos.right == True:
                        ways = "up, left and right."
                    else:
                        ways = "up and left."
                elif self.pos.down == True:
                    if self.pos.right == True:
                        ways = "up, down and right."
                    else:
                        ways = "up and down."
                elif self.pos.right == True:
                    ways = "up and right."
                else:
                    ways = "up."
            elif self.pos.left == True:
                if self.pos.down == True:
                    if self.pos.right == True:
                        ways = "left, down and right."
                    else:
                        ways = "left and down."
                elif self.pos.right == True:
                    ways = "left and right."
                else:
                    ways = "left."
            elif self.pos.down == True:
                if self.pos.right == True:
                    ways = "down and right."
                else:
                    ways = "down."
            elif self.pos.right == True:
                ways = "right."
            print("Of the valid directions you can go " + ways)
            return 0
    def move(self):
        if self.mov == 2:
            print("Valid directions are up, down, left and right.")
            self.mov = 0
        if self.pos.up == True:
            if self.pos.left == True:
                if self.pos.down == True:
                    if self.pos.right == True:
                        ways = "UP, LEFT, DOWN and RIGHT."
                    else:
                        ways = "UP, LEFT and DOWN."
                elif self.pos.right == True:
                    ways = "UP, LEFT and RIGHT."
                else:
                    ways = "UP and LEFT."
            elif self.pos.down == True:
                if self.pos.right == True:
                    ways = "UP, DOWN and RIGHT."
                else:
                    ways = "UP and DOWN."
            elif self.pos.right == True:
                ways = "UP and RIGHT."
            else:
                ways = "UP."
        elif self.pos.left == True:
            if self.pos.down == True:
                if self.pos.right == True:
                    ways = "LEFT, DOWN and RIGHT."
                else:
                    ways = "LEFT and DOWN."
            elif self.pos.right == True:
                ways = "LEFT and RIGHT."
            else:
                ways = "LEFT."
        elif self.pos.down == True:
            if self.pos.right == True:
                ways = "DOWN and RIGHT."
            else:
                ways = "DOWN."
        elif self.pos.right == True:
            ways = "RIGHT."
        print("You can go " + ways)
        direct = input("Which direction do you want to go?: ")
        event = self.__move(direct)
        if event == 1:
            self.currentPosition = forest
        elif event == 2:
            if self.progress == 4:
                if self.level >= 5:
                    print("The Lord of Goblins watches you enter the room,\n and challenges you to a battle to the death!")
                    enemy1.newEnemy(1,"boss")
                    battle(self,enemy1)
                    print("You look around after the duel,\nand find that the Goblins have fled!")
                    #Progress 5: You beat the Lord of Goblins!
                    self.progress = 5
                    print("You decide to head back out.")
                    self.pos = self.forestGrid[0][4]
                else:
                    print("The Lord of Goblins is here!\nThey look at you for a few moments\nbefore they signal guards to throw you out.")
                    self.pos = self.forestGrid[0][4]
            else:
                print("All that remains are\na few scavengers...")
                self.pos = self.forestGrid[0][4]
    def forestSleep(self,enemy1):
        forestChance = random.randint(1,7)
        if forestChance >= 6:
            while True:
                sleepEnemy = random.randint(1,6)
                if sleepEnemy == 1: 
                    enemy1.newEnemy(1,"1")
                    break
                elif sleepEnemy == 2:
                    enemy1.newEnemy(2,"1")
                    break
                if self.level >= 2:
                    if sleepEnemy == 3:
                        enemy1.newEnemy(1,"2")
                        break
                    elif sleepEnemy == 4:
                        enemy1.newEnemy(2,"2")
                        break
                if self.level >= 3:
                    if sleepEnemy == 5:
                        enemy1.newEnemy(1,"3")
                        break
                    elif sleepEnemy == 6:
                        enemy1.newEnemy(2,"3")
                        break
            print("An enemy attacks while you sleep!")
            player1.health = player1.health + ((player1.maxHealth / 3)//1)
            if player1.health > player1.maxHealth:
                player1.health = player1.maxHealth
            battle(self,enemy1)
        else:
            print("You were able to sleep peacefully!")
            player1.health = (((player1.maxHealth / 4)*3)//1) + player1.health
            if player1.health > player1.maxHealth:
                player1.health = player1.maxHealth
    # END OF LOTS OF FOREST STUFF
    # Game over code.
    def youLose(self):
        # Progress -1: You FAIL.
        self.progress = -1
        print("You have died.\nYou lose.\nYou were able to defeat " + str(self.enemiesDefeated) + " enemies,\n and obtained a total of " + str(self.totalGold) + " gold.\n You also reached level " + str(self.level) + ".\nPlease restart the game,\nas I haven't added save files.")
        YOUFAIL = math.inf/0
        print(YOUFAIL)
# Code for rangers.
class ranger(player):
    maxHealth = 5
    health = 5
    attack = 3
    magic = 2
    classChoose = 0
    def startGame(self):
        print("You are a " + playerclass + ".\n This game is just a demo right now.\n There may be bugs or glitches.")
        # Progress 1: You started started game.
        self.progress = 1
# Code for warriors.
class warrior(player):
    maxHealth = 10
    health = 10
    attack = 2
    magic = 1
    classChoose = 1
    def startGame(self):
        print("You are a " + playerclass + ".\n This game is just a demo right now.\n There may be bugs or glitches.")
        # Progress 1: You started started game.
        self.progress = 1
# Code for shielders.
class shielder(player):
    maxHealth = 15
    health = 15
    attack = 1
    magic = 3
    classChoose = 2
    def startGame(self):
        print("You are a " + playerclass + ".\n This game is just a demo right now.\n There may be bugs or glitches.")
        # Progress 1: You started started game.
        self.progress = 1





# Start menu code.
while True:
    print("---------------")
    print("Game menu:")
    print("1 - Start game.")
    print("2 - Choose player.")
    print("3 - Choose magic.")
    print("---------------")
    choice = input("Choose: ")
    # Choose menu code.
    if choice == "2":
        if i != 1:
            playerclass = input("Choose a class:\nRanger, Warrior, or Shielder.")
            # If playerclass is "ranger", you're a ranger.
            if str.lower(playerclass) == "ranger":
                play = ranger
                i = 1
                print("You are a ranger!\nYou have an amazing attack damage,\n but are frail in comparison to others!")
            # Else, if playerclass is "warrior", you're a warrior.
            elif str.lower(playerclass) == "warrior":
                play = warrior
                i = 1
                print("You are a warrior!\nYou have relatively good defence,\nAND have a good strength of attacks!")
            # Else, if playerclass is "shielder", you're a shielder.
            elif str.lower(playerclass) == "shielder":
                play = shielder
                i = 1
                print("You are a defender!\nYou're hard to take down,\n but aren't good at attacking!")
            # Else, display an error message.
            else:
                print("Please try again.")
        # If you already chose your player class, show an error message.
        else:
            print("You already chose your player class!")
    # Start the game if you chose your player's class. Else, error message.
    elif choice == "1":
        if i == 1 and j == 1:
            play.startGame
            break
        elif i == 0 and j == 1:
            print("You haven't chosen your player class yet!")
        elif i == 1 and j == 0:
            print("You haven't chosen your player's magic yet!")
        else:
            print("You haven't chosen your\nplayer magic and class yet!")
    elif choice == "3":
        if j == 0:
            playermagic = input("Choose a magic type:\nFire, Lightning or Void.")
            if str.lower(playermagic) == "fire":
                print("You are capable of fire magic!")
                j = 1
                playermagic = "fire"
            elif str.lower(playermagic) == "lightning":
                print("You can handle lightning magic!")
                j = 1
                playermagic = "lightning"
            elif str.lower(playermagic) == "void":
                print("You can control void magic!")
                j = 1
                playermagic = "void"
            else:
                print("That isn't an option!")
        else:
            print("You already chose your magic!")
    # Else if you choose anything else, show an error message.
    else:
        print("Choose a choice.")





def levelUp(player1):
    if player1.exp >= (player1.level * 10):
        player1.level += 1
        newStats = "Level up!\nYour level is now " + str(player1.level) + "!\nHealth: " + str(player1.maxHealth) + " => " + str(player1.maxHealth + lvlUp[player1.classChoose][0]) + "!\nAttack: " + str(player1.attack) + " => " + str(player1.attack + lvlUp[player1.classChoose][1]) + "!\nMagic: " + str(player1.magic) + " => " + str(player1.magic + lvlUp[player1.classChoose][2]) + "!\nSkill points: " + str(player1.maxSkillPoints) + " => " + str(player1.maxSkillPoints + 2) + "!"
        print(newStats)
        player1.maxHealth += lvlUp[player1.classChoose][0]
        player1.health = player1.maxHealth
        player1.attack += lvlUp[player1.classChoose][1]
        player1.magic += lvlUp[player1.classChoose][2]
        player1.maxSkillPoints += 2
        player1.skillPoints = player1.maxSkillPoints
        player1.exp = 0
        
        
        
        
        
# Items code.
class item:
    itemType = " "
    itemHeal = 0
    itemHealth = 0
    itemAttack = 0
    itemMagic = 0
    itemGold = 0
    itemName = " "
    itemSlot = 0
    def equip(self,player1):
        
        
        
        if self.itemType == "weapon":
            if player1.equipped[0] == None:
                print("You equipped the " + self.itemName + ".")
                player1.equipped[0] = self
                player1.attack = player1.attack + player1.equipped[0].itemAttack
                player1.magic = player1.magic + player1.equipped[0].itemMagic
                player1.inventory[player1.inventory.index(self)] = None
            else:
                print("You put away your " + player1.equipped[0].itemName + "\nand equip the " + self.itemName + ".")
                player1.attack = player1.attack - player1.equipped[0].itemAttack
                player1.magic = player1.magic - player1.equipped[0].itemMagic
                for item in player1.inventory:
                    if item == None:
                        item = player1.equipped[0]
                        break
                player1.inventory[player1.inventory.index(self)] = None
                player1.equipped[0] = self
                player1.attack = player1.attack + player1.equipped[0].itemAttack
                player1.magic = player1.magic + player1.equipped[0].itemMagic
                
                
                
        elif self.itemType == "armor":
            if player1.equipped[1] == None:
                print("You wear the " + self.itemName + ".")
                player1.equipped[1] = self
                player1.maxHealth = int(player1.maxHealth) + int(player1.equipped[1].itemHealth)
                player1.health = int(player1.health) + int(player1.equipped[1].itemHealth)
                player1.magic = int(player1.magic) + int(player1.equipped[1].itemMagic)
                player1.inventory[player1.inventory.index(self)] = None
            else:
                print("You take off your " + player1.equipped[1].itemName + "\nand wear the " + self.itemName + ".")
                player1.maxHealth = player1.maxHealth - player1.equipped[1].itemHealth
                player1.health = player1.health - player1.equipped[1].itemHealth
                player1.magic = player1.magic - player1.equipped[1].itemMagic
                itemnum = 0
                for item in player1.inventory:
                    if item == None:
                        empty = 0
                        for item in player1.inventory:
                            if item == None:
                                empty = empty + 1
                        if empty == 10:
                            player1.inventory[0] = player1.equipped[1]
                            self.itemSlot = 0
                        elif empty == 9:
                            player1.inventory[1] = player1.equipped[1]
                            self.itemSlot = 1
                        elif empty == 8:
                            player1.inventory[2] = player1.equipped[1]
                            self.itemSlot = 2
                        elif empty == 7:
                            player1.inventory[3] = player1.equipped[1]
                            self.itemSlot = 3
                        elif empty == 6:
                            player1.inventory[4] = player1.equipped[1]
                            self.itemSlot = 4
                        elif empty == 5:
                            player1.inventory[5] = player1.equipped[1]
                            self.itemSlot = 5
                        elif empty == 4:
                            player1.inventory[6] = player1.equipped[1]
                            self.itemSlot = 6
                        elif empty == 3:
                            player1.inventory[7] = player1.equipped[1]
                            self.itemSlot = 7
                        elif empty == 2:
                            player1.inventory[8] = player1.equipped[1]
                            self.itemSlot = 8
                        elif empty == 1:
                            player1.inventory[9] = player1.equipped[1]
                            self.itemSlot = 9
                        else:
                            1 / 0
                        break
                player1.equipped[1] = self
                player1.inventory[self.itemSlot] = None
                player1.maxHealth = player1.maxHealth + player1.equipped[1].itemHealth
                player1.health = player1.health + player1.equipped[1].itemHealth
                player1.magic = player1.magic + player1.equipped[1].itemMagic
                
        else:
            print("You can't equip that!")
            
            
            
    def use(self,player1):
        if self.itemType == "potion":
            print("You drink the " + self.itemName + ".")
            print("You restored " + str(self.itemHeal) + " health!")
            player1.health += self.itemHeal
            if player1.maxHealth <= player1.health:
                player1.health = player1.maxHealth
            player1.inventory[self.itemSlot] = None
            return True
        else:
            print("You can't use that!")
            return False
            
            
            
            
            
class potion(item):
    def __init__(self,healType,player1,empty = 0):
        for item in player1.inventory:
            if item == None:
                empty = empty + 1
        if empty == 10:
            player1.inventory[0] = self
            self.itemSlot = 0
        elif empty == 9:
            player1.inventory[1] = self
            self.itemSlot = 1
        elif empty == 8:
            player1.inventory[2] = self
            self.itemSlot = 2
        elif empty == 7:
            player1.inventory[3] = self
            self.itemSlot = 3
        elif empty == 6:
            player1.inventory[4] = self
            self.itemSlot = 4
        elif empty == 5:
            player1.inventory[5] = self
            self.itemSlot = 5
        elif empty == 4:
            player1.inventory[6] = self
            self.itemSlot = 6
        elif empty == 3:
            player1.inventory[7] = self
            self.itemSlot = 7
        elif empty == 2:
            player1.inventory[8] = self
            self.itemSlot = 8
        elif empty == 1:
            player1.inventory[9] = self
            self.itemSlot = 9
        else:
            1 / 0
        self.itemType = "potion"
        if healType == "small":
            self.itemHeal = 3
            self.itemName = "Small Potion"
            self.itemGold = 5
        elif healType == "medium":
            self.itemHeal = 5
            self.itemName = "Potion"
            self.itemGold = 10
        elif healType == "large":
            self.itemHeal = 10
            self.itemName = "Large Potion"
            self.itemGold = 15
            
            
            
            
            
class weapon(item):
    def __init__(self,weaponType,player1,empty = 0):
        newItems = self
        for item in player1.inventory:
            if item == None:
                empty = empty + 1
        if empty == 10:
            player1.inventory[0] = newItems
            self.itemSlot = 0
        elif empty == 9:
            player1.inventory[1] = newItems
            self.itemSlot = 1
        elif empty == 8:
            player1.inventory[2] = newItems
            self.itemSlot = 2
        elif empty == 7:
            player1.inventory[3] = newItems
            self.itemSlot = 3
        elif empty == 6:
            player1.inventory[4] = newItems
            self.itemSlot = 4
        elif empty == 5:
            player1.inventory[5] = newItems
            self.itemSlot = 5
        elif empty == 4:
            player1.inventory[6] = newItems
            self.itemSlot = 6
        elif empty == 3:
            player1.inventory[7] = newItems
            self.itemSlot = 7
        elif empty == 2:
            player1.inventory[8] = newItems
            self.itemSlot = 8
        elif empty == 1:
            player1.inventory[9] = newItems
            self.itemSlot = 9
        else:
            1 / 0
        self.itemType = "weapon"
        if playerclass == "ranger":
            if weaponType == "weak":
                self.itemAttack = 1
                self.itemName = "Weak Bow"
                self.itemGold = 10
            elif weaponType == "strong":
                self.itemAttack = 2
                self.itemName = "Bow"
                self.itemGold = 20
            elif weaponType == "magic":
                self.itemAttack = 2
                self.itemMagic = 1
                self.itemName = "Mystic Bow"
                self.itemGold = 30
        if playerclass == "warrior":
            if weaponType == "weak":
                self.itemAttack = 1
                self.itemName = "Rusty Sword"
                self.itemGold = 10
            elif weaponType == "strong":
                self.itemAttack = 2
                self.itemName = "Sword"
                self.itemGold = 20
            elif weaponType == "magic":
                self.itemAttack = 2
                self.itemMagic = 1
                self.itemName = "Mystic Sword"
                self.itemGold = 30
        if playerclass == "shielder":
            if weaponType == "weak":
                self.itemAttack = 1
                self.itemName = "Wooden Shield"
                self.itemGold = 10
            elif weaponType == "strong":
                self.itemAttack = 2
                self.itemName = "Iron Shield"
                self.itemGold = 20
            elif weaponType == "magic":
                self.itemAttack = 2
                self.itemMagic = 1
                self.itemName = "Mystic Shield"
                self.itemGold = 30
                
                
                
                
                
class armor(item):
    def __init__(self,armorType,player1,empty = 0):
        newItems = self
        for item in player1.inventory:
            if item == None:
                empty = empty + 1
        if empty == 10:
            player1.inventory[0] = newItems
            self.itemSlot = 0
        elif empty == 9:
            player1.inventory[1] = newItems
            self.itemSlot = 1
        elif empty == 8:
            player1.inventory[2] = newItems
            self.itemSlot = 2
        elif empty == 7:
            player1.inventory[3] = newItems
            self.itemSlot = 3
        elif empty == 6:
            player1.inventory[4] = newItems
            self.itemSlot = 4
        elif empty == 5:
            player1.inventory[5] = newItems
            self.itemSlot = 5
        elif empty == 4:
            player1.inventory[6] = newItems
            self.itemSlot = 6
        elif empty == 3:
            player1.inventory[7] = newItems
            self.itemSlot = 7
        elif empty == 2:
            player1.inventory[8] = newItems
            self.itemSlot = 8
        elif empty == 1:
            player1.inventory[9] = newItems
            self.itemSlot = 9
        else:
            1 / 0
        self.itemType = "armor"
        if armorType == "weak":
            self.itemName = "Leather Armor"
            self.itemHealth = 3
            self.itemGold = 15
        elif armorType == "strong":
            self.itemName = "Steel Armor"
            self.itemHealth = 6
            self.itemGold = 25
        elif armorType == "magic":
            self.itemName = "Mystic Armor"
            self.itemHealth = 10
            self.itemMagic = 3
            self.itemGold = 40
            
            
            
            
            
weapon1 = weapon("weak",play)
armor1 = armor("weak",play)





# Enemy class code.
class enemy:
    def __init__(self,enemytype):
        self.exp = 4
        self.gold = 10
        self.level = "1"
        # Choose what enemy is spawned, from the closen type and level.
        if enemytype == 1:
            self.name = "Goblin"
            self.maxHealth = 3
            self.health = 3
            self.attack = 2
        elif enemytype == 2:
            self.name = "Shield Goblin"
            self.maxHealth = 5
            self.health = 5
            self.attack = 1
    # Method for changing the spawned enemy.
    def newEnemy(self,enemytype,enemylevel):
        self.level = str(enemylevel)
        if self.level == "boss":
            if enemytype == 1:
                #Level 4
                self.name = "Goblin Warlord"
                self.maxHealth = 40
                self.health = 40
                self.attack = 5
                self.exp = 40
                self.gold = 100
            elif enemytype == 2:
                #Level 8
                self.name = "Dragon"
                self.maxHealth = 75
                self.health = 75
                self.attack = 8
                self.exp = 80
                self.gold = 250
        if self.level == "1":
            if enemytype == 1:
                self.name = "Goblin"
                self.maxHealth = 3
                self.health = 3
                self.attack = 2
                self.exp = 4
                self.gold = 10
            elif enemytype == 2:
                self.name = "Shield Goblin"
                self.maxHealth = 5
                self.health = 5
                self.attack = 1
                self.exp = 4
                self.gold = 10
        elif self.level == "2":
            if enemytype == 1:
                self.name = "Goblin Bowman"
                self.maxHealth = 5
                self.health = 5
                self.attack = 3
                self.exp = 6
                self.gold = 15
            elif enemytype == 2:
                self.name = "Sword Goblin"
                self.maxHealth = 8
                self.health = 8
                self.attack = 2
                self.exp = 6
                self.gold = 15
        elif self.level == "3":
            if enemytype == 1:
                self.name = "Goblin Hogrider"
                self.maxHealth = 7
                self.health = 7
                self.attack = 4
                self.exp = 8
                self.gold = 20
            elif enemytype == 2:
                self.name = "Armored Goblin"
                self.maxHealth = 10
                self.health = 10
                self.attack = 3
                self.exp = 8
                self.gold = 20
        elif self.level == "4":
            if enemytype == 1:
                self.name = "Goblin Crossbowman"
                self.maxHealth = 9
                self.health = 9
                self.attack = 5
                self.exp = 10
                self.gold = 25
            if enemytype == 2:
                self.name = "Goblin Chariot"
                self.maxHealth = 12
                self.health = 12
                self.attack = 4
                self.exp = 10
                self.gold = 25
            
            
    # Enemy fight code.
    def fight(self,target):
        target.health = target.health - self.attack
        print(self.name + " attacks!")
        print("The enemy attacked for " + str(self.attack) + " damage!")


    # Code for when enemy is defeated.
    def defeated(self,target):
        print("You defeated " + self.name + "!")
        print("You won " + str(self.gold) + " gold\nand " + str(self.exp) + " exp.")
        target.totalGold += self.gold
        target.gold += self.gold
        target.exp += self.exp
        target.enemiesDefeated += 1
        
        
        
        
        
# Fight code.
def fight(player1,enemy1):
    if playerclass == "ranger":
        # If you're a ranger, fight like this.
        print("You fire an arrow at the enemy for " + str(player1.attack) + " damage!")
        enemy1.health = enemy1.health - player1.attack

    elif playerclass == "warrior":
        print("You slash at the enemy for " + str(player1.attack) + " damage!")
        enemy1.health = enemy1.health - player1.attack

    elif playerclass == "shielder":
        print("You bash the enemy with your\nshield for " + str(player1.attack) + " damage!")
        enemy1.health = enemy1.health - player1.attack
        
#SKILLS GO HERE.
def strongArrow(player1,enemy1):
    if player1.skillPoints >= 1:
        skillDamage = player1.attack * 2
        enemy1.health = enemy1.health - skillDamage
        player1.skillPoints = player1.skillPoints - 1
        print("You fire a heavy arrow at the enemy!")
        return True
    else:
        print("You don't have enough skill points!")
        
def poisonArrow(player1,enemy1):
    if player1.skillPoints >= 2:
        skillDamage = (player1.attack * 1.5) // 1
        enemy1.health = enemy1.health - skillDamage
        player1.skillPoints = player1.skillPoints - 2
        print("You fire a poison-tipped arrow at the enemy!")
        return True
    else:
        print("You don't have enough skill points!")
        
def strongSlash(player1,enemy1):
    if player1.skillPoints >= 1:
        skillDamage = player1.attack * 2
        enemy1.health = enemy1.health - skillDamage
        player1.skillPoints = player1.skillPoints - 1
        print("You hit the enemy with\nenough force to cut down a tree!")
        return True
    else:
        print("You don't have enough skill points!")
        
def fireBlade(player1,enemy1):
    if player1.skillPoints >= 2:
        skillDamage = player1.attack + (2 * player1.level)
        enemy1.health = enemy1.health - skillDamage
        player1.skillPoints = player1.skillPoints - 2
        print("You slash at the enemy so\nfast that your blade is ablaze!")
        return True
    else:
        print("You don't have enough skill points!")
        
def shieldCharge(player1,enemy1):
    if player1.skillPoints >= 1:
        skillDamage = player1.attack * (2 + player1.level)
        enemy1.health = enemy1.health - skillDamage
        player1.skillPoints = player1.skillPoints - 1
        print("You charge at the enemy and\nsmash your shield into them!")
        return True
    else:
        print("You don't have enough skill points!")
        
def shieldThrow(player1,enemy1):
    if player1.skillPoints >= 2:
        skillDamage = (enemy1.health / 2)
        if (skillDamage // 1) != skillDamage:
            skillDamage += 0.5
        enemy1.health = enemy1.health - skillDamage
        player1.skillPoints = player1.skillPoints - 2
        print("You throw your shield at the enemy,\nand it bounces back to you!")
        return True
    else:
        print("You don't have enough skill points!")
        
        
        
        

#Skills menu code.
def skillsMenu(player1,enemy1):
    #Skills list.
    if playerclass == "ranger":
        skillslist = ("     1 - Strong Shot","     2 - Poison Arrow")
    elif playerclass == "warrior":
        skillslist = ("     1 - Strong Slash","     2 - Fire Blade")
    elif playerclass == "shielder":
        skillslist = ("     1 - Shield Charge","     2 - Shield Throw")
    skilMenu = """
-------------------------
         SKILLS!
  Your skill points: """ + str(player1.skillPoints) + "/" + str(player1.maxSkillPoints) + "\n" + skillslist[0] + "\n" + skillslist[1] + "\n        3 - Back" + "\n-------------------------"
    print(skilMenu)
    while True:
        skilMenu = """
-------------------------
         SKILLS!
  Your skill points: """ + str(player1.skillPoints) + "/" + str(player1.maxSkillPoints) + "\n" + skillslist[0] + "\n" + skillslist[1] + "\n        3 - Back" + "\n-------------------------"
        choice = input("    Choose option:  ")
        if str(choice) == str(1):
            if playerclass == "ranger":
                if strongArrow(player1,enemy1) == True:
                    player1.turn = 1
                    break
            elif playerclass == "warrior":
                if strongSlash(player1,enemy1) == True:
                    player1.turn = 1
                    break
            elif playerclass == "shielder":
                if shieldCharge(player1,enemy1) == True:
                    player1.turn = 1
                    break
        elif str(choice) == str(2):
            if playerclass == "ranger":
                if poisonArrow(player1,enemy1) == True:
                    player1.turn = 1
                    break
            elif playerclass == "warrior":
                if fireBlade(player1,enemy1) == True:
                    player1.turn = 1
                    break
            elif playerclass == "shielder":
                if shieldThrow(player1,enemy1) == True:
                    player1.turn = 1
                    break
        elif str(choice) == str(3):
            break
        else:
            print("That was not an option.")
            
            
            
#Magic menu code.
def magicMenu(player1,enemy1):
    while True:
        print("-------------------------")
        print("         MAGIC!")
        print("        1 - Heal")
        if playermagic == "fire":
            print("      2 - Fireball")
        elif playermagic == "lightning":
            print("   2 - Lightning bolt")
        else:
            print("     2 - Void blast")
        print("        3 - Back")
        print("-------------------------")
        choice = input("     Choose option: ")
        if str(choice) == str(1):
            print("You healed " + str((player1.maxHealth/2)//1) + " health points!")
            player1.health = int(player1.health) + int((player1.maxHealth/2)//1)
            if player1.health > player1.maxHealth:
                player1.health = player1.maxHealth
            player1.turn = 0
            break
        elif choice == "2":
            if playermagic == "fire":
                print("You threw an inferno compressed\n into a fist-sized blast at the enemy!")
                print(str(player1.magic*2) + " damage!")
                enemy1.health = enemy1.health - (player1.magic * 2)
                player1.turn = 0
                break
            elif playermagic == "lightning":
                print("You struck a thunderbolt down\nfrom the heavens at the enemy!")
                magicdamage = player1.magic*1.5
                if magicdamage//1 != magicdamage:
                    magicdamage += 0.5
                magicdamage = int(magicdamage)
                print(str(magicdamage) + " damage!")
                enemy1.health == enemy1.health - magicdamage
                player1.turn = 0
                break
            else:
                print("You fire void towards the enemy!")
                print(str(player1.magic*3)+" damage!")
                enemy1.health = enemy1.health - player1.magic*3
                player1.turn = 0
                break
        elif str(choice) == str(3):
            player1.turn = 1
            break
        else:
            print("That isn't an option!")
#Items code



def itemsMenu(player1):
    while True:
        if player1.inventory[0]:
            print("-------------------------")
            print("       INVENTORY!")
            itemNumber = 0
            for item in player1.inventory:
                print("       " + str(itemNumber) + " - " + item.itemName)
                itemNumber = itemNumber + 1
            print("        " + str(itemNumber) + " - Back")
            print("-------------------------")
            choice = input("    Choose option: ")
            if str(choice) == str(itemNumber):
                player1.turn = 0
                break
            elif player1.inventory[int(choice)]:
                if player1.inventory[int(choice)].use(player1) == True:
                    player1.turn = 1
                    break
                else:
                    player1.turn = 0
            else:
                print("That isn't an option!")
        print("You have no items!")
        player1.turn = 0
        break
    
    
    
#Fleeing code
def flee(player1,enemy1):
    if enemy1.level == "boss":
        print("You can't run from this!")
        rolls = 0
        escaped = False
        return False
    elif int(player1.level) == int(enemy1.level):
        escapeChance = 5
        rolls = 2
    elif int(player1.level) > int(enemy1.level):
        escapeChance = 8
        rolls = 3
    else:
        escapeChance = 3
        rolls = 1
    while rolls > 0:
        rolled = random.randint(1,10)
        if rolled <= escapeChance:
            escaped = True
            rolls = rolls - 1
            return escaped
        else:
            rolls = rolls - 1
    if not escaped:
        escaped = False
        return escaped
        
        
        
#Fight menu code
def fightMenu(player1,enemy1):
    i = 0
    while i != 1:
        print("-------------------------")
        print("         BATTLE!")
        print("     Your health: " + str(player1.health) + "/" + str(player1.maxHealth))
        print("     Enemy health: " + str(enemy1.health) + "/" + str(enemy1.maxHealth))
        print("       1 - Attack!")
        print("       2 - Skills!")
        print("       3 - Magic!")
        print("       4 - Items")
        print("       5 - Flee!")
        print("-------------------------")
        choice = input("    Choose option:  ")
        if str(choice) == str(1):
            fight(player1,enemy1)
            i = 1
        elif str(choice) == str(2):
            skillsMenu(player1,enemy1)
            if player1.turn == 1:
                player1.turn = 0
                i = 1
        elif str(choice) == str(3):
            magicMenu(player1,enemy1)
            if player1.turn == 0:
                i = 1
        elif str(choice) == str(4):
            itemsMenu(player1)
            if player1.turn == 1:
                player1.turn = 0
                i = 1
        elif str(choice) == str(5):
            print("You try to escape!")
            escaped = flee(player1,enemy1)
            i = 1
            if escaped == True:
                player1.turn = 4
                print("You got away!")
            else:
                print("You failed to run away!")
            break
        else:
            print("That isn't an option.")
            
            
            
#Battle code.
def battle(player1,enemy1):
    print(enemy1.name + " appears!")

    if playerclass == "ranger":
        print("You prepare your bow and arrows.")
    elif playerclass == "warrior":
        print("You grip your sword tightly.")
    elif playerclass == "shielder":
        print("You hold onto your shield.")

    # First attack decider.
    first = random.randint(1,2)
    while True:
        if first == 1:
            print("You attack first!")
            fightMenu(player1,enemy1)
            if player1.turn == 4:
                break
            if enemy1.health <= 0:
                break
            else:
                enemy1.fight(player1)
                if player1.health <= 0:
                    player1.youLose

        else:
            enemy1.fight(player1)
            if player1.health <= 0:
                player1.youLose
            else:
                print("You attack!")
                fightMenu(player1,enemy1)
                if player1.turn == 4:
                    break
                if enemy1.health <= 0:
                    break
        first = random.randint(1,2)

        print("--------------------")
        print("End of turn:")
        print("Player health: " + str(player1.health) + "/" + str(player1.maxHealth))
        print("Enemy health: " + str(enemy1.health) + "/" + str(enemy1.maxHealth))
        print("--------------------")
    if player1.turn == 4:
        if player1.gold >= 5:
            print("You won nothing...\n...Apart from -5 gold...\n...that you dropped...\n...when running away...")
            player1.gold = player1.gold - 5
        elif player1.gold >= 3:
            print("You won nothing...\n...Apart from 3 gold...\n...that you dropped...\n...when running away...")
            player1.gold = player1.gold - 3
        elif player1.gold >= 1:
            print("You won nothing...\n...Apart from some gold...\n...that you dropped...\n...when running away...")
            player1.gold = player1.gold - 1
        else:
            print("You won nothing...")
    else:
        enemy1.defeated(player1)
        levelUp(player1)
    enemy1.health = enemy1.maxHealth
    
    
    
potion1 = potion("medium",play)
potion2 = potion("medium",play)
potion3 = potion("medium",play)
weapon1.equip(play)
armor1.equip(play)
enemytypechoice = random.randint(1,2)
enemy1 = enemy(1)
if enemytypechoice == 1:
    enemy1.newEnemy(1,1)
elif enemytypechoice == 2:
    enemy1.newEnemy(2,1)
battle(play,enemy1)
print("-------------------------")
play.health = play.maxHealth
#Progress 2: You won a combat!
play.progress = 2
#Place descriptions
desc = {"startVillage": "You find yourself inside a small village,\nwith a mountain to one side\nand a forest to the other,\nwith a river between.","debugArea": "This is the debug area.","forest": "You are deep within a forest\ninhabited by Goblins...","mountain": "You're at the entrance of\nthe Dragon's mountain lair!","deepForest": "The trees block out most\nlight this far into the forest.\nThe goblins could be anywhere..."}





#Place code
class place:
    def __init__(self,name,isShop,isRest,descr):
        self.name = name
        self.description = descr
        self.shop = isShop
        self.heal = isRest
        self.firsttime = True
        self.north = None
        self.east = None
        self.south = None
        self.west = None
    def __setOtherPlaces(self,north,east,south,west):
        if north == None:
            print("There is nothing north of here.")
            self.north = None
        else:
            print(north.name + " is north of here.")
            self.north = north
        if east == None:
            print("There is nothing east of here.")
            self.east = None
        else:
            print(east.name + " is east of here.")
            self.east = east
        if south == None:
            print("There is nothing south of here.")
            self.south = None
        else:
            print(south.name + " is south of here.")
            self.south = south
        if west == None:
            print("There is nothing west of here.")
            self.west = None
        else:
            print(west.name + " is west of here.")
            self.west = west
    def isHere(self,n,e,s,w):
        if self == debugArea:
            play.isDebug = True
        else:
            play.currentLocation = self
        print("-~--~--~--~-\n" + self.name + "\n-~--~--~--~-")
        print(self.description + "\n-~--~--~--~-")
        if self.shop and self.heal == 413:
            while True:
                break
        elif self.shop:
            if self.heal:
                print("You can see a shop and\na healing place here.")
            else:
                print("You can see a shop here.")
        elif self.heal:
            print("You can see a healing place here.")
        else:
            print("There seems to be no\nshops or healing places here.")
        print("-~--~--~--~-")
        if self == deepForest:
            if self.firstTime == True:
                print("You can't find which way is\nnorth, east, south or west...")
                self.firstTime == False
        elif self.firsttime:
            self.firsttime = False
            self.__setOtherPlaces(n,e,s,w)
        elif self == forest:
            if startTown.north == self:
                print("The forest is deep north of here.")
                print("The forest is blocked to the east.")
                print("The way back to town is south.")
                print("The forest is blocked to the west.")
            elif startTown.east == self:
                print("The forest is blocked to the north.")
                print("The forest is deep east of here.")
                print("The forest is blocked to the south.")
                print("The way back to town is west.")
            elif startTown.south == self:
                print("The way back to town is north.")
                print("The forest is blocked to the east.")
                print("The forest is deep south of here.")
                print("The forest is blocked to the west.")
            else:
                print("The forest is blocked north of here.")
                print("The way back to town is east.")
                print("The forest is blocked south of here.")
                print("The forest is deep west of here.")
        else:
            if self.north == None:
                print("There is nothing north of here.")
            else:
                print(self.north.name + " is north of here.")
            if self.east == None:
                print("There is nothing east of here.")
            else:
                print(self.east.name + " is east of here.")
            if self.south == None:
                print("There is nothing south of here.")
            else:
                print(self.south.name + " is south of here.")
            if self.west == None:
                print("There is nothing west of here.")
            else:
                print(self.west.name + " is west of here.")
                
                
                
                
                
startTown = place("Starting Village",True,True,desc["startVillage"])
debugArea = place("Debug Testing Area",413,413,desc["debugArea"])
forest = place("Goblin Forest",413,413,desc["forest"])
mountain = place("Dragon Mountain",False,True,desc["mountain"])
deepForest = place("Deep Forest",413,413,desc["deepForest"])
debugArea.isHere(None,None,None,None)


def debugAreaPlace(player1):
    while True:
        print("-------------------------")
        print("  DEBUG TESTING STUFF!")
        print("      1 - Battle!")
        print("   2 - Player stats")
        print("    3 - More stuff")
        print(" 4 - Experimental stuff")
        print("      5 - Exit")
        print("-------------------------")
        choice = str(input("      Choose: "))
        if choice == "5":
            print("You can't come back\nif you leave.")
            j = str(input("1 - Leave\n2 - Stay"))
            if j == "1":
                print("Ok.")
                break
            elif j == "2":
                print("Ok.")
            else:
                print("That isn't an option.")
        elif choice == "4":
            print("Nothing yet.")
        elif choice == "1":
            while True:
                print("Choose an enemy:")
                print("1 - Goblin LVL1\n3 health, 2 attack.")
                print("2 - Shield Goblin LVL1\n5 health, 1 attack.")
                print("3 - Goblin Bowman LVL2\n5 health, 3 attack.")
                print("4 - Sword Goblin LVL2\n8 health, 2 attack.")
                print("5 - Goblin Hogrider LVL3\n7 health, 4 attack.")
                print("6 - Armored Goblin LVL3\n10 health, 3 attack.")
                print("7 - Goblin Crossbowman LVL4\n9 health, 5 attack.")
                print("8 - Goblin Chariot LVL4\n12 health, 4 attack.")
                print("9 - Goblin Warlord LVL5\n40 health, 5 attack.")
                print("10 - Dragon LVL10\n75 health, 8 attack.")
                print("11 - Back")
                choose = str(input("Choose: "))
                if choose == "1":
                    enemy1.newEnemy(1,"1")
                    battle(player1,enemy1)
                elif choose == "2":
                    enemy1.newEnemy(2,"1")
                    battle(player1,enemy1)
                elif choose == "3":
                    enemy1.newEnemy(1,"2")
                    battle(player1,enemy1)
                elif choose == "4":
                    enemy1.newEnemy(2,"2")
                    battle(player1,enemy1)
                elif choose == "5":
                    enemy1.newEnemy(1,"3")
                    battle(player1,enemy1)
                elif choose == "6":
                    enemy1.newEnemy(2,"3")
                    battle(player1,enemy1)
                elif choose == "7":
                    enemy1.newEnemy(1,"4")
                    battle(player1,enemy1)
                elif choose == "8":
                    enemy1.newEnemy(2,"4")
                    battle(player1,enemy1)
                elif choose == "9":
                    enemy1.newEnemy(1,"boss")
                    battle(player1,enemy1)
                elif choose == "10":
                    enemy1.newEnemy(2,"boss")
                    battle(player1,enemy1)
                elif choose == "11":
                    break
                else:
                    print("That isn't an option!")
        elif choice == "2":
            print("Player health: " + str(player1.health) + "/" + str(player1.maxHealth))
            print("Player attack: " + str(player1.attack))
            print("Player magic: " + str(player1.magic))
            print("Player skill points: " + str(player1.skillPoints) + "/" + str(player1.maxSkillPoints))
            print("Player level: " + str(player1.level))
            print("Player exp: " + str(player1.exp))
            print("Player gold: " + str(player1.gold))
            print("Player total gold: " + str(player1.totalGold))
            print("Enemies defeated: " + str(player1.enemiesDefeated))
        elif choice == "3":
            while True:
                print("Choose an option:")
                options = """1 - Restore Health
2 - Restore SkillPoints
3 - Level Up
4 - Back"""
                print(options)
                choice = str(input("Choose: "))
                if choice == "4":
                    break
                elif choice == "1":
                    player1.health = player1.maxHealth
                elif choice == "2":
                    player1.skillPoints = player1.maxSkillPoints
                elif choice == "3":
                    player1.exp += 10 * player1.level
                    levelUp(player1)
                else:
                    print("That isn't an option!")
        else:
            print("That isn't an option!")
    play.isDebug = False
    #Progress 3: You exited the debug area!
    play.progress = 3
    
    
    
    
    
def buy(player1,item):
    if item == "potion2":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = potion("medium",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "potion3":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = potion("large",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "armor1":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = armor("weak",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "armor2":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = armor("strong",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "armor3":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = armor("magic",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "weapon1":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = weapon("weak",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "weapon2":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = weapon("strong",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "weapon3":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = weapon("magic",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    elif item == "potion1":
        if player1.gold >= item.itemGold:
            for item in player1.inventory:
                if item == None:
                    item = potion("small",player1)
                    break
            player1.gold = player1.gold - item.itemGold
        else:
            print("You don't have enough gold!")
    else:
        print("This is an error message.")
        
        
def shop(player1):
    print("-~--~--~--~-")
    if player1.currentLocation == startTown:
        print("You're inside of the town's\nonly store for adventurers.")
    else:
        print("The pair of Goblins show you their wares.")
    print("1 - Small potion. 5 gold.")
    print("Heals 3 health.")
    if player1.level == 2:
        print("2 - Potion. 10 gold.")
        print("Heals 5 health.")
        print("3 - Leather armor.")
        print("15 gold. +3 health.")
        if playerclass == "ranger":
            print("4 - Weak Bow.")
            print("10 gold. +1 attack.")
        elif playerclass == "warrior":
            print("4 - Rusty Sword.")
            print("10 gold. +1 attack.")
        elif playerclass == "shielder":
            print("4 - Wooden Shield.")
            print("10 gold. +1 attack.")
    elif player1.level == 3:
        print("2 - Potion. 10 gold.")
        print("Heals 5 health.")
        print("3 - Leather armor.")
        print("15 gold. +3 health.")
        print("4 - Steel armor.")
        print("25 gold. +6 health.")
        if playerclass == "ranger":
            print("5 - Weak Bow.")
            print("10 gold. +1 attack.")
            print("6 - Bow.")
            print("20 gold. +2 attack.")
        elif playerclass == "warrior":
            print("5 - Rusty Sword.")
            print("10 gold. +1 attack.")
            print("6 - Sword.")
            print("20 gold. +2 attack.")
        elif playerclass == "shielder":
            print("5 - Wooden Shield.")
            print("10 gold. +1 attack.")
            print("6 - Iron Shield.")
            print("20 gold. +2 attack.")
    elif player1.level >= 4:
        print("2 - Potion. 10 gold.")
        print("Heals 5 health.")
        print("3 - Large Potion. 15 gold.")
        print("Heals 10 health.")
        print("4 - Leather armor.")
        print("15 gold. +3 health.")
        print("5 - Steel armor.")
        print("25 gold. +6 health.")
        print("6 - Mystic armor. 40 gold.")
        print("10 health, +3 magic.")
        if playerclass == "ranger":
            print("7 - Weak Bow.")
            print("10 gold. +1 attack.")
            print("8 - Bow.")
            print("20 gold. +2 attack.")
            print("9 - Mystic Bow. 30 Gold.")
            print("+2 attack, +1 magic.")
        elif playerclass == "warrior":
            print("7 - Rusty Sword.")
            print("10 gold. +1 attack.")
            print("8 - Sword.")
            print("20 gold. +2 attack.")
            print("9 - Mystic Sword. 30 Gold.")
            print("+2 attack, +1 magic.")
        elif playerclass == "shielder":
            print("7 - Wooden Shield.")
            print("10 gold. +1 attack.")
            print("8 - Iron Shield.")
            print("20 gold. +1 attack.")
            print("9 - Mystic Shield. 30 Gold.")
            print("+2 attack, +1 magic.")
        if player1.level == 1:
            print("2 - Exit")
        elif player1.level == 2:
            print("5 - Exit")
        elif player1.level == 3:
            print("7 - Exit")
        else:
            print("10 - Exit")
    print("-~--~--~--~-")
    
    while True:
        choice = str(input("Choose: "))
        if choice == "1":
            #Small potion, 5 gold
            buy("potion1",player1)
        elif choice == "2":
            if player1.level >= 2:
                #Potion, 10 gold
                buy("potion2",player1)
            else:
                break
        elif choice == "3":
            if player1.level >= 4:
                #Large potion, 15 gold
                buy("potion3",player1)
            elif player1.level == 3 or 2:
                #Armor tier 1, 15 gold
                buy("armor1",player1)
            else:
                print("That isn't an option!")
        elif choice == "4":
            if player1.level >= 4:
                #Armor tier 1, 15 gold
                buy("armor1",player1)
            elif player1.level == 3:
                #Armor tier 2, 25 gold
                buy("armor2",player1)
            elif player1.level == 2:
                #Weapon tier 1, 10 gold
                buy("weapon1",player1)
            else:
                print("That isn't an option!")
        elif choice == "5":
            if player1.level >= 4:
                #Armor tier 2, 25 gold
                buy("armor2",player1)
            elif player1.level == 3:
                #Weapon tier 1, 10 gold
                buy("weapon1",player1)
            elif player1.level == 2:
                break
            else:
                print("That isn't an option!")
        elif choice == "6":
            if player1.level >= 4:
                #Armor tier 3, 40 gold
                buy("armor3",player1)
            elif player1.level == 3:
                #Weapon tier 2, 20 gold
                buy("weapon2",player1)
            else:
                print("That isn't an option!")
        elif choice == "7":
            if player1.level >= 4:
                #Weapon tier 1, 10 gold
                buy("weapon1",player1)
            elif player1.level == 3:
                break
            else:
                print("That isn't an option!")
        elif choice == "8":
            if player1.level >= 4:
                #Weapon tier 2, 20 gold
                buy("weapon2",player1)
            else:
                print("That isn't an option!")
        elif choice == "9":
            if player1.level >= 4:
                #Weapon tier 3, 30 gold
                buy("weapon3",player1)
            else:
                print("That isn't an option!")
        elif choice == "10":
            if player1.level >= 4:
                break
            else:
                print("That isn't an option!")
        else:
            print("That isn't an option!")
            
            
            
            
            
def mapStartTown(maxTry):
    direction1 = "direction"
    direction2 = "direction"
    tries = random.randint(1,maxTry*7)
    while tries > 4:
        tries = tries - 4
    if tries == 1:
        direction1 = "north"
    elif tries == 2:
        direction1 = "east"
    elif tries == 3:
        direction1 = "south"
    else:
        direction1 = "west"
    tries = random.randint(1, maxTry*13)
    while tries > 3:
        tries = tries - 3
    if tries == 1:
        if direction1 == "north":
            direction2 = "east"
        else:
            direction2 = "north"
    if tries == 2:
        if direction1 == "north" or "east":
            direction2 = "south"
        else:
            direction2 = "east"
    else:
        if direction1 == "west":
            direction2 = "south"
        else:
            direction2 = "west"
    return direction1,direction2





#FOREST MAZE CODE
class forestTile:
    def __init__(self,up,left,down,right):
        self.up = up
        self.left = left
        self.down = down
        self.right = right
xy00 = forestTile(False,False,True,True)
xy10 = forestTile(False,True,False,True)
xy20 = forestTile(False,True,False,True)
xy30 = forestTile(False,True,True,False)
xy40 = forestTile(True,False,True,False)#up is exit of the forest
xy01 = forestTile(True,False,True,False)
xy11 = forestTile(False,False,True,True)
xy21 = forestTile(False,True,True,False)
xy31 = forestTile(True,False,False,True)
xy41 = forestTile(True,True,False,False)
xy02 = forestTile(True,False,True,True)
xy12 = forestTile(False,True,False,False)#enterance to village
xy22 = forestTile(True,False,False,True)
xy32 = forestTile(False,True,False,True)
xy42 = forestTile(False,True,True,False)
xy03 = forestTile(True,False,True,False)
xy13 = forestTile(False,False,False,False)
xy23 = forestTile(False,False,False,False)#the village
xy33 = forestTile(False,False,False,False)#this is the village healer
xy43 = forestTile(True,False,True,False)
xy04 = forestTile(True,False,False,True)
xy14 = forestTile(True,True,False,False)#village entrance
xy24 = forestTile(False,False,False,False)#this is the village shop
xy34 = forestTile(False,False,True,True)#down is entrance to the forest
xy44 = forestTile(True,True,False,False)
forestRow0 = (xy00,xy10,xy20,xy30,xy40)
forestRow1 = (xy01,xy11,xy21,xy31,xy41)
forestRow2 = (xy02,xy12,xy22,xy32,xy42)
forestRow3 = (xy03,xy13,xy23,xy33,xy43)
forestRow4 = (xy04,xy14,xy24,xy34,xy44)
forestMap = (forestRow0,forestRow1,forestRow2,forestRow3,forestRow4)
play.pos = forestMap[4][3]
play.forestGrid = forestMap
def deepForestMaze(forestMaze,player1):
    while True:
        forestMaze.isHere(None,None,None,None)
        if player1.pos == player1.forestGrid[3][3]:#forest healer
            print("1 - Heal")
            print("2 - Talk")
            print("3 - Leave")
        elif player1.pos == player1.forestGrid[4][2]:#forest shop
            print("1 - Shop")
            print("2 - Talk")
            print("3 - Leave")
        elif player1.pos == player1.forestGrid[3][2]:#forest village
            print("1 - Goblin shop")
            print("2 - Healer's hut")
            print("3 - Talk to Goblins")
            print("4 - Village gate")
            print("5 - Leave")
        elif player1.pos == player1.forestGrid[3][1]:#forest village gate
            print("1 - Look at map")
            print("2 - Talk to Goblins")
            print("3 - Leave")
        elif player1.pos == player1.forestGrid[4][1]:#forest village entrance
            print("1 - Enter village")
            print("2 - Explore")
            print("3 - Sleep")
        else:#most forest maze tiles
            print("1 - Explore")
            print("2 - Sleep")
        print("-~--~--~--~-")
        choice = str(input("Choose: "))
        if player1.pos == player1.forestGrid[3][3]:#forest healer
            if choice == "1":
                print("HEAL")
                player1.health = player1.maxHealth
                player1.skillPoints = player1.maxSkillPoints
            elif choice == "2":
                print("STUFF")
            elif choise == "3":
                print("LEAVE")
                player1.pos = player1.forestGrid[3][2]
            else:
                print("That isn't an option!")
        elif player1.pos == player1.forestGrid[4][2]:#forest shop
            if choice == "1":
                print("SHOP")
                shop(player1)
            elif choice == "2":
                print("STUFF")
            elif choice == "3":
                print("LEAVE")
                player1.pos = player1.forestGrid[3][2]
            else:
                print("That isn't an option!")
        elif player1.pos == player1.forestGrid[3][2]:#forest village
            if choice == "1":
                print("ENTER SHOP")
                player1.pos = player1.forestGrid[4][2]
            elif choice == "2":
                print("ENTER HEAL")
                player1.pos = player1.forestGrid[3][3]
            elif choice == "3":
                print("STUFF")
            elif choice == "4":
                print("ENTER GATE")
                player1.pos = player1.forestGrid[3][1]
            elif choice == "5":
                print("LEAVE")
                player1.pos = player1.forestGrid[4][1]
            else:
                print("That isn't an option!")
        elif player1.pos == player1.forestGrid[3][1]:#forest village gate
            if choice == "1":
                print("From village to entrance:\nLeft,Up,Up,Right,Up,\nRight,Down,Right,Right,\nDown,Down,Left,Down.")
                print("From village to exit:\nLeft,Up,Up,Up,Up,\nRight,Right,Right,\nDown,Right,Up,Up.")
                print("From entrance to village:\nRight,Up,Up,Left,\nLeft,Up,Left,Down,\nLeft,Down,Down,Right.")
                print("From entrance to exit:\nRight,Up,Up,Left,Left,Up,\nLeft,Down,Left,Up,Up,Right,\nRight,Right,Down,Right,Up,Up.")
                print("From exit to village:\nDown,Left,Up,Right,Right,Right,\nDown,Down,Down,Down,Right.")
                print("From exit to entrance:\nDown,Left,up,Right,Right,Right,\nDown,Down,Right,Up,Right,Down,\nRight,Right,Down,Down,Left,Down.")
            elif choice == "2":
                print("STUFF")
            elif choice == "3":
                print("LEAVE")
                player1.pos = player1.forestGrid[3][2]
            else:
                print("That isn't an option!")
        elif player1.pos == player1.forestGrid[4][1]:#forest village entrance
            if choice == "1":
                print("ENTER")
                player1.pos == player1.forestGrid[3][2]
            elif choice == "2":
                print("MOVEMENT")
                player1.move
            elif choice == "3":
                print("SLEEP")
            else:
                print("That isn't an option!")
        else:#most forest maze tiles
            if choice == "1":
                print("MOVEMENT")
                player1.move
            elif choice == "2":
                print("You try to sleep...")
                player1.forestSleep(enemy1)
            else:
                print("That isn't an option!")
#FOREST MAZE CODE




def startStartTown(town):
    maxTry = random.randint(1,100)
    townDirections = mapStartTown(maxTry)
    if townDirections[0] == "north":
        townNorth = forest
        if townDirections[1] == "east":
            townEast = mountain
            townSouth = None
            townWest = None
        elif townDirections[1] == "south":
            townSouth = mountain
            townEast = None
            townWest = None
        else:
            townWest = mountain
            townEast = None
            townSouth = None
    elif townDirections[0] == "east":
        townEast = forest
        if townDirections[1] == "north":
            townNorth = mountain
            townSouth = None
            townWest = None
        elif townDirections[1] == "south":
            townSouth = mountain
            townNorth = None
            townWest = None
        else:
            townWest = mountain
            townNorth = None
            townSouth = None
    elif townDirections[0] == "south":
        townSouth = forest
        if townDirections[1] == "east":
            townEast = mountain
            townNorth = None
            townWest = None
        elif townDirections[1] == "north":
            townNorth = mountain
            townEast = None
            townWest = None
        else:
            townWest = mountain
            townEast = None
            townNorth = None
    else:
        townWest = forest
        if townDirections[1] == "north":
            townNorth = mountain
            townSouth = None
            townEast = None
        elif townDirections[1] == "east":
            townEast = mountain
            townSouth = None
            townNorth = None
        else:
            townSouth = mountain
            townEast = None
            townNorth = None
    town.north = townNorth
    town.east = townEast
    town.south = townSouth
    town.west = townWest
def startTownPlace(player1):
    if startTown.firsttime == True:
        startTown.isHere(startTown.north,startTown.east,startTown.south,startTown.west)
        startTown.firstTime = False
    print("-~--~--~--~-")
    print(" 1 - North")
    print(" 2 - East")
    print(" 3 - South")
    print(" 4 - West")
    print(" 5 - Shop")
    print(" 6 - Heal")
    print("-~--~--~--~-")
    choice = str(input(" Choose: "))
    if choice == "1":
        if startTown.north == None:
            print("That way's blocked!")
        else:
            if startTown.north == forest:
                player1.currentLocation = forest
                print("You walk the old road\ntowards Goblin Forest.")
            elif startTown.north == mountain:
                if player1.progress > 4:
                    player1.currentLocation = mountain
                    print("You walk the now-unused\nroad to Dragon Mountain.")
                else:
                    print("You aren't allowed through.\nThey don't trust you enough yet.")
    elif choice == "2":
        if startTown.east == None:
            print("That way's blocked!")
        else:
            if startTown.east == forest:
                player1.currentLocation = forest
                print("You walk the old road\ntowards Goblin Forest.")
            elif startTown.east == mountain:
                if player1.progress > 4:
                    player1.currentLocation = mountain
                    print("You walk the now-unused\nroad to Dragon Mountain.")
                else:
                    print("You aren't allowed through.\nThey don't trust you enough yet.")
    elif choice == "3":
        if startTown.south == None:
            print("That way's blocked!")
        else:
            if startTown.south == forest:
                player1.currentLocation = forest
                print("You walk the old road\ntowards Goblin Forest.")
            elif startTown.south == mountain:
                if player1.progress > 4:
                    player1.currentLocation = mountain
                    print("You walk the now-unused\nroad to Dragon Mountain.")
                else:
                    print("You aren't allowed through.\nThey don't trust you enough yet.")
    elif choice == "4":
        if startTown.west == None:
            print("That way's blocked!")
        else:
            if startTown.west == forest:
                player1.currentLocation = forest
                print("You walk the old road\ntowards Goblin Forest.")
            elif startTown.west == mountain:
                if player1.progress > 4:
                    player1.currentLocation = mountain
                    print("You walk the now-unused\nroad to Dragon Mountain.")
                else:
                    print("You aren't allowed through.\nThey don't trust you enough yet.")
    elif choice == "5":
        nones = 0
        for item in play.inventory:
            if item == None:
                nones = nones + 1
        if nones != 0:
            shop(play)
        else:
            print("You're carrying too much!")
    elif choice == "6":
        print("You were healed by\nthe town's healers!")
        play.health = play.maxHealth
        play.skillPoints = play.maxSkillPoints
    else:
        print("That isn't a choice!")

startStartTown(startTown)
def forestPlace(player1):
    if forest.firsttime == True:
        print("Welcome to the entrance...\n...of Goblin Forest!")
        #Progress 4: Welcome to Goblin Forest!
        play.progress = 4
    if startTown.north == forest:
        forest.south = startTown
        forest.isHere(None,None,startTown,None)
    elif startTown.east == forest:
        forest.west = startTown
        forest.isHere(None,None,None,startTown)
    elif startTown.south == forest:
        forest.north = startTown
        forest.isHere(startTown,None,None,None)
    else:
        forest.east = startTown
        forest.isHere(None,startTown,None,None)
    print("-~--~--~--~-")
    print("1 - North")
    print("2 - East")
    print("3 - South")
    print("4 - West")
    print("5 - Sleep")
    print("-~--~--~--~-")
    choice = str(input("Choose: "))
    if choice == "1":
        if startTown.south == forest:
            player1.currentLocation = startTown
            print("You walk the road back\ntowards the town...")
        elif forest.south == startTown:
            print("You descend deeper inside\nthe forest of goblins...")
            while True:
                forestProgress = player1.move
                if forestProgress == 1:
                    break
                elif forestProgress == 2:
                    if player1.progress == 4:
                        if player1.level >= 5:
                            print("The Lord of Goblins watches you enter the room,\n and challenges you to a battle to the death!")
                            enemy1.newEnemy(1,"boss")
                            battle(player1,enemy1)
                            print("You look around after the duel,\nand find that the Goblins have fled.")
                            #Progress 5: You beat the Lord of Goblins!
                            player1.progress = 5
                            print("You decide to head back out.")
                            break
                        else:
                            print("The Lord of Goblins is here!\nThey look at you for a few moments\nbefore they signal guards to throw you out.")
                            break
                    else:
                        print("All that remains are\na few scavengers...")
            if startTown.north == forest:
                forest.isHere(None,None,startTown,None)
            elif startTown.east == forest:
                forest.isHere(None,None,None,startTown)
            elif startTown.south == forest:
                forest.isHere(startTown,None,None,None)
            else:
                forest.isHere(None,startTown,None,None)
        else:
            print("That way's blocked by too many trees!")
    elif choice == "2":
        if startTown.west == forest:
            player1.currentLocation = startTown
            print("You walk the road back\ntowards the town...")
        elif forest.west == startTown:
            print("You descend deeper inside\nthe forest of goblins...")
            while True:
                forestProgress = player1.move
                if forestProgress == 1:
                    break
                elif forestProgress == 2:
                    if player1.progress == 4:
                        if player1.level >= 5:
                            print("The Lord of Goblins watches you enter the room,\n and challenges you to a battle to the death!")
                            enemy1.newEnemy(1,"boss")
                            battle(player1,enemy1)
                            print("You look around after the duel,\nand find that the Goblins have fled.")
                            #Progress 5: You beat the Lord of Goblins!
                            player1.progress = 5
                            print("You decide to head back out.")
                            break
                        else:
                            print("The Lord of Goblins is here!\nThey look at you for a few moments\nbefore they signal guards to throw you out.")
                            break
                    else:
                        print("All that remains are\na few scavengers...")
            if startTown.north == forest:
                forest.isHere(None,None,startTown,None)
            elif startTown.east == forest:
                forest.isHere(None,None,None,startTown)
            elif startTown.south == forest:
                forest.isHere(startTown,None,None,None)
            else:
                forest.isHere(None,startTown,None,None)
        else:
            print("That way's blocked by too many trees!")
    elif choice == "3":
        if startTown.north == forest:
            player1.currentLocation = startTown
            print("You walk the road back\ntowards the town...")
        elif forest.north == startTown:
            print("You descend deeper inside\nthe forest of goblins...")
            while True:
                forestProgress = player1.move
                if forestProgress == 1:
                    break
                elif forestProgress == 2:
                    if player1.progress == 4:
                        if player1.level >= 5:
                            print("The Lord of Goblins watches you enter the room,\n and challenges you to a battle to the death!")
                            enemy1.newEnemy(1,"boss")
                            battle(player1,enemy1)
                            print("You look around after the duel,\nand find that the Goblins have fled.")
                            #Progress 5: You beat the Lord of Goblins!
                            player1.progress = 5
                            print("You decide to head back out.")
                            break
                        else:
                            print("The Lord of Goblins is here!\nThey look at you for a few moments\nbefore they signal guards to throw you out.")
                            break
                    else:
                        print("All that remains are\na few scavengers...")
            if startTown.north == forest:
                forest.isHere(None,None,startTown,None)
            elif startTown.east == forest:
                forest.isHere(None,None,None,startTown)
            elif startTown.south == forest:
                forest.isHere(startTown,None,None,None)
            else:
                forest.isHere(None,startTown,None,None)
        else:
            print("That way's blocked by too many trees!")
    elif choice == "4":
        if startTown.east == forest:
            player1.currentLocation = startTown
            print("You walk the road back\ntowards the town...")
        elif forest.west == startTown:
            print("You descend deeper inside\nthe forest of goblins...")
            while True:
                forestProgress = player1.move
                if forestProgress == 1:
                    break
                elif forestProgress == 2:
                    if player1.progress == 4:
                        if player1.level >= 5:
                            print("The Lord of Goblins watches you enter the room,\n and challenges you to a battle to the death!")
                            enemy1.newEnemy(1,"boss")
                            battle(player1,enemy1)
                            print("You look around after the duel,\nand find that the Goblins have fled.")
                            #Progress 5: You beat the Lord of Goblins!
                            player1.progress = 5
                            print("You decide to head back out.")
                            break
                        else:
                            print("The Lord of Goblins is here!\nThey look at you for a few moments\nbefore they signal guards to throw you out.")
                            break
                    else:
                        print("All that remains are\na few scavengers...")
            if startTown.north == forest:
                forest.isHere(None,None,startTown,None)
            elif startTown.east == forest:
                forest.isHere(None,None,None,startTown)
            elif startTown.south == forest:
                forest.isHere(startTown,None,None,None)
            else:
                forest.isHere(None,startTown,None,None)
        else:
            print("That way's blocked by too many trees!")
    elif choice == "5":
        print("You try to sleep...")
        sleepAttack = random.randint(1,7)
        if sleepAttack == 2 or 4:
            if player1.level == 1:
                enemyS = random.randint(1,2)
            elif player1.level == 2:
                enemyS = random.randint(1,4)
            elif player1.level >= 3:
                enemyS = random.randint(1,6)
            if enemyS == 1:
                enemy1.newEnemy(1,"1")
            elif enemyS == 2:
                enemy1.newEnemy(2,"1")
            elif enemyS == 3:
                enemy1.newEnemy(1,"2")
            elif enemyS == 4:
                enemy1.newEnemy(2,"2")
            elif enemyS == 5:
                enemy1.newEnemy(1,"3")
            elif enemyS == 6:
                enemy1.newEnemy(2,"3")
            player1.health = player1.health + (((player1.maxHealth - player1.health)/2)//1)
            player1.health = player1.maxHealth
            print("An enemy tried to attack\nwhile you were asleep!")
            battle(player1,enemy1)
        else:
            player1.health = player1.health + ((((player1.maxHealth - player1.health)/8)*7)//1)
            if player1.health > player1.maxHealth:
                player1.health = player1.maxHealth
        if startTown.north == forest:
            forest.isHere(None,None,startTown,None)
            forest.south == startTown
        elif startTown.east == forest:
            forest.isHere(None,None,None,startTown)
        elif startTown.south == forest:
            forest.isHere(startTown,None,None,None)
        else:
            forest.isHere(None,startTown,None,None)

debugAreaPlace(play)
play.currentLocation = startTown
while True:
    if play.currentLocation == startTown:
        startTownPlace(play)
    elif play.currentLocation == forest:
        forestPlace(play)
    elif play.currentLocation == mountain:
        mountainPlace(play)
