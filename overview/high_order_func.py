# Accepting Parameters in Decorator Functions

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

# print_full_name("Asabeneh", "Yetayeh",'Finland')


#Decorator

def decorator_func(function):
    def wrapper_func():
        func=function()
        result = func.upper()
        return result
    return wrapper_func

@decorator_func
def greeting():
    return "hello guys!"
print(greeting())


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

for country in countries:
    print(country)


# Use map to create a new list by changing each country to uppercase in the countries list

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

mapping=map(lambda x: x.upper(),countries)
print(list(mapping))



# Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result=map(lambda x: x**2, numbers)
print(list(result))


# Use filter to filter out countries containing 'land'.

# result =filter(lambda x: x == "land",countries)
# print(list(result))

result = filter(lambda country: 'land' in country,countries)
print(list(result))


# Use filter to filter out countries having exactly six characters.

# x = filter(lambda country: country == 6,countries)
# print(list(x))

x = filter (lambda country: len(country) == 6, countries)
print(list(x))


# Use filter to filter out countries containing six letters and more in the country list.

y=filter(lambda country: len(country) >= 6,countries)
print(list(y))


# Use filter to filter out countries starting with an 'E'

result= filter(lambda country: country.startswith('E'),countries)
print(list(result))