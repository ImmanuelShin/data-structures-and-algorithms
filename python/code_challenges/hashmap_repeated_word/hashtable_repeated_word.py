from code_challenges.hashtable.hashtable import Hashtable
import re

def first_repeated_word(str):
    ht = Hashtable()

    for word in re.sub(r"[^A-Za-z0-9 ]+", '', str).split():
        if ht.has(word.lower()):
            if ht.get(word.lower()) > 0:
                return word.lower()
        else:
            ht.set(word.lower(), 1)