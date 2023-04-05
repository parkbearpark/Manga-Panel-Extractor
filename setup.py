from setuptools import setup, find_packages

setup(
    name='PanelExtractor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-image',
        'opencv-python',
        'torch',
        'torchvision==0.12.0',
        'tqdm',
    ],
    include_package_data=True,
    author='Ito Yuma',
    author_email='yumai6205@gmail.com',
    description='A package for extracting panels from manga images.',
    url='https://github.com/parkbearpark/Manga-Panel-Extractor.git',
)
