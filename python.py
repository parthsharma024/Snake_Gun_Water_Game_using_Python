import random
rand=random.randint(0,2)
# print(rand)
score_of_player=0
score_of_computer=0
a= input("Player Turn : Snake(S) Water(W) or Gun(G) ")
print(a)
l1=["Snake","Water","Gun"]
b= input(l1[rand])
print(b)
if a=="Gun" and rand==2:
   print("Both have chosen Gun"+" "+"Tie")
elif(a=="Water" and rand==1):
    print("Both have chosen Water"+" "+"Tie")
elif(a=="Snake" and rand==0):
    print("You both chose Snake"+" "+"Tie")
elif(a=="Snake" and rand==1):
    score_of_player=score_of_player+1
    print("Player 1 will win the match ")
elif(a=="Snake" and rand==2):
    score_of_computer=score_of_computer+1
    print("Computer Win the game")
elif(a=="Water" and rand==0):
    score_of_computer=score_of_computer+1
    print("Computer win the Game")
elif(a=="Water" and rand==2):
    score_of_player=score_of_player+1
    print("Player 1 will win the match ")
elif(a=="Gun" and rand==0):
    score_of_player=score_of_player+1
    print("Player 1 will win the match ")
elif(a=="Gun" and rand==1):
    score_of_computer=score_of_computer+1
    print("Computer Win the game")



print(score_of_player)
print(score_of_computer)

if(score_of_computer>score_of_player):
    print("Computer Wins the Match")
elif(score_of_player==score_of_computer):
    print("Match Tie ")
else:
    print(" Player Win The Match")