import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


randNo = random.randint(1,3)
print("Comp turn: Snake(s) or Water(w) or Gun(g)")
comp = ""
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp == 'g'



player = input("Your turn: Snake(s) or Water(w) or Gun(g)")
val = gameWin(comp, player)


print(f"Comp choose {comp}")
print(f"You choose {player}")

if val == None:
    print("It is a Tie!")
elif val:
    print("Hurray! You Win!")
elif val:
    print("Boo! You Loose!")


