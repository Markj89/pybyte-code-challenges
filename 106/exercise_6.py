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

def strip_vowels(text=text):
    
    # vars
    zen_list = []
    count = 0
    
    # Convert string to list
    text = text.split("\n")
    
    # Lets makes some loops...
    for words in text:
        
        # Cont..
        for letter in words:
            
            # If vowel is present
            if letter in vowels:
                letter = letter.replace(letter, '*')
            
            # Append to new string    
            zen_list.append(letter)
            
    str = ''.join(zen_list) 
    return str
    
print(strip_vowels())
    
def count_vowels(updated_text):
    
    # Initializing count variable to 0
    count = 0
    while updated_text:
        count = count + 1
                              
    return count


##def strip_vowels(text: str) -> (str, int):
    ##"""Replace all vowels in the input text string by a star
    ##    character (*).
    ##    Return a tuple of (replaced_text, number_of_vowels_found)
        
    ##    So if this function is called like:
    ##    strip_vowels('hello world')

   ##... it would return:
   ##('h*ll* w*rld', 3)

   ##The str/int types in the function defintion above are part
   ##of Python's new type hinting:
   ##https://docs.python.org/3/library/typing.html"""
##pass