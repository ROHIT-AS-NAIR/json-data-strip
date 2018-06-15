import json
import os
from pprint import pprint
n = 11
nfirstlines = []
for aa in range(2000):
    with open(str( aa )) as f, open("temp", "w") as out:
	for x in xrange(n):
            nfirstlines.append(next(f))
        for line in f:
            out.write(line)

# NB : it seems that `os.rename()` complains on some systems
# if the destination file already exists.
    os.remove(str( aa ))
    os.rename("temp", str( aa ))
#2nd
    with open(str(aa)) as data_file:
        data_item = json.load(data_file)
    a=(data_item['data']['password'])
#print a
#print(data_item['data']['password'])

#3rd
    with open('f', 'a') as the_file:
        the_file.write(a+'\n')
