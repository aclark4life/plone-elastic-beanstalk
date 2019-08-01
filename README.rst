Plone on Elastic Beanstalk
==========================

Installation
------------

::

    make virtualenv-2
    source bin/activate
    export LDFLAGS="-L/usr/local/opt/zlib/lib"
    export CPPFLAGS="-I/usr/local/opt/zlib/include"
    make pip-install
    make b
