# put your code here.
import sys

file_open = open(sys.argv[1])

word_count = {}

for line in file_open:
    line = line.rstrip()
    words = line.split(" ")
    for word in words:
        word = word.lower()
        if not word[-1:].isalpha():
            word = word[:-1]
        word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.iteritems():
    #print "%r %r" % (word, count)
    print word + " " + str(count)


