from setuptools import setup, find_packages
setup(name='resfinder', packages=find_packages(exclude=['scripts','tests']), entry_points={"console_scripts": ['resfinder = resfinder.run_resfinder:main']}, zip_safe=False,
      version='4.2.1.2'
      )
