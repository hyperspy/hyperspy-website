This repository host the source code of the [hyperspy.org](https://hyperspy.org) website. The built website is pushed automatically to the [hyperspy/hyperspy.github.com](https://github.com/hyperspy/hyperspy.github.com) repository.

# Build the website

The website is built using the [Sphinx](https://www.sphinx-doc.org) framework and the [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io).

To install the dependencies in a python environment:
```
pip install -r requirement.txt
```

To build the website
```
make html
```

# Add a news entry

The news entries are managed using the [ABlog](https://ablog.readthedocs.io) Sphinx extension.

- add a entry in the `news` folder
- use the `post` directive
