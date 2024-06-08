#The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.
import time
import random 
moods_types= [ "happy", "sad", "energetic", "excited", "pumped", "concerned", "ill"]
days_week=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", " Saturday", "Sunday"]
mornings="morning","afternoon","evening"
morning_time= 0
#Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week.

for i in range (len( moods_types)):
    days=days_week[i]
while True >0:
        for morning in mornings:
            for days in days_week:
                for mood in moods_types:
                    for time in morning:
                        new_moods=random.choice(moods_types)
                        print(f'On', days, {morning}, "you were feeling",new_moods)
                        if time=="morning":
                            if days== days_week:
                                morning_time = 1
                                if morning_time== 1:
                                    print(f'On', days, {morning}, "you were feeling", new_moods)
                                    break
                                if morning_time== 1:
                                    continue
                                
           
 
     