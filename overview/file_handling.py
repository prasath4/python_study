# file_Path= r"C:\Users\lenovo\Desktop\workspace\Python\File.txt"

# f= open (file_Path,'r')
# txt= f.read()
# print(type(txt))
# print(txt)
# f.close()

# read= f.readlines()
# read=f.readline()


# Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])




# Changing Dictionary to JSON
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)




#python Web Scrapping

# requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)

import requests

url = 'https://ihatereading.in/'

response = requests.get(url)

print('STATUS CODE:',response.status_code)
print(response.json)



"""
import requests
from bs4 import BeautifulSoup
url = 'https://ihatereading.in/'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful
"""




import requests
from bs4 import BeautifulSoup
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.text) # <title>UCI Machine Learning Repository: Data Sets</title>
# print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)