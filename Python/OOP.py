class Land:

    def __init__(self,landname, address, space, buyPrice):
        self.landname = landname
        self.address = address 
        self.space = space
        self.buyPrice = buyPrice

    def show_details(self):
        print(f"land is {self.landname}")
        print(f"land address is {self.address}")
        print(f"land space is {self.space}")
        print(f"land buy Price is {self.buyPrice}")
        print("_________________________________")


    



