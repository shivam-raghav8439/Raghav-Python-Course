p1= "make a lot of money "
p2= "Buy now Click here"
p3= "Susbcribe this"
p4="win click this link"
messege=input("Enter your comment here : ")
if((p1 in messege) or p2 in messege or p3 in messege or p4 in messege):
    print("This is spam. Alert !")
else:
    print("THis is not spam. Chill Guis:)-")