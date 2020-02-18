# -*- coding: utf-8 -*-
"""
https://dzone.com/articles/executable-package-pip-install

Created on Tue Feb  4 16:16:31 2020

@author: Jerry
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='jrImgTools',  
     version='0.1.0',
     scripts=['jrImgTools_setup'] ,
     author="Jerry Xing",
     author_email="j.xing.www@gmail.com",
     description="Image utility functions for personal use",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/jr-xing/jrImgTools",
     packages=setuptools.find_packages(),
     install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'SimpleITK'
      ],
    #  classifiers=[
    #      "Programming Language :: Python :: 3",
    #      "License :: OSI Approved :: MIT License",
    #      "Operating System :: OS Independent",
    #  ],
 )