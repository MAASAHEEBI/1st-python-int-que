#1)Write an even length words in a string

def printWords():
   s = "i am muskan"
# split the string
   a = s.split(' ')

# iterate in words of string
   for word in a:

# if length is even
        if len(word)%2==0:
            print(word)


printWords()
