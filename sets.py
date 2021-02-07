a = {1,4,6,8}
b = {2,5,6,8,6}

print(a-b)

a = [1, 2, 3, 4, 5, 6, 6, 7, 9]
print(a.index(6))

import numpy as np
a = np.array(a).reshape(3,3)
print(np.argwhere(a==6))
