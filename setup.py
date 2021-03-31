from setuptools import setup, find_packages

setup(
    name='depack',
    version='0.0.1',
    description='Universal archive file tool',
    url='https://github.com/voidful/depack',
    author='Voidful',
    author_email='voidful.stack@gmail.com',
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    setup_requires=['setuptools-git'],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Archiving :: Compression",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python"
    ],
    license="Apache",
    keywords='zip unzip tar targz gz 7zip',
    packages=find_packages(),
    install_requires=[
        "patool",
        "nlp2"
    ],
    entry_points={
        'console_scripts': ['depack=src.main:main', 'unpack=src.main:main']
    },
    zip_safe=False,
)
