import time
import os
import random
import platform
#covered under GPL v3

timer2 = 0.1 #note
timer3 = 0.01 #note

def word_core_human(sen):
    for letter in sen:
        print(letter, end='', flush=True)
        timerand = random.randint(1, 3)
        timer = float(str("0." + str(timerand)))
        time.sleep(timer)
    print("\n")

def word_core_menu(sen):
    for letter in sen:
        print(letter, end='', flush=True)
        time.sleep(timer2)
    print("\n")

def word_core_rapid(sen):
    for letter in sen:
        print(letter, end='', flush=True)
        time.sleep(timer3)
    print("\n")

def core(): #Just the preamble, maybe some licensing stuff
    word_core_human("This is a Python based version of Reflect, all the graphics were stripped away")
    word_core_human("All art and videos were made by 78_Alpha (myself)")
    word_core_human("Although, if you are running the text only option, you won't see any of it")
    word_core_human("")
    word_core_human("")
    word_core_rapid("!!! INSTRUCTIONS !!!")
    word_core_rapid("Text menus will appear that give you options, selectable options have the '>' and '<' characters"
                    "In these menus, you type out your options as a word. The secondary menu contains numbered lists"
                    "The lists look like 'X.)', for these types you only need to type the digit to the option you want")
    menu()

#Excessive/needless use of globals, but I like them
global u
u = platform.system()

global c #possible ending types
c = ['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'black']

global o
o = []

global d #character library
d = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]{}<>?"

global q
q = []

global p
p = []

def test(): #Test corrupt file
    for i in range(1, 10000):
        x = random.randint(0, len(d)-1)
        with open('corrupt.txt', 'a') as file_of:
            file_of.write("%s" % d[x])

def menu(): #The beginning of the story
    word_core_menu("1.) Begin story")
    word_core_menu("2.) Scene select\n")
    choice = int(input("Choice: "))
    print("\n")
    if choice == int(1):
        init()
    elif choice == int(2):
        scene_select()
    else:
        print("Runtime Error")

def init():
    word_core_rapid("[---|  [----  [----  |      [----  [----  --^--")
    word_core_rapid("|   /  |      |      |      |      |        |  ")
    word_core_rapid("|--/   [----  |----  |      [----  |        |  ")
    word_core_rapid("|  |   |      |      |      |      |        |  ")
    word_core_rapid("|   |  [----  |      [____  [----  [----    |  ")
    print("\n")
    word_core_human("You are a reflection...\n"
          "       A dull life needs change...\n"
          "                Maybe with your other...\n"
          "       Maybe not at all...\n"
          "Live...\n")
    time.sleep(1)
    menu1()

def menu1(): #first part of the story
    word_core_human("You stare at your other self")
    word_core_menu("You could Leave...")
    word_core_menu("Try to Talk to them...")
    word_core_menu("Or simply Take what you want...")
    word_core_menu(">>Leave<<  >>Talk<<  >>Take<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Leave" or ans == "leave": #Blue
        word_core_human("You left...")
        Blue()
        menu_blue1()
    elif ans == "Talk" or ans == "talk": #Yellow
        word_core_human("You spoke...")
        Yellow()
        menu_yellow1()
    elif ans == "Take" or ans == "take": #Red
        word_core_human("You took...")
        Red()
        menu_red1()
    else:
        print("Runtime Error")
        menu1()

def menu_blue1():
    word_core_human("You left them alone...")
    word_core_menu("You could Stare at them...")
    word_core_menu("Maybe Knock...")
    word_core_menu("Or just Leave them alone...")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Stare" or ans == "stare":
        Blue()
        menu_blue4() #Blue
    elif ans == "Knock" or ans == "knock":
        Yellow()
        menu_yellow3() #Yellow
    elif ans == "Leave" or ans == "leave":
        Blue()
        blue_end() #Blue
    else:
        print("Runtime Error")
        menu_blue1()

def menu_blue2(): #Probably a useless menu, unused
    word_core_human("You stare at them...")
    menu_blue1() #Blue

def menu_blue3():
    word_core_human("You try to explain your situation...")
    word_core_menu("But they won't listen")
    word_core_menu("You can give up...")
    word_core_menu("Or take what you want...")
    word_core_menu(">>Give Up<<  >>Take<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Give Up" or ans == "give Up" or ans == "Give up" or ans == "give up":
        word_core_human("You gave up...")
        Blue()
        blue_end()
    elif ans == "Take" or ans == "take":
        Red()
        menu_red1()
    else:
        print("Runtime Error")
        menu_blue3()

def menu_blue4():
    word_core_human("You stare at them...")
    word_core_human("They stare back as though nothing is different")
    word_core_menu("You can Leave them alone...")
    word_core_menu("You could always Knock...")
    word_core_menu("Or just Take what you want...")
    word_core_menu(">>Leave<<  >>Knock<<  >>Take<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Leave" or ans == "leave":
        word_core_human("You left them alone...")
        word_core_human("                       ...Forever...")
        Blue()
        blue_end()
    elif ans == "Knock" or ans == "knock":
        Yellow()
        menu_yellow3()
    elif ans == "Take" or ans == "take":
        Red()
        menu_red1()
    else:
        print("Runtime Error")
        menu_blue4()

def menu_blue5():
    word_core_human("You ran...")
    word_core_human("           ...Your troubles are behind you...")
    word_core_rapid("                                              ...For now...")
    Blue()
    blue_end()

def blue_end():
    word_core_rapid("Blue Ending...")
    word_core_human("You shatter into pieces...")
    end()

def menu_yellow1():
    word_core_human("You talked to them...")
    word_core_menu("What do you say?")
    word_core_menu(">>Explain<<  >>Ask<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Explain" or ans == "explain":
        Blue()
        menu_blue3()
    elif ans == "Ask" or ans == "ask":
        Yellow()
        menu_yellow2()
    else:
        print("Runtime Error")
        menu_yellow1()

def menu_yellow2():
    time.sleep(1)
    if len(q) == int(0):
        word_core_human("You ask them for a day...")
        word_core_human("They accept... Do you...")
    word_core_menu("Talk to people...")
    word_core_menu("Interact ith people...")
    word_core_menu("Go home...")
    word_core_menu("Or have some Fun...")
    word_core_menu(">>Talk<<  >>Interact<<  >>Fun<<  >>Home<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Talk" or ans == "talk":
        Yellow()
        if len(q) == int(0):
            q.append("1")
            word_core_human("You talk to some people...")
            word_core_human("Some are nice, some are not...")
            menu_yellow2x()
            menu_yellow2()
        elif len(q) == int(1):
            q.append("1")
            word_core_human("You talk with your other's friends and family...")
            word_core_human("They all laugh and smile with you...")
            menu_yellow2x()
            menu_yellow2()
        elif len(q) == int(2):
            q.append("1")
            word_core_human("You make a few friends...")
            word_core_human("They take a liking to you very quickly...")
            menu_green1()
        else:
            print("Runtime Error")
    elif ans == "Interact" or ans == "interact":
        Yellow()
        if len(q) == int(0):
            q.append("1")
            word_core_human("You visit a skate park...")
            word_core_human("The tricks all look impossible until they are executed perfectly...")
            menu_yellow2x()
            menu_yellow2()
        elif len(q) == int(1):
            q.append("1")
            word_core_human("You watch some people...")
            word_core_human("They all move and act strangely to you... Backwards...")
            menu_yellow2x()
            menu_yellow2()
        elif len(q) == int(2):
            q.append("1")
            word_core_human("You go to the bay...")
            word_core_human("There seems to be families having a picnic...")
            menu_green1()
        else:
            print("Runtime Error")
    elif ans == "Fun" or ans == "fun":
        Yellow()
        if len(q) == int(0):
            q.append("1")
            word_core_human("You visit the town carnival...")
            word_core_human("Everyhting is loud and the people look like none you have seen before, but everyone is happy")
            menu_yellow2x()
            menu_yellow2()
        elif len(q) == int(1):
            q.append("1")
            word_core_human("You swim in a pool for the first time...")
            word_core_human("No longer are you just a ripple in the water...")
            menu_yellow2x()
            menu_yellow2()
        elif len(q) == int(2):
            q.append("1")
            word_core_human("You sneak into a movie theater...")
            word_core_human("There are feflections with no other on the silver screen, larger than everyone...")
            menu_green1()
    elif ans == "Home" or ans == "home":
        Yellow()
        if len(q) == int(0):
            q.append("1")
            menu_yellow5()
        elif len(q) == int(1) or len(q) == int(2):
            q.append("1")
            menu_yellow5()
        elif len(q) == int(3):
            q.append("1")
            menu_green1()
    else:
        print("Runtime Error")
        if "1" in q:
            q.remove("1")
            menu_yellow2()
        else:
            menu_yellow2()

def menu_yellow2x():
    word_core_human("What do you do on your day...")

def menu_yellow3():
    word_core_human("You knocked on the glass...")
    word_core_human("They jump in surprise...")
    word_core_menu("You can try to Talk to them...")
    word_core_menu("Or you can just Leave...")
    word_core_menu(">>Talk<<  >>Leave<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Talk" or ans == "talk":
        Yellow()
        menu_yellow4()
    elif ans == "Leave" or ans == "leave":
        word_core_human("You left them alone...")
        word_core_human("                       ...Forever...")
        Blue()
        blue_end()
    else:
        print("Runtime Error")
        menu_yellow3()

def menu_yellow4():
    word_core_human("You talk to them after pulling them into the mirror...")
    word_core_menu("Do you Explain your situation...")
    word_core_menu("Or do you just Ask them...")
    word_core_menu(">>Explain<<  >>Ask<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Explain" or ans == "explain":
        Blue()
        menu_blue3()
    elif ans == "Ask" or ans == "ask":
        Yellow()
        menu_yellow2()
    else:
        print("Runtime Error")
        menu_yellow4()

def menu_yellow5():
    word_core_human("Both of you return to your lives...")
    word_core_menu("Will you Say one last thing...")
    word_core_menu("Stay in teh real world...")
    word_core_menu("Or let things Go as they will...")
    word_core_menu(">>Say<<  >>Stay<<  >>Go<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Say" or ans == "say":
        Pink()
        menu_pink1()
    elif ans == "Stay" or ans == "stay":
        Orange()
        menu_orange1()
    elif ans == "Go" or ans == "go":
        Yellow()
        yellow_end()
    else:
        print("Runtime Error")
        menu_yellow5()

def yellow_end():
    word_core_rapid("Yellow Ending")
    word_core_human("Both of you return to your lives...")
    word_core_rapid("                                   ...Nothing more...")
    word_core_rapid("                                                     ...Nothing less...")
    end()

def menu_red1():
    word_core_human("How will you do it?")
    word_core_menu(">>Lunge<<  >>Pull<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Lunge" or ans == "lunge":
        Red()
        menu_red2()
    elif ans == "Pull" or ans == "pull":
        Red()
        menu_red2x()
    else:
        print("Runtime Error")
        menu_red1()

def menu_red2():
    word_core_human("They stare at you with a look of terror...")
    word_core_menu("You could try to Talk to them...")
    word_core_menu("But maybe Killing them is easier...")
    word_core_menu("Or Run...")
    word_core_menu(">>Talk<<  >>Kill<<  >>Run<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Talk" or ans == "talk":
        Orange()
        menu_orange2()
    elif ans == "Kill" or ans == "kill":
        Red()
        menu_red3()
    elif ans == "Run" or ans == "run":
        Purple()
        menu_purple1()
    else:
        print("Runtime Error")
        menu_red2()

def menu_red2x():
    word_core_human("They stare at you, frightened...")
    word_core_menu("You could try to Talk to them...")
    word_core_menu("But maybe Killing them is easier...")
    word_core_menu("Or Run...")
    word_core_menu(">>Talk<<  >>Kill<<  >>Run<<")
    ans = str(input("Action: "))
    print("\n")
    if ans == "Talk" or ans == "talk":
        Yellow()
        menu_yellow4()
    elif ans == "Kill" or ans == "kill":
        Red()
        menu_red3()
    elif ans == "Run" or ans == "run":
        Blue()
        menu_blue5()
    else:
        print("Runtime Error")
        menu_red2x()

def menu_red3():
    word_core_human("You decide to kill them...")
    word_core_human("The walls are painted red with blood, the air filled with nothing but screams of anguish...")
    time.sleep(1)
    menu_red4()


def menu_red4():
    word_core_human("You took a life...")
    word_core_human("Now you have your own")
    word_core_menu("What will you do now...\n")
    word_core_menu(">>End<<  >>4s5Um3<<")
    ans = str(input("Your Choice: "))
    print("\n")
    if ans == "End" or ans == "end":
        Red()
        red_end()
    elif ans == "4s5Um3" or ans == "Assume" or ans == "assume":
        Black()
        menu_black1()

def red_end():
    print(o)
    with open('Red.txt', 'a') as the_file:
        the_file.write("You are a killer... ")
    word_core_rapid("Re-Live?")
    word_core_menu(">>Yes<<")
    word_core_rapid(">>No<<")
    ans = str(input("Choice: "))
    print("\n")
    if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
        word_core_human("You can't forget what you did...")
        time.sleep(5)
        menu()
    elif ans == "No" or ans == "no":
        exit()
    else:
        print("Runtime Error")
        red_end()

def menu_black1():
    word_core_human("You decide to assume their life...")
    word_core_human("You become them...")
    Black()
    word_core_human("Runtime Error")
    corrupt()
    word_core_human("Resuming Process")
    word_core_human("W1lL U g0 0N?")
    word_core_rapid(">>Yes<< >>No<<")
    ans = str(input("Do it: "))
    print("\n")
    if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
        Black()
        menu_black2()
    else:
        Black()
        black_end()

def menu_black2():
    word_core_human("You massacre all your Other's family and friends...")
    word_core_menu("Child screams...")
    word_core_menu("                 ...Mother cries...")
    word_core_menu("                                    ...Brother yells...")
    word_core_menu("                                                        Everyone dies")
    Black()
    black_end()

def black_end():
    corrupt_loop()
    print(o)
    word_core_human("Re-Live?")
    word_core_rapid("You're")
    corrupt()
    word_core_rapid("       A")
    corrupt()
    word_core_rapid("         Monster")
    corrupt()
    word_core_rapid("                 You")
    corrupt()
    word_core_rapid("           Won't")
    corrupt()
    word_core_rapid("    forget")
    corrupt()
    word_core_menu(">>Yes<<")
    word_core_menu(">>No<<")
    ans = str(input("Choice: "))
    print("\n")
    if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
        menu()
    elif ans == "No" or ans == "no":
        exit()
    else:
        print("Runtime Error")
        end()

def menu_green1():
    word_core_human("You were out too long...")
    Green()
    green_end()

def green_end():
    word_core_rapid("Green Ending")
    word_core_human("What seemed like hours were days, your other died in the mirror...")
    word_core_human("All you can do is stare at them, knowing you will follow soon enough...")
    end()

def menu_pink1():
    word_core_human("You talk with them one more time...")
    word_core_human("You become friends...")
    pink_end()

def pink_end():
    word_core_human("Pink Ending")
    word_core_human("They now let you have all the days you could ever want...")
    end()

def menu_orange1():
    word_core_human("You like this life...")
    word_core_human("So why would you leave it...")
    Orange()
    orange_end()

def menu_orange2():
    word_core_human("You talk to them after attacking them...")
    word_core_human("They push back...")
    word_core_human("It was their undoing...")
    time.sleep(5)
    orange_end()

def orange_end():
    word_core_rapid("Orange Ending")
    word_core_human("You leave them to dies in the mirror, living life as you want...")
    end()

def menu_purple1():
    word_core_human("You attempted to run...")
    word_core_human("But they stop you...")
    Purple()
    purple_end()

def purple_end():
    word_core_rapid("Purple Ending")
    word_core_human("Your body shatters like frail glass...")
    end()

def end():
    print(o)
    word_core_menu("Re-Live?")
    word_core_menu(">>Yes<<")
    word_core_menu(">>No<<")
    ans = str(input("Choice: "))
    print("\n")
    if ans == "yes" or ans == "Yes" or ans == "y" or ans == "Y":
        menu()
    elif ans == "No" or ans == "no":
        exit()
    else:
        print("Runtime Error")
        end()

def Red(): #red path
    o.append("Red")

def Blue(): #blue path
    o.append("Blue")

def Yellow(): #yellow path
    o.append("Yellow")

#etc path

def Black():
    o.append("Black")

def Pink():
    o.append("Pink")

def Orange():
    o.append("Orange")

def Green():
    o.append("Green")

def Purple():
    o.append("Purple")

def corrupt(): #creates corrupt file, may balloon to a large size
    for i in range(1, 100):
        with open("Monster.txt", 'a') as file:
            file.write("YOU MONSTER ")
        z = random.randint(1, len(d)-1)
        print(d[z], end='', flush=True)
    print("YOU MONSTER")

def corrupt_loop(): #loops corrupt
    for i in range(1, 100):
        corrupt()

def scene_select():
    word_core_human("What category would you like to look in?")
    word_core_menu(">>Red<< >>Orange<< >>Yellow<< >>Green<< >>Blue<< >>Purple<< >>Pink<< >>Black<< >>Return<<")
    ans = str(input())
    if ans == "Red" or ans == "red":
        word_core_human("Which Scene?")
        word_core_menu("1: 'How will you do it...")
        word_core_menu("2: 'They stare at you with a look of terror...'")
        word_core_menu("3: 'They stare at you, frightened...'")
        word_core_menu("4: 'You decide to kill them...'")
        word_core_menu("5: 'You took a life...'")
        word_core_menu("6: 'Red Ending'")
        word_core_menu(">>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_red1()
        elif ans == "2":
            menu_red2()
        elif ans == "3":
            menu_red2x()
        elif ans == "4":
            menu_red3()
        elif ans == "5":
            menu_red4()
        elif ans == "6":
            red_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()
    elif ans == "Orange" or ans == "orange":
        word_core_human("Which Scene?")
        word_core_menu("1: ''You like this life...")
        word_core_menu("2: 'You talk to them after attacking them...'")
        word_core_menu("3: 'Orange Ending'")
        word_core_menu(">>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_orange1()
        elif ans == "2":
            menu_orange2()
        elif ans == "3":
            orange_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()
    elif ans == "Yellow" or ans == "yellow":
        word_core_human("Which Scene?")
        word_core_menu("1: 'You talked to them...'")
        word_core_menu("2: 'You ask them for a day...'")
        word_core_menu("3: 'You knocked on the glass...'")
        word_core_menu("4: 'You talk to them after pulling them into the mirror...'")
        word_core_menu("5: 'Both of you return to your lives...'")
        word_core_menu("6: 'Yellow Ending'")
        word_core_menu(">>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_yellow1()
        elif ans == "2":
            menu_yellow2()
        elif ans == "3":
            menu_yellow3()
        elif ans == "4":
            menu_yellow4()
        elif ans == "5":
            menu_yellow5()
        elif ans == "6":
            yellow_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()
    elif ans == "Green" or ans == "green":
        word_core_human("Which Scene?")
        word_core_menu("1: 'You were out too long...")
        word_core_menu("2: 'Green Ending")
        word_core_menu(">>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_green1()
        elif ans == "2":
            green_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()
    elif ans == "Blue" or ans == "blue":
        word_core_human("Which Scene?")
        word_core_menu("1: 'You left them alone...'")
        word_core_menu("2: 'You try to explain your situation...'")
        word_core_menu("3: 'You stare at them...'")
        word_core_menu("4: 'You ran...'")
        word_core_menu("5: 'Blue Ending'")
        word_core_menu(">>>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_blue1()
        elif ans == "2":
            menu_blue3()
        elif ans == "3":
            menu_blue4()
        elif ans == "4":
            menu_blue5()
        elif ans == "5":
            blue_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()
    elif ans == "Purple" or ans == "purple":
        word_core_human("Which Scene?")
        word_core_menu("1: 'You attempted to run...'")
        word_core_menu("2: 'Purple Ending'")
        word_core_menu(">>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_purple1()
        elif ans == "2":
            purple_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()
    elif ans == "Pink" or ans == "pink":
        word_core_human("Which Scene?")
        word_core_menu("1: 'You talk with them one more time...'")
        word_core_menu("2: 'Pink Ending'")
        word_core_menu(">>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_pink1()
        elif ans == "2":
            pink_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()
    elif ans == "Black" or ans == "black":
        word_core_human("Which Scene?")
        word_core_menu("1: ''You decide to assume their life...")
        word_core_menu("2: 'You massacre...'")
        word_core_menu("3: 'Black Ending'")
        word_core_menu(">>Go back<<")
        ans = str(input("Selection: "))
        print("\n")
        if ans == "1":
            menu_black1()
        elif ans == "2":
            menu_black2()
        elif ans == "3":
            black_end()
        elif ans == "Go back" or ans == "go back" or ans == "Go Back" or ans == "go Back":
            scene_select()
        else:
            print("Error, Falling Back")
            scene_select()

core()
