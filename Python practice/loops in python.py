#For Loop in strings

name = 'NoobMaster69'
print(len(name))

#PLay with strings 
#If you want to print 4 characters from start then stepping you should 
for i in range(0,len(name),4):
    print(name[i:i+4])

#If you want to print 4 characters from start until ending 
for i in range(0,len(name),4):
    print(name[:i+4])

name = 'NoobMaster72' #new string is created here  you can check the address of first 
#index of both the string it should be different
print(name)