
#Strip method removes white space
a = 'hello world'
# print(a.strip())

#lower() method returns the string in lower case
print(a.lower())
# # # #
#upper() method returns the string in upper case
print(a.upper())
#
# # ##replace() method replaces a string with another string
print('replace',a.replace("hel", "Hik"))
#

b ='kushal Bhavsar'
print(b.split("a"))
#

# #The capitalize() function returns a string with first letter capitalized and all other characters lowercased. It doesn't modify the original string.
string = "hello .woRlD"
capitalized_string = string.capitalize()
print('Old String: ', string)
print('Capitalized String:',     capitalized_string)

#The swapcase() method returns the string where all uppercase characters are converted to lowercase, and lowercase characters are converted to uppercase
print(string.swapcase())