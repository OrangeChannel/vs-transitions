# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sys
from os.path import abspath

sys.path.insert(0, abspath('..'))

__author__, __version__ = str(), str()
exec(open(abspath('../vs_transitions/_metadata.py')).read())
if not __author__ or not __version__:
    raise ValueError("setup: package missing metadata")


# -- Project information -----------------------------------------------------

project = 'vs_transitions'
author = __author__.split()[0]


# The full version, including alpha/beta/rc tags
version = release = __version__


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/theme_overrides.css'
]

html_style = 'css/theme_overrides.css'

autosummary_generate = True
autodoc_mock_imports = ['vapoursynth']
smartquotes = True
html_show_sphinx = False
# add_module_names = False
pygments_style = 'sphinx'
typehints_document_rtype = False


# -- Extension configuration -------------------------------------------------

todo_include_todos = True
