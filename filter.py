import os
import shutil

def compare_and_copy(src_folder, dest_folder, output_folder):
    # 获取源文件夹中的文件列表
    src_files = set(os.listdir(src_folder))

    # 获取目标文件夹中的文件列表
    dest_files = set(os.listdir(dest_folder))

    # 计算在源文件夹中但不在目标文件夹中的文件
    files_to_copy = src_files - dest_files

    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 复制文件到输出文件夹
    for file_to_copy in files_to_copy:
        src_path = os.path.join(src_folder, file_to_copy)
        dest_path = os.path.join(output_folder, file_to_copy)
        shutil.copy2(src_path, dest_path)
        print(f"Copying {file_to_copy} to {output_folder}")

# 设定源文件夹、目标文件夹和输出文件夹的路径
prediction_out_folder = "./prediction_out"
design_out_folder = "./design_out"
output_folder = "./prediction_out5"

# 比对并复制文件
compare_and_copy(prediction_out_folder, design_out_folder, output_folder)
