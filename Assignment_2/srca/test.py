'''
Created on Sep 20, 2016

@author: sonaje_a
'''
#!/usr/bin/python
import collections
d =collections.defaultdict(str)
d = {'Name': 'Zabra', 'Age': 7}
if(d.get('lol') == ''):
    print (d.get('lol'))
else:
    print(d.get('Age'))
