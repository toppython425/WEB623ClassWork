import os

current_abs_path = r'D:\work_Top_Academy_web\WEB623ClassWork\module_06\lesson_01'

# for path, dirnames, filenames in os.walk(current_abs_path):
#     print(f'path >> {path}')
#     print(f'dirs >> {dirnames}')
#     print(f'files >> {filenames}')
#     print()


# disk = 'D:\\'
# dir1 = 'work_Top_Academy_web'
# dir2 = 'WEB623ClassWork'
# dir3 = 'module_06'
# dir4 = 'lesson_01'
#
# path_join = os.path.join(disk, dir1, dir2, dir3, dir4)
# print(path_join)
#
# for path, dirnames, filenames in os.walk(path_join):
#     print(f'path >> {path}')
#     print(f'dirs >> {dirnames}')
#     print(f'files >> {filenames}')
#     print()

base_dir = '.'
data_dir = 'data_files'
data_path = os.path.join(base_dir, data_dir)

for path, dirnames, filenames in os.walk(data_path):
    print(f'path >> {path}')
    print(f'dirs >> {dirnames}')
    print(f'files >> {filenames}')
    print()


print(os.path.abspath('.'))
print(os.path.abspath('files_01.py'))
print(os.path.abspath(r'data_files\ex.txt'))
