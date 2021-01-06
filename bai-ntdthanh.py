import os

list1 = []
list2 = []
target = 'C:\\Users\\MyPC\\Documents'
for x in os.walk(target):
    print(x)
for root, dirname, files in os.walk(target):
    for x in dirname:
        list2.append(root + '\\' + x)
    for x in files:
        list1.append(root + '\\' + x)
print("Danh sách tập tin:" + str(list1))
print("Danh sách thư mục: " + str(list2))