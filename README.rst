==============
Music Analyser
==============

A simple script to extract a table of artist, song and play time from your YouTube Music history.

Installation
------------
This package can be installed using something like poetry.
.. code-block:: bash
    poetry add --git https://github.com/stuartncook/music_analyser.git

Alternatively, download and run
.. code-block:: bash
    poetry install

Usage
-----

Download your YouTube Music history by going to `Google Takeout <https://takeout.google.com/settings/takeout>`_. 
Deselect all and select "YouTube and YouTube Music", then click "All YouTube data included", deselect all, and just select history, 
then proceed with next steps, leaving 2 GB and zip file selected.

With the zip file downloaded run
.. code-block:: python
    from music_analyser import read_ytm_takeout
    df = read_ytm_takeout("<takeout filename>")