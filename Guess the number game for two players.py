import random
c = random.randint(1,99)
a_player = 0
while True:
    a = int(input("Guess a number form 1 to 99:\n"))
    d=c
    print(d)
    if a==d:
        a_player = a_player + 1
        print(f"Your guess is {a}\n")
        print(f"You won the game in {a_player} chance")
        break
    else:
        a_player=a_player+1
        print(f"Your guess is {a}\n")
        print(f"Your guess is {a} and your tried {a_player} Time")
        if a<c:
            print(f"Your guess is low guess some higher number")
        elif a>c:
            print(f"Your guess is high guess some smaller number")

print("\t\tb_plyer this is your chance")
b_player=0
z = random.randint(1,99)
while True:
    b = int(input("Guess a number form 1 to 99\n"))
    e=z
    print(e)
    if b==e:
        b_player = b_player + 1
        print(f"Your guess is {b}\n")
        print(f"You won the game in {b_player} chance")
        break
    else:
        b_player=b_player+1
        print(f"Your guess is {b}\n")
        print(f"Your guess is {b} and your tried {b_player} Time\n")
        if b<e:
            print(f"Your guess is low guess some higher number")
        elif b>e:
            print(f"Your guess is high guess some smaller number")

if a_player<b_player:
    print("a_player won the game!")
elif a_player==b_player:
    print("Match tied both have same points")
else:
    print("b_player won the game!")