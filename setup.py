import setuptools
from distutils.util import convert_path

__author__, __version__ = str(), str()
exec(open(convert_path("vs_transitions/_metadata.py")).read())
if not __author__ and not __version__:
    raise ValueError("setup: package missing metadata")

with open("README.md") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    install_requires = fh.read()

setuptools.setup(
    name="vs_transitions",
    version=__version__,
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OrangeChannel/vs-transitions",
    author=__author__.split()[0],
    author_email=__author__.split()[1][1:-1],
    license="UNLICENSE",
    install_requires=install_requires,
    extras_require={"better wipe gradient creation": ["numpy>=1.16.0"]},
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
        "Documentation": "https://vapoursynth-transitions.readthedocs.io/en/latest/",
        "Source": "https://github.com/OrangeChannel/vs-transitions/blob/master/vs_transitions/__init__.py",
        "Tracker": "https://github.com/OrangeChannel/vs-transitions/issues",
    },
    packages=setuptools.find_packages(),
    package_data={"vs_transitions": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.8",
)
