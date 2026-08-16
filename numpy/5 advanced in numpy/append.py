import numpy as np

arr=np.array([10,20,30])
print(arr)
new_arr=np.append(arr,[40,50,60],axis=0)     #np.insert(array name,index,value,axis=0 or 1)   
print(new_arr)                                                          #axis 0 for rows and 1 for column