with open('binary.bin', 'rb') as f:
    data = f.read()
print(data)

#array로 가져오기
data = array.array('B')
with open('binary.bin', 'rb') as f:
    f.seek(0, os.SEEK_END) #파일 끝으로 감
    filesize = f.tell()
    f.seek(0)
    data.fromrile(f, filesize) # 파일 끝 위치, 즉 파일 사이즈
for item in data:
    print(item)