# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HyperSpy'
copyright = '2024, The HyperSpy community'
author = 'The HyperSpy community'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    "sphinx_favicon",
    "sphinx.ext.githubpages",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

favicons = ["hyperspy_logo.ico", ]


html_theme_options = {
    "external_links": [
        {
            "url": "https://hyperspy.org/hyperspy-doc/current",
            "name": "Documentation",
        },
        {
            "url": "https://hyperspy.org/hyperspy-doc/current/user_guide/install.html",
            "name": "Install",
        },
    ],
    "github_url": "https://github.com/hyperspy/hyperspy",
    "icon_links": [
        {
            "name": "Gitter",
            "url": "https://gitter.im/hyperspy",
            "icon": "fab fa-gitter",
        },
    ],
    "logo": {
        "text": "HyperSpy",
        "image_light": "_static/hyperspy_logo.png",
        "image_dark": "_static/hyperspy_logo.png",
    },
    "announcement": "<a href='https://hyperspy.org/hyperspy-doc/v2.0/changes.html'>HyperSpy 2.0 released!</a>",
    "secondary_sidebar_items": [],
}
