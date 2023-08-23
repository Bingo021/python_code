num = 4
#旧版本
print(bin(num))
print('出现1的次数：',bin(num).count('1'))

#新版本 bit_count()
print('出现1的次数：',num.bit_count())