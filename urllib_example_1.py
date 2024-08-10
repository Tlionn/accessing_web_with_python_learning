"""
This is a simple program that uses urllib library to get the contents present in a URL and print it out.
There is some additional code to count the number of times a word occurs in the conent obtained.  
"""

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}

print("Here is the content obtained from the URL:")
for line in fhand:
    line = line.decode() #Content obtained is UTF-8 encoded (that's the usual assumption) and is in bytes format, so decoding needs to be done.
    print(line.strip()) 
    words = line.split() 
    for word in words:
        counts[word] = counts.get(word,0) + 1 #add to the count of a word if it is present in the dictionary, else create a ew entry with a count of 1

print("Here are the counts of the different words:\n",counts)
