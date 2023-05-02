
# nums = [100,4,200,1,3,2]
nums=[-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
# Output: 4
nums.sort()
count,final=1,1
for i in range(len(nums)-1):
    if nums[i]+1==nums[i+1]:
        count+=1
        if count > final:
            final=count
    else:
        count=1


print(final)
print(final)
print(final)