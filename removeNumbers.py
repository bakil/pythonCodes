def remove_number(text):
    text_without_no = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character not in '0123456789':    #that's a single space
            text_without_no = text_without_no + next_character
        text = text[1:]
    return text_without_no
print remove_number("hello 145321 my name is andy how are you?")