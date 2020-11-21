import re

mystr = '''Sanjay Gandhi’s role as a politician was short lived due to his premature death. Nonetheless, he made his presence felt on Indian political horizon in a very short span of time. 

The ‘controversial Gandhi’ had his political career full of storms and arguments primarily on account of his tough and brash attitude. Sanjay Gandhi was the youngest son of Indira and Feroze Gandhi. 
12235-12234
He was born on 14th December, 1946 and is said to be his mother’s favorite son. Rajiv Gandhi was Sanjay Gandhi’s elder brother.

Today on his death anniversary, let’s have a look at his personal life and political journeyiiiiiiiiiiiiiiiiiiii.
'''
# patt = re.compile(r'role')
# patt = re.compile(r'He')
# patt = re.compile(r'journey.$')
# patt = re.compile(r'i{3}')
# patt = re.compile(r'\Aon')
patt = re.compile(r'\d{5}-\d{1}')
matches = patt.finditer(mystr)

for match in matches:
    print(match)

