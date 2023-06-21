# Write a Python program to create an empty dictionary and add key-value pairs to it.
# x = {}
# x["brand"] = "mercedes"
# x["model"] = "benz"
# x["year"] = "20001"
# thisDict = x.copy()
# print(thisDict)

# Write a program to iterate over a dictionary and print all keys and their corresponding values.
# for i in thisDict:
#     print(i, thisDict[i])

# for x,y in thisDict.items():
#     print(x, y)

# write a program if key exists in dictionary
# if "model" in thisDict:
#     print("yes the key is present")

# else:
#     print("No, the key is not present in the dictionary")

# wap to get specific value of a given dictionary
# print(thisDict["year"])
# res = thisDict.get("model")
# print(res)

# wap to update specific value in dictionary
# thisDict.update({"brand":"toyota"})
# print(thisDict)
# thisDict["model"] ="landCruizer"

# wap program to remove key from the dictionary
# thisDict.pop("model")
# print(thisDict)

# wap to sort a dictionary by its keys
# my_dict =[]
# new_dict ={}
# for i in thisDict:
#     my_dict.append(i)
# my_dict.sort(reverse=True)
# for i in my_dict:
#     new_dict.update({i:thisDict[i]})
# print(new_dict)


#Write a program to concatenate two dictionaries.

# x = {1:"sajan",
#      2:"pahim",
#      3:"limbu",}
# y = {4:"rajan",
#      5:"kumar",
#      6:"subba"}

# x.update(y)
# print(x)

# write a program to find the lenght of dictionary

# x = {1:"sajan",
#      2:"pahim",
#      3:"limbu",}
# print(len(x))

#Write a program to find the sum of all values in a dictionary.
# thisDict= {1:23,2:30, 3:40,4:"sajan"}
# c = 0
# d =0
# for i in thisDict.values():
#     if  not isinstance(i, str):
#         c+=i
#     else:
#         d+=1   
# print("The sum of of all integer values except "+str(d)+" non  integer values is",c)
## wap to find the maximum and minimum value in a dictionary.
# thisDict= {1:23,2:30, 3:40}
# mydict = thisDict.values()
# print(mydict)
# max_value =max(thisDict.values())
# min_value = min(thisDict.values())
# print(max_value)
# print(min_value)