user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']

def find_longest_common_sequence(sequence1, sequence2):
    longest_sequence_length = -1
    longest_sequence = None

    def find_indices_of_word_in_sequence(sequence, word):
        return [i for i, val in enumerate(sequence) if val == word]

    for index, word in enumerate(sequence1):
        occurences_of_word_in_other_sequence = find_indices_of_word_in_sequence(sequence2, word)
        for occurence in occurences_of_word_in_other_sequence:
            common_sequence = []
            s1_index = index
            s2_index = occurence
            while True:
                if (s1_index >= len(sequence1) or s2_index >= len(sequence2)):
                    if (len(common_sequence) > longest_sequence_length):           
                        longest_sequence_length = len(common_sequence)
                        longest_sequence = common_sequence
                    break
                s1_val = sequence1[s1_index]
                s2_val = sequence2[s2_index]
                if (s1_val == s2_val):
                    common_sequence.append(s1_val)
                    s1_index += 1
                    s2_index += 1
                else:
                    if (len(common_sequence) > longest_sequence_length):           
                        longest_sequence_length = len(common_sequence)
                        longest_sequence = common_sequence
                    break
    return longest_sequence

print(find_longest_common_sequence(user1, user2))
