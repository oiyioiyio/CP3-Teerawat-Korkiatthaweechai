class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastName,"'s cart")

Friend_1 = Customer()
Friend_1.name = "Ploy"
Friend_1.lastName = "Cherman"
Friend_1.age = 28
Friend_1.addCart()

Friend_2 = Customer()
Friend_2.name = "Aum"
Friend_2.lastName = "Patcharapa"
Friend_2.age = 26
Friend_2.addCart()

Friend_3 = Customer()
Friend_3.name = "Ann"
Friend_3.lastName = "Thongpasom"
Friend_3.age = 27
Friend_3.addCart()