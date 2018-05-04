.. django-goodgrids documentation master file, created by
   sphinx-quickstart on Fri May  4 16:56:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-goodgrids's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

django-goodgrids
================

`django-goodgrids` is a client library for GoodGrids. If your application is currently
serving CSV files, it can be extended to allow beautiful Excel downloads with ease.

About GoodGrids
===============

`GoodGrids`_ is a service for creating Excel files from CSV files
programmatically. You upload an example Excel file to serve as a
template. You can then use the GoodGrids API to create Excel files from
CSV files based on this template. You can style cells, include formulas,
and avoid all the issues that plague CSV files.

Using GoodGrids with class-based views
======================================

Let’s assume your Django application already has a class-based view
``DownloadDataCSVView`` that returns a CSV file for your users to
download. To create a view that let’s your users download Excel files,
use the following snippet:

.. code:: python

   from django_goodgrids.views import DownloadDataAsExcelView

   class DownloadDataAsExcelView(GoodGridsExcelExportViewMixin, DownloadDataCSVView):
       goodgrids_api_url = 'https://goodgrids.com/create-excel-file/3a6c0d9ac7c74d'
       excel_file_name = 'data.xlsx'

Make sure to set ``goodgrids_api_url`` to your actual API URL.

You can then include this in your ``urls.py``:

.. code:: python

   url(r'^download-data-as-excel-file/?$',
       views.DownloadDataAsExcelView.as_view(),
       name='download_data_as_excel_file'),

Using Goodgrids with function-based views
=========================================

Let’s assume your Django application already has a function-based view
named ``download_data_as_csv_view`` that returns a CSV file for your
users to download. To create a view that let’s your users download Excel
files, use the following snippet:

.. code:: python

   from django_goodgrids.views import create_goodgrids_excel_export_view

   download_data_as_excel_view = create_goodgrids_excel_export_view(
       csv_export_view=download_data_as_csv_view,
       goodgrids_api_url='https://goodgrids.com/create-excel-file/3a6c0d9ac7c74d',
       excel_file_name='data.xlsx',
   )

Make sure to set ``goodgrids_api_url`` to your actual API URL.

You can then include this in your ``urls.py``:

.. code:: python

   url(r'^download-data-as-excel-file/?$',
       views.download_data_as_excel_view,
       name='download_data_as_excel_file'),

.. _web-based GoodGrids API: https://goodgrids.com
.. _GoodGrids: https://goodgrids.com


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
