# Write your code for readable_timedelta here.

def readable_timedelta(days):
    """
    funtion to calculate the weeks and days of the given number 
    of days
    """
    
    weeks=days//7;
    left_days=days%7
    msg = "{} week(s) and {} day(s)".format(weeks,left_days)
    return msg

# Uncomment this function call to test it:
print(readable_timedelta(2739))

