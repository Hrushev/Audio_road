import moviepy.editor

video = moviepy.editor.VideoFileClip('audio_vid.MP4')
audio = video.audio
audio.write_audiofile('audio_vid.mp3')