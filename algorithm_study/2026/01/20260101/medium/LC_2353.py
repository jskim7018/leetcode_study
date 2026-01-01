from typing import List
from collections import defaultdict
from sortedcontainers import SortedDict, SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_curr_rating = defaultdict(int)
        self.food_to_cuisine = defaultdict(str)
        self.cuisines_mp = defaultdict(SortedDict)
        for i in range(len(foods)):
            self.food_to_cuisine[foods[i]] = cuisines[i]
            self.food_curr_rating[foods[i]] = ratings[i]
            self.cuisines_mp[cuisines[i]].setdefault(ratings[i], SortedSet()).add(foods[i])

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        curr_rating = self.food_curr_rating[food]
        # remove from curr rating
        self.cuisines_mp[cuisine][curr_rating].remove(food)
        if not self.cuisines_mp[cuisine][curr_rating]:
            del self.cuisines_mp[cuisine][curr_rating]

        # add to new rating
        self.cuisines_mp[cuisine].setdefault(newRating, SortedSet()).add(food)
        self.food_curr_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_mp[cuisine].peekitem(-1)[1][0]
