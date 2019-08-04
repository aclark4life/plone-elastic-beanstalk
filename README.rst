Plone on Elastic Beanstalk
==========================

Development
-----------

*macOS*

Using https://github.com/aclark4life/universal-project-makefile. Pillow needs /usr/local/opt/zlib.

::

    make virtualenv-2
    source bin/activate
    export LDFLAGS="-L/usr/local/opt/zlib/lib"
    export CPPFLAGS="-I/usr/local/opt/zlib/include"
    make pip-install
    make b

Deployment
----------

EB defaults to Python 3, so to run Plone 4 we need to go back to Python 2.7.

::

    aws elasticbeanstalk update-environment --environment-name <ENV> \
        --solution-stack-name "64bit Amazon Linux 2018.03 v2.7.6 running Python 2.7"


EB deploy.

::

    make d


Debug
-----

To be run after ``eb ssh``.

::

    cd /opt/python/current
    source ./env
    cd app
