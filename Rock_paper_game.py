import random
print('''
                          _____            ____   ______  __     __ ______
                             \      _      / |____   | |     |       |    |  | \___/ | |___
                              \    / \    /  |____|  | |___  |       |    |  |       | |___|   
                               \__/   \__/   |_____  |_____| |____   |____|  |       | |______  
                                                           _____________                             
                                                           |____   ____|  ____
                                                                |  |     |    |
                                                                |  |     |    |
                                                                |__|     |____|          
                                   __      __
                                  |  \    /  |    ____   _____      _________      ______      __      __   _______
                                  |   \__/   |    \   |__|   /      |             /      \     | \    / |  |
                                  |          |     \__    __/       |    ____    /   __   \    |  \__/  |  |____
                                  |          |        |  |          |    |  |   /   |  |   \   |        |  |
                                  |          |        |  |          |____|  |   |___|  |___|   |        |  |_______  
                                    ROCK PAPER AND SCISSORS   ''')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
r=0
p=1
s=2
selector=[r,p,s]
play=int(random.choice(selector))
user=int(input('ENTER "0" FOR ROCK,"1" FOR PAPER,"2" SCISSOR \n'))
print("COMPUTER CHOSSES:- ")

#FOR COMPUTER
if play==r: 
    print(rock)
elif play==p:
    print(paper)
else :
    print(scissors)   
print("YOUR PLAY :-")
#FOR USER
if user==r:
    print( rock)
elif user==p:
    print(paper)   
else:
    print(scissors)     


if play==user:
    print("its draw")
if play==0 and user==1:
    print("You won")
elif play==0 and user==2:
    print("You lost")  
elif play==2 and user==0:
    print("you won")
elif play==1 and user==0:
    print("You lost")       
elif play==1 and user==2:
    print("you won")
elif play==2 and user==1:
    print("You lost")   



    


    

