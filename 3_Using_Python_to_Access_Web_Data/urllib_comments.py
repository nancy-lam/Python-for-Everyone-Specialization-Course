#Scraping Numbers from HTML using BeautifulSoup.
#In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers in the file.
#Actual data: http://py4e-data.dr-chuck.net/comments_38796.html
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   # Look at the parts of a tag
 #  print 'TAG:',tag
  # print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs
#You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.


from urllib.request import urlopen
from bs4 import BeautifulSoup

fhand = urlopen('http://py4e-data.dr-chuck.net/comments_38796.html').read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('span')
list = []
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    list.append(int(tag.contents[0]))

print(f'The sum of the numbers in the file is {sum(list)}')




