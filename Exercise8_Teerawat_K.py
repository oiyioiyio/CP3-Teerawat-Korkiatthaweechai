UsernameInput = input("Username: ")
PasswordInput = input("Password: ")
UsbHubPrice = 100
DvdDrivePrice = 300
MousePrice = 50
Vat = 7
Currentcy = "THB"
UsbHubTotalPrice = 0
DvdDriveTotalPrice = 0
MouseTotalPrice = 0
AmountofUsbHub = 0
AmountofDvdDrive = 0
AmountofMouse = 0

if UsernameInput == "TestUser" and PasswordInput == "TestPassword":
    print("!!!Login Success!!!")
    print("----- Welcome to TestShop -----")
    print("1. USB Hub:   Price ",UsbHubPrice, Currentcy)
    print("2. DVD Drive: Price ",DvdDrivePrice, Currentcy)
    print("3. Mouse:     Price ",MousePrice, Currentcy)
    print("-------------------------------")
    ItemSelected = input("Please select the number of item you need: ")

    if ItemSelected == "1":
        AmountofUsbHub = int(input("Amount of item: "))
        UsbHubTotalPrice = UsbHubPrice * AmountofUsbHub
    elif ItemSelected == "2":
        AmountofDvdDrive = int(input("Amount of item: "))
        DvdDriveTotalPrice = DvdDrivePrice * AmountofDvdDrive
    elif ItemSelected == "3":
        AmountofMouse = int(input("Amount of item: "))
        MouseTotalPrice = MousePrice * AmountofMouse
    else:
        print("Invalid selection please login to try again")

    TotalPrice = UsbHubTotalPrice + DvdDriveTotalPrice + MouseTotalPrice
    if AmountofUsbHub > 0 and ItemSelected == "1":
        print("USB Hub", AmountofUsbHub, "item Price: ", UsbHubTotalPrice, Currentcy)
        print("Total Price Before Vat: ", TotalPrice, Currentcy)
        print("Total Price Vat Included: ", TotalPrice * (1 + Vat / 100), Currentcy)
    if AmountofDvdDrive > 0 and ItemSelected == "2":
        print("DVD Drive", AmountofDvdDrive, "item Price: ", DvdDriveTotalPrice, Currentcy)
        print("Total Price Before Vat: ", TotalPrice, Currentcy)
        print("Total Price Vat Included: ", TotalPrice * (1 + Vat / 100), Currentcy)
    if AmountofMouse > 0 and ItemSelected == "3":
        print("Mouse", AmountofMouse, "item Price: ", MouseTotalPrice, Currentcy)
        print("Total Price Before Vat: ", TotalPrice, Currentcy)
        print("Total Price Vat Included: ", TotalPrice * (1 + Vat / 100), Currentcy)
else:
    print("Login Failed: Please check your username and password and try to login again")