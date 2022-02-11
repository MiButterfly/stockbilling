print("Stock billing system")
sum=0
dict={'Book':500,'Boxes':100,'Candle':50, 'Bottles':80}
lst=list(dict.keys())
print(lst)
while True:
    print("Book (500 rs.)")
    print("Boxes (100 rs.)")
    print("Candle (50) rs.)")
    print("Bottles (80 rs.)")
    print("press E for exit")
    order=input("Enter your order")
    if order in lst:
        sum=sum+dict[order]
    elif order== 'T':
        break
    else:
        print("Enter right iteam")
print("Your Total Stock bill is=",sum)            
