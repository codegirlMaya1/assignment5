#Objective:Task 1: The for Loop DJ Set Using the provided genres list, write a for loop that prints out each genre with a custom message. Extend this task by adding a counter that displays the number of the track before the genre.
music_genre=["Jazz", "Rock", "Hip-Hop", "Classical"]
music_sub=music_genre[1:]
print(music_genre)
print( music_sub)

#Task 2: The Remix Artist with while
new_playlist=music_genre
new_playlist.append("Music")
print(new_playlist)


# Task three Light Show Technician Loop Using the range() function, loop through the genres list by index. 

timer=10

while timer >0:
    print (timer)
    timer -=1
    print("The beat drops now!")
