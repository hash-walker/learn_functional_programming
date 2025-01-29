def find_longest_word(document, longest_word=""):

    if (len(document) == 0 or document.strip() == ""):
        return ""

    if (len(document.split()[0]) > len(longest_word) ):
        longest_word = document.split()[0]
        

    result = find_longest_word(" ".join(document.split()[1:]), longest_word)

    if len(result) > len(longest_word):
        longest_word = result  

    return longest_word
    

    
    


