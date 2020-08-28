=============
API Reference
=============

.. automodule:: vs_transitions


Direction Enumeration
=====================

.. autoclass:: vs_transitions.Direction
    :members:


Non-directional Transitions
===========================

**Linear Transitions**

.. autofunction:: vs_transitions.fade

.. code-block:: python
    :emphasize-lines: 3

    marine = core.ffms2.Source('marine.mp4').resize.Bilinear(width=320, height=180, format=vs.YUV444P8)[:96]
    pekora = core.ffms2.Source('pekora.mp4').resize.Bilinear(width=320, height=180, format=vs.YUV444P8)[:96]
    fade(marine, pekora, 48).set_output()

.. image:: /images/fade.gif
    :align: center
    :target: https://twitter.com/kaynimatic

.. autofunction:: vs_transitions.fade_to_black

----

**Non-linear Transitions**

.. autofunction:: vs_transitions.poly_fade
