#files in python(01)
#with open("file.txt","w") as f:
    #f.write("Hello my dear boys,How do you do")
    #f.read()

#files in python(02)
#st = "Hey Harry you are amazing\n"

#f = open("myfile.txt","a")

#f.write(st)

#f.close()

#files in python(03)
'''
import random

def game():
    print("You are playing a game")
    score = random.randint(1,100)
    # fetch the hiscore
    with open("hiscore.txt")as f:
       hiscore=f.read()
       if(hiscore!=""):
          hiscore=int(hiscore)
       else:
          hiscore = 0

    print(f"your score: {score}")
    if(score>hiscore):
       with open("hiscore.txt","w") as f:
          f.write(str(score))
    return score
game()
'''