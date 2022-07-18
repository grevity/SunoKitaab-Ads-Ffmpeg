# import os
# from pathlib import Path

# import re 

# def sorted_nicely( l ): 
#     convert = lambda text: int(text) if text.isdigit() else text 
#     alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
#     return sorted(l, key = alphanum_key)

# fileSequence = 1
# folderSequence = 1
# current_working_dir = os.getcwd()

# for folder in os.listdir(current_working_dir):
# 	if folder != "rename.py" and folder != "System Volume Information" :
# 		f_unsorted = os.listdir(current_working_dir + "/" + str(folderSequence))
# 		for x in sorted_nicely(f_unsorted):
# 			print('ffmpeg -ss 0 -i "' + x + '" -t 6 output.mp3')
# 			# do editing...
# 			#1. clipping...
# 			os.system('ffmpeg -ss 0 -i "' + x + '" -t 6 output.mp3')
# 			fileSequence +=1
# 		# fnames = sorted(list(Path(os.listdir(current_working_dir + "\\" + str(folderSequence))).iterdir()), key=lambda path: int(path.stem))
# 		# os.listdir(current_working_dir + "\\" + str(folderSequence)).sort()
# 		# for filename in os.listdir(current_working_dir + "\\" + str(folderSequence)):
# 		# 	os.rename(current_working_dir + "\\" + str(folderSequence) +"\\"+ filename, str(fileSequence) + '.mp3')
# 		folderSequence +=1


import os
from pathlib import Path

current_working_dir = os.getcwd()

for folder in os.listdir(current_working_dir):
	if os.path.isdir(current_working_dir + "/" + folder) and folder != "Books" and folder != "Book":
		for mp3_audio in os.listdir(current_working_dir + "/" + folder):
			if(mp3_audio.endswith('.mp3')):
				#clip audio....
				os.system('ffmpeg -i "' + current_working_dir + '/' + folder + '/' + mp3_audio + '" -ss 6 "' + mp3_audio + '"')

				#delete orginal file from place....
				os.remove(current_working_dir + '/' + folder + '/' + mp3_audio)

				#join ad with output file...
				os.system('ffmpeg -i intro.mp3 -i "' + mp3_audio + '" -filter_complex [0:a][1:a]concat=n=2:v=0:a=1 -b:a 192k "' + current_working_dir + '/' + folder + '/' + mp3_audio + '"')
				
				#delete output file...
				os.remove(mp3_audio)