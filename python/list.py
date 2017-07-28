groceries = ["milk","butter", "eggs", "bacon", "bread"]


print range(0,10)


for i in range(0,len(groceries)):
    print groceries[i]


#going thru list, if don't need index
for item in groceries:
    print item

#went thru index
number = [4,3,2,1]
for i in range(0,len(number)):
    print number[i]* 2

# or

#new_list = []
#for num in numbers:
    #num = num * 2
    #new_list.append(num)
#print new_list


#reverse
# this goes thru elements, range = index
reverse_num = []
for i in number:
    i = number[len(number)-i]
    reverse_num.append(i)
print


#or

reverse_num = []
for index in range(0,len(number)):
    val = number[len(number)-1-ndx]
    reverse_num.append(val)
print reverse_num
