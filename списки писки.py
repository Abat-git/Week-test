#nums= [4, 1, 3, 4, 5,7,True,'hello', [5, 6]]

#nums[0]=8
#nums [6]= False
#print(nums[-1][0])


#numbers= [5, 6, 7, 9]
#numbers=[3]=100
#numbers.append(100)
#numbers.insert(1,True)

#b =[8,9,0]
#numbers.extend(b)
#numbers.reverse()
#numbers.sort()
#numbers.pop(1)
#numbers.remove(6)
#numbers.clear()

#print(numbers.count(True))
#print(len(numbers))



#nums= [5, 3, 3, 5,5,6,2]

#for el in nums:
 #   el*=2
  #  print(el)



n= int(input("Enter length of number: "))

user_list=[]

i=0
while i<n:
    string= "Enter number: "+ str(i+1)+":"
    user_list.append(input (string))
    i+=1
print(user_list)
