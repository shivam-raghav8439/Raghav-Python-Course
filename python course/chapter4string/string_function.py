myname="suriya pratap singh rajput" 
print(len(myname))# 1 type string function

print(myname.endswith("rajput"))             # 2 type string function

print(myname.startswith("Suriya"))               # 3 type string function

print(myname.capitalize())              # 4 type string function
print(myname.title())        # 5 type string function
print("jai Shree ram".title())              # 6 type string function

print(myname.count("a"))               # 7 type string function

print(myname.find("singh"))                     # 8 type string function
print(myname.index("singh"))          # 9 type string function

print(myname.lower())                                                                    # 10 type string function
print(myname.upper())               # 11 type string function

print(myname.replace("pratap","Raghav"))                       # 12 type string function

print(myname.split())           # 13 type string function

print("".join(myname))             # 14 type string function

print("1234".isdigit())                           # 15 type string function
print("1we34".isdigit())                  # 16 type string function

print("abc".isalpha())                    # 17 type string function
print("123".isalpha())                                                # 18 type string function
print("1234abhbbd".isalnum())


name ="Raghav"
age="19"
print("My name is {} and I am {} year old".format(name,age))   # or print(f"my name is {name} and I am {age} year old")  
print(f"My name is {myname} and I am {age} year old")            # 18 type string function

print("SuRIya SiNgH RAjPut ".swapcase())            # 19 type string function

print(f"Welcome{myname}")             # 20 type string function