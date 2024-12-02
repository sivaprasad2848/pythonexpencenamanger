expences=[]
y=0
while(y==0):
    print("1-> For insert an expence")
    print("2-> For display an expence")
    option=int(input("Enter the option"))
    if(option==1):
        title=input("Enter the title")
        amount=input("Enter the amount")
        edate=input("Expence Date")
        expences.append((title,amount,edate))
    if(option==2):
        print(expences)

    y=int(input("Do you want to continue? 0 for yes"))

