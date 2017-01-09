# put your code here.
import sys

file_open = open(sys.argv[1])

# word_count = {}

from collections import Counter

whole_text = file_open.read()


lines_list = whole_text.split("\n")
whole_text_clean = " ".join(lines_list)
words = whole_text_clean.split(" ")

for i in range(len(words)):
    # word = words[i]
    word = words[i].lower()
    if not word[-1:].isalpha():
        words[i] = word[:-1]
    else:
        words[i] = word

c = Counter(words)

for word, count in c.iteritems():
    #print "%r %r" % (word, count)
    print word + " " + str(count)

# for line in file_open:
#     line = line.rstrip()
#     words = line.split(" ")
#     for word in words:
#         word = word.lower()
#         if not word[-1:].isalpha():
#             word = word[:-1]
#         word_count[word] = word_count.get(word, 0) + 1

# for word, count in word_count.iteritems():
#     #print "%r %r" % (word, count)
#     print word + " " + str(count)
