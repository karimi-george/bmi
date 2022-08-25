height = float(input())
weight = float(input())
Body_Mass_Index = weight/(height*height)
if Body_Mass_Index<=10:
    print("underweight")
elif Body_Mass_Index>10 and Body_Mass_Index<15:
    print("normal")
elif Body_Mass_Index>=15 and Body_Mass_Index<20:
    print("overweight")
elif Body_Mass_Index>=20 and Body_Mass_Index<25:
    print("obesity")
