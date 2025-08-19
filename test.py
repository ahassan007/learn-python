def reverse_words(text):
    result = ''
    word = ''
    
    for char in text:
        if char != ' ':
            word += char
        else:
            result += word[::-1] + ' '
            word = ''
    
    # Add the last word (no space after it)
    #result += word[::-1]
    
    return result


reverse_words = reverse_words("Hello World")
print(reverse_words)  # Output: "olleH dlroW"



def maskify(cc):
    last_four = cc[-4:]
    masked_cc = ''
    temp_cc = ''
    for char in cc:
        char == '#'
        temp_cc += char
    return temp_cc + last_four

print(maskify('123456'))