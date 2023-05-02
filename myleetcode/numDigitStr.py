# def numberToWords(n):
#     if len(n)==1:
#         oneDigit(n)

#     if len(n)==2:
#         twoDigit(n)

#     if len(n)==3:
#         threeDigit(n)

#     if len(n) > 3 and len(n) <=6:
#         threeToSix(n)

#     if len(n) > 6 and len(n) <=9:
#         sixToNine(n)

#     if len(n) > 9: 
#         nineToEnd(n)


# n='6685687'
# numberToWords(n)

# digits = {0: '', 1: 'One',2: 'Two',3: 'Three', 4: 'Four',5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine' }
# tens_place = {9: 'Ninety', 8: 'Eighty', 7: 'Seventy',6: 'Sixty',5: 'Fifty',4: 'Forty',3: 'Thirty',2: 'Twenty',0: ''}
# teens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19:'Nineteen'}

# def oneDigit(s):
#         print(digits[int(s)],end='')

# def twoDigit(s):
#     a,b=int(s[0]),int(s[1])
#     if 10*a + b < 10:
#         oneDigit(str(10*a + b))

#     if 10*a + b >= 10 and 10*a + b <20:
#         print(teens[10*a + b],end='')

#     if 10*a + b >= 20:
#         print(f'{tens_place[a]} {digits[b]}',end='')

# def threeDigit(s):
#     a=int(s[0])
#     if a>0:
#         print(f"{digits[a]} Hundred " , end='')
#         twoDigit(s[1:])
#     else:
#         twoDigit(s[1:])

# def threeToSix(s):
#    if len(s)==6:
#         threeDigit(s[:3])
#         print(' Thousand ',end='')
#         threeDigit(s[3:])
#    if len(s)==5:
#         twoDigit(s[:2])
#         print(' Thousand ',end='')
#         threeDigit(s[2:])
#    if len(s)==4:
#         oneDigit(s[:1])
#         print(' Thousand ',end='')
#         threeDigit(s[1:])
        

# def sixToNine(s):
#    if len(s)==9:
#         threeDigit(s[:3])
#         print(' Million ',end='')
#         threeToSix(s[3:])
#    if len(s)==8:
#         twoDigit(s[:2])
#         print(' Million ',end='')
#         threeToSix(s[2:])
#    if len(s)==7:
#         oneDigit(s[:1])
#         print(' Million ',end='')
#         threeToSix(s[1:])


# def nineToEnd(s):
#    if len(s)==12:
#         threeDigit(s[:3])
#         print(' Billion ',end='')
#         sixToNine(s[3:])
#    if len(s)==11:
#         twoDigit(s[:2])
#         print(' Billion ',end='')
#         sixToNine(s[2:])
#    if len(s)==10:
#         oneDigit(s[:1])
#         print(' Billion ',end='')
#         sixToNine(s[1:])
        

