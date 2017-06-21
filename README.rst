Installation
============

Package requires at least Python 3.5.

::

  pip install -U https://github.com/eea/eea.test.git


Usage
=====

::

  seleniumtesting http://localhost/Plone/2015/ eea.test.sandbox \
    -ea roles manager username \
    -ea users "username" "password"

Please also check the ``edw.seleniumtesting`` `usage page <https://github.com/eaudeweb/edw.seleniumtesting#usage>`_ for additional information.

