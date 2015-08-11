# Restaurant_recommendation

Restaurant recommendation built using python2.7 and Pydev environment.
Input file restaurant_small.txt contains 4 values of restaurant 
restarant_name,
rating,
price,
cuisine,
restaurant are grouped based on price , rating and cuisine.
How to run the program :python restaurant.py
FILENAME =restaurant_small.txt
cuisne ->set of cuisines you are looking
price->100, 200,300 (your budget)
>>>recommend(FILENAME, Price, cuisine)
output :list names of the restaurant with rating
test case
>>>recommend(FILENAME, "400", ["Continental"])
Output:[('Pizza Hut', '4')]
