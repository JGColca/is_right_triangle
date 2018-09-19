def is_right_triangle(a, b, c):
    array = [a,b,c]
    sorted_array = sorted(array)
    if ((sorted_array[0]^2) + (sorted_array[1]^2)) == (sorted_array[2]^2):
      return True
    else:
      return False

print(is_right_triangle(1,2,2))
