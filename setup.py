from setuptools import find_packages, setup
import codecs

long_description = ''
with codecs.open('./README.md', encoding='utf-8') as readme_md:
    long_description = readme_md.read()

setup(
    name='kittymocklib_py',
    packages=find_packages(include=['kittymocklib_py']),
    version='0.1.0.1',
    description='A library in python for simulated API server',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Evandro Silva',
    license='MIT',
    install_requires=[],
    setup_requires=[],
    tests_requires=['pytest==6.2.3'],
    tests_suite=['tests'],
    author_email='evandrojunior1615@gmail.com',
    url='https://github.com/Suspir0n/kitty-Mock-Lib-Python.git',
    download_url='https://github.com/Suspir0n/kitty-Mock-Lib-Python/archive/refs/tags/0.1.0.1.tar.gz',
    python_requires='>=3.6',
    maintainer='Evandro Silva, Ismael Carvalho',
    maintainer_email='evandrojunior1615@gmail.com',
)