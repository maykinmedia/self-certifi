Self-certifi
============

:Version: 1.0.0
:Source: https://github.com/maykinmedia/self-certifi
:Keywords: requests, certifi, self-signed, certificates
:PythonVersion: 3.7

|build-status| |coverage| |linting| |black| |python-versions| |pypi-version|

Create a CA-bundle based on certifi_ and self-signed certificates, for usage with requests_.

.. contents::

.. section-numbering::

Features
========

* Keep original ``certifi`` CA-bundle
* Add your own custom/self-signed (root) certificates
* Configuration via environment variable

Installation
============

Requirements
------------

* Python 3.7 or newer
* setuptools 30.3.0 or above

Install
-------

.. code-block:: bash

    pip install self-certifi


Usage
=====

.. code-block:: python

    from self_certifi import load_self_signed_certs

    load_self_signed_certs("/path/to/installation/directory")

.. _certifi: https://pypi.org/project/certifi/
.. _requests: https://pypi.org/project/requests/

.. |build-status| image:: https://github.com/maykinmedia/self-certifi/workflows/Run%20CI/badge.svg
    :target: https://github.com/maykinmedia/self-certifi/actions?query=workflow%3A%22Run+CI%22
    :alt: Run CI

.. |linting| image:: https://github.com/maykinmedia/self-certifi/workflows/Code%20quality%20checks/badge.svg
    :target: https://github.com/maykinmedia/self-certifi/actions?query=workflow%3A%22Code+quality+checks%22
    :alt: Code linting

.. |coverage| image:: https://codecov.io/gh/maykinmedia/self-certifi/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/self-certifi
    :alt: Coverage status

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/self-certifi.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/self-certifi.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/self-certifi.svg
    :target: https://pypi.org/project/self-certifi/
