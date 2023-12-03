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


class Sections(Land):
    plants_by_section = 4

    def __init__(self,landname, address, space, sections = 4):
        super().__init__(landname, address, space)
        self.sections = sections

    def show_sections_details(self):
        print(f"land is {self.sections}")





