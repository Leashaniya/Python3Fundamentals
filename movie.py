current_movies={'The Grinch':'11.00am',
                'Rudolph':'1.00pm',
                'Frosty the snowman':'3.00pm',
                'Christmas vacation':'5.00pm'}

print("we're showing the following movies:")
for result in current_movies:
    print(result)
    
movie=input('what movie you gonna watch: ')

showtime=current_movies.get(movie)

if showtime== None:
    print("requested movie isn't playing")

else:
    print(movie," is playing at ",showtime)
