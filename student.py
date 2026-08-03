name=input("Enter your name: ")
print("Hello, " + name + "! Welcome to the student portal.")    

degree=(int(input("Enter your degree program: ")))
if degree>=90:
    print("A")
elif degree>=80:
    print("B")
elif degree>=70:
    print("C")
elif degree>=60:
    print("D")  
else:
    print("F")    