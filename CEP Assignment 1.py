#Expense tracker
import datetime
expense=[]
def expense_tracker():

    def Add_expense():
        d=input("Enter the date in format 'YYYY/MM/DD' \n (if the date is todays then enter 'today' : ").strip()
        amt=int(input("Enter the amount spent in INR : "))
        itm=input("Enter the name of item on which money is spent : ")
        if d.lower()=="today":
            d=datetime.date.today()
        else:
            d=datetime.datetime.strptime(d,"%Y/%m/%d").date()
        exp={"Date":d,"Amount":amt,"Item":itm.lower()}
        expense.append(exp)
                      
    def View_expense():
        Ch=input("Do you want to view full expense list Y/N : ")
        if Ch=="Y" or Ch=="y":
            for exp in expense:
                print("Date:", exp['Date'].strftime('%Y/%m/%d'),
                    "Amount:", exp['Amount'], 
                    "Item:", exp['Item'])
        else:         
            B=input("Enter the name of item whose expense you want to view : ")
            for i in expense:
                if i["Item"]==B.lower():
                    print(i)
        
    def Delete_expense():
        A=input("Enter the name of item whose expense you want to delete : ")
        for i in expense:
            if i["Item"]==A.lower():
                expense.remove(i)
                print("The expense is deleted sucessfully ")
        print("The remaining expenses are :")
        print(expense)
    def Total_expense():
        total = 0
        for i in expense:
            total = total + i["Amount"]
        print("The total expense spent in INR is : ", total)
    
    print("Welcome to the expense tracking system ")
    print("You can perform : \n 1.Adding the expense \n 2.Viewing the expense \n 3.Removing an expense \n 4.Total expenses \n 5.Exit")
    while True : 
        c=int(input("Enter your choice between 1-5 : "))
        if c==1:       
            Add_expense()
        elif c==2:
            View_expense()
        elif c==3:
            Delete_expense()
        elif c == 4:
            Total_expense()
        elif c == 5:
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Invalid choice.")

expense_tracker()