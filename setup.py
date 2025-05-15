from setuptools import setup

# from distutils.core import setup

setup(
    name='peak_detection_extra',
    # version='0.1.0',
    packages=['randomforest'],
    package_data={
        # If you have non-Python files, specify them here:
        '': ['*.yaml', '*.pt', '*.csv', '*.tar', '*.pkl']
    },
    url='https://github.com/uw-cmg/peak_detection_extra.git',
    license='MIT',
    author='Ryan Jacobs',
    author_email='rjacobs3@wisc.edu',

)