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

.. postlist::
   :list-style: circle
   :format: {title}
   :tags: upcoming


.. _ecosystem_label:

.. rst-class:: text-center sd-font-weight-bold sd-fs-3

   HyperSpy Ecosystem

.. list-table:: 
   :widths: 12 5 30
   :header-rows: 0

   * - .. image:: _static/hyperspy-banner-small-light.svg
           :alt: HyperSpy logo
           :class: only-light
           :target: https://hyperspy.org/hyperspy-doc/current
           :height: 50
       .. image:: _static/hyperspy-banner-small-dark.svg
           :alt: HyperSpy logo
           :class: only-dark
           :target: https://hyperspy.org/hyperspy-doc/current
           :height: 50
     - `HyperSpy <https://hyperspy.org/hyperspy-doc/current>`_
     - Generic multi-dimensional data analysis toolbox
   * - .. image:: _static/rosettasciio-banner-light.svg
           :alt: RosettaSciIO logo
           :class: only-light
           :target: https://hyperspy.org/rosettasciio/
           :height: 50
       .. image:: _static/rosettasciio-banner-dark.svg
           :alt: RosettaSciIO logo
           :class: only-dark
           :target: https://hyperspy.org/rosettasciio/
           :height: 50
     - `RosettaSciIO <https://hyperspy.org/rosettasciio/>`_
     - Reading and writing scientific data formats
   * - .. image:: _static/exspy-banner-light.svg
           :class: only-light
           :alt: eXSpy logo
           :target: https://hyperspy.org/exspy
           :height: 50
       .. image:: _static/exspy-banner-dark.svg
           :class: only-dark
           :alt: eXSpy logo
           :target: https://hyperspy.org/exspy
           :height: 50
     - `eXSpy <https://hyperspy.org/exspy>`_
     - X-rays Energy Dispersive Spectroscopy (EDS) and Electron Energy Loss Spectroscopy (EELS) data analysis
   * - .. image:: _static/pyxem-banner.svg
           :class: sd-bg-transparent
           :alt: pyxem logo
           :target: https://pyxem.readthedocs.io
           :height: 50
     - `pyxem <https://pyxem.readthedocs.io>`_
     - 4D-STEM (electron diffraction data) analysis
   * - .. image:: _static/kikuchipy-banner-light.svg
           :class: only-light
           :alt: kikuchipy logo
           :target: https://kikuchipy.org
           :height: 50
       .. image:: _static/kikuchipy-banner-dark.svg
           :class: only-dark
           :alt: kikuchipy logo
           :target: https://kikuchipy.org
           :height: 50
     - `kikuchipy <https://kikuchipy.org>`_
     - Electron backscatter diffraction (EBSD) data analysis
   * - .. image:: _static/lumispy-banner-light.svg
           :class: only-light
           :alt: lumiSpy logo
           :target: https://lumispy.org
           :height: 50
       .. image:: _static/lumispy-banner-dark.svg
           :class: only-dark
           :alt: lumiSpy logo
           :target: https://lumispy.org
           :height: 50
     - `lumiSpy <https://lumispy.org>`_
     - Luminescence spectroscopy data analysis (cathodoluminescence, photoluminescence, Raman, ...)
   * - .. image:: _static/atomap-banner.png
           :class: sd-bg-transparent
           :alt: Atomap logo
           :target: https://atomap.org
           :height: 50
     - `Atomap <https://atomap.org>`_
     - Analysis of atomic resolution scanning transmission electron microscopy images
   * - .. image:: _static/holospy-banner-light.svg
           :class: only-light
           :alt: holoSpy logo
           :target: https://hyperspy.org/holospy
           :height: 50
       .. image:: _static/holospy-banner-dark.svg
           :class: only-dark
           :alt: holoSpy logo
           :target: https://hyperspy.org/holospy
           :height: 50
     - `holoSpy <https://hyperspy.org/holospy>`_
     - Off-axis electron holography data analysis
   * - .. image:: _static/particlespy-banner-light.svg
           :class: only-light
           :alt: ParticleSpy logo
           :target: https://epsic-dls.github.io/particlespy
           :height: 50
       .. image:: _static/particlespy-banner-dark.svg
           :class: only-dark
           :alt: ParticleSpy logo
           :target: https://epsic-dls.github.io/particlespy
           :height: 50
     - `ParticleSpy <https://epsic-dls.github.io/particlespy>`_
     -  Segmentation and analysis of nanoparticles from electron microscopy data
   * - .. image:: _static/etspy-banner-light.svg
           :class: only-light
           :alt: ETSpy logo
           :target: https://pages.nist.gov/etspy
           :height: 50
       .. image:: _static/etspy-banner-dark.svg
           :class: only-dark
           :alt: ETSpy logo
           :target: https://pages.nist.gov/etspy
           :height: 50
     - `ETSpy <https://pages.nist.gov/etspy>`_
     -  Processing, alignment, and reconstruction of electron tomography data
   * - .. image:: _static/hyperspyui-banner-light.svg
           :class: only-light
           :alt: HyperSpyUI logo
           :target: https://hyperspy.org/hyperspyUI
           :height: 50
       .. image:: _static/hyperspyui-banner-dark.svg
           :class: only-dark
           :alt: HyperSpyUI logo
           :target: https://hyperspy.org/hyperspyUI
           :height: 50
     - `HyperSpyUI <https://hyperspy.org/hyperspyUI>`_
     - Streamlined user interface to HyperSpy


.. _support_label:

.. rst-class:: text-center sd-font-weight-bold sd-fs-3

   Support


.. grid:: 2 2 4 4
  :gutter: 4

  .. grid-item-card::

    User Guides
    ^^^

    Comprehensive documentation on how to use `Hyperspy <https://hyperspy.org/hyperspy-doc/current>`__
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

    .. button-link:: https://gitter.im/hyperspy/hyperspy
        :color: primary
        :shadow:
        :class: sd-rounded-3

        :fa:`comments` Chat on Gitter

.. rst-class:: text-center sd-font-weight-bold sd-fs-3

   Cite

.. grid:: 1 1 1 1

    .. grid-item::
        :columns: 12 8 8 8 

        If you use HyperSpy and its extensions, please cite it in your publications. Our 
        software is made by scientists who generously donate their time and attention. 
        Citations help us justify the effort that goes into building and maintaining 
        this project. Each of our libraries obtains DOIs from `zenodo 
        <https://zenodo.org>`_ that can be found in the respective :ref:`documentations 
        <ecosystem_label>`. DOIs for specific 
        versions of HyperSpy can be found by clicking on the `Concept DOI 
        <https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning>`_ button.
        

    .. grid-item::
        :columns: 12 4 4 4
        :margin: auto

        .. button-link:: https://doi.org/10.5281/zenodo.592838
            :color: primary
            :shadow:
            :class: sd-rounded-3
            :align: center

            :fa:`bookmark` HyperSpy DOI: 10.5281/zenodo.592838


.. meta::
    :description lang=en:
        Landing page of the HyperSpy project with information on the main 
        features and characteristics, related projects extending the 
        functionality, latest news and possibilities to get support and learn 
        about the project. HyperSpy is an open-source  python project to ease 
        analysis and visualization of multi-dimensional datasets
    :keywords:
        HyperSpy, python, numpy, scipy, physics, materials science, 
        semiconductors, scientific data analysis, spectral imaging, spectrum 
        image, hyperspectral, hyperspectrum, hyperspectral imaging, 
        multidimensional, multidimensional data, multi-dimensional data, 
        analysis, visualization, quantification, curve fitting, machine 
        learning, denoising, principal component analysis, RosettaSciIO, eXSpy, 
        pyxem, kikuchipy, LumiSpy, Atomap, holoSpy, ParticleSpy, HyperSpyUI, 
        microscopy, electron microscopy, EELS, electron energy loss 
        spectroscopy, EDX, EDS, energy-disperspive X-ray spectroscopy, 4D-STEM, 
        scanning transmission electron microscopy, EBSD, energy backscatter 
        diffraction, high-resolution electron microscopy, spectroscopy, 
        luminescence spectroscopy, CL, cathodoluminescence, PL, 
        photoluminescence, electron holography, off-axis electron holography, 
        segmentation, particle analysis
