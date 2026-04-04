# age = int(input("Entwr your age : "))
# if(age>=18):
#     print("You are adult catogary and you are able to voted.")
# elif(age<0):
#     print("Bro you are entering wrong age.")
# else:
#     print("You are minor catagory and you are unable to voted.")


# marks= int(input("Enter marks :"))
# if(marks>=80):
#     print("Grade A")
# elif(marks>=50):
#     print("Pass")
# elif(marks>30):
#     print("Passbility")
# else:
#     print("fail")


marks= int(input("Enter your marks : "))
result="Grade A" if marks>90 else "Grade B" if marks>75 else "Pass" if marks>40 else "Fail"
print(result)