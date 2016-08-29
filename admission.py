a=input("enter fees paid :")
a=int(a)
b=input("within how many days have you cancel the admission :")
b=int(b)
if(b<5):
    print("fee will be deducted as 10%")
elif(b<10 and b>=5):
    print("fee will be deducted as 15%")
elif(b<15 and b>=10):    
    print("fee will be deducted as 20%")
else:
    print("fee will be deducted as 30%")



    
