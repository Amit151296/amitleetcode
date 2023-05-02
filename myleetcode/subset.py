
def subset(nums):
    output=[]
    def helper(start,temp,output):
        output+=[temp]
        for i in range(start,len(nums)):
            helper(i+1,temp+[nums[i]],output)
    helper(0,[],output)
    return output

    





nums = [1,2]
# nums=[1,2]
print(subset(nums))

# Approch 2
# def subset(nums):
#     output=[[]]
#     for i in nums:
#         for j in range(len(output)):
#             output.append([i]+[j])
#     print(output)

# nums = [1,2,3]
# subset(nums)

# str=''
# def subset(arr):
    
#     if len(arr)==1:
#         str+=str(arr)
#     else:
#         subset(arr[1:])
#         str+=str(arr)

# print(str)




# nums = [1,2,3,4,5,6]
# subset(nums)
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# out=[[],[1]]
# for i in range(len(out)):
#     out.append(out[i]+[2])
#     print(out)
# print("Amit")
