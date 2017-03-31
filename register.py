import pypandoc
import os

output = pypandoc.convert('README.md', 'rst')
f = open('README.txt','w+')
f.write(output)
f.close()