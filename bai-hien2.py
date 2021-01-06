import os,random
import string

t = input('Nhập tên thư mục: ') #Em muốn tạo thư mục trực tiếp trên python
path = 'C:\\Users\\MyPC\\Documents\\'
os.chdir(path)
os.mkdir(t)
file_name = input("Nhập tên file dữ liệu: ") #Em muốn tạo tên file trực tiếp trên python
n = int(input("Nhập tổng số lượng file với dung lượng 1MB-1024MB: ")) #vì 1MB=>1024KB nên số lượng file nằm từ khoảng 2->1048 files
i = 1
for i in range(n):
    path1 = path + t
    os.chdir(path1)
    i = str(i)
    f = open(file_name + i + '.txt','w+')
    f.seek(1024*1000-1)
    f.write(random.choice(string.ascii_lowercase))
if f.seek(0):
    os.remove(f) #Lọc file 0KB