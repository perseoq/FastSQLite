from asyncore import read
from setuptools import setup

readme = open('./README.md','r')

setup(
    name='fastsqlite',
    packages=['fastsqlite'],
    version='1.0',
    description='Micro ORM SQLite3',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Roy Quintanar',
    author_email='royquintanar@comunidad.unam.mx',
    url='',
    download_url='',
    keywords=['orm', 'sqlite', 'laudaro'],
    classifiers=[ ],
    license='GNU General Public License v3.0',
    include_package_data=True
)