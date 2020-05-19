=======
monitor
=======


.. image:: https://img.shields.io/pypi/v/monitor.svg
        :target: https://test.pypi.org/project/monitor/0.1.9/

.. image:: https://img.shields.io/travis/fieryjoy/monitor.svg
        :target: https://travis-ci.com/fieryjoy/monitor

.. image:: https://readthedocs.org/projects/monitor/badge/?version=latest
        :target: https://samonitor.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Very basic site monitoring system based on kafka and postgresql.
The producer checks periodically the status of the site and retrieves some statistics that are put on a kafka topic.
The consumer reads statistics from the topic and stores them in a postgresql database.


* Free software: MIT license
* Documentation: https://samonitor.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
