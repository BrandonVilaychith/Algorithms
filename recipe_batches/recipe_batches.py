#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    possible_batches = []
    if set(recipe) == set(ingredients):
        for item_needed in recipe:
            batch = ingredients[item_needed] // recipe[item_needed] 
            if batch == 0:
                return 0
            elif batch >= 1:
                possible_batches.append(batch)
    else:
        return 0
    
    return min(possible_batches)
            



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))