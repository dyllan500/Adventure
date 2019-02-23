# def count_substring(string, sub_string):
#     counts = 0
#     num = len(sub_string)
#     n = len(string)
#     x = 0
#     while x < len(string):
#         sub = string[x:num]
#         if sub == sub_string:
#             counts+=1
#         x+=1
#         num+=1
#     return counts
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
import sys

nums = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums.append(n)
ar = []
x = 0
print(ar)
sum = 0
while x < t:
    w = nums[x]-1
    while w > 0:
        if w % 5 == 0 or w%3 == 0:
            sum = sum + w
        w-=1
    ar.append(sum)
    x+=1
    sum = 0
for i in ar:
    print(i)