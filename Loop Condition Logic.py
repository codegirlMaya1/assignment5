#Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.
#Task 1: Loop Condition ExplorationWrite a while loop with a condition that will never be false (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.
love_meter=50

while love_meter > 0:
    
    print(f"The decreasing doubt meter is now at only {love_meter},% You have found a true love!")
    love_meter-=1
   
#Task 2: Conditional Exit Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. The loop should terminate naturally once the condition is met.
while love_meter>=1:
    
    break
print("Congrats! There is no more doubt! You truly found the right person!")




