def checkioMy(text):
    lst = [0] * 26
    for i in range(len(text)):
        k = text[i].lower()
        if k < 'a' or k > 'z':
            continue
        lst[ord(k)-ord('a')] += 1
    return chr(ord('a') + lst.index(max(lst)))
	
def checkio1(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
	
checkio2 = lambda text: max(string.ascii_lowercase, key=text.lower().count)


def checkio3(text):
	from collections import Counter
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]
	
def checkio4(text):
	import collections
    freq_list = collections.Counter(filter(str.isalpha, text.lower())).most_common()
    most_freq_count = max(freq[1] for freq in freq_list)
    return sorted([freq[0] for freq in freq_list if freq[1] == most_freq_count])[0]

def checkio5(text):
    s = list(text.lower())
    letters = [s.count(chr(x)) for x in range(97,123)]
    
    return chr(97+letters.index(max(letters)))	
	
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
	assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")