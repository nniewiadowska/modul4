list1 = [2, 4, 6, 10, 28, 77]

def find_max(elem):
  lst = []
  max_elem = 0
  for elem in list1:
    if elem > max_elem:
      max_elem = elem
  lst.append(max_elem)
  return lst
