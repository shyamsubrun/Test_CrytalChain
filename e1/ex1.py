def entryTime(s, keypad):

    digit_to_pos = {}       #dico   
    for i in range(0,len(keypad)-1):      #jusqua 9 nb caracteres
        digit = keypad[i]         
        digit_to_pos[digit] = (i // 3, i % 3) #tuple deplacer et appuyer

    
    total_time = 0
    cur_pos = digit_to_pos[s[1]] # on stocke le premiere element
    
    for i in range(1, len(s)):
        digit = s[i]
        next_pos = digit_to_pos[digit]

        time = abs(next_pos[0] - cur_pos[0]) + abs(next_pos[1] - cur_pos[1])#case0+curseur pos0+curseur pos1+curseur pos1

        total_time += time
        cur_pos = next_pos #curseur prend la postion du curseur suivant

    return total_time

s = "423692"
keypad = "923857614"
result = entryTime(s, keypad)
print(result)  # devrait afficher 8
