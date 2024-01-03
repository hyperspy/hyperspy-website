# -*- coding: utf-8 -*-
#
# HyperSpy documentation build configuration file, created by
# sphinx-quickstart on Sat Dec 18 17:03 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#m
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import datetime
from packaging.version import Version
import sys, os

import sphinx
    

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('sphinxext'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.githubpages',
              ]

# Add comments to news using diskus
#disqus_shortname = 'hyperspy'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'HyperSpy'
copyright = f'2011-{datetime.today().year}, The HyperSpy development team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'pydata_sphinx_theme' 

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
   "github_url": "https://github.com/hyperspy/hyperspy",
   "icon_links": [
      {
         "name": "Gitter",
         "url": "https://gitter.im/hyperspy/hyperspy",
         "icon": "fab fa-gitter",
      },
      {
         "name": "HyperSpy",
         "url": "https://hyperspy.org",
         "icon": "_static/hyperspy.ico",
         "type": "local",
      },
   ],
   "logo": {
      "text": "HyperSpy",
   },
   "announcement": "HyperSpy API changed in version 2.0, see the <a href='https://hyperspy.org/hyperspy-doc/v2.0/changes.html'>release notes!</a>",
}

# Only works with the default theme, makes the sidebar not scroll:
#html_theme_options = { "stickysidebar": "true" }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".ke
html_title = u"HyperSpy"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "HyperSpy"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
html_logo = "images/hyperspy_banner.png"

# The name of an image file (within the static path) to use as favicon of the
# pixels large.
html_favicon = "images/hyperspy_logo.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# TODO: split this up into several chunks
html_sidebars = {
   '**': ['sidebar_versions.html', 'sidebar_links.html'],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Setting intersphinx to resolve the links to the project's docs.

intersphinx_mapping = {'hyperspy': ('https://hyperspy.org/hyperspy-doc/current/', None)}

# https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
html_baseurl = 'https://hyperspy.org'