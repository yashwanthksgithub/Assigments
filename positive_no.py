#TO LIST THE RANGE OF POSITIVE NUMBERS
'''start=int(input("Enter the starting number :\n"))
end=int(input("Enter the ending number :\n"))

print("Positive numbers are :")
for i in range(start,end+1):
    print(i)

print("Done")'''

list1 = [12, -7, 5, 64, -14]

#TO PRINT THE NUMBERS : 

for num in list1:
    if num >= 0:
       print(num, end = ",")


#TO PRINT AS LIST:

print("\nthe number in the list\n")
list2= [i for i in list1 if i>= 0] 
print(list2)
