# Using CRUD to update data structures
# CREATE - How to add a new item to a data structure
# READ - How to access an item in a data structure
# UPDATE - How to change or replace an item in a data structure.
# DELETE - How to remove an item from a data structure

class_names = ['Alison', 'Anushka', 'Audrey', 'Mashrafi', 'Mauricio', 'Maxime', 'Nhaomi', 'Praveena', 'Raekwon',
               'Sanila', "Ta'Ziyah", 'Taher', 'Taralynn', 'Thessaly', 'Vi', 'Zanggar']

# update this dictionary with your faves!
my_faves = {
    "dessert": "ice cream",
    "lunch food": "pizza",
    "dinner food": "pizza",
    "breakfast": "Peanut Butter Captain Crunch",
    "music genres": ["Pop", "Lofi", "Sad Rap"],
    "color": ["purple", "yellow"],
    "number": 9
}

# print your favorite dessert from my_faves
# print(my_faves["dessert"])
#
# # print out your favorite color from my_faves
# print(my_faves["color"][0])
#
# # print out one of your favorite music genres
# print(my_faves["music genres"][0])

# Add a key-value pair to the dictionary to store your favorite show or movie
my_faves["show"] = "Suits"

class_faves_dict = {
    "book_recs": ["Atomic Habits"],
    "music_recs": ["Unlike Pluto - Sunlight or Demise", "Vampire - Olivia Rodrigo", "I can see you - Taylor Swift",
                   "Mona Lisa - Dominic Fike", "Infrunami - Steve Lacy",
                   "I'm not gonna teach your boyfriend how to dance - Glee"],
    "travel_destinations": ["Alaska"],
    "podcasts": ["planet money"],
    "movie_tv_recs": ["Spirited Away", "Suits", "Warm Bodies"],
    "food_recs": ["Poke Bowls", "Asiago Bagels", "Mac N Cheese"],
    "activity_recs": ["Start a Diary", "Go out for a 30 minute jog", "drink lots of water", "Ice baths", "Ride a bike",
                      "Get a lot of sleep"]
}

# # print out the show recommendation "Suits"
# print(class_faves_dict["movie_tv_recs"][1])
#
# # print out the activity recommendation "Ride a bike"
# print(class_faves_dict["activity_recs"][4])
#
# # print out all of the music recommendations one at a time
# for i in class_faves_dict["music_recs"]:
#     print(i)

for k, v in class_faves_dict.items():
    print(v, k)