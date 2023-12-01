with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

total = 0

# print ("part 1")
# for i in input:
#     nums = []
#     for c in i :
#          if c.isdigit():
#             print(c)
#             nums.append(c)
#     print(nums[0] + nums[-1])
#     total += int(nums[0] + nums[-1])
# 
# total = 0

print("part 2")

for i in input:
    nums = []
    for n in range (1, len(i)+1):
        if i[:n][-1].isdigit():
            #print(c)
            nums.append(i[:n][-1])
        if i[:n].endswith('one'):
             nums.append('1'),
        if i[:n].endswith('two'):
            nums.append('2')
        if i[:n].endswith('three'):
             nums.append('3'),
        if i[:n].endswith('four'):
            nums.append('4')
        if i[:n].endswith('five'):
             nums.append('5'),
        if i[:n].endswith('six'):
            nums.append('6')
        if i[:n].endswith('seven'):
             nums.append('7'),
        if i[:n].endswith('eight'):
            nums.append('8')
        if i[:n].endswith('nine'):
             nums.append('9'),
    print(i)
    print(nums[0] + nums[-1])
    total += int(nums[0] + nums[-1])
    #print(i)



print (total)