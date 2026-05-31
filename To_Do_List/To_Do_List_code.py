#To do list 
#to add a new task(list,dictionary)
#to view The tasks(enumerate->1.study English)
My_Tasks=[]
Task_info={}

#main.py
def main():
    while True:
        options=int(input("1.Add New Task.\n" \
        "2.View The Tasks.\n" \
        "Enter your choice:"))   
        match options:
            case 1:
                Add_Task(My_Tasks)
            case 2:
                Veiw_Tasks(My_Tasks)
            case _:
                print("Invalid choice.\nPlease,Enter a Number 1 or 2.") 


def Add_Task(My_Tasks): 
    Task=input("The Task:")
    Note=input("the Note")
    Duration=input("duration:")
    Task_info={"The Task is":Task,"Note:":Note,"Duration:":Duration}
    My_Tasks.append(Task_info)
    print("The Task added is sucessfully.")
    
def Veiw_Tasks(My_Tasks):
    if not My_Tasks:
        print("There is not any Tasks.")
        return
    
    for index,Task in enumerate(My_Tasks,1):
        print(index,".",Task["The Task is"],Task["Note:"],Task["Duration:"])
        print("*"*30)
  



if __name__=="__main__":
    main()

         

            
   
       