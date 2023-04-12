#Use re.compile to find more target
#\S fits everything except whitspace, $ means to search from the end
#open the file and create a new file
#cleave the line and only preserve the name of the gene
#upload the changes to ensure every name is only preserved onece
#put the name and the sequence into one line
#find out the sequences end with TGA and delete others
#print the result in the form I want
import re
result1 = re.compile(r'>(\S+)')
result2 = re.compile(r'TGA$')
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as gene, open('TGA_genes.fa', 'w') as TGA:
    for line in gene:
        if line.startswith('>'):
            new_result1 = result1.match(line).group()
            new_result2 = ''
        else:
            new_result2+=line.strip()
            if result2.search(new_result2):
                TGA.write('{}\n{}\n\n'.format(new_result1, new_result2))
gene.close()
TGA.close()
