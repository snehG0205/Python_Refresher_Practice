def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    input_list = sorted(input_list, reverse=True)
    if len(input_list)<=3:
        return input_list
    return (input_list[0:3])
    
    
    
    
    
    
maxThree = top_three([2,3,5,6,8,4,2,1])
print (maxThree)