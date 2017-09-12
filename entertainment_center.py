import media
import fresh_tomatoes

'''
Defines the movie objects
'''

into_the_wild = media.Movie("Into the Wild",
                            "After graduating from Emory University, top student and athlete Christopher McCandless abandons his possessions, gives his entire $24,000 savings account to charity and hitchhikes to Alaska to live in the wilderness. Along the way, Christopher encounters a series of characters that shape his life.",
                            "https://upload.wikimedia.org/wikipedia/pt/8/8a/Into-the-wild.jpg",
                            "https://www.youtube.com/watch?v=g7ArZ7VD-QQ")


moana = media.Movie("Moana",
                    "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana's island, she answers the Ocean's call to seek out the Demigod to set things right.",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")


in_time = media.Movie("In Time",
                      "In a future where people stop aging at 25, but are engineered to live only one more year, having the means to buy your way out of the situation is a shot at immortal youth. Here, Will Salas finds himself accused of murder and on the run with a hostage - a connection that becomes an important part of the way against the system.",
                      "https://upload.wikimedia.org/wikipedia/pt/a/a3/In_Time.jpg",
                      "https://www.youtube.com/watch?v=fdadZ_KrZVw")


coco = media.Movie("Coco",
                   "Aspiring musician Miguel (voice of newcomer Anthony Gonzalez) teams up with charming trickster Hector (voice of Gael Garcia Bernal) on an extraordinary journey through the Land of the Dead.",
                   "https://upload.wikimedia.org/wikipedia/en/d/d7/Coco_%282017_film%29_logo.jpg",
                   "https://www.youtube.com/watch?v=zNCz4mQzfEI")


the_perks = media.Movie("The Perks of Being  Wallflower",
                        "An introvert freshman is taken under the wings of two seniors who welcome him to the real world.",
                        "https://upload.wikimedia.org/wikipedia/en/0/0b/The_Perks_of_Being_a_Wallflower_Poster.jpg",
                        "https://www.youtube.com/watch?v=2vb2qrcPEEs")

beauty_beast = media.Movie("Beauty and the Beast",
                           "An adaptation of the fairy tale about a monstrous-looking prince and a young woman who fall in love.",
                           "https://upload.wikimedia.org/wikipedia/pt/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                           "https://www.youtube.com/watch?v=e3Nl_TCQXuw")


'''
Send the movie objects to generate page
'''

movies = [into_the_wild, moana, in_time, coco, the_perks, beauty_beast]
fresh_tomatoes.open_movies_page(movies)
