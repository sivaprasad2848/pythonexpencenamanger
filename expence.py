expences=[]
y=0
while(y==0):
    print("1-> For insert an expence")
    print("2-> For display an expence")
    print("3-> For display an expence")
    option=int(input("Enter the option"))
    if(option==1):
        title=input("Enter the title")
        amount=input("Enter the amount")
        edate=input("Expence Date")
        expences.append((title,amount,edate))
    if(option==2):
        print(expences)
    if(option==3):
        total=0
        dt=input("Enter a date")
        for item in expences:
            if(item[2]==dt):
                total=total+int(item[1])
        print("Total amount for the entered date:"+str(total))
                

    y=int(input("Do you want to continue? 0 for yes"))

