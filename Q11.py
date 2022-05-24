# part-1
def break_into_words(sentence):
    b=sentence.split()
    return b
    # list_Of_words=list(sentence)
    # return list_Of_words
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
a=break_into_words(sentence)

print(a)

# part-2
words = "navgurukul is great"
counter = 0
while counter < len(words):
    print (words[counter])
    counter+=1