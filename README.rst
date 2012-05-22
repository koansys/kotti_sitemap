kotti_sitemap
=============

A sitemap plugin for Kotti.

`Find out more about Kotti`_

Setup
-----

To activate the ``kotti_sitemap`` add-on in your Kotti site, you need to add an entry to the ``kotti.configurators`` setting in your Paste Deploy config.

If you don't have a ``kotti.configurators`` option, add one.
The line in your ``[app:main]`` section could then look like this::

    kotti.configurators = kotti_sitemap.kotti_configure

With this, you'll be able to use ``/sitemap.xml`` as your sitemap.

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti