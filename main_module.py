import Gaurav as gv
#import #module2
#import #module3
import Deepam as da

filename='/Users/dmehta1/Documents/wiki.txt'
#file_object  = open('/Users/dmehta1/Documents/wiki.txt', 'r')
#for i in file_object:
    #print(i)
file_object  = open('/Users/dmehta1/Documents/wiki.txt', 'r')
filecont=file_object.read()

maxword=gv.MaxWordLen(filecont)
print(maxword)

wordcount=da.open_file(filename)
print(wordcount)
