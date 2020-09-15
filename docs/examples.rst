Examples
========

Line Graph
----------

Basic Line
^^^^^^^^^^

.. code-block:: csv

    1
    3
    2

.. code-block:: shell

    plot line -i simple.csv

.. image:: https://user-images.githubusercontent.com/6437204/78481527-cdc54c00-7780-11ea-98b2-370c8c4ae702.png
    :alt: Basic Line

with Header
^^^^^^^^^^^

.. code-block:: csv

    x
    1
    3
    2

.. code-block:: shell

    plot line -i simple-with-header.csv --header


.. image:: https://user-images.githubusercontent.com/6437204/78469555-43b7bc00-775d-11ea-9ab9-83761b2a8944.png
    :alt: Basic Line with Header

Set Title, Label and Legend
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    plot line -i simple.csv --title "Basic Line" --x-label x --y-label y --legends line


.. image:: https://user-images.githubusercontent.com/6437204/78469531-1408b400-775d-11ea-9863-814f2a6b13ff.png
    :alt: Basic Line with Title and Label

Change line style
^^^^^^^^^^^^^^^^^

.. code-block:: shell

    plot line -i simple.csv --marker o --linestyle dashed

.. image:: https://user-images.githubusercontent.com/6437204/78501898-03762f00-7799-11ea-8cf6-473389ee3313.png
    :alt: Basic Line Changed Style

Multiple Lines
--------------

.. code-block:: csv

    year,a,b
    1990,20,4
    1997,18,25
    2003,489,281
    2009,675,600
    2014,1776,1900


.. code-block:: shell

    plot line -i multiple.csv --header --index-col 0


.. code-block:: shell

    plot line -i multiple.csv --header --index-col year


.. image:: https://user-images.githubusercontent.com/6437204/78489195-f0586480-7782-11ea-9160-0cbee89ccaf1.png
    :alt: Multiple Lines

Bar Graph
---------

Vertical Bar
^^^^^^^^^^^^

.. code-block:: shell

    plot bar -i random.csv --header

.. image:: https://user-images.githubusercontent.com/6437204/78498634-6ca07700-7786-11ea-8ff0-4dbf9c273c3b.png
    :alt: Vertical Bar

Horizontal Bar
^^^^^^^^^^^^^^

.. code-block:: shell

    plot bar -i random.csv --header --horizontal


.. image:: https://user-images.githubusercontent.com/6437204/78498666-90fc5380-7786-11ea-8fda-69422227290b.png
    :alt: Horizontal Bar

Stacked Bar
^^^^^^^^^^^

.. code-block:: shell

    plot bar -i random.csv --header --stacked


.. image:: https://user-images.githubusercontent.com/6437204/78498807-6f4f9c00-7787-11ea-8b48-53f4ad19a889.png
    :alt: Stacked Bar

Histogram
---------

Basic Histogram
^^^^^^^^^^^^^^^

.. code-block:: shell

    plot hist -i uniform.csv --header --use-cols 0 --no-legend

.. image:: https://user-images.githubusercontent.com/6437204/78499145-fbfb5980-7789-11ea-84e1-8192b7493384.png
    :alt: Basic Hist

Multiple Histogram
^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    plot hist -i uniform.csv --header --alpha 0.5


.. image:: https://user-images.githubusercontent.com/6437204/78499522-1f270880-778c-11ea-8dd5-a49f411e54d4.png
    :alt: Multiple Hist

Box Plot
--------

.. code-block:: shell

    plot box -i random.csv --header


.. image:: https://user-images.githubusercontent.com/6437204/78500061-5d71f700-778f-11ea-9c8e-ff44600ba38f.png
    :alt: Box Plot

Area Plot
---------

.. code-block:: shell

    plot area -i random.csv --header


.. image:: https://user-images.githubusercontent.com/6437204/78500345-d160cf00-7790-11ea-9faf-f1429253736d.png
    :alt: Area Plot

Scatter Plot
------------

.. code-block:: shell

    plot scatter -i random.csv --header


.. image:: https://user-images.githubusercontent.com/6437204/78500349-d4f45600-7790-11ea-9c30-4081942a19b9.png
    :alt: Scatter

Pie Chart
------------

.. code-block:: shell

    plot pie -i with-index.csv --index-col 0 --header


.. image:: https://user-images.githubusercontent.com/6437204/78500945-6b764680-7794-11ea-9451-3c17a9b07416.png
    :alt: Pie Chart
