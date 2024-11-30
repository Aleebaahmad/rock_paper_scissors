import random
options=["rock","paper","scissors"]
users_score=0
comp_score=0
random_guess= random.randint(0,2)                 # here a random option would be generated

while True:
   user_guess=str(input("Enter your turn or q to quit: "))
   comp_guess = options[random_guess]
   if user_guess=="q":
       print("Good BYE!!!!!")
       break
   elif user_guess not in options:
       continue
    elif user_guess=="Paper" and comp_guess=="rock":
       print("Hey U won!!!!!!!!!!!!!!!!!!!!")
       users_score+=1
       print("Your score is",users_score)
       print("My guess was", comp_guess + ".")
   elif user_guess=="scissors" and comp_guess=="paper":
       print("Hey U won!!!!!!!!!!!!!!!!!!!!")
       users_score+=1
       print("Your score is",users_score)
       print("My guess was",comp_guess + "." )
   elif user_guess=="rock" and comp_guess=="scissors":
       print("Hey U won!!!!!!!!!!!!!!!!!!!!")
       users_score+=1
       print("Your score is",users_score)
       print("My guess was", comp_guess + ".")
   else:
       comp_score+=1
       print("Hey I won!!!!!!!!!!")
       print("My score",comp_score)
       print("My guess was", comp_guess)
print("U won",users_score,"times")
print("I won",comp_score,"times")