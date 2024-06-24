
# Video to Live Photo Converter

Este pacote Python permite converter vídeos em live-fotos, um formato que combina uma foto estática com um curto vídeo ou gif, semelhante ao recurso Live Photos nos iPhones.

## Funcionalidades

- Extrai uma foto estática de um vídeo.
- Cria um gif curto a partir de um vídeo para simular uma live-foto.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Python instalado em seu sistema. Este projeto foi testado com Python 3.12.

## Instalação

Clone o repositório para sua máquina local usando:

```bash
git clone https://github.com/seu-usuario/video2livephoto.git
```

Navegue até o diretório do projeto e instale as dependências:

```bash
cd video2livephoto
pip install -r requirements.txt
```

## Como Usar

Para usar o pacote, execute o seguinte comando no terminal, substituindo `path_to_video` pelo caminho do vídeo e `output_directory` pelo diretório onde os arquivos resultantes serão salvos:

```bash
python -m video2livephoto.converter path_to_video output_directory
```

## Testes

Para executar os testes, instale `pytest` se ainda não estiver instalado e execute:

```bash
pytest
```

## Contribuição

Contribuições são sempre bem-vindas! Sinta-se livre para forkar o projeto, fazer suas alterações e enviar um pull request.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.