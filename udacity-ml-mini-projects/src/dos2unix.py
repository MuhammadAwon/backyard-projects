#!/usr/bin/env python

original = './resources/enron/python2_lesson14_keys.pkl'
destination = './resources/enron/python2_lesson14_keys_unix.pkl'

content = ''
outsize = 0

with open(original, 'rb') as infile:
    content = infile.read()

with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content)-outsize))
