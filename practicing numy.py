import numpy as np 

list_1 = [1,2,3]
list_2 = [2,2,33]
list_3 = [11,3,2]
list_4 = [111,4,2]

arr = np.array([list_1,list_2,list_3,list_4])
print(arr[:2,0:3])