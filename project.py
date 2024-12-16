m=n = int(input("Enter a number to convert from Dec to Binary: "))
s = ""

while(n>0):
    r=n%2  #to find the remainder which will be 1 or 0 by dividing by 2
    s=str(r)+s
    n=n//2 #onces you found the quotient, assign the quotient to "n"
print("The Binary number of ", m, "is" ,s)
