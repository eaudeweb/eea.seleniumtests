Installation
============

Package requires at least Python 3.5.

::

  pip install -U https://github.com/eea/eea.seleniumtests.git


Usage
=====

::

  seleniumtesting http://localhost/Plone/ eea.seleniumtests.sandbox \
    -ea roles manager username \
    -ea users "username" "$(< pwd_file)"


Example with GNU Parallel (5 users):

::

  $ echo "secret_password" >> pwd_file

  $ cat <<'EOF' > runtest.sh
  #!/bin/bash
  sleep $1
  ./bin/seleniumtesting http://localhost/Plone/sandbox/ eea.seleniumtests.sandbox -ea roles manager username -ea users username "$(< pwd_file)"
  EOF

  $ parallel ./runtest.sh ::: {1..5}


Please also check the ``edw.seleniumtesting`` `usage page <https://github.com/eaudeweb/edw.seleniumtesting#usage>`_ for additional information.

