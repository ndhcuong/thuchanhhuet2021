import os, random, string, math

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
    return ''.join(random.choice(letters) for i in range(length))


foldername = str(input('Nhập tên thư mục: '))
filename = str(input('Nhập tên tệp tin: '))
don_vi = 1048576 #1kb tinh theo byte
size = don_vi * float(input('Nhập dung lượng dữ liệu giới hạn là 1MB <= size <= 1024MB: '))
os.mkdir('C:\%s' %foldername)
os.chdir('C:\%s' %foldername)
for i in range(int(size/1048576)+1):
    if float(get_size('C:\%s' %foldername)) <= size-1024*1000:
        f = open(filename+'%d' %i,'a')
        f.write(random_string(1024*1000))
        f.close()
    else:
        f = open(filename+'%d' %i,'a')
        f.write(random_string(int(size)-get_size('C:\%s' %foldername)))
        f.close()