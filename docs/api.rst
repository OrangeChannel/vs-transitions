=============
API Reference
=============

.. automodule:: vs_transitions


Direction Enumeration
=====================

.. autoclass:: vs_transitions.Direction
    :members:
    :undoc-members:


Non-directional Transitions
===========================

**Linear Transitions**

.. autofunction:: vs_transitions.fade

.. code-block:: python
    :emphasize-lines: 3

    marine = core.ffms2.Source('marine.mp4').resize.Bilinear(width=320, height=180)[:96]
    pekora = core.ffms2.Source('pekora.mp4').resize.Bilinear(width=320, height=180)[:96]
    fade(marine, pekora, 48).set_output()

.. image:: /images/fade.gif
    :align: center
    :target: https://twitter.com/kaynimatic

.. autofunction:: vs_transitions.fade_to_black

.. code-block:: python
    :emphasize-lines: 2

    pekora = core.ffms2.Source('pekora.mp4').resize.Bilinear(width=320, height=180)[:96]
    fade_to_black(pekora, 48).set_output()

.. image:: /images/fade_to_black.gif
    :align: center
    :target: https://twitter.com/kaynimatic

----

**Non-linear Transitions**

.. autofunction:: vs_transitions.poly_fade

.. code-block:: python
    :emphasize-lines: 17

    red = core.std.BlankClip(format=vs.RGB24, color=[255, 0, 0], length=96, width=320, height=40)
    blue = core.std.BlankClip(format=vs.RGB24, color=[0, 0, 255], length=96, width=320, height=40)
    div = core.std.Merge(red, blue, weight=0.5).resize.Point(height=2)

    normal_fade = vs_transitions.fade(blue, red, 96)
    normal_fade += vs_transitions.fade(red, blue, 96)

    poly1 = vs_transitions.poly_fade(blue, red, 96)
    poly1 += vs_transitions.poly_fade(red, blue, 96)

    poly2 = vs_transitions.poly_fade(blue, red, 96, exponent=2)
    poly2 += vs_transitions.poly_fade(red, blue, 96, exponent=2)

    poly5 = vs_transitions.poly_fade(blue, red, 96, exponent=5)
    poly5 += vs_transitions.poly_fade(red, blue, 96, exponent=5)

    core.std.StackVertical([normal_fade, div, poly1, div, poly2, div, poly5]).set_output()

.. image:: /images/poly_fade_diff.gif
    :align: center
