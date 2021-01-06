import os, glob
print(dir(os)) # Các hàm có trong thư viện OS
# Liệt kê các thư mục con trong ổ đĩa
list1 = []
list2 = []
path = 'C:\\Users\\MyPC\\Documents'
for root, dirs, files in os.walk(path):
    ten_tap_tin = glob.glob(path)
    list1.append(ten_tap_tin)
    ten_thu_muc = os.path.dirname(path)
    list2.append(ten_thu_muc)
print('Tên tập tin là: ', list1)
print('Tên thư mục là: ', list2)