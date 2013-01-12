from setuptools import setup, find_packages

version = '0.1'


def read(name):
    try:
        with open(name) as fd:
            return fd.read()
    except:
        return ''

setup(name='wsgi_proxy',
      version=version,
      long_description=read('README.rst') + '\n' + read('CHANGES.rst'),
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          ],
      keywords='wsgi proxy',
      author='Gael Pasgrimaud',
      author_email='gael@gawel.org',
      url='https://github.com/gawel/wsgi_proxy/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'README_fixt', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['webob', 'six'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )