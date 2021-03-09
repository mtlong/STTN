

import sys
import os

DATASET_ROOT="/media/malong/7665cf70-1886-4554-b39d-f6a0e600d53e/workspace/Data_Storage/Datasets/DAVIS/480P/DAVIS-2017-Unsupervised-trainval-480p/DAVIS/"
RESULT_FOLDER = "/media/malong/7665cf70-1886-4554-b39d-f6a0e600d53e/workspace/2021/Video_Inpainting/Results/STTN/DAVIS/"

vid_list = os.listdir(DATASET_ROOT + 'JPEGImages/480p/')

#os.system("cd tool")
for i in range(len(vid_list)):
    vid_name = vid_list[i]
    frame_folder_name = DATASET_ROOT + 'JPEGImages/480p/' + vid_name + '/'
    mask_folder_name = DATASET_ROOT +  'Annotations/480p/' + vid_name + '/'
    output_folder_name = RESULT_FOLDER + vid_name
    command_str = "CUDA_VISIBLE_DEVICES=3 python MTL_test.py --folder " + frame_folder_name + " --mask " + mask_folder_name + " --result " + output_folder_name + " --ckpt checkpoints/sttn.pth "
    os.system(command_str)

