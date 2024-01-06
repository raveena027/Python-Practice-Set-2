'''Question 6: Reverse String 
Write a Python function that takes a sentence as input and returns the sentence with reversed words'''

def reverse_sentence(sentence): 

    words = sentence.split(' ') 
 
    reverse_sentence = ' '.join(reversed(words)) 

    return reverse_sentence 


input = 'Python Training 2023 by Vimal Daga'
print (reverse_sentence(input)) 
