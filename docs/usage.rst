Usage
=====

Installation
------------

Install using pip:

.. code-block:: shell

    pip install plot-cli

Plot Graphs
-----------

To plot from file, use :code:`-i` option:

.. code-block:: shell

    plot -i data.csv

To plot from stdin:

.. code-block:: shell

    cat data.csv | plot

To save to file, use :code:`-o` option:

.. code-block:: shell

    plot -i data.csv -o plot.png

If you do not use :code:`-o` option, it is saved in a temporary file and opened.

To use tsv file:

.. code-block:: shell

    plot -i data.tsv --delimiter '\t'

To change `style <https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html>`_:

.. code-block:: shell

    plot --style ggplot

See also :code:`plot --help`.

Available Graph Types
---------------------

Subcommands allow you to use a variety of graphs.

========== ============
subcommand graph type
========== ============
line       Line graph
bar        Bar graph
area       Area plot
box        Box plot
hist       Histogram
scatter    Scatter plot
pie        Pie chart
========== ============

Shell Complete
--------------

The plot-cli supports Shell completion.

For Bash, add this to :code:`~/.bashrc`:

.. code-block:: shell

    eval "$(_PLOT_COMPLETE=source plot)"

For Zsh, add this to :code:`~/.zshrc`:

.. code-block:: shell

    eval "$(_PLOT_COMPLETE=source_zsh plot)"

For Fish, add this to :code:`~/.config/fish/completions/plot-cli.fish`:

.. code-block:: shell

    eval (env _PLOT_COMPLETE=source_fish plot)
