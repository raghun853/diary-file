from setuptools import setup, find_packages
# from distutils.core import setup
# import py2exe
# import sys
import os
del os.link

# sys.setrecursionlimit(5000)

#def readme():
#    with open('README.rst') as f:
#        return f.read()

setup(name='diary-file',
      version='0.1',
      description='Diary Framework for log files',
      author='Raghunandan',
      license='MIT',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'diaryFile = diaryFile.__main__:main'
          ]
      },
      include_package_data=True,
      zip_safe=True)
