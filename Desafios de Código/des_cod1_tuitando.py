#O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
# Conferir se um texto vai caber em um tuíte é sua tarefa.
T= input()
count = 0

for i in T:
     count += 1
     
if count > 140:
     print ('MUTE')
else:
     print ('TWEET')