

********
Download
********

.. _stable-releases:

HyperSpy
========


There are multiple ways to install HyperSpy, please refer to the 
`installation chapter of the User Guide <http://hyperspy.org/hyperspy-doc/current/user_guide/install.html>`_ for details.

If you are on Microsoft Windows and you are new to Python the easiest way to get started is installing the Windows bundle below. For other platforms and experienced users we recommend installing with `Anaconda <http://hyperspy.org/hyperspy-doc/current/user_guide/install.html#quick-instructions-to-install-hyperspy-using-anaconda-linux-macos-windows>`_. 


Windows bundle installers
-------------------------

These installers install `WinPython <https://winpython.github.io/>`_ 3.5.1.2
modified to include HyperSpy and its dependencies. This is the *recommended
installation method* in Windows for users not familiar with Python. Since v1.2 the bundle distribution
includes `HyperSpyUI <http://hyperspy.org/hyperspyUI/>`_.

`HyperSpy-1.3 for Windows 32-bits
<https://github.com/hyperspy/hyperspy/releases/download/v1.3/HyperSpy-v1.3-Bundle-Windows-32bit.exe>`_

`HyperSpy-1.3 for Windows 64-bits
<https://github.com/hyperspy/hyperspy/releases/download/v1.3/HyperSpy-v1.3-Bundle-Windows-64bit.exe>`_


.. NOTE::

   If HyperSpy fails to start install the Visual C++ 2015 (`x64 and x86 <https://www.visualstudio.com/downloads/download-visual-studio-vs#d-visual-c>`_ for CPython 3.5) redistributable packages.

Older releases are available in `GitHub <https://github.com/hyperspy/hyperspy/releases>`_.

Related software
================


.. _import-rpl:

ImportRPL Digital Micrograph plugin
-----------------------------------

Lastest version release date: 24/05/2012. Minor bugs were solved and new features added.

This Digital Micrograph plugin is designed to import Ripple files into Digital Micrograph. 
It is used to ease data transit between DigitalMicrograph and HyperSpy without losing 
the calibration using the extra keywords that HyperSpy adds to the standard format.

When executed it will ask for 2 files:

#. The riple file with the data  format and calibrations
#. The data itself in raw format.

If a file with the same name and path as the riple file exits
with raw or bin extension it is opened directly without prompting

ImportRPL was written by Luiz Fernando Zagonel.


`Download ImportRPL <https://github.com/downloads/hyperspy/ImportRPL/ImportRPL.s>`_

.. _hyperspy-matlab:

readHyperSpyH5 MATLAB Plugin
---------------------------

Initial release date: 18/04/2017. 

This MATLAB script is designed to import HyperSpy's saved .hdf5 files. 
Like the Digital Micrograph script above, it is used to easily transfer data
between MATLAB and HyperSpy without losing the axial calibration information.
The underlying data is returned as the primary output, and axis metadata 
(such as names, units, scales, etc.) are returned as supplemental output.

The script has been tested on 2D and 3D hyperspectral data (spectrum images),
but should work for arbitrarily sized data. Please raise an issue on 
`Github <https://github.com/hyperspy/hyperspy/issues>`_ or in the 
`Gitter chat <https://gitter.im/hyperspy/hyperspy>`_ with any issues.

readHyperSpyH5 was written by `Joshua Taillon <https://www.nist.gov/people/joshua-taillon>`_.

`Download readHyperSpyH5 <https://github.com/downloads/hyperspy/readHyperSpyH5/readHyperSpyH5.m>`_
