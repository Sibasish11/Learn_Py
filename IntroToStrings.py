
# Single line comment
letter = 'S'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I like how things are going in my life."
print(sentence)

# Multiline String
multiline_string = '''Leo messi is the best footballer of all time.
He made football look so simple yet magical.
He truely is a man worth idolising.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """Leo messi is the best footballer of all time.
He made football look so simple yet magical.
He truely is a man worth idolising."""
print(multiline_string)

# String Concatenation
first_name = 'Sibasish'
last_name = 'Padhihari'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Sibasish Padhihari
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 9
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 17

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

print(challenge.startswith('thirty')) # False
