import os, shutil


folder_name = os.path.join('results_trainset', 'summer2winter', 
    'summer2winter_yosemite_pretrained', 'test_latest', 'images')
dst_folder_name = os.path.join('/home/haotao/GAN_Slimming_CycleGAN/train_set_result/summer2winter_yosemite', 'B')
for file_name in os.listdir(folder_name):
    if 'fake' in file_name:
        shutil.copy(os.path.join(folder_name, file_name), dst_folder_name)


folder_name = os.path.join('results_trainset', 'winter2summer', 
    'winter2summer_yosemite_pretrained', 'test_latest', 'images')
dst_folder_name = os.path.join('/home/haotao/GAN_Slimming_CycleGAN/train_set_result/summer2winter_yosemite', 'A')
for file_name in os.listdir(folder_name):
    if 'fake' in file_name:
        shutil.copy(os.path.join(folder_name, file_name), dst_folder_name)


folder_name = os.path.join('results', 'summer2winter', 
    'summer2winter_yosemite_pretrained', 'test_latest', 'images')
dst_folder_name = os.path.join('/home/haotao/GAN_Slimming_CycleGAN/test_set_result/summer2winter_yosemite', 'B')
for file_name in os.listdir(folder_name):
    if 'fake' in file_name:
        shutil.copy(os.path.join(folder_name, file_name), dst_folder_name)


folder_name = os.path.join('results', 'winter2summer', 
    'winter2summer_yosemite_pretrained', 'test_latest', 'images')
dst_folder_name = os.path.join('/home/haotao/GAN_Slimming_CycleGAN/test_set_result/summer2winter_yosemite', 'A')
for file_name in os.listdir(folder_name):
    if 'fake' in file_name:
        shutil.copy(os.path.join(folder_name, file_name), dst_folder_name)
