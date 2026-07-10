"""
write() 函数用于从文件中写入内容。
语法：
文件.write(写入数据)
其中， 写入数据表示要写入的内容。

写入时，open有三种参数 x， w， a
分别为创建模式，写入模式，追加模式
"x" - 创建 - 将创建一个文件，如果文件存在则返回错误。
"a" - 追加 - 如果指定的文件不存在，将创建一个文件，如果有则在文件内容后追加。
"w" - 写入 - 如果指定的文件不存在，将创建一个文件，有也删除文件内容重新写入数据。
"""

f = open("documents/test1.txt", "a")
content = f.write("ddd")
print(content)
f.close()

f = open("documents/test2.txt", "w")
content = f.write("ddd")
print(content)
f.close()

f = open("documents/test3.txt", "x")
