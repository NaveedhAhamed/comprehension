nums = [1,2,3,4,5,6,7,8,9,10]


#i want 'n' for each 'n' in nums
my_list=[]
for n in nums:
     my_list.append(n)
print(my_list)


#another way to do this
my_list=[n for n in nums]
print(my_list)



#i want 'n*n' for each'n' in nums
my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)


#another way to do this 2nd one
my_list=[n*n for n in nums]
print(my_list)



#using a map + lambda
my_list = list(map(lambda n: n*n, nums))
print(my_list)



#i want 'n' for each 'n' in nums if 'n' is even
my_list=[]
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)



#another way for 2nd
my_list=[n for n in nums if n % 2 == 0]
print(my_list)


#i want a (letter , num) pait for each letter in abcd and each number in 1234
my_List=[]
for letter in 'abcd':
    for num in range (4):
        my_List.append((letter,num))
print(my_List)


#easy another way
my_List=[(letter,num) for letter in 'abcd' for num in range(4)]
print(my_List)


#another way but it works in order only(zip functioning)
letters=['a','b','c','d']
nums=[1,2,3,4]
print(list(zip(letters, nums)))



#extended zip way
my_dict={}
for letter,num in zip(letters,nums):
    my_dict[letter]=num
print(my_dict)

#print without peter
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}

print(my_dict)



#setting comprehension

# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

my_set = set()
for n in nums:
    my_set.add(n)

print(my_set)


#another way
my_set = {n for n in nums}
print(my_set)



#generator expressions

# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print(i)



#another way
my_gen = gen_func(nums)
for i in my_gen:
    print(i)
