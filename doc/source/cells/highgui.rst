.. _ecto_opencv.highgui:

Highgui Cells
==============
Common opencv image input and out, plus display.


Tricks
------

Saving images on a key stroke
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ectocell:: ecto_opencv.highgui imshow

imshow accepts an optional dict of string to key value, that it will output as
trigger bools, useful with the :ref:`ecto.If` idiom.

See :ref:`sample-imshow-save`


Reference
---------
.. ectomodule:: ecto_opencv.highgui
