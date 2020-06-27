#Foram Gandhi
#MadLib

import random

n = []
v = []

random_verb=open('verbs.txt','r')                           
verb=random_verb.readlines()

for s in verb:
    v.append(s.replace('\n', ''))
random_choice=random.choice(v)

random_noun=open('nouns.txt','r')                           
noun=random_noun.readlines()

for s in noun:
    n.append(s.replace('\n', ''))
random_choice1=random.choice(n)

textToSearch="#"                                        
textToSearch1="%"                                         

phrase=''                                                   
story=open('story1.txt', 'r')
contents=story.readlines()
for ele in contents:
    phrase=phrase+ele                                       

random_verb.close()                                         
random_noun.close()                                     
story.close()

phrase1=phrase.replace(textToSearch1,random_choice)        
phrase2=phrase1.replace(textToSearch,random_choice1, 1)      
phrase3=phrase2.replace(textToSearch,random_choice1, 1)
print(phrase3)                                              
