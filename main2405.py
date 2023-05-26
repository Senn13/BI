# Name: Huynh Thanh Vu - GCS210232
# Class: GCS1003A

#Ex 1: 

# User input
name = input("Type your name: ")
age = int(input("Type your age: "))
entrance = int(input("Type your entrance: "))

#Calculate
year = 2023 - entrance

#Print function
def info(name, age, year):
    print("Your name is", name, ", you are", age, "years old, you are", year, "year student at Greenwich.")

#Run
info(name, age, year)

#Ex 2: 

# Input
text = input("Type your text: ")
order = int(input("Type order: "))
word_replace = input("Type your replace word: ")

# Color code
color_default = "\033[0m"
color_red = "\033[1;31;40m"

print("---------------------------------")

# Calculate original text length
original_text = text.split()
original_text_length = len(original_text)

# Print original text
print("Original text:", text)
print("Length of original text:", original_text_length)

print("---------------------------------")

# Modified text function
def change_text(text, order, word_replace):
    text[order-1] = word_replace
    return " ".join(text)

# Modified text
modified_text = change_text(original_text, order, word_replace)
a = modified_text.replace(original_text[order-1], f"{color_red}{word_replace}{color_default}")
modified_text_length = len(modified_text.split())

# Print modified text
print("Modified text:", a)
print("Length of modified text: ", modified_text_length)

