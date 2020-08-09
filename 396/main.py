
value = "MAPTPTMTPA"

def find_longes_sequence2(sequence):
    sequences = []
    for i in range(len(sequence)):
        first_letter = sequence[i]
        for j in range(len(sequence) - 1, i, -1):
            last_letter = sequence[j]
            if (first_letter == last_letter):
                sequences.append(sequence[i:j+1])
    longest_s = None
    s_len = -1
    for s in sequences:
        s_rev = s[::-1]
        count = 0
        for l, l_r in zip(s, s_rev):
            if (l != l_r):
                count += 1
        if(len(s) - count > s_len):
            s_len = len(s) - count
            longest_s = s
    
    return check_sequence(longest_s)
    
    


def check_sequence(sequence):  
    letter_map = {}
    for letter in sequence:
        if (letter in letter_map):
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    first_index = 0
    last_index = len(sequence) - 1
    while first_index <= last_index:
        first_letter = sequence[first_index]
        last_letter = sequence[last_index]

        if(first_letter == last_letter):
            first_index += 1
            last_index -= 1
            continue

        pos1 = ""
        pos2 = ""
        
        if (letter_map[first_letter] % 2 == 1):
            alt1 = sequence[:first_index] + sequence[first_index+1:]
            alt1_rev = alt1[::-1]
            if (alt1 == alt1_rev):
                pos1 = alt1
            else:
                pos1 = check_sequence(alt1)

        if (letter_map[last_letter] % 2 == 1):
            alt2 = sequence[:last_index] + sequence[last_index+1:]
            alt2_rev = alt2[::-1]
            if (alt2 == alt2_rev):
                pos2 = alt2
            else:
                pos2 = check_sequence(alt2)
        
        if (len(pos1) == len(pos2)):
            return pos1
        elif (len(pos1) > len(pos2)):
            return pos1
        elif (len(pos2) > len(pos1)):
            return pos2
        else:
            return ""
    
    return ""

        


print(find_longes_sequence2(value))