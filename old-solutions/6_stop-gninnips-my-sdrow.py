def spin_words(sentence):
    
    if sentence != str(sentence):
        raise Exception("Input not a string")
        
    ans = ""
    
    for word in sentence.split(" "):
        if len(word) < 5:
            ans += word
        else:
            reversed = ""
            for i in range(len(word)-1, -1, -1):
                reversed += word[i]
            ans += reversed
        ans += " "
    
    return ans.strip()