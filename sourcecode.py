import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
plt.ion()
fig , ax = plt.subplots(figsize=(10,6))
result = []
my_array = []
for i in range(100):
  my_array.append(random.randint(0,100))
def visualization():
  plt.title("Sorting Algorithm Visualization")
  plt.xlabel('x')
  plt.ylabel('y')
def sortlist(arr):
  global result
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
  result =  sortlist(left_list) + mid_list + sortlist(right_list)
  ax.clear()
  ax.bar(range(len(result)), result, color='salmon')
  plt.pause(0.05)
  return result

sorted_list=sortlist(my_array)
plt.ioff()
ax.clear()
plt.show()





