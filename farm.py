import unittest
import sys
from main import *

class Item():
    # Water: Litres
    # Energy: unknown - Kj maybe?
    def __init__(this, name, water, energy):
        this.water = water
        this.energy = energy
        this.name = name
    
Allingredients = [
    Item("Chicken",1960,10),
    Item("Salami", 5, 2),  
    Item("Carrot",10,5),  
    Item("Sashimi",2,20),
    Item("Bread",40,23),  
    Item("Lettuce", 20, 5),  
    Item("Potato",20,20),  
    Item("Sushi",13,123),
    Item("Mi Goreng",1,1),
    Item("Rice",2,5),
    Item("Cheese",2,4),
    Item("Milk", 10, 3)
]

def get_item_by_name_implemented(name):
    item = get_item_by_name(Allingredients, name)
    if item is None:
        print(f"The ingredient {name} does not exist")
        exit()
    else:
        return item

def process_input(inputString):
    itemVals = inputString.split(",")
    return [get_item_by_name_implemented(i) for i in itemVals]

def main(ingredients):
    print(f"""Your finished meal contains {list_all_items_in_order(ingredients)}
    Your meal requires {sum_energy_costs(ingredients)} kJ of energy to create
    Your meal requires {sum_water_costs(ingredients)} litres of water to create
    The item with the lowest energy cost is {find_lowest_energy_cost(ingredients)}""")

class Tests(unittest.TestCase):
    def test_get_item_by_name(self):
        ##Copy numbers below
        self.assertEqual(get_item_by_name("Chicken"),Item("Chicken",1,10))
        self.assertEqual(get_item_by_name("Bread"),Item("Bread",40,23))
        

    def sum_water_costs(self):
        chickenItem = get_item_by_name("Chicken")
        breadItem = get_item_by_name("Bread")
        ##Set number below
        self.assertEqual(sum_water_costs([chickenItem,breadItem],41))

    def test_sum_energy_costs(self):
        chickenItem = get_item_by_name("Chicken")
        breadItem = get_item_by_name("Bread")
        ##Set number below
        self.assertEqual(sum_energy_costs([chickenItem,breadItem],33))

    def test_find_lowest_energy_cost(self):
        ##Set number below
        lowestCostItem = get_item_by_name("Bread")
        self.assertEqual(find_lowest_energy_cost(ingredients),lowestCostItem)

    def test_list_all_items_in_order(self):
        self.assertEqual(list_all_items_in_order,sorted(Allingredients.items(), key=lambda x: x.name))


    
if __name__ == "__main__":

    main(process_input(input("Input your ingredients: ")))