import setuptools

with open('README.rst') as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    install_requires = fh.read()

setuptools.setup(
    name='vs_transitions',
    version='0.0.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/OrangeChannel/vs-transitions',
    author='Dave',
    author_email='orangechannel@pm.me',
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
        'Documentation': '',
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
