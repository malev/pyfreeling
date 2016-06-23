from setuptools import setup, find_packages
from pyfreeling import version

install_requires = ['lxml']
version = '.'.join([str(x) for x in version])


setup(
    name='pyfreeling',
    version=version,
    author='Marcos Vanetta',
    author_email='marcosvanetta@gmail.com',
    url='http://github.com/malev/pyfreeling',
    description='Python wrapper for Freeling 4.0',
    keywords="nlp freeling spanish",
    license='GPL2',
    packages=find_packages(),
    install_requires=install_requires
)
