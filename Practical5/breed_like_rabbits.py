#star with the first generation and the two rabbits
generation=1
rabbit=2
while rabbit<100:
#to ensure the rabbit number is less than 100
#each couple will pruduce two rabbits, so the number will double each generation
  rabbit=rabbit*2
  generation+=1
print(generation)
