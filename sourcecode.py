import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
my_array = []
x_axis = []
for i in range(100):
  x_axis.append(i)
for i in range(100):
  my_array.append(random.randint(0,100))

def sortlist(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2 ]
  left_list = []
  mid_list = []
  right_list = []
  for values in arr:
    if values < pivot:
      left_list.append(values)
    elif values == pivot:
      mid_list.append(values)
    else:
      right_list.append(values)
  return sortlist(left_list) + mid_list + sortlist(right_list)

  
