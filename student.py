name=input("Enter your name: ")
print("Hello, " + name + "! Welcome to the student portal.")    

degree=(int(input("Enter your degree program: ")))
if degree>=90:
    print("A")
    print("Congratulations! You have achieved an excellent grade.")
elif degree>=80:
    print("B")
    print("Good job! You have achieved a good grade.")
elif degree>=70:
    print("C")
    print("You have achieved a satisfactory grade.")
elif degree>=60:
    print("D")
    print("You have achieved a passing grade.")
else:
    print("F")
    print("Faild")