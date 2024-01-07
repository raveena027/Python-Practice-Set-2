'''Question 2: File Manipulation 
Write a Python script to read a text file, count the occurrences of each word, and display the result. '''

def word_count(str):
    
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

my_file = open("file.txt", mode = "r")
text = my_file.read()
print(text)
print( word_count(text))
