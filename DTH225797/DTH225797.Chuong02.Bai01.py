import math
try:
    r = float(input("Nhap ban kinh duong tron:"))
    cv = 2*math.pi*r
    dt = math.pi*r**2
    print("Chu vi: ",cv)
    print("Dien tich",dt)
except:
    print("Loi!")
    

