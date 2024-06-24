from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name='video2livephoto',
    version='0.1.0',
    author='Ródiney Wanderson',
    author_email='rodineyw@yahoo.com.br',
    description='Um pacote para converter vídeos em live-fotos, comum em dispositivos iOS.',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/seu_usuario/video2livephoto',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'Pillow'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.7',
)
