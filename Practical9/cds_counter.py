#input the sequence of the DNA
#count the number of TGA and TAA
#add them together and get the number of possible coding sequences
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
a=seq.count('TGA')
b=seq.count('TAA')
number=a+b
print(number)
