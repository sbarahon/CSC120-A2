from typing import Dict, Union, Optional

class ResaleShop:
    """ This class defines the resale shop and manages the shop inventory. 
    """
    def __init__(self):
        """ Constructs the resale shop by defining the inventory and the current itemID. 
        inventory: a dictionary where we'll store our inventory
        The key is an int representing the item number
        The value is another dictionary containing information about the machine
        """
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {} 
        self.itemID : int = 0
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        """Takes in a computer object containing all the information about a computer and adds it to the inventory
        """
        self.itemID += 1 # increment itemID everytime buy is called
        self.inventory[self.itemID] = computer
    def sell(self, item_id: int):
        """ Takes in an item_id, removes the associated computer if it is the inventory, 
        prints error message otherwise
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    def print_inventory(self):
        """ prints all the items in the inventory (if it isn't empty), prints error otherwise
        """
        # If the inventory is not empty
        if self.inventory:
        # For each item
            for item_id in self.inventory:
            # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")
    def update(self, computer:Dict[str, Union[str, int, bool]], item_id:int):
        """ updates a computer item within the inventory if it has been refurbished or price has been changed
        """
        if item_id in self.inventory:
            self.inventory[item_id]= computer