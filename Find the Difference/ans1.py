s = 'abcd'
t = 'abcde'

ss = list(s)
tt = list(t)
cc = ' '

for e in tt:
    if s.count(e) != t.count(e):
        cc = e

print cc