import os
import pytest
from video2livephoto.converter import convert_video_to_livephoto, capture_frame, create_gif_from_video


def test_capture_frame():
    """ Testa se a captura de frame está funcionando corretamete. """
    # Supondo que 'test_video.mp4' seja um video de teste no diretorio de testes
    frame = capture_frame('tests/test_video.MP4')
    assert frame is not None


def test_create_gif_from_video():
    """ Testa se a criação de GIF a partir de video está funcionando. """
    gif_path = create_gif_from_video(
        'tests/test_video.MP4', duration=1, fps=10)
    assert os.path.exists(gif_path)
    os.remove(gif_path)  # limpa oarquivo criado após o teste


def test_convert_video_to_livephoto():
    """ Testa  a função de converão de video para live photo. """
    image_path, gif_path = convert_video_to_livephoto(
        'tests/test_video.MP4', 'tests')
    assert os.path.exists(image_path)
    assert os.path.exists(gif_path)
    os.remove(image_path)  # Limpa os arquivos criados após o teste
    os.remove(gif_path)

    # Rodar os testes com o pytest diretamente ou definir uma configuração de CI pra fazê-lo automaticament
