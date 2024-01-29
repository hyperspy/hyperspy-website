# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from os import path

project = 'HyperSpy'
copyright = '2024, The HyperSpy community'
author = 'The HyperSpy community'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'ablog',
    'sphinx_design',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx_favicon',
    'sphinxcontrib.youtube',
    'selective_css',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    "hyperspy": ("https://hyperspy.org/hyperspy-doc/current/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = "https://hyperspy.org"
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_title = "HyperSpy Website"

favicons = ["hyperspy_logo.ico", ]


html_theme_options = {
    "analytics": {
        "google_analytics_id": "G-B0XD0GTW1M",
    },
    "announcement": "<font size='+1'><b><a href='https://hyperspy.org/hyperspy-doc/v2.0/changes.html'>HyperSpy 2.0 released!</a></b></font>",
    "external_links": [
        {
            "url": "https://hyperspy.org/hyperspy-doc/current",
            "name": "Documentation",
        },
        {
            "url": "https://hyperspy.org/hyperspy-doc/current/user_guide/install.html",
            "name": "Install",
        },
        {
            "url": "https://hyperspy.org/jupyterlite-hyperspy",
            "name": "Try",
        },
    ],
    "github_url": "https://github.com/hyperspy",
    "icon_links": [
        {
            "name": "Gitter",
            "url": "https://gitter.im/hyperspy/hyperspy",
            "icon": "fab fa-gitter",
        },
    ],
    "logo": {
        "text": "HyperSpy",
        "image_light": "_static/hyperspy_logo.png",
        "image_dark": "_static/hyperspy_logo.png",
    },
    "navbar_persistent": [ ],
    "secondary_sidebar_items": [],
    "show_prev_next": False,
}

# -- ABlog ---------------------------------------------------

blog_path = "news/index"
blog_authors = {
    "hyperspy": ("HyperSpy", "https://hyperspy.org"),
}

html_sidebars = {
    "sections/**": [ ],
    "news/**": [
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/authors.html",
    ],
}

# add path to local sphinx extensions
sys.path.append(path.join(path.dirname(path.abspath(__file__)), "extensions"))
