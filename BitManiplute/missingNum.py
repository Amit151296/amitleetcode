

# The following function would take as input a text string and create a list of all the words in the text each of which contains only lower-case letters and is of length no longer than 6.

# Please fill the missing code at the space underlined using list comprehension.


# from curses.ascii import isdigit


text = "The following function would TAKE as input a text string and create a list of all \
the words in the text each of Which contains only lower-case letters and is of length no \
longer than 5"



final=[ i for i in text.split() if len(i) <6  and i==i.lower() and i.isdigit()==False ]
print(final)
# def word_collect(s):
    
#     capital=[i for i in range(65,91)]
#     final=[]
#     list1=s.split()
#     for i in list1:
#         for j in i:
#             if ord(j) in capital:
#                 print (j)
#                 break
#         final.append(i)
        
#     # print(capital)
#     print(list1)
#     print(final)


#     return 

# print(word_collect(text))




x='abcd5'
for i in x:
    if  i.isdigit()==False:
        print(i)