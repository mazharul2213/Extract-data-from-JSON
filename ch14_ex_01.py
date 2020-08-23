#Extract data from JSON
import urllib.request, urllib.parse, urllib.error
import json

lst = list()
count = 0

url = input("Enter location: ")
if len(url)<1:
    url = "http://py4e-data.dr-chuck.net/comments_643361.json"
print('Retrieving', url)

uh = urllib.request.urlopen(url)  # connect
data = uh.read()  # read
print('Retrieved', len(data), 'characters')  # check data qty

#tree = ET.fromstring(data)  # create a tree
info = json.loads(data)
for comment in info['comments']:
    #print(comment['count'])
    numb = lst.append(comment['count'])
    count = count + 1

print("Count: ", count)
print("Sum: ", sum(lst))
