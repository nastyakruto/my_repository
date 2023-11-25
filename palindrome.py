def is_palindrome(s):
    l = len(s) 
    k = l - 1
    i = 0
    for q in range(l):
        print(ord(s[q]))
        if ord(s[q]) in range(32,65) or ord(s[q]) in range(91,97) or ord(s[q]) in range(123,127):
            s.replace(s[q], '')
    print(s)
    while i < l and k >= 0:
        if s[i].lower() == s[k].lower():
            k -= 1
            i += 1
        else:
            return False
    return True    
s = 'a!a'
print(is_palindrome(s))