def banner(text, ch='=', length=64):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner

i = 0
s1 = 'Hello JAVA!'
while True:
    print (banner(s1)+'\n')
    if len(s1) == i:
        break;
    s1 = s1[-1] + s1[:len(s1)-1]
    i = i + 1
