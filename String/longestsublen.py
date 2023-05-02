# def judgeSquareSum( c):
#     for i in range(c+1):
#         if i*i > c:
#             x=i
#             print(x)
#             break
#     for i in range((x//2)+1):
#         for j in range(i,x):
#             if i*i + j*j ==c:
#                 return True
#     return False

# print(judgeSquareSum(1))

def judgeSquareSum(self, c: int) -> bool:
    if c==1 or c==0:
        return True
    for i in range(1,int(c**0.5)+1):
        k=c-(i*i)
        sk=k**0.5
        if sk==int(sk):
            return True
    return False