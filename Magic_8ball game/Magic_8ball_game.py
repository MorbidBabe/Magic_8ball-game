

# Import the modules
import sys
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print ("Absolutely")
    
    elif answers == 2:
        print ("Outlook good")
    
    elif answers == 3:
        print ("You may rely on it")
    
    elif answers == 4:
        print ("Ask again later")
    
    elif answers == 5:
        print ("Duh")
    
    elif answers == 6:
        print ("Maybe")
    
    elif answers == 7:
        print ("no")
    
    elif answers == 8:
        print ("Someday")

    elif answers == 9:
        print ("Hell no")