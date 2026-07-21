old_name = input("请输入要备份的文件名：")
index = old_name.rfind(".")
new_name = old_name[:index] + "[备份]" + old_name[index:]
print("备份后的文件名为：" + new_name)
