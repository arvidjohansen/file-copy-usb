from varinfo import *
import os
import shutil

dst_dir = r'E:\Arvid\Projects\Opptak\2022-11\Set 3'
src_dir = r'F:\4CH\FOLDER04'

os.chdir(src_dir)
files = os.listdir('.')

count = 0
total_files_num = 0

def user_choice_dir():
    while True:
        os.chdir('..')
        files = os.listdir()
        print(list(enumerate(files)))
        choice = int(input('Please enter a number: '))
        print(f'CHanging dir to {files[choice]}')
        os.chdir(files[choice])
        return files[choice]

if not files:
    print(f'{src_dir} is empty!')
    src_dir = user_choice_dir()
    files = os.listdir()

total_files_num = len(files)
print(f'Copying {total_files_num} files to {dst_dir}')
for f in files:
    print(f'Copying file {f}')
    shutil.copy2(f,dst_dir)
    count += 1

print(f'Finished copying {count} files')




