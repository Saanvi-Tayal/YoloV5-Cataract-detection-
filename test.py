# import os
# import cv2

# path = os.path.join("dataset", "3_retina_disease")
# dic={}
# dic2 ={}
# for obj in os.listdir(path):
#     img = cv2.imread(os.path.join(path, obj))
#     x = img.shape[0:2]
#     print(obj , ".",x)
#     if x in dic2:
#         dic2[x] +=1 
#     else:
#         dic2[x] =1

# print(dic2)

# cook your dish here
for k in range(int(input())):
    n=int(input())
    if n >= 7:
        lst = [int(l) for l in range(len(str(input())))]
        for i in lst:
            if lst[i] == lst[i+1] or lst[i] == (lst[i+1] -1) or lst[i] == (lst[i+1]+1):
                for j in lst:
                    if lst[::j] == lst[::-1]:
                        print("yes")
            else:
                print("no")

            
