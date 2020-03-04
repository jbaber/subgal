subgal (*sub*standard *gal*lery) is a collection of tools for creating html
galleries from photos that have already been sorted by [sortphotos].

It depends on ffmpeg and imagemagick already being installed.


Installation
------------

    pip install subgal

Help
----

    subgal help

for main help

    subgal make-thumbs help

for help with `subgal make-thumbs`, etc.

subgal make-thumbs
------------------

`subgal make-thumbs` creates a directory full of thumbnails indexed by sha256 and outputs the correspondence to a json file.


subgal make-indices
-------------------

`subgal make-indices` creates .html files which are a gallery of images based on a json file as output by `subgal make-thumbs`

subgal update
-------------

`subgal update` combines information from multiple json files into one.


[sortphotos]: https://github.com/andrewning/sortphotos
