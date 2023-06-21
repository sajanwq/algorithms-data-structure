#returns the index posistion of value if found else returns none
# def linear_search(list,target):
#     for i in range(0, len(list)):
#         if list[i] == target:
#             return i
#     return None


# def verify(index):
#     if index is not None:
#         print("Target value is found at index:",index)
#     else:
#         print("The target value is not found!")

# num = [1,2,3,4,5,6,7,8,9,10]

# result =linear_search(num, 12)
# verify(result)

# result =linear_search(num, 10)
# verify(result)

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
    
def verify(index):
    if index is not None:
        print("The target is found at", index)
    else:
        print("The target value is not found") 
list = [1,2,5,6,8,9]
result = linear_search(list, 9)
verify(result)

   

