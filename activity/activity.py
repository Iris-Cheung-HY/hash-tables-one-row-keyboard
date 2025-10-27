def typing_time(layout, word):
    positions = {letter: pos for pos, letter in enumerate(layout)}
    location = 0
    typed_time = 0
    
    for letter in word:
        next_loc = positions[letter]
        time = abs(next_loc - location)
        typed_time += time
        location = next_loc
    return typed_time


#Inefficient Version
    
    # curr_pos = 0
    # total_time = 0

    # for letter in word:
    #     letter_pos = 0
    #     for key in layout:
    #         if key == letter:
    #             break
    #         letter_pos += 1
    #     time = abs(letter_pos - curr_pos)
    #     total_time += time
    #     curr_pos = letter_pos
    # return total_time
    
# skipping error handling
# empty keys? empty word? repeated letters in keys?

