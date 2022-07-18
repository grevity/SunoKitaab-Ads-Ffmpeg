import os
from pathlib import Path

current_working_dir = os.getcwd()

for folder in os.listdir(current_working_dir):
	if os.path.isdir(current_working_dir + "/" + folder) and folder != "Books" and folder != "Book":
		for mp3_audio in os.listdir(current_working_dir + "/" + folder):
			if(mp3_audio.endswith('.mp3') or mp3_audio.endswith('.m4a') or mp3_audio.endswith('.aac') or mp3_audio.endswith('.wav') or mp3_audio.endswith('.mp4') or mp3_audio.endswith('.mp4')):
				os.system('ffmpeg -i "' + current_working_dir + '/' + folder + '/' + mp3_audio + '" -af loudnorm=I=-16:LRA=11:TP=-1.5 -b:a 192k "' + current_working_dir + '/' + folder + '/norm_' + mp3_audio + '"')
				os.remove(current_working_dir + '/' + folder + '/' + mp3_audio)
				os.rename(current_working_dir + '/' + folder + '/norm_' + mp3_audio, mp3_audio)