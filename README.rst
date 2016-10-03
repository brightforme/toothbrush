toothbrush
==========


toothbrush allows you to easily use environment variables for your app. Variables and values are stored in a centralized Redis.

Installation
------------

Method with pip: if you have pip installed, just type this in a terminal
(sudo is optional on some systems)

::

    pip install toothbrush

Method by hand: download the sources, either on PyPI or (if you want the
development version) on Github, unzip everything in one folder, open a
terminal and type

::

    python setup.py install

Usage
-----


List available variables and values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: shell

    toothbrush -h REDIS_HOST -a REDIS_PASSWORD list --app foo --stage production

Set a new variable
~~~~~~~~~~~~~~~~~~~

.. code:: shell

    toothbrush -h REDIS_HOST -a REDIS_PASSWORD set --app foo --stage production --name foo --value bar

Unset a variable
~~~~~~~~~~~~~~~~

.. code:: shell

    toothbrush -h REDIS_HOST -a REDIS_PASSWORD unset --app foo --stage production --name foo

Export your variables to a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

    toothbrush -h REDIS_HOST -a REDIS_PASSWORD export --app foo --stage production --target /path/to/your/env/file
