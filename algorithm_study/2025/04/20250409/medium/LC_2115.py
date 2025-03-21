from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supplies_st = set(supplies)
        ingredients_st = set()

        for ingredient in ingredients:
            ingredients_st.update(ingredient)

        recipe_to_ingr = {recipes[i]:ingredients[i] for i in range(n)}
        def create_recipe(recipe) -> bool:
            nonlocal parent_recipes

            if recipe in supplies_st:
                return True
            else:
                if recipe in recipe_to_ingr:
                    ingredients_need = recipe_to_ingr[recipe]
                    is_possible = True
                    for ingr in ingredients_need:
                        # check cycle
                        if ingr in parent_recipes:
                            return False
                        parent_recipes.add(recipe)
                        is_create = create_recipe(ingr)
                        parent_recipes.remove(recipe)
                        if not is_create:
                            is_possible = False
                            break

                    if is_possible:
                        supplies_st.add(recipe)
                        return True
                    else:
                        return False
                else:
                    return False

        ans = []
        parent_recipes = set()
        for recipe in recipes:
            if create_recipe(recipe):
                ans.append(recipe)
        return ans
