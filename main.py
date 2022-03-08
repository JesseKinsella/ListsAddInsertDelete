fav_movies = ['Sandlot', 'The Lego Movie', 'Dune']

#length, number of items in list
print(len(fav_movies))

#add thing to list

fav_movies.append("Iron Man")

print(len(fav_movies))
print(fav_movies) #append adds to end

#add an item to a specific place with insert

fav_movies.insert(1,'Batman') #rember, based on 0 so 1 is second spot
print(fav_movies)

#remove list item with del
del(fav_movies[2]) #delete at the index of 2
print(fav_movies)

#remove all except 0

del(fav_movies[1])
del(fav_movies[1])
del(fav_movies[1])
print(fav_movies)