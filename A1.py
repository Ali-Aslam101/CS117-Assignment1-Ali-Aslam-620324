V=int(input("enter a voltage:"))
R=int(input("enter a resistance:"))
I=V/R
print(I)
if I>2:
    print("fuse will blow")
elif  I<=0 :
    print("Invalid resistance")
else:
    print("circuit is safe")
