"""month = ['January', 'February', 'March', 'April', 
         'May', 'June', 'July', 'August', 'September',
         'October', 'November', 'December']
entry = int(input())

print (month[entry-1])"""

month = int(input())

#chave:valor
months_dict = {
    1:'January', 2:'February', 3:'March', 4:'April', 
         5:'May', 6:'June', 7:'July', 8:'August', 9:'September',
         10:'October', 11:'November', 12:'December'}
print (months_dict[month])