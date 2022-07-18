import os
import shutil
from pathlib import Path

current_working_dir = os.getcwd()

for folder in os.listdir(current_working_dir):
	if os.path.isdir(current_working_dir + "/" + folder) and folder != "Books" and folder != "Book":
		for mp3_audio in os.listdir(current_working_dir + "/" + folder):
			if(mp3_audio.endswith('.mp3') or mp3_audio.endswith('.m4a') or mp3_audio.endswith('.aac') or mp3_audio.endswith('.wav') or mp3_audio.endswith('.mp4') or mp3_audio.endswith('.adts')):
				os.system('ffmpeg -i start.mp3 -i "' + current_working_dir + '/' + folder + '/' + mp3_audio + '" -filter_complex [0:a][1:a]concat=n=2:v=0:a=1 -b:a 192k "' + mp3_audio + '"')

				shutil.copy('end.mp3', os.path.basename(mp3_audio) + '_end.mp3')

				os.remove(current_working_dir + '/' + folder + '/' + mp3_audio)

				os.system('ffmpeg -i "' + mp3_audio + '" -i "' + os.path.basename(mp3_audio) + '_end.mp3' + '" -filter_complex [0:a][1:a]concat=n=2:v=0:a=1 -b:a 192k  "' + current_working_dir + '/' + folder + '/' + mp3_audio + '"')
				
				os.remove(mp3_audio)
				os.remove(os.path.basename(mp3_audio) + '_end.mp3')