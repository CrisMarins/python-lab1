str=input("Write what you want to cut ")

#looking for the lenght of the string
len = len(str)

if len<2:
    print("")
else:
    print("{}".format(str[0]+str[1]+str[len-2]+str[len-1]))

"""lenght=0
for char in str:
    lenght=lenght+1
    
"""