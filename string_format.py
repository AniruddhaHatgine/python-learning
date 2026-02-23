name = "Miraj City"
name_upper_case = name.upper()    #All capital letters
name_lower_case = name.lower()   

# name.lower() -> assign value to new variable "name_lower_case " and print new variable

#print(name_upper_case)

#print(name.lower())   # all in lowercase direct print output

# print("Title", name.title()) # First Charater Capital of statement

#print("Capitalize", name.capitalize())  # All Capital statement

# print(name.swapcase())

#### Trimming and Cleaning
word = "  Learn   "

#user_input = input("Enter any text:")  # input() method accepts values or textfrom user in terminal

#print(word)
#print(word.strip())   # it removes spaces from both sides of text

#print("Right Space Removed:", word.rstrip())   # removes right side space

#print("Left Side Space Removed:",word.lstrip())   # removes left side space

### Searching and & Checking

bike = "Super Ninja R15 Minja"

#print(bike.find("p"))     # this is to find any text in given string

#print(bike.index("Ninja"))  # index is to get the position of that string 

#print(bike.count("j"))   # to get the count of give string or char/ letter

#print(bike.startswith("Mi"))  # this check that given string starts with provided text "Mi" -> False

#print(bike.startswith("Su"))  # True

print(bike.endswith("ja"))     # True