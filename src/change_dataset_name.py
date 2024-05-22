import os

for i in range(10):

    folder_path = f'../datasets/mnist_png/testing/{i}'

    # 获取文件夹中的所有文件名
    file_list = os.listdir(folder_path)

    # 遍历文件名列表
    for filename in file_list:
        # 获取文件的绝对路径
        old_name = os.path.join(folder_path, filename)
        # 分割文件名和扩展名
        name, extension = os.path.splitext(filename)
        # 修改文件名
        new_name = os.path.join(folder_path, f"{name}_{i}{extension}")
        # 重命名文件
        os.rename(old_name, new_name)
