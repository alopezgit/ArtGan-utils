import csv
import os
import random
from torch.utils.serialization import load_lua
data_folder = '/media/adrian/SSD/clean_dataset_art'

out_base_f = './art_data'
if not os.path.exists(out_base_f):
	os.makedirs(out_base_f)
max_folder_length = 40
vocab = {}
import IPython;IPython.embed()
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
with open(os.path.join(data_folder, 'new_info.csv'), 'r') as file:
	reader = csv.reader(file, delimiter='|')
	header = next(reader)
	train_ids = open(os.path.join(out_base_f, 'trainvalids.txt'), 'w')

	for k, row in enumerate(reader):
		print(row)
		new_folder = row[0].replace('/', '_')[:-4][:max_folder_length]
		new_folder =new_folder
		out_text_folder = os.path.join(out_base_f, 'text_c10',  str(k+1).zfill(5)+'.'+new_folder)
		out_im_folder = os.path.join(out_base_f, 'images', new_folder)
		if not os.path.exists(out_text_folder):
			os.makedirs(out_text_folder)
		### Text
		file_name = new_folder + '.txt'
		with open(os.path.join(out_text_folder, file_name), 'w') as txt_file:
			txt_file.write(row[-1])

		if random.random() < 0.8:
			train_ids.write(str(k+1).zfill(5)+'\n')
			
