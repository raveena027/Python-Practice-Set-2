'''Question 3: String Formatting
Write a Python function that takes a sentence as input and returns the number of words in it.  '''

def count_words(sentence):
    words = sentence.split()  
    return len(words) 

input_sentence = "This is a sample sentence."
result = count_words(input_sentence)

print(f"Number of words in the sentence: {result}")
