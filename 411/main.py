

def can_make_palindrome(sequence, deletions_left):
    reversed_sequence = sequence[::-1]
    s_lenght = len(sequence)
    for (index, (letter, letter_r)) in enumerate(zip(sequence, reversed_sequence)):
        if (letter != letter_r):
            if (deletions_left == 0):
                return False
            else:
                left_sequence = sequence[0:index]+sequence[index+1:]
                right_sequence = sequence[0:s_lenght-index-1]+sequence[s_lenght-index:]
                return can_make_palindrome(left_sequence, deletions_left - 1) or can_make_palindrome(right_sequence, deletions_left - 1)
    print(sequence)
    return True

print(can_make_palindrome("waterrfetawx", 2))