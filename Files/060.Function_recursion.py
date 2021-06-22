# --------------------------
# --- Function recursion ---
# --------------------------
# -----------------------------------------------------------------------
# --- To understand recursion, you need first to understand recursion ---
# -----------------------------------------------------------------------

# Test word ( WWWoooorrrldd )   # print(x[1:])

def clean_word(word) :

    if len(word) == 1 :

        return word
    
    print(f"Print start function {word}")

    if word[0] == word[1] : 

        print(f"Print before condition {word}")

        return clean_word(word[1:])

    print(f"Print before return {word}")

    return word[0] + clean_word(word[1:])

    # Stash ( World ) 

print(clean_word("WWWoooorrrldd"))
