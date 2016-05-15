from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='zype',
      version='0.1.0',
      description='Zype API Python Client',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='zype api client',
      url='http://github.com/khfayzullaev/zype-python',
      author='Khurshid Fayzullaev',
      author_email='khurshidfayzullaev@yahoo.com',
      license='Apache License 2.0',
      packages=['zype'],
      install_requires=[
          'requests',
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
