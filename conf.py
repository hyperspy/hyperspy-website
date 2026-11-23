# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime
import sys
from os import path, environ

from docutils import nodes
from sphinx.application import Sphinx

project = 'HyperSpy'
copyright = f"2007-{datetime.today().year}, The HyperSpy community"
author = 'The HyperSpy community'
language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'ablog',
    'selective_css',
    'sphinx_design',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx_favicon',
    'sphinx_sitemap',
    'sphinxcontrib.youtube',
]

linkcheck_ignore = [
    "https://sbmm.org.br/en/28o-csbmm",  # 403 Client Error: Forbidden for url
    "https://www.diamond.ac.uk/Home/Events",  # - 403 Client Error: Forbidden for url: https://www.diamond.ac.uk/Home/Events/2023/HyperSpy_2023.html
    "https://microscopy.org/files", # - Recurring connection timeout error
    "https://doi.org/10.5281/zenodo.592838",  # - 403 Client Error: Forbidden for url: https://doi.org/10.5281/zenodo.592838
    "https://dx.doi.org/10.5281/zenodo.16850", # - 403 Client Error: Forbidden for url: https://dx.doi.org/10.5281/zenodo.16850
    "https://zenodo.org",  # - 403 Client Error: Forbidden for url: https://zenodo.org
]

# sitemap settings
html_baseurl = environ.get("SPHINX_HTML_BASE_URL", "https://hyperspy.org")
sitemap_url_scheme = "{link}"
sitemap_show_lastmod = True

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
    "announcement": "<font size='+1'><b><a href='https://hyperspy.org/news/Award2025.html'>HyperSpy receives Award for Open Source Research Software!</a></b></font>",
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
        "alt_text": "HyperSpy",
        "image_light": "_static/hyperspy-banner-small-light.svg",
        "image_dark": "_static/hyperspy-banner-small-dark.svg",
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


# -- Define a custom role for GitHub -------------------------
# Inline SVG of GitHub logo (official, scalable, no external deps)
# Inline SVG of GitHub logo (official, scalable)
GITHUB_SVG = (
    '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" '
    'xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">'
    '<path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.205 11.385.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.466-1.334-5.466-5.931 0-1.31.469-2.38 1.236-3.22-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.3 1.23.957-.266 1.988-.399 3.004-.404 1.016.005 2.047.138 3.006.404 2.28-1.552 3.289-1.23 3.289-1.23.653 1.653.242 2.874.118 3.176.77.838 1.235 1.908 1.235 3.22 0 4.61-2.805 5.625-5.479 5.921.42.36.811 1.096.811 2.22 0 1.606-.015 2.897-.015 3.286 0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>'
    '</svg>'
)

def github_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    url = f"https://github.com/{text}"
    node = nodes.reference(
        rawtext,
        '',  # No text content — icon only
        refuri=url,
        target='_blank',
        title=f"View on GitHub: {text}",
        classes=['github-link'],
        **options
    )
    # Add the SVG as raw HTML inside the link
    node += nodes.raw('', GITHUB_SVG, format='html')
    return [node], []

def setup(app: Sphinx):
    app.add_role('gh', github_role)
    return {'version': '0.1', 'parallel_read_safe': True, 'parallel_write_safe': True}
