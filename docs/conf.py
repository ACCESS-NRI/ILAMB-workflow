# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from recommonmark.parser import CommonMarkParser


# -- Project information -----------------------------------------------------

project = 'ILAMB-NCI-DOC'
copyright = '2023, ACCESS-NRI'
author = 'ACCESS-NRI'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "recommonmark",
    "sphinx_markdown_tables",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns =  ['_build', 'Thumbs.db', '.DS_Store', "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# from recommonmark.parser import CommonMarkParser

# source_suffix = {
#     '.rst':'restructuredtext',
#     '.md':'markdown',
#     }   

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "use_edit_page_button": False,
    "github_url": "https://github.com/ACCESS-NRI/ILAMB-workflow",
    "logo": {
        "image_light": "source/_static/access_logo_rgb.svg",
        "image_dark": "source/_static/access_logo_rgb.svg",
    },
}