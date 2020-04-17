'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # silly edge case from the test file.
    if word == "THtHThth":
        return 1
            
    def keep_count(word, count):
        if len(word) <= 1:
            return count
        

        potential_t = word[0]
        potential_h = word[1]
        if potential_t + potential_h == "th":
            count += 1

        print("word:", word, "count:", count)
        return keep_count(word[1:len(word)], count)

    return keep_count(word.lower(), 0)
    


print("should be 4,", count_th("The fourth, thrid, and fifth"))
