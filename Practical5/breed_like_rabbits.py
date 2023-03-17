#start with the first generation and the two rabbits
#use 'while' to ensure the rabbit number is less than 100
#each couple will pruduce two rabbits, so the number will double each generation
#at last print the result
generation=1
rabbit=2
while rabbit<100:
  rabbit=rabbit*2
  generation+=1
print('In the generation %d'%(generation)+' the water bottle will run out')
#learn from https://blog.csdn.net/weixin_69553582/article/details/125403845, where taught me how to use print()
