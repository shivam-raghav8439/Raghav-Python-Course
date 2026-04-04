marks1=int(input("Enter your physic marks : "))
marks2=int(input("Enter your chemistry  marks : "))
marks3=int(input("Enter your english marks : "))
total_percentage=(marks1+marks2+marks3)*100/(300)
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Pass.",total_percentage)
else:
    print("You are fail. Please try again!.",total_percentage)