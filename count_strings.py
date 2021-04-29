#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#Date: 29 April 2021

"""
Write a Python program to count the number of strings where the string length is 2 or more 
	and the first and last character are same from a given list of strings
	
"""
my_list = ["abc", "aba", "cbc", "bbb", "alama", "656"] #list of strings 
count = 0 #count
for x in my_list: # loop through the items of the list
    if x[0] == x[-1]: # compare the first character with the last character
        count = count + 1 # add one to count
        
print("Number of strings with first and last character the same is:  ", count)