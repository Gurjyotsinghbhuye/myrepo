# check if string is symmettrical

str = 'katkat'

def is_symmetric(str):
    mid= len(str) //2
    # print(str[:1] ,str[-1:])  aggo di ek word and picho ek word
    return str[:mid] == str[-mid:]
        
print(is_symmetric(str))
        
# remove letters from a string in py
str1 = "remove123 letter5 4 you" 
str2 = ''
for ch in str1:
    if ch.isdigit():
        continue
    else:
        str2+=ch
print(str2)

# check if string contains substring 
strr= "Remove"
print(str1.find(strr.lower()))