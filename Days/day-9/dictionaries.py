##sample#
##
#dictionary = {#
#    123:"This is something",#
#    "new": "This is something #new",
#}#
##
##retrieve an item from diction#ary
##
#print(dictionary["new"])#
#print(dictionary[123])#
##
##adding new item#
##
#dictionary["add"] = "agregamos# algo"
##
#print(dictionary)#
##
##
##create new empty dictionary#
##
#empty_dic = {}#
##
##wipe a existing dictionary#
##
##dictionary = {}#
##print(dictionary)#
##
##loop#
##
#for key in dictionary:#
#    print(key) #print the keys#
#    print(dictionary)



#-----------------------------------------------------

#Nesting dictionary in dictionary
travel_log = {
    "France": {"cities-visited": ["Paris", "Lille", "Dijon"]},
    "Argentina": {"ciudades": ["Buenos Aires", "Cordoba"]}
}

print(travel_log)

#Nesting dictionary in list

travel_log = [
    {"country": "France", 
    "cities-visited": ["Paris", "Lille", "Dijon"]
    },


    {"country": "Argentina", 
    "ciudades": ["Buenos Aires", "Cordoba"]
    },
]

print(travel_log)

"""country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
  

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
"""