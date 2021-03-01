def sum_water_costs(ingredients):
    sum_water = 0
    for ingredient in ingredients:
        sum_water += ingredient.water
    return sum_water

def sum_energy_costs(ingredients):
    sum_energy = 0
    for ingredient in ingredients:
        sum_energy += ingredient.water
    return sum_energy 

def find_lowest_energy_cost(ingredients):
    lowest_ingredient = ingredients[0]
    for ingredient in ingredients:
        if ingredient.energy < lowest_ingredient.energy:
            lowest_ingredient = ingredient
    return lowest_ingredient

def list_all_items_in_order(ingredients):
    return sorted(ingredients, key=lambda x: x.name)

def get_item_by_name(ingredients, name):
    for ingredient in ingredients:
        if ingredient.name == name:
            return ingredient
    return None

