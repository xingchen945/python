import os


def rename_files(path, replace_name):
    movie_name = os.listdir(path)
    for temp in movie_name:
        new_name = temp.replace(replace_name, '')
        os.rename(os.path.join(path, temp), os.path.join(path, new_name))


if __name__ == "__main__":
    isExit = False
    while not isExit:
        path = input("请输入文件夹地址：")
        if path == 'exit':
            isExit = True
        else:
            replace_name = input("请输入要替换的字符串：")
            rename_files(path, replace_name)
            print("修改成功")
