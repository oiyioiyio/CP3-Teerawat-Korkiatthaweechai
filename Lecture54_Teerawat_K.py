def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")

    if usernameInput == "TestUser" and passwordInput == "TestPassword":
        return showMenu()
    else:
        print("Invalid Username or Password")
        return login()

def showMenu():
    print("----- TestShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. Exit")
    return menuSelection()

def menuSelection():
    userSelected = int(input("Please select the option: "))

    if userSelected == 1:
        priceInput = int(input("Please fill your custom price: "))
        print("Total vat: ",vatCalculator(priceInput))
        return menuSelection()
    elif userSelected == 2:
        print("Total price with vat 7% included: ",priceCalculator())
        return menuSelection()
    elif userSelected == 3:
        return exit()
    else:
        print("Please select the number which are shown on the menu")
        return menuSelection()

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    priceInput_1 = int(input("Price of first product: "))
    priceInput_2 = int(input("Price of second product: "))
    totalPriceNoVat = priceInput_1 + priceInput_2
    print("Total price vat excluded: ",totalPriceNoVat)
    return vatCalculator(priceInput_1 + priceInput_2)

login()