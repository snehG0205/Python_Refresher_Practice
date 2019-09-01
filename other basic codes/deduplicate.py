 # Define the remove_duplicates function
def remove_duplicates(list):
    output = []
    for value in list:
        if value not in output:
            output.append(value)
    return output
    
in_list = [5,2,3,5,7,8,7,6,3,2,2,1,2,0,0,9,8,1]
print ("Input List -")
print (in_list)
print ("Input List Lenth")
print (len(in_list))

out_list = remove_duplicates(in_list)
print ("Output List -")
print (out_list)
print ("Output List Lenth")
print (len(out_list))