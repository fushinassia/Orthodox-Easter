months=[1,2,3,4,5,6,7,8,9,10,11,12]
EasterYear=int(input("Enter the Year: "))
a=EasterYear%19
b=EasterYear%4
c=EasterYear%7
d=((a*19)+15)%30
e=(2*b+4*c+6*d+6)%7
EasterDay=d+e+4
if (EasterDay>30):
    EasterDay-=30
    print(f"Easter Day is at :{EasterDay}/{month[4]}")
else:
    print(f"Easter Day is at: {EasterDay}/{months[3]}")
"""ΑΘΑΝΑΣΙΑ ΤΖΑΝΙΔΗ 3Δ-ΠΛΠ01 20/11/2026"""