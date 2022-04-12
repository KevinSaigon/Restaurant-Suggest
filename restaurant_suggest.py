import random
import json

def get_any_restaurant(data):
    i = random.randint(0, len(data) - 1)
    option = data[i]
    # print(option["name"])
    return(option["name"])

## only get new restaurants
def get_new_restaurant(data):
    found = 0
    while not found:
        i = random.randint(0, len(data) - 1)
        option = data[i]
        if option["visited"] == 0:
            found = 1
            # print(option["name"])
    return option["name"]

def get_data():
    with open('data/restaurants.txt', encoding='utf-8-sig' ) as f:
        lines = f.read()

    # print(lines)
    restaurants = lines.split('\n\n')
    # print(restaurants)
    data = []
    for spot in restaurants:
        if spot == "": # in case of trailing new lines
            break
        restaurant_dict = {}
        elements = spot.split("\n")
        # print(elements)
        restaurant_dict['name'] = elements[0]
        restaurant_dict["visited"] = 0 if elements[1].split(": ")[1].lower() == "no" else 1
        restaurant_dict["review"] = elements[2].split(": ")[1]
        restaurant_dict["neighbourhood"] = elements[3].split(": ")[1]
        data.append(restaurant_dict)
    # print(data)
    return data

def write_data(name, visited, review, neighbourhood):
    f = open("data/restaurants.txt", "a")
    f.write("\n")
    f.write(name + "\n")
    f.write("Visisted: " + visited + "\n")
    if review != "":
        f.write("Review: " + review + "\n")
    else: 
        f.write("Review: N/A" + "\n")
    f.write("Neighbourhood: " + neighbourhood + "\n")
    f.close()

if __name__ == "__main__":
    data = get_data()
    get_new_restaurant = get_new_restaurant(data)
    any_restaurant = get_any_restaurant(data)
    print("New: " + get_new_restaurant)
    print("Any: " + any_restaurant)
# write_data("Medley's Italian Grill", "No", "", "North Van")

