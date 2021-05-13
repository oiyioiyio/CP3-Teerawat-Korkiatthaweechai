Username = input("Username : ")
Password = input("Password : ")

while Username != "TestUser" or Password != "TestPassword":
    print("Username or Password invalid please try again")
    Username = input("Username : ")
    Password = input("Password : ")

print("!!! Login Success !!!")