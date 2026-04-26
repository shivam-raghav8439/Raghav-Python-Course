# n= int(input("Eneet a number :"))
# for i in range(1, n+1):
#     print("" *(n-1) + ("*")*(2*i-1))  pyramid triangle  for loooop 


# n= int(input("Eneet a number :"))
# i=1
# while i<=n+1: 
#     print(""*(n-1) + "*"*(2*i-1))       pyramid triangle while loop 
#     i+=1



# n= int(input("Eneet a number :"))
# i=n
# while i>=1:
#     print(""*(n-i) + "*"*(2*i-1))      inveted   pyramid triangle while loop 
#     i-=1


# n= int(input("Eneet a number :"))       inveted   pyramid triangle for loop
# for i in range(n,0,-1):
#     print(""*(n-i) + "*"*(2*i-1))


n= int(input("Eneet a number :"))
for i in range (1,n+1):
    for j in range(1,2*n):
        if j == n-i+1 or  j==n+i-1 or n==i:
            print("*",end="")                 # Hollow Pyramid triangle
        else:
            print(" ",end="")
    print(" ")


