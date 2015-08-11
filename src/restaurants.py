"""
Restaurant recommendation
"""
FILENAME = "restaurants_small.txt"


class Restaurant(object):
    """
    Restaurant class
    :type name: str
    :type rating: int
    :type price: str
    :type cuisine: list of str
    """

    def __init__(self, name, rating, price, cuisine):
        self.name = name
        self.rating = rating
        self.price = price
        self.cuisine = cuisine
    # Formating a string
    def __str__(self):
        return "%s - %s" % (self.name, self.rating)


def recommend(filename, price, cuisine):
    """
    Restaurant recommendation
    :type filename: str
    :type price: str
    :type cuisine: list of str
    :rtype: list[tuple[str, int]]
    >>> recommend(FILENAME, "100", ["North Indian])
    [('Biryani Hut', 3)]
    """
    restaurants = read_restaurants(filename)
    (ratings, prices, cuisines) = group_restaurants(restaurants)
    price_set = set(prices[price])
    cuisine_set = set()
    for c in cuisine:
        cuisine_set = cuisine_set.union(set(cuisines[c]))

    result_set = price_set.intersection(cuisine_set)
    result = []
    for rest in result_set:
        result.append((rest, ratings[rest]))
    result = sorted(result, key=lambda a: a[1], reverse=True)
    return result


def group_restaurants(restaurants):
    """
    Takes a list of restaurants and outputs a dicts of ratings, prices, cuisines
    :type restaurants: list of Restaurant
    :rtype: tuple[dict, dict, dict]
    >>> restaurants = read_restaurants(FILENAME)
    >>> (ratings, prices, cuisines) = group_restaurants(restaurants)
    >>> len(ratings)
    17
    >>> len(prices)
    4
    >>> len(cuisines)
    13
    """

    ratings = dict()
    cuisines = dict()
    prices = dict()
    for rest in restaurants:
        ratings[rest.name] = rest.rating
        if not rest.price in prices:
            prices[rest.price] = []
        prices[rest.price].append(rest.name)
        for rest_cuisine in rest.cuisine:
            if not rest_cuisine in cuisines:
                cuisines[rest_cuisine] = []
            cuisines[rest_cuisine].append(rest.name)
    return ratings, prices, cuisines


def read_restaurants(filename):
    """
    Reads the file and returns list of restaurants
    :type filename: str
    :rtype: list of Restaurant
    >>> alist = read_restaurants(FILENAME)
    >>> len(alist)
    17
    """
    # read the file and append into a list
    with open(filename) as filehandle:
        result = []

        i = 1
        record = ""
        for line in filehandle:
            if not line == "\n":
                record += line
                if i == 4:
                    result.append(read_restaurant(record))
                    i = 1
                    record = ""
                else:
                    i += 1
    return result


def read_restaurant(s):
    """
    Reads a restaurant for a string and returns a data structure
    :type s: str
    :rtype: Restaurant
    >>> s = "Priyadarshini\\n\
        5\\n\
        200\\n\
        South Indian\\n"
    >>> rest = read_restaurant(s)
    >>> rest.name
    'Priyadarshini'
    >>> rest.rating
    5
    >>> rest.cuisine
    ['South Indian']
    >>> rest.price
    '100'
    """
    lines = s.split("\n")
    name = lines[0]
    rating = lines[1]
    price = lines[2]
    cuisine = lines[3].split(",")
    restaurant = Restaurant(name, rating, price, cuisine)
    return restaurant

if __name__ == "__main__":
    print recommend(FILENAME, "400", ["Continental"])
    
    
    
