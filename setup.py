from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

AUTHOR_NAME = 'Priyanka Sett'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO, 
    version='0.0.1',
    author=AUTHOR_NAME, 
    author_email='sett.priyanka@gmail.com',
    description= 'A small simple package for movie recommendation.',
    long_description= long_description, 
    long_description_content_type = 'text/markdown', 
    package = [SRC_REPO],
    python_requires =  '>=3.8', 
    install_requires = LIST_OF_REQUIREMENTS
)

