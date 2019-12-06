#
# for n in range (5, 18, 3):
#     print(n)

#
# def sum(a,b):
#     return a +b

# print ("Enter a list of numbers, one per line, entding with a zero")
#
# total = 0
# count = 0
#
# num = float(input())
# while num != 0:
#     total += numpri
#     count += 1
#     num = (float(input()))
#
# print ("Average: ", total/count)

line = input ("enter a list of numbers")

numlist = line.split()
total = 0
for num in numlist:
    total += float(num)

print(total/len(numlist))