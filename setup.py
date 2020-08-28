from distutils.util import convert_path

import setuptools

meta = {}
exec(open(convert_path('vs_transitions/_metadata.py')).read(), meta)

with open('README.rst') as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    install_requires = fh.read()

setuptools.setup(
    name='vs_transitions',
    version=meta['__version__'],
    description='',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/OrangeChannel/vs-transitions',
    author=meta['__author__'].split()[0],
    author_email=meta['__author__'].split()[1][1:-1],
    license='UNLICENSE',
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "License :: Public Domain",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Non-Linear Editor",
        "Typing :: Typed",
    ],
    keywords="vapoursynth encoding powerpoint transitions",
    project_urls={
        'Documentation': 'https://vapoursynth-transitions.readthedocs.io/en/latest/',
        'Source': 'https://github.com/OrangeChannel/vs-transitions/blob/master/vs_transitions/__init__.py',
        'Tracker': 'https://github.com/OrangeChannel/vs-transitions/issues',
    },
    packages=setuptools.find_packages(),
    package_data={
        'vs_transitions': ['py.typed']
    },
    include_package_data=True,
    python_requires='>=3.8',
)
