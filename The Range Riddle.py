#The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.
import random 
moods_types=[ " happy", "sad", "energetic", "excited", "pumped", "concerned", "ill"]
days_week=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", " Saturday", "Sunday"]

 #Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm

for i in range  (len(moods_types)):
    moods= (moods_types)[i]
    days=days_week[i]
    new_moods=random.choice(moods_types)
    
    print(f'On', days, "you were feeling",  new_moods)
     