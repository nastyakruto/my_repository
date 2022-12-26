def calculator(string):
    if '+' in string:
        a = string.index('+')
        s1 = string[:a]
        s1 = float(s1)
        s2 = string[a+1:]
        s2 = float(s2)
        return s1+s2
    elif '-' in string:
        a1 = string.index('-')
        d1 = string[:a1]
        d1 = float(d1)
        d2 = string[a1+1:]
        d2 = float(d2)
        return d1-d2
    elif '*' in string:
        a2 = string.index('*')
        m1 = string[:a2]
        m1 = float(m1)
        m2 = string[a2+1:]
        m2 = float(m2)
        return m1*m2
    elif ':' in string:
        a3 = string.index(':')
        de1 = string[:a3]
        de1 = float(de1)
        de2 = string[a3+1:]
        de2 = float(de2)
        return de1 / de2
    elif '!' in string:
        a4 = string.index('!')
        f = string[:a4]
        f = int(f)
        ans = 1
        for i in range(1, f+1):
            ans *= i
        return ans
n = input()
print(calculator(n))