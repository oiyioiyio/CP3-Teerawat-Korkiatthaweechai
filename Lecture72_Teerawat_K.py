menuList = []

def showBill():
    totalPrice = 0
    print("---- MY FOOD ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice = totalPrice + int(menuList[number][1])
    print("Total price: ",totalPrice)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])

showBill()