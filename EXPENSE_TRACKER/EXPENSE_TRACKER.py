#main.py
def main():
    Total=0
    Total_day=0
    totalhome=0
    totalStudy=0
    totalFoods=0
    totalPersonal=0
    totalFun=0
    try:
        Budget=int(input("Please, Enter your budget:"))
    except ValueError:
         print("Invalid Data") 

    while True:
        #defensive technique
        try:
            #I/P->Take from user the product name,its price for one product ,the amount of product,its category number
            expense_name=str(input("\nPlease,Enter the product name: "))
            expense_price=int(input("\nEnter its Price for one: "))
            amount_o_product=int(input("\nthe number of product: "))
            Categories=int(input("1.Home.\n" \
                                "2.Study.\n"
                                "3.Food & Drinks.\n"
                                "4.Personal things.\n"
                                "5.fun.\n" \
                                "\nplease, Enter a Category number:"))
        except ValueError:
            #if error is happened continue in program
            print("Invalid Data")   
            continue
        
        if (Categories==1):
            totalhome=expense_price*amount_o_product
        if (Categories==2):
            totalStudy=expense_price*amount_o_product 
        if (Categories==3):
            totalFoods=expense_price*amount_o_product
        if (Categories==4):
            totalPersonal=expense_price*amount_o_product
        if (Categories==5):
            totalFun=expense_price*amount_o_product

        Total_day=int(totalhome+totalStudy+totalFoods+totalPersonal+totalFun)

        Total+=int(Total_day)
        print("You've added ",amount_o_product,expense_name,"its price is (",expense_price,"$)for each one",",so the Total for Today is",Total_day,"$")
        print("*"*25)
        #the kill switch if the user is out of your budget
        if(Total>=Budget):
            print("We are out of your budget")
            break

        State=int(input("for continue click 1." \
        "\nQuit click 2.\n"))
        #control(the kill switch if the user need to out)
        if((State==2)):
            break

    print("*"*25)
    print("\nThe Total Expenses:",Total,"$\n","You have",(Budget-Total),"$left") 

    print("*"*25)  
    
    print("Expenses by Category:-\n","*"*25,"\nHome:",totalhome,"$"
          ,"\nStudy:",totalStudy,"$"
          ,"\nFood & Drinks:",totalFoods,"$"
          ,"\nPersonal things:",totalPersonal,"$"
          ,"\nFun:",totalFun,"$")


if __name__=="__main__":
    main()
