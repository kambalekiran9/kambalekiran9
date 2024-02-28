# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'dba-tutorial-By Kiran Kambale'

html_sidebars = {
    '**': ['custom_sidebar.html'],
}

copyright = '2024, Kiran.kambale'
author = 'Kiran.kambale'
release = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Kiran basic info :

#html_sidebars = {
 #   '**': ['about.html']
#}

#html_logo = '/home/kiran/kambalekiran9/docs/images/kiran3.png'
#html_logo_width = 80
#html_logo_height = 15 
