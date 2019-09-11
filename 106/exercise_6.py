text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'    

def number_of_vowels_found(updated_text):
    
    # Initializing count variable to 0
    count = 0
    
    for updated_word in updated_text:
        if '*' in updated_word:                
                
            # Lets count it up!
            count += 1
                              
    return count


def replaced_text(text=text):
    
    # vars
    zen_list = []
    
    # Convert string to list
    text = text.split('\n')
    
    # Lets makes some loops...
    for words in text:
        
        # Cont..
        for letter in words:
            
            # If vowel is present
            if letter in vowels:
                    
                # Pass the value
                letter = letter.replace(letter, '*')

            # Append to new string    
            zen_list.append(letter)            
        number_of_vowels_found(zen_list)    
    str = ''.join(zen_list)
    return str
    
str = ( replaced_text(), number_of_vowels_found(replaced_text()) )

def strip_vowels(str=str):
    return str
    
print(strip_vowels())