def which_prize(points):
    """
        function returns the prize depending on the points
    """
    if (points<=50):
        prize = "Congratulations! You have won a wooden rabbit!"
    elif (points<=150):
        prize = "Oh dear, no prize this time."
    elif (points<=180):
        prize = "Congratulations! You have won a wafer-thin mint!"
    elif (points<=200):
        prize = "Congratulations! You have won a penguin!"
    else:
        prize = "unknown"
    return prize
    
points = 12
print(which_prize(points))

points = 149
print(which_prize(points))

points = 164
print(which_prize(points))

points = 194
print(which_prize(points))