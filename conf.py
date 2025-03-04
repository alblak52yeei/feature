# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'feature'
copyright = '2025, Maxim'
author = 'Maxim'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns to exclude from source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # или 'alabaster'
html_static_path = ['_static']

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))  # Путь к корню вашего проекта

source_suffix = '.rst'
master_doc = 'docs/index' 

source_dir = 'docs'