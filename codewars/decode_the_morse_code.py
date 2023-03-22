def decode_morse(morse_code):
    words = morse_code.split("  ")
    letters = []
    for word in words:
        letters.append(word.split(" "))
    print(words)
    print(letters)

#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


decode_morse('.... . -.--   .--- ..- -.. .')