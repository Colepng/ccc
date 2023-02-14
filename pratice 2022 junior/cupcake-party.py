reg_boxes = int(input())
small_boxes = int(input())

num_cupcakes = reg_boxes * 8 + small_boxes * 3
num_cupcakes -= 28
print(num_cupcakes)