#start with the first generation and the two rabbits
#each couple will pruduce two rabbits each generation, so the number will double per generation
#if the number of rabbits is less than 100,the generation will add 1
#use 'while' to ensure the rabbit number is less than 100
#at last print the result
#learn how to use 'print()' from https://blog.csdn.net/weixin_69553582/article/details/125403845
generation=1
rabbit=2
while rabbit<100:
  rabbit=rabbit*2
  generation+=1
print('In the generation %d'%(generation)+' the water bottle will run out')
