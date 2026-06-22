import pyfiglet
from random import randint
text=pyfiglet.figlet_format("ROCK , PAPER , SCISSORS")
print(text)
computer_choice=user_choice=-1
def get_choice():
    global computer_choice,user_choice
    print("Please choose one of the following options: \n")
    print("1. Rock 🪨  \n2. Paper 📄 \n3. Scissors ✂️ ")
    user_choice=int(input("Enter your choice: "))
    computer_choice=randint(1,3)

def main():
    global computer_choice,user_choice
    arr=["Rock 🪨","Paper 📄","Scissors ✂️"]
    get_choice()
    if user_choice==computer_choice:
        print(f"u choose {arr[user_choice-1]} and the computer is {arr[computer_choice-1]} : tie")
    if user_choice==1 and computer_choice==2:
        print(f"u choose {arr[user_choice-1]} and the computer is {arr[computer_choice-1]} :You Lose")
    if user_choice==1 and computer_choice==3:
        print(f"u choose {arr[user_choice-1]} and the computer is {arr[computer_choice-1]} :You Win")
    if user_choice ==2 and computer_choice==1:
        print(f"u choose {arr[user_choice-1]} and the computer is {arr[computer_choice-1]} :You Win")
    if user_choice==2 and computer_choice==3:
        print(f"u choose {arr[user_choice-1]} and the computer is {arr[computer_choice-1]} :You Lose")
    if user_choice==3 and computer_choice==1:
        print(f"u choose {arr[user_choice-1]} and the computer is {arr[computer_choice-1]} :You Lose")
    if user_choice==3 and computer_choice==2:
        print(f"u choose {arr[user_choice-1]} and the computer is {arr[computer_choice-1]} :You Win")

def play_game():
    choice=input("u want to start (Y/N) :")
    while choice.upper()=="Y":
        main()
        choice=input("u want to start (Y/N) :")
    print("Good Bye 👋")
play_game()