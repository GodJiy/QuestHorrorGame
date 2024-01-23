from random import randint as r

score_list = []

def start_game():
    points = 0
    player_name = input("Enter your name: ")
    print(f"Welcome to QuestGame, {player_name}...")
    wanna_play = input("Would you like to play?(Enter Yes/No): ")

    if wanna_play.lower() != "yes":
        print("Okay, bye")
        exit()
    while wanna_play.lower() == "yes":
        room = r(1,5)
        if room == 1:
            print("This room is dark. You go straight and see stairs. You can go straight or back. (Enter 1 or 2): \n")
            choice = int(input())
            dead_choice = r(1,2)
            if choice < 1 or choice > 2:
                raise ValueError
            if choice == dead_choice:
                show_score()
                print("Oh... Monster kill you..")
                wanna_play = input("\n Would you like to play again or you scared?(Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Bye bye...")
                    exit()
                else:
                    print("Great.")
                    continue
            else:
                points += 100
                print("\n You select right choice! You get 100 points.")
                score_list.append(points)
                continue
        if room == 2:
            print("This is hallway. You see bookshelves and wardrobes. You can go on the right, on the left or straight. (Enter 1, 2 or 3): \n")
            choice = int(input())
            dead_choice = r(1,3)
            if choice < 1 or choice > 3:
                raise ValueError
            if choice == dead_choice:
                show_score()
                print("\n Oh... You die..")
                wanna_play = input("\n Would you like to play again?(Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Bye bye...")
                    exit()
                else:
                    print("Great.")
                    continue
            else:
                points += 50
                print("\n You select right choice! You get 50 points.")
                score_list.append(points)
                continue
        if room == 3:
            print("This is maze. You see green bushes. You can go straight, on the right or on the left. (Enter 1, 2 or 3): \n")
            choice = int(input())
            lost_choice = r(1,3)
            if choice < 1 or choice > 3:
                raise ValueError
            if choice == lost_choice:
                if choice == 1:
                    show_score()
                    print("\n You go straight and you lost.")
                    wanna_play = input("\n Would you like to play again or you loser?(Enter Yes/No): ")
                    if wanna_play.lower() != "yes":
                        print("Bye bye...")
                        exit()
                    else:
                        print("Great.")
                        continue
                if choice == 2:
                    show_score()
                    print("\n You go on the right and you fell in the trap...")
                    wanna_play = input("\n Would you like to play again?(Enter Yes/No): ")
                    if wanna_play.lower() != "yes":
                        print("Bye bye...")
                        exit()
                    else:
                        print("Great.")
                        continue
                if choice == 3:
                    show_score()
                    print("\n You go on the left and you met a monster. You try run, but it is uselessly...")
                    wanna_play = input("\n Would you like to play again?(Enter Yes/No): ")
                    if wanna_play.lower() != "yes":
                        print("Bye bye...")
                        exit()
                    else:
                        print("Great.")
                        continue
            else:
                points += 80
                print("\n You select right choice! You get 80 points.")
                score_list.append(points)
                continue
        if room == 4:
            print("\n You see ocean. You can go in the ocean, on the right, on the left.(Enter 1,2 or 3): ")
            choice = int(input())
            lost_choice = r(1,3)

            if choice < 1 or choice > 3:
                raise ValueError
            if choice == lost_choice:
                if choice == 1:
                    show_score()
                    print("\n You go in ocean and something take your leg and get down...")
                    wanna_play = input("\n Would you like to play again?(Enter Yes/No): ")
                    if wanna_play.lower() != "yes":
                        print("Bye bye...")
                        exit()
                    else:
                        print("Great.")
                        continue
                if choice == 2 or choice == 3:
                    show_score()
                    print("\n You go near the ocean and you see monster, but you can't run...")
                    wanna_play = input("\n Would you like to play again?(Enter Yes/No): ")
                    if wanna_play.lower() != "yes":
                        print("Bye bye...")
                        exit()
                    else:
                        print("Great.")
                        continue
            else:
                print("You survive and you get 100 points!")
                points += 100
                score_list.append(points)
                continue
        if room == 5:
            print("\n This room is so bright. You can go straight, on the left, on the right and back.(Enter 1,2,3 or 4): ")
            choice = int(input())
            right_choice = r(1,4)

            if choice < 1 or choice > 3:
                raise ValueError
            if choice == right_choice:
                print("You so lucky... Chance for survive: 25%. Nice! You get 200 points!")
                points += 200
                score_list.append(points)
                continue
            else:
                show_score()
                print("You lost...")
                wanna_play = input("\n Would you like to play again?(Enter Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Bye bye...")
                    exit()
                else:
                    print("Great.")
                    continue

def show_score():
    if not score_list:
        print("You currently don't have points!")
    else:
        print(f"You high score: {max(score_list)} points")

start_game()