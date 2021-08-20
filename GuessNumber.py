from random import randint
def menu():
    print("*******************\n")
    print("******1.Play*******\n")
    print("******0.Exit*******\n")
    print("*******************\n")

def game():
    x = randint(0, 100)
    while True:
        digit=int(input("Please input a number between 0 and 100:"))
        if digit == x:
            print("Bingo")
            break
        elif digit >x:
            print("Too large, please try again.")
        else:
            print("Too small, please try again.")

def main():
    while True:
        menu()
        go=input("Choose your number:")
        if go=="1":
            game()
        elif go=="0":
            print("Good Bye.")
            break
        else:
            print("Please enter the correct number as prompted.")

main()
