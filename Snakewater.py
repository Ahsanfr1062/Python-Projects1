print("Welcome to Snake Water Gun Game:")
print("You will Play with the Cmoputer:")
#importing random module for the computer
import random
round = 0
computer_point = 0
user_point = 0
#using while loop to give the user and computer number of rounds
while round<10:
    lis = ["S","W","G"]
    #with random computer will use randomly from the list
    computer_choice = random.choice(lis)
    User_choice = input("Please Choose One of the following:\n 1:Snake=S\n 2:Water = W \n 3:Gun = G")
    #using if condition if there is a Tie
    if User_choice == computer_choice:
        print(f"computer choosed {computer_choice}")
        print("Their is Tie Please Play Again")
        #Make sure code make infinite loop
        round= round+1
        print(f"No of Choice Used {round}")
        #conditon if user chooses Snake and computer water
    elif User_choice == "S" and computer_choice == "W":
        print(f"computer choosed {computer_choice}")
        print(" Oops! Snake has Drowned in the Water,Computer Has won this, Computer Got won 1 Point!")
        computer_point = computer_point+1
        print(f"Computer has {computer_point} Points")
        round = round+1
        print(f"No of Choice Used {round}")
    elif User_choice == "S" and computer_choice == "G":
        print(f"computer choosed {computer_choice}")
        print("You Killed the Snake with Gun, computer has Got one Point")
        computer_point= computer_point +1
        print(f"Computer has {computer_point} Points")
        round = round+1
        print(f"No of Choice Used {round}")
    elif User_choice == "W" and computer_choice == "S":
        print(f"computer choosed {computer_choice}")
        print("Snake has been drowned in the water, User has got one point")
        user_point = user_point+1
        print(f"User has {user_point} points")
        round = round+1
        print(f"No of Choice Used {round}")
    elif User_choice == "W" and computer_choice=="G":
        print(f"computer choosed {computer_choice}")
        print("Gun has been Drownd,User has got one Point")
        user_point = user_point+1
        print(f"User has {user_point} points")
        round= round+1
        print(f"No of Choice Used {round}")
    elif user_point == "G" and computer_choice=="S":
        print(f"computer choosed {computer_choice}")
        print("Gun Killed the Snake, User got one point")
        user_point= user_point+1
        print(f"User has {user_point} points")
        round= round+1
        print(f"No of Choice Used {round}")
    elif computer_choice=="W" and User_choice == "G":
        print(f"computer choosed {computer_choice}")
        print("Gun has been Drowned in the Water, Computer Got 1 point")
        computer_point = computer_point+1
        print(f"Computer has {computer_point} Points")
        round = round+1
        print(f"No of Choice Used {round}")
    else:
        print("Invalid Input")

#if  number of attmepts are more than other,he wins
if computer_point>user_point:
    print(f"Computer has won the game with {computer_point} Points")
if user_point < computer_point:
    print(f"user has won the game with {user_point} Points")