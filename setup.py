from setuptools import find_packages, setup

setup(name='xqdm',
      version='0.0.1',
      url='https://github.com/Kitsunetic/xqdm',
      license='MIT',
      author='Kitsunetic',
      author_email='1996.jh.shim@gmail.com',
      description='XQDM is progrssbar on multiprocessing',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=['tqdm'],
      test_suite='nose.collector')
