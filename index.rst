:sd_hide_title:
:html_theme.sidebar_secondary.remove:

.. title:: Home

.. toctree::
   :hidden:

   sections/about
   news/index

.. grid:: 1 2 2 2

    .. grid-item::
        :columns: 12 5 5 5
        :child-align: center

        .. image:: _static/hyperspy_light_banner.svg
           :alt: HyperSpy logo
           :class: logo, mainlogo, only-light
           :align: center
           :width: 500

        .. image:: _static/hyperspy_dark_banner.svg
           :alt: HyperSpy logo
           :class: logo, mainlogo, only-dark
           :align: center
           :width: 500


    .. grid-item::
        :columns: 12 7 7 7

        .. div:: sd-text-left sd-font-weight-bold sd-fs-4 sd-width-50

           Open source Python framework for exploring, visualizing and analyzing
           multi-dimensional data

        .. button-link:: https://hyperspy.org/hyperspy-doc/current/user_guide/index.html
            :color: primary
            :shadow:
            :class: sd-rounded-3

            :fa:`rocket` Get Started


.. grid:: 2 3 3 3
  :gutter: 4

  .. grid-item-card::

    :octicon:`eye;2em;sd-text-info` Visualization
    ^^^

    Interactive :external+hyperspy:ref:`visualization tools <visualization-label>`
    for multi-dimensional spectra and images.

  .. grid-item-card::

    :octicon:`gear;2em;sd-text-info` Analysis
    ^^^

    Easy access to analytical tools that exploit the multi-dimensionality
    of datasets, including :external+hyperspy:ref:`curve fitting <model-label>`
    and :external+hyperspy:ref:`blind source separation<ml-label>`.

  .. grid-item-card::

    :octicon:`table;2em;sd-text-info` Named and Scaled Axes
    ^^^

    :external+hyperspy:ref:`Two families of axes <axes-handling>`: *signal* and
    *navigation* with powerful numpy-style indexing mechanism and support for
    non-uniform axes.

  .. grid-item-card::

    :octicon:`zap;2em;sd-text-info` Performance
    ^^^

    Built on top of `NumPy <https://numpy.org>`_, `SciPy <https://scipy.org>`_,
    `Numba <https://numba.pydata.org/>`_, `Matplotlib <https://matplotlib.org>`_,
    `Dask <https://dask.org>`_ and `Scikit-learn <https://scikit-learn.org>`_ for
    high performance and stability.

  .. grid-item-card::

    :octicon:`rocket;2em;sd-text-info` Ecosystem
    ^^^

    :ref:`Domain-specific libraries <ecosystem_label>` and modular design for
    :external+hyperspy:ref:`easy extensibility <writing_extensions-label>`.

  .. grid-item-card::

    :octicon:`people;2em;sd-text-info` Community Driven
    ^^^

    :external+hyperspy:ref:`Developed and maintained <development>` by scientists
    for scientists.


.. rst-class:: text-center sd-font-weight-bold sd-fs-3

   Latest News

.. postlist:: 3
   :list-style: circle
   :format: {title}


.. _ecosystem_label:

.. rst-class:: text-center sd-font-weight-bold sd-fs-3

   HyperSpy Ecosystem


.. grid:: 2 3 4 5
   :gutter: 3

   .. grid-item-card:: HyperSpy
      :img-top: _static/hyperspy_logo.png
      :img-alt:
      :link: https://hyperspy.org/hyperspy-doc/current

      ^^^
      Generic multi-dimensional data analysis toolbox

   .. grid-item-card:: RosettaSciIO
      :img-top: _static/rosettasciio.svg
      :img-alt:
      :link: https://hyperspy.org/rosettasciio/

      ^^^
      Reading and writing scientific data formats


   .. grid-item-card:: exSpy
      :img-top: _static/hyperspy_logo.png
      :img-alt:
      :link: https://hyperspy.org/exspy

      ^^^
      X-rays Energy Dispersive Spectroscopy (EDS) and Electron Energy Loss Spectroscopy (EELS)

   .. grid-item-card:: pyxem
      :img-top: _static/pyxem.png
      :img-alt:
      :link: https://pyxem.readthedocs.io

      ^^^
      Electron diffraction data (4DSTEM)

   .. grid-item-card:: kikuchipy
      :img-top: _static/kikuchipy.svg
      :img-alt:
      :link: https://kikuchipy.org/

      ^^^
      Electron backscatter diffraction (EBSD)

   .. grid-item-card:: LumiSpy
      :img-top: _static/lumispy.svg
      :img-alt:
      :link: https://docs.lumispy.org

      ^^^
      Luminescence spectroscopy (cathodoluminescence, photoluminescence, Raman)

   .. grid-item-card:: atomap
      :img-top: _static/atomaplogo.png
      :img-alt:
      :link: https://atomap.org

      ^^^
      Atomic resolution scanning transmission electron

   .. grid-item-card:: HoloSpy
      :img-top: _static/hyperspy_logo.png
      :img-alt:
      :link: https://hyperspy.org/holospy

      ^^^
      Off-axis electron holograph

   .. grid-item-card:: HyperSpyUI
      :img-top: _static/hyperspyui_logo.png
      :img-alt:
      :link: https://hyperspy.org/hyperspyUI

      ^^^
      Streamlined user interface to HyperSpy


.. _support_label:

.. rst-class:: text-center sd-font-weight-bold sd-fs-3

   Support


.. grid:: 2 2 4 4
  :gutter: 4

  .. grid-item-card::

    User Guides
    ^^^

    Comprehensive documentation on how to use `Hyperspy <https://hyperspy.org/hyperspy-doc/current>`_
    and the various extensions that form the :ref:`Ecosystem <ecosystem_label>`.

  .. grid-item-card::

    Tutorials
    ^^^

    Tutorials in the form of jupyter notebooks to demonstrate typical analysis
    workflows are hosted in dedicated repositories for each library, see e.g.
    `HyperSpy demos <https://github.com/hyperspy/hyperspy-demos>`_.

  .. grid-item-card::

    Workshops
    ^^^

    Attend one of the HyperSpy workshops organised regularly. Past and future
    events can be found under :ref:`news_label`.

  .. grid-item-card::

    Chat
    ^^^

    Ask the HyperSpy Community on the `Gitter chat <https://gitter.im/hyperspy/hyperspy>`_.

    .. image:: https://img.shields.io/gitter/room/hyperspy/hyperspy
        :target: https://gitter.im/hyperspy/hyperspy
        :alt: Gitter chat
