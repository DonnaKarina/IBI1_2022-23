#let the user input the stop codon
#use compile for several targets
#the first compile match the genes' names, the second compile match the stop code
#open the file and create a new file
#find the genes that ends with the sequence we want
#count the numbers of the codon and print out in a certain form
import re
codon = input('Stop condon:')
result1 = re.compile(r'>(\S+)')
result2 = re.compile('{}$'.format(codon))
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as gene, open('{}_stop_genes.fa'.format(codon), 'w') as op:
    for line in gene:
        if line.startswith('>'):
            new_result1 = result1.match(line).group()
            new_result2 = ''
        else:
            new_result2+=line.strip()
            if result2.search(new_result2):
                number = len(re.findall(codon, new_result2))
                op.write('{}:    {}\n{}\n\n'.format(new_result1, number, new_result2))
gene.close()
op.close()
