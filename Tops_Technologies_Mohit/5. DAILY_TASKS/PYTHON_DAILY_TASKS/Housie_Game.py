"""
-> random
-> conditional , looping
-> list

"""

import random

data = """

                       WELCOME TO LINEAR HOUSIE

"""

print(data)

main_ticket_list = []
game_list = []
player1 = []
player2 = []

while len(main_ticket_list)<12:
    ticket = random.randint(1,100)
    if ticket not in main_ticket_list:
        main_ticket_list.append(ticket)

print()

game_list = list(main_ticket_list)

player1 = main_ticket_list[0:6]
player2 = main_ticket_list[6:]

random.shuffle(main_ticket_list)

for ticket in main_ticket_list:
    print(ticket,end="  ")

print()

print(player1)
print(player2)

status = True

while status:
    p1_length = len(player1)
    p2_length = len(player2)
    if p1_length<1 or p2_length<1:
        status = False
        if p1_length<1:
           print("PLAYER 1 WON THE MATCH")
        elif p2_length<1:
           print("PLAYER 2 WON THE MATCH")
    else:

        input()
        main_ticket = random.choice(main_ticket_list)
        print(f"             {main_ticket}              ")
        if main_ticket in player1:
            player1.remove(main_ticket)
            main_ticket_list.remove(main_ticket)
        elif main_ticket in player2:
            player2.remove(main_ticket)
            main_ticket_list.remove(main_ticket)
        print()
        print(main_ticket_list)
        print(player1)
        print(player2)

   