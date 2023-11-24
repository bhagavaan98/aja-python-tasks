'''Take some single digit numbers from the user and findout min, maximum, sum, average'''
from statistics import mean
nums = list(map(int,input("Enter your numbers here : ").split(",")))
print(max(nums))
print(min(nums))
print(sum(nums))
print(mean(nums))