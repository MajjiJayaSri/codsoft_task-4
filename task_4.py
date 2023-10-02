import random
list = [1, 2, 3]
cscore = 0
uscore = 0
while True:
    print("\n1.Rock\n2.Paper\n3.Scissor\n4.Exit the game")
    ch = int(input("Enter your choice : "))
    num = random.choice(list)
    print("Computer choice :",num)
    if ch == 1 and num == 1:
        continue
    elif ch == 1 and num == 2:
        print("\nI won")
        cscore += 1
        print("My score is :",cscore)
        print("Your score is :",uscore)
    elif ch == 1 and num == 3:
        uscore += 1
        print("\nYou Won")
        print("My score is :",cscore)
        print("Your score is :",uscore)
    elif ch == 2 and num == 1:
        uscore += 1
        print("\nYou Won")
        print("My score is :",cscore)
        print("Your score is :",uscore)
    elif ch == 2 and num == 2:
        continue
    elif ch == 2 and num == 3:
        cscore += 1
        print("\nI Won")
        print("My score is :",cscore)
        print("Your score is :",uscore)
    elif ch == 3 and num == 1:
        cscore += 1
        print("\nI Won")
        print("My score is :",cscore)
        print("Your score is :",uscore)
    elif ch == 3 and num == 2:
        uscore += 1
        print("\nYou Won")
        print("My score is :",cscore)
        print("Your score is :",uscore)
    elif ch == 3 and num == 3:
        continue
    elif ch == 4:
        if(uscore >= cscore):
            print("Congratulations !!!\nFinally you won the game.")
        else:
            print("Computer won the game.")
        exit()
    else:
        print("Choose correct option")
        