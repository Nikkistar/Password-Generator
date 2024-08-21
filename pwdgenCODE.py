#The strength of this program is that its uses a process which the user can easily 
#and generate a password which is hard to guess my others.
#The weakness of this code is that the numeric values that passwords 
#contain are repeating when generating a new one. This is because the number portray 
#index values and index values do not vary.

'''
Start
Ask for site name
Ask for site name length
Ask for name
Ask for name length

Rewrite site’s name as all CAPS

Replace even index places with 1 + index number

Take the sum of user name length and website name length

If the sum is double-digit:		
    split sum into two different digits

If sum is single digit:
    take sum as a digit
    take the number one less that the sum as another digit

Create and use dictionary to generate corresponding/designated special characters  

Add the characters to the starting and ending of the password

Take first letter of user’s name in lower case, add it to the end of the password
Take last letter of user’s name, add to beginning of the password

if length of password is greater than or equal to 8:
    Return the password

if length of password is less that 8:
    find by how much the password short
    ask user to input that many number (how much the password is less that eight) 
    of letters which they can remember
    add it to the password
    return the new password

'''
#Ask for user's name (Ex: Jasmine)
user_name = input("What is your name?")

#Ask for site's name (Ex: Instagram)
site_name = input("What is the site's name?")

#First step completed: Make the site name Uppercase (Ex: INSTAGRAM)
first_part = site_name.upper()

#Process for finding and replacing index places
firstlist = list(first_part)
index = 2
while (index <= len(first_part)-1):
    firstlist[index] = str(index + 1)
    index = index + 2
    
#Second step completed: Replace even index places with 1 + index number (Ex: IN3T5G7A9)
second_part = ''.join(firstlist)

#Take the sum of user name length and website name length (Ex: 7 + 9 = 12)
names_sum = len(user_name) + len(site_name)

#Split sum into two different digits for two digit sum values 
#(Ex: First digit = 1 Second Digit = 2)
if(names_sum >= 10):
    total_sum = str(names_sum)
    first_digit = total_sum[0]
    last_digit = total_sum[1]
    new_first_digit = int(first_digit)
    new_last_digit = int(last_digit)

# take sum as a digit, take the number one less that the sum as another digit
# if the sum is single digit
elif(names_sum < 10):
    total_sum = str(names_sum)
    first_digit = total_sum[0]
    last_digit = str(names_sum - 1)
    new_first_digit = int(first_digit)
    new_last_digit = int(last_digit)
    
#Create and use dictionary to generate corresponding/designated special characters  
designated_characters = {
  0: ")",
  1: "!",
  2: "@",
  3: "#",
  4: "$", 
  5: "%",    
  6: "^",    
  7: "&",    
  8: "*",    
  9: "(",    
}    

#Process for placing characters in password
def special_character (string,site):
    string_list = list(string)
    string_list[0] = designated_characters[new_first_digit]
    string_list[len(site)-1] = designated_characters[new_last_digit]
    return (''.join(string_list))    

#Third step completed: Add the characters to the starting and ending of the password
#(Ex: IN3T5G7A^)
third_part = special_character(second_part,site_name)

#Lowercased user's name (Ex:jasmine)
user_name = user_name.lower()

#Fourth step completed: Take first letter of user’s name in lower case, add it to 
#the end of the password. Take last letter of user’s name, add to beginning of the password
#(Ex: e!N3T5G7A^j)
fourth_part = user_name[len(user_name) - 1] + third_part + user_name[0]

#Final formation of output (Ex: Your Instagram Password: e!N3T5G7A^j)
final_output = "Your " + site_name + " Password: " + fourth_part

#password is greater than 8 characters (Your Instagram Password: e!N3T5G7A^j)
if(len(fourth_part) >= 8):
    print(final_output)

#password is less than 8 characters
else:
    length_needed = str(8 - len(fourth_part))
    letters = input("Your password is a bit short, please enter " + length_needed + " letters that are memorable to you")
    new_output = letters + fourth_part
    print(new_output)






