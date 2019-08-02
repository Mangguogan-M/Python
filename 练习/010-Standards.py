def standards(s):
    t = '0'
    t = s.lower()
    t = t.capitalize()
    print(t)
    return t


print(list(map(standards, ['ADMAG','JACK', 'LISA'])))

print(map(standards, ['ADMAG','JACK', 'LISA']))
print(type(map(standards, ['ADMAG','JACK', 'LISA'])))