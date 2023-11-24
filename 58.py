'''Take numbers from the user and find out min, maximum, sum, average'''
from statistics import mean
nums = list(map(int,input("Enter the numbers here : ").split()))
print(min(nums))
print(max(nums))
print(sum(nums))
print(mean(nums))