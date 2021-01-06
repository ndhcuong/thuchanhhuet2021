import os

list1 = []   #list1 luu danh sach cac tap tin
list2 = []   #list2 luu danh sach cac thu muc

#Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C
for root, dirs, files in os.walk('C:\\Users\\MyPC\\Documents'):
    list1.append(files)
    list2.append(dirs)

print('Danh sach cac thu muc cua cua C')
print(list2)
print('Danh sach cac tap tin thuoc o dia C')
print(list1)