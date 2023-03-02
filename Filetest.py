# # 文件操作
# # 打开文件 open 如果不存在会自动新建一个
# # 默认编码是中文GBK编码 最好的习惯是打开文件的时候指定一种编码
# fobj=open('./Test.txt','w')
# 开始操作 读/写
# fobj.write('危楼高百尺\r\n')
# fobj.write('手可摘星辰\r\n')
# 运行会覆盖掉文件原本的内容
# fobj.close() # 保存并关闭

# # 以二进制形式书写
# fobj=open('Test_1.txt','wb') # str-->bytes
# fobj.write('不敢高声语'.encode('utf-8'))
# fobj.close()

# fobj=open('Test_1.txt','ab') # 数据追加
# fobj.write('不敢高声语\r\n'.encode('utf-8'))
# fobj.write('恐惊天上人\r\n'.encode('utf-8'))
# fobj.close()


f=open('Test.txt','rb') # r 为读取 rb为以二进制方式读取
data=f.read()
# print(data)
print(data.decode('gbk'))
# print(f.read(5))
# print(f.read()) # 第一次读到第五个字，下次还接着读取
# print(f.readlines()) # 读取所有行
# print(f.readlines(1))# 读取一行