from distutils.core import setup
version = '0.3.1'
setup(
    name='truerandomdice',
    version=version,
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
    download_url='https://github.com/EarthModule/TrulyRandomDiceThrower/releases/tag/' + version,
    license='',
    author='toni nurmi',
    author_email='toni.nurmi@hotmail.com',
    description=''
)
