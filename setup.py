from setuptools import setup

setup(name='better_requests',
      version='0.1',
      description='Wrapper around python requests library which allows for global defaults',
      url='https://github.com/ProjectThor/better_requests',
      author='Franco Sebregondi',
      author_email='franco.sebregondi@siroop.ch',
      license='MIT',
      packages=['better_requests'],
      install_requires=['requests'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest', 'pytest-dotenv', 'doubles', 'args_catcher'],
      dependency_links=['https://github.com/ProjectThor/args_catcher/master#egg=args_catcher-0.1.0'],
      zip_safe=False)
