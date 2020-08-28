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
    :emphasize-lines: 5

    marine = core.ffms2.Source('marine.mp4')
    marine = marine.resize.Bilinear(width=320, height=180, format=marine.format.replace(subsampling_w=0, subsampling_h=0).id)[:96]
    pekora = core.ffms2.Source('pekora.mp4')
    pekora = pekora.resize.Bilinear(width=320, height=180, format=pekora.format.replace(subsampling_w=0, subsampling_h=0).id)[:96]
    fade(marine, pekora, 48).set_output()

.. image:: /images/fade.gif

.. autofunction:: vs_transitions.fade_to_black

----

**Non-linear Transitions**

.. autofunction:: vs_transitions.poly_fade
