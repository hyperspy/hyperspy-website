

********
Download
********

.. _stable-releases:

Stable release
==============

.. warning::

    **Since version 0.8.4 HyperSpy only supports Python 3. If you need to install
    HyperSpy in Python 2.7 install HyperSpy 0.8.3.**

This page contains links to HyperSpy installers for different operating systems.
These installers should meet the needs of most users.  Advanced installation options are
documented in the `User Guide
<http://hyperspy.org/hyperspy-doc/current/user_guide/install.html>`_.


Windows
-------


1. Windows bundle installers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These installers install `WinPython <https://winpython.github.io/>`_ 3.5.1.2
modified to include HyperSpy and its dependencies. This is the *recommended
installation method* in Windows for users not familiar with Python.

`HyperSpy-0.8.5 for Windows 32-bits
<https://github.com/hyperspy/hyperspy/releases/download/v0.8.5/HyperSpy-0.8.5-Bundle-Windows-32bit.exe>`_

`HyperSpy-0.8.5 for Windows 64-bits
<https://github.com/hyperspy/hyperspy/releases/download/v0.8.5/HyperSpy-0.8.5-Bundle-Windows-64bit.exe>`_



.. NOTE::

   If HyperSpy fails to start install the Microsoft Visual C++ 2008
   redistributable packages (`64 bit
   <http://www.microsoft.com/download/en/details.aspx?id=15336>`_ or `32 bit
   <http://www.microsoft.com/download/en/details.aspx?id=29>`_).


.. _python_installers:

2. Windows HyperSpy Python installers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The  Python installers install only HyperSpy i.e. Python and all the required
libraires must be installed separately. This installation method is only
recommend for users who are familiar with Python. You can
download the Python installers from `pypi
<https://pypi.python.org/pypi/hyperspy>`_.

Mac OS, Linux and Windows
-------------------------

Follow `this link
<http://hyperspy.org/hyperspy-doc/current/user_guide/install.html#quick-instructions-to-install-hyperspy-using-anaconda-linux-macos-windows>`_
for quick instructions on how to install HyperSpy in MacOS, Linux or Windows
using Anaconda.


Related software
================

.. _import-rpl:

ImportRPL Digital Micrograph plugin
-----------------------------------

Lastest version release date: 24/05/2012. Minor bugs were solved and new features added.

This Digital Micrograph plugin is designed to import Ripple files into Digital Micrograph. It is used to easy data transit between DigitalMicrograph and HyperSpy without losing the calibration using the extra keywords that HyperSpy adds to the standard format.

When executed it will ask for 2 files:

#. The riple file with the data  format and calibrations
#. The data itself in raw format.

If a file with the same name and path as the riple file exits
with raw or bin extension it is opened directly without prompting

ImportRPL was written by Luiz Fernando Zagonel.


`Download ImportRPL <https://github.com/downloads/hyperspy/ImportRPL/ImportRPL.s>`_
