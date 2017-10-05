from distutils.core import setup

setup(
    name='truerandomdice',
    version='0.2',
    packages=['truerandomdice'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'peewee',
        'rdoclient',
        'requests',
    ],
    url='https://github.com/EarthModule/TrulyRandomDiceThrower',
    download_url='https://github.com/EarthModule/TrulyRandomDiceThrower/releases/tag/0.2',
    license='',
    author='toni nurmi',
    author_email='toni.nurmi@hotmail.com',
    description=''
)
