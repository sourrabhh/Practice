print("Calculator")


print("""
1. Addition 
2. Substraction
3. Multiplication
4. Division""")

ch = int(input("Select the Choice"))


if(ch == 1) :
    x = int(input("Enter the value :: "))
    y = int(input("Enter the second Number :: "))

    c = x+ y
    print("Addition is :: ", c)

elif(ch == 2) :
    x = int(input("Enter the value :: "))
    y = int(input("Enter the second Number :: "))

    c = x - y
    print("Substraction is :: ", c) 
    
elif(ch == 3) :
    x = int(input("Enter the value :: "))
    y = int(input("Enter the second Number :: "))

    c = x * y
    print("Multiplication is :: ", c)
    
elif(ch == 4) :
    x = int(input("Enter the value :: "))
    y = int(input("Enter the second Number :: "))

    c = x / y
    print("Division is :: ", c)
    
elif(ch > 4 or ch < 1 ) :
    print("Sorry !! You have Entered Wrong Choice")
    