

def fn(s, k):

    subs = []

    intervals = [x for x in range(0, len(s), k)]

    for i in intervals:

        _s = ''
        for letter in s[i:i+k]:
            if letter not in _s:
                _s = _s + letter

        subs.append(_s)

    return subs    

        
a = 'AAABCADDE'

fn(a, 3)
