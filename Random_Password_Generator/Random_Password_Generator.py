#1.Take length from user(at least 15)
# 2.store/prepare the characters
#main.py
def main():
    Password=[]
    while True:
        try:
            Len=int(input("Please, Enter the Password Length:"))
            if(Len<15):
                Len=int(input("Invalid Length.\n Please, Enter the Length again:"))
            else:
                break    
        except ValueError:
            print("Invalid.")

    ch1=list(string.ascii_uppercase)
    ch2=list(string.ascii_lowercase)
    ch3=list(string.digits)
    ch4=list(string.punctuation)
#3.shulffing to made it stronger
    secrets.SystemRandom(ch1)
    secrets.SystemRandom(ch2)
    secrets.SystemRandom(ch3)
    secrets.SystemRandom(ch4)
#specific the relation between Alpa.60% & digits,Punc.40%
    Range1=round(Len*(30/100))
    Range2=round(Len*(20/100))

    for i in range(Range1):
        P1=secrets.choice(ch1)
        Password.append(P1)
        P2=secrets.choice(ch2)
        Password.append(P2)
    for i in range(Range2):    
        P3=secrets.choice(ch3)
        Password.append(P3)
        P4=secrets.choice(ch4)
        Password.append(P4)
#Entropy Validation
    R=len(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
    Entropy=Len * math.log2(R)
#concatanate & Display Strong Password
    Password=''.join(Password[0:])
    print("\n")
    print("*"*25)
    print("\nThe Strong Password:",Password)
    print("\nThe Entropy Validation:",Entropy,"Bits")
    print("\n")
    print("*"*25)

if __name__=="__main__":
    import string
    import secrets
    import math
    main()