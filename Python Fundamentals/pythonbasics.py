# Variables in Python

first_name = 'Sibasish'
last_name = 'Padhihari'
country = 'India'
city = 'Bhubaneshwar'
age = 20
is_married = False
skills = ['HTML', 'CSS', 'JS', 'SQL', 'Python']
person_info = {
    'firstname':'Sibasish', 
    'lastname':'Padhihari', 
    'country':'India',
    'city':'Bhubaneshwar'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Sibasish', 'Padhihari', 'Bhubaneshwar', 20, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
