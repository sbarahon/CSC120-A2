from types import MemberDescriptorType
from typing import Dict, Union, Optional


class Computer:
    """ Defines a computer with it's information
    """
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int, itemID: int):
        self.description: str = description
        self.processor_type: str = processor_type
        self.hard_drive_capacity: int = hard_drive_capacity
        self.memory: int = memory
        self.operating_system:str = operating_system
        self.year_made: int = year_made
        self.price: int = price
        self.itemID = itemID
    def refurbish(self, new_os: Optional[str] = None):
        """ Refurbishes the defined computer object
        """
        if int(self.year_made) < 2000:
            self.price = 0 # too old to sell, donation only
        elif int(self.year_made) < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif int(self.year_made) < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff
        if new_os is not None:
            self.operating_system = new_os # update details after installing new OS
    def update_price(self, new_price: int):
        """ Takes in a new price for the given computer object
        """
        self.price = new_price
    def __str__(self):
        """ Allows the computer object to be printed to the console in dictionary format
        """
        return str({'description': self.description,
            'processor_type': self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price
    })