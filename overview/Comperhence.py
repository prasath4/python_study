# List comperhence

value = 'Malayalam'

# ls=[i for i in value]
# print(ls)


ls=[i for i in range(1,10,2)]
# print(ls)

ls= [(i, i*i) for i in range(10)]
# print(ls)

ls= [i for i in range(10) if i % 2 == 0]
# print(ls)


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

ls=[i for i in numbers if i >= 0]
# print(ls)



list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flater_lists=[numbers for sub_list in list_of_lists for row in sub_list for numbers in row]
# print(flater_lists)

table=[(n,1)+tuple(n ** i for i in range(1,6)) for n in range(11)]
# print(table)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# ls=[list(word) for row in countries for word in row]
# print(ls)

ls=[[countries.upper(),countries[:3].upper(), capital.upper()] for row in countries for (countries, capital) in row]
# print(ls)



ls=[{'County':countries.upper(), 'City':capital.upper()} for row in countries for (countries, capital) in row]
# print(ls)



names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# ls=[first_name,last_name for sub_name in names for row in sub_name for (first_name+last_name) in row]
# print(ls)


filter_name=[" ".join(name) for row in names for name in row]
print(filter_name)