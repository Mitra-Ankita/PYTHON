print("welcome to my game")

playing=input("Do you want to play?(yes/no) ")
if(playing!="yes"):
    quit()

def again():    
    print("Okay,let;s play😊😊")  
    score=0

    answer=input("what does CPU stands for ? ").lower()
    if(answer=="central processing unit" ):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer")
    
    answer=input("what does GPU stands for ? ").lower()
    if(answer=="graphics processing unit" ):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer") 
    
    answer=input("what does RAM stands for ? ").lower()
    if(answer=="random access memory" ):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer")
     
    answer=input("what does ROM stands for ? ").lower()
    if(answer=="read only memory" ):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer") 
             
    print(f"you got {score} question correct") 
    print(f"you got {score/4*100} %")

#calling the function    
again() 

#play again loop
while True:
    play_again=input("Do you want to play again (yes/no)").lower()
    if(play_again!="yes"):
        quit()
    again()