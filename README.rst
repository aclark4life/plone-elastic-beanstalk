Plone on Elastic Beanstalk
==========================

Development
-----------

*macOS*

::

    make virtualenv-2
    source bin/activate
    export LDFLAGS="-L/usr/local/opt/zlib/lib"
    export CPPFLAGS="-I/usr/local/opt/zlib/include"
    make pip-install
    make b

Deployment
----------

::

    aws elasticbeanstalk update-environment --environment-name <ENV> --solution-stack-name "64bit Amazon Linux 2018.03 v2.7.6 running Python 2.7"
