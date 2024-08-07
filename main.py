from moviepy.editor import ImageClip, AudioFileClip

# Función para crear un video con una imagen fija y un audio
def crear_video_con_imagen_fija(imagen_path, audio_path, output_path):
    # Cargar el audio
    audio = AudioFileClip(audio_path)
    
    # Cargar la imagen
    imagen = ImageClip(imagen_path)
    
    # Establecer la duración del video a la duración del audio
    imagen = imagen.set_duration(audio.duration)
    
    # Configurar la tasa de fotogramas
    imagen = imagen.set_fps(24)
    
    # Agregar el audio al video
    video = imagen.set_audio(audio)
    
    # Exportar el video final
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Función para detectar beats en el audio (para futuras mejoras de animación)
def detectar_beats(audio_path):
    import librosa
    y, sr = librosa.load(audio_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    return beats

# Rutas de los archivos
imagen_path = r'D:\Users\josek\descargas\fotomolino.jpeg'  # Cambia esto a la ruta de tu imagen
audio_path = r'D:\Users\josek\musica\SET\03gateway.mp3'    # Cambia esto a la ruta de tu audio
output_path = r'D:\Users\josek\musica\SET\output_video.mp4'  # Cambia esto al nombre deseado para el archivo de salida

# Crear el video con la imagen fija
crear_video_con_imagen_fija(imagen_path, audio_path, output_path)

# Detectar beats en el audio (para futuras mejoras)
beats = detectar_beats(audio_path)
print(f"Beats detectados en el audio: {beats}")
