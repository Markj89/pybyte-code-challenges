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
vowels = list(vowels)


def strip_vowels(text: str) -> (str, int):
    """Replace all vowels in the input text string by a star
        character (*).
        Return a tuple of (replaced_text, number_of_vowels_found)
        So if this function is called like:
        strip_vowels('hello world')
        ... it would return:
        ('h*ll* w*rld', 3)
        The str/int types in the function defintion above are part
        of Python's new type hinting:
        https://docs.python.org/3/library/typing.html"""

    # vars
    zen_list = list()
    
    words = ""

    # Initializing count variable to 0
    count = 0
    
    # Convert string to list
    text = list(text)
        
    # Lets makes some loops...
    for letter in text:
        bigvowels = 'AEIOU'
    
        # If vowel is present
        if letter in vowels or letter in bigvowels:
            
            # Pass the value
            letter = letter.replace(letter, "*")
            count += 1

        # Append to new string  
        zen_list.append(letter)
                       
        #number_of_vowels_found(zen_list)
          
    str = ''.join(zen_list)
    updated_str = (str, count)
    
    return updated_str
    
    pass