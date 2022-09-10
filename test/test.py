import random

flag = True 
while flag:
     num = input("type a number: ")

     if num.isdigit():
          print("let's play !")
          num = int(num)
          flag = False
     else:
          print("invalid input !! try again !")

secret = random.randint(1, num)

guess = None
count = 0

while guess!= secret :
     guess=input("please type a number between 1 and " + str(num) + ": ")
     if guess.isdigit():
         guess= int(guess)

     count += 1
     if guess == secret :
           print("you got it !") 
           break   
     else :
          if guess > secret:
               print("you were above the number!")
          else :
                print("you were below the number !")

print("it took you" , count , "guesses !!")         
