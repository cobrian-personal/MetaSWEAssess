import requests
from bs4 import BeautifulSoup

url = "https://gentoo.osuosl.org/distfiles/"

todive = set() #hrefs to dive
todive.add("")

files = set()

def dive(url, extension):
    url = url + extension
    r = requests.get(url)
    print("diving for {}".format(url))
    print(r)

    soup = BeautifulSoup(r.content, "html.parser")

    content = soup.find_all('tr')

    for val in content[3:len(content)-2]: #ditch unneeded header and footer on table
        if len(val.findChildren('td')) == 5:
            temp = val.findChildren('td') #find row items, check tag on image, if dir add to dive list, else add to printlist
            alt = temp[0].findChild('img')['alt']

            if alt == "[DIR]":
                todive.add(temp[1].findChild('a')['href'])
                continue
            else:
                files.add(temp[1].findChild('a')['href'])

    print("{} files found and {} directories to dive".format(len(files), len(todive)))

while len(todive) > 0: #simple queue to know when we are done 
    dir = todive.pop()
    dive(url,dir)

for file in files:
    print(file)

#In a real world scenario I would multithread this to make it execute much faster, but I will stop here
#for simplicity 