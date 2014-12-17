#you have to replace the key sections with your own access keys, of course
#find a list of around 1000 book titles to search, get the isbndb data for each of them, then use that data to query goodreads
#then save into a .csv file there levant info including the rating and the number of ratings for each book, in a row
#see https://www.goodreads.com/topic/show/776821-get-review-statistics-given-a-list-of-isbns for more advice

import urllib2
import xml.etree.ElementTree as ET
import time
import json
import requests
from pprint import pprint
import csv

#goodreadsAPIinfo
key=
#secret=

#isbndbapiinfo
key=
#data to get from isbndb = isbn, author, year published

with open("1001_novels.txt","rb") as f:
	list_of_novel_data=f.readlines()

list_of_books=[]	
for line in list_of_novel_data:
	words=line.split("by")
	list_of_books.append(words[0])
    
book_data_LoL=[ []for book in list_of_novel_data]

#might want to also try to get author or publisher data from the book
isbndb_data = [ [] for book in list_of_novel_data]
isbn13_string="9780590353427"
i=0
for book in list_of_books:
    book_title=book.rstrip().replace(" ","+").replace(",","").replace("?","").replace("'","")
    print book_title
    response=urllib2.urlopen(str("http://www.isbndb.com/api/books.xml?access_key=&index1=title&value1="+book_title))
    xml = response.read()
    root = ET.fromstring(xml)
    if i<1001:
        for child in root: 
            j = 0
            for child2 in child: 
                isbn = child2.attrib['isbn13'] 
                isbn13 = "," + str(isbn)
                if j == 0: 
                    isbn13_string += isbn13
                    isbndb_data[i].append(book.rstrip().replace(",","").replace("?","").replace("'",""))
                    isbndb_data[i].append(isbn13)
                else: 
                    break
                j += 1
    else: 
        break
    time.sleep(2)
    i+=1


print isbndb_data
print isbn13_string


#http://www.goodreads.com/book/review_counts.json?isbns=9780590353427&9780582210202&9788426572363&key=
u=("http://www.goodreads.com/book/review_counts.json?isbns=" + isbn13_string + "&key=")

#Take the goodreads json, spit out back the isbn13, the ratings count, and the rating

data = json.loads(requests.get(u).text)

print type(data['books'])
print data['books']
i = 0 
for book in data['books']:
    print type(book_data_LoL[i])
    book_data_LoL[i].append(book['isbn13'])
    book_data_LoL[i].append(book['work_ratings_count'])
    book_data_LoL[i].append(book['average_rating'])
    i += 1

with open("output_title_isbn1.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(isbndb_data)

with open("output_goodreads_isbn1.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(book_data_LoL)

