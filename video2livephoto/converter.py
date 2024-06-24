import cv2
from PIL import Image
import os


def capture_frame(video_path):
    """ Captura um único frame do video para usar como foto estática. """
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()
    cap.release()
    if not success:
        raise ValueError("Não foi possivel capturar um frame do vídeo.")
    return frame


def create_gif_from_video(video_path, duration=2, fps=10):
    """ Cria um GIF a partir de um trecho do vido. """
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    start_frame = 0
    end_frame = min(frame_count, int(cap.get(cv2.CAP_PROP_FPS) * duration))

    frames = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    while cap.get(cv2.CAP_PROP_POS_FRAMES) < end_frame:
        success, frame = cap.read()
        if not success:
            break
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        frames.append(image)

    cap.release()
    gif_path = os.path.splitext(video_path)[0] + ".gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:0],
                   optimize=False, duration=1000//fps, loop=0)
    return gif_path


def convert_video_to_livephoto(video_path, output_dir):
    """ Converte um video em uma 'live photo' (imagem + GIF). """
    os.makedirs(output_dir, exist_ok=True)

    # Captura a foto estática
    frame = capture_frame(video_path)
    image_path = os.path.join(output_dir, 'static_image.jpg')
    cv2.imwrite(image_path, frame)

    # Criar o GIF
    gif_path = create_gif_from_video(video_path)

    return image_path, gif_path


if __name__ == '__main__':
    import sys
    video_path = sys.argv[1]
    output_dir = sys.argv[2]
    convert_video_to_livephoto(video_path, output_dir)
