#main.py
#1.Ask & Capture and the user if incorrect in answer has  one chance again
#2.Sentize by Filter
#3.Evaluate
#4.Excute
def main():
    Score=0
    print("************ Welcome to the game! Ready to test your limits? ************")
#for question 1
    The_Answer1=input("The Frist Question:\n"
                              "What is The Capital of Palestine?")
    The_Cleaned_Answer1=The_Answer1.strip().lower()
    if(The_Cleaned_Answer1=="alquds"):
        Score+=1
        print("Great!")
    else:
        print("it's OK,Try with the Next Question")
#for question 2

    The_Answer2=input("The Second Question:\n"
                              "Which prophet is given the title of the 'Seal of the Prophets and Messengers'?")
    The_Cleaned_Answer2=The_Answer2.strip().lower()
    if(The_Cleaned_Answer2=="mohamed" or The_Cleaned_Answer2=="muhammad"):
        Score+=1
        print("Great!")
    else:
        print("it's OK,Try with the Next Question")

#for question 3            
    The_Answer3=input("The Last Question:\n"
                              "According to Islamic tradition, which prophet is believed to be still alive?")
    The_Cleaned_Answer3=The_Answer3.strip().lower()
    if(The_Cleaned_Answer3=="isa"):
        Score+=1
        print("Great!")




# Excution
    print(f"********************************\n Your Score is:{Score}\n********************************")            
    if(Score==3):
        print("Incredible! Perfect Score! You are a true champion! 🌟")              
    elif(Score==2):
        print("Well done! You’ve got the hang of it! ✨")
    elif(Score==1):  
        print("Good effort! Every step forward counts. Keep practicing! 🎯")
    else:
        print("No worries! Every master was once a beginner.⚡")         




if __name__=="__main__":
    main()
