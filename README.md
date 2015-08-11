# Restaurant_recommendation

Restaurant recommendation built using python2.7 and Pydev environment.
Input file restaurant_small.txt contains 4 values of restaurant 
restarant_name
rating
price
cuisine
restaurant are grouped based on price and rating and cuisine.
How to run the program :python restaurant.py
FILENAME =restaurant_small.txt

>>>recommend(FILENAME, Price, cuisine)
output :list name of the restaurant
eg:
>>>recommend(FILENAME, "400", ["Continental"])
[('Pizza Hut', '4')]
