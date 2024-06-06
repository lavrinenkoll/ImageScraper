import subprocess

modules = ('tensorflow', 'numpy', 'pillow', 'matplotlib', 'scikit-learn', 'bs4',
           'selenium', 'opencv-python', 'scikit-image', 'imagehash', 'requests', 'PySide6')


for module in modules:
    subprocess.run('pip install {}'.format(module))
