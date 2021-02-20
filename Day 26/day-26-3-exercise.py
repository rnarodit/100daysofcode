
numbers1=[]
numbers2=[]

with open ("Day 26/file1.txt" ) as numbers:
    numbers1 = numbers.readlines()

with open ("Day 26/file2.txt" ) as numbers:
    numbers2 = numbers.readlines()

result = [int(n) for n in numbers1 if n in numbers2]
# Write your code above 👆

print(result)


