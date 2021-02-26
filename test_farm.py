class Item():
    def __hash__(this):
        return this.name

    def __init__(this, name, water, energy):
        this.water = water
        this.energy = energy
        this.name = name
    
ingredients = [
    Item("Chicken",1,10),
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

#Already implmemented
def combine(name, *ingredients):
    pass

def item_by_name(ingredients, name):
    pass


import unittest

class Tests(unittest.TestCase):
    def test_get_item_by_name(self):
        self.assertEqual(sum_water_costs(ingredients, ))
        
    def sum_water_costs(self):
        pass

    def test_sum_energy_costs(self):
        pass

    def test_find_lowest_energy_cost(self):
        pass

    def test_list_all_items_in_order(self):
        pass

    def test_get_item_by_name(self):
        pass

    
if __name__ == "__main__":
    unittest.main()
    main(input("Input you ingredients to make a meal! "))