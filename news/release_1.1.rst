HyperSpy 1.1  has been released!
================================

.. feed-entry::
   :date: 2016-8-3

We are pleased to announce the release of HyperSpy 1.1


.. cut::

This is a minor release. Follow the following links for details on all
the `bugs fixed
<https://github.com/hyperspy/hyperspy/issues?q=label%3Abug+is%3Aclosed+milestone%3A1.1>`_.

NEW
---

* :ref:`signal.transpose`.
* :ref:`protochips-format` reader.

Enhancements
------------


* :py:meth:`~.model.BaseModel.fit` takes a new algorithm, the global optimizer
  `differential evolution`.
* :py:meth:`~.model.BaseModel.fit` algorithm, `leastsq`, inherits SciPy's bound
  constraints support (requires SciPy >= 0.17).
* :py:meth:`~.model.BaseModel.fit` algorithm names changed to be consistent
  `scipy.optimze.minimize()` notation.


