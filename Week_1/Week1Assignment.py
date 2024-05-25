n = int(input("Enter the number of rows\n"))

print("\nLower Triangle\n")
for i in range(0, n):    
    for j in range(0, i+1):    
        print("* ", end="")    
    print() 

print("\nUpper Triangle\n")
for i in range(n, 0, -1):
    for j in range(0, i):
        print("* ", end="")
    print()    

print("\nPyramid\n") 
k = 2 * n - 2   
for i in range(0,n):      
    for j in range(0,k):    
        print(end=" ")    
    k = k-1
    for j in range(0, i + 1):    
        print("* ", end="")     
    print()   