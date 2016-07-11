from os import path
import codecs
from setuptools import setup, find_packages

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

setup(
    name='Django-Tumblr',
    version='0.0.1',
    author='Joe Curlee',
    author_email='joe.curlee@gmail.com',
    packages=find_packages(),
    url='https://github.com/curlee/Django-Tumblr',
    license='MIT',
    description="A django template tag to display posts from a given Tumblr blog.",
    long_description=read(path.join(path.dirname(__file__), 'README')),
    install_requires=[
        "django-templatetag-sugar==0.1",
        "TumblrAPI==0.2.4",
    ],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)