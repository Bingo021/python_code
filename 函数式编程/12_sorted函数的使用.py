sorter1 = sorted([1,3,6,-20,3])
print("升序排列：",sorter1)

sorter2 = sorted([1,3,6,-20,-70],key=abs)
print("自定义排序：",sorter2)

sorter3 = sorted([1,3,6,-20,-70],key=abs,reverse=True)
print("自定义反向排序：",sorter3)