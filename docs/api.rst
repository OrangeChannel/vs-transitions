=============
API Reference
=============

.. automodule:: vs_transitions


All transitions, unless explicitly stated,
start with a pure frame from ``clipa``, or generally the first clip.
The transition ends with a pure frame from ``clipb``,
or generally the second clip.
If specified, the transition will be ``frames`` long.
If not given (or given ``0``), the transition will be the entire length of the shortest clip given.
The ``frames`` parameter cannot excede the number of frames in either clip.

All transitions, unless explicitly stated,
*consume* frames from both clips in the same way.
As the transition progresses, frames from the **end** of the first clip
and from the **start** of the second clip are consumed simultaneously.
Frame *0* of the transition, although purely ``clipa``,
consumes the first frame from ``clipb``.

As an example, two 5-frame clips are faded,
with the frame numbers for ``clipa`` on the left,
and for ``clipb`` on the right.

.. image:: /images/example_consume_frames.gif
    :align: center

The next example starts with a 15-frame long black clip,
and a 10-frame long white clip. The transition lasts 4 frames.
(Frames 12, 13, 14, 15 from the first clip are consumed concurrently with
frames 1, 2, 3, 4 from the second clip). *Notice how only frames 13 and 14
seem to be involved in the transition,
as the first and last frames are pure frames from their respective clip.*

.. image:: /images/example_consume_frames_long.gif
    :align: center

For a 24-fps clip, specifying ``frames=24`` will make the transition last a full second.
However, since the first and last frame of the transition
are purely from ``clipa`` / ``clipb`` respectively,
``frames=26`` will give a *visually* one second long transition.


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

    fade(hero[:96], dweebs[:96], frames=48).set_output()

.. image:: /images/fade.gif
    :align: center

.. autofunction:: vs_transitions.fade_to_black

.. code-block:: python

    fade_to_black(dweebs[:96], frames=36).set_output()

.. image:: /images/fade_to_black.gif
    :align: center

.. autofunction:: vs_transitions.fade_from_black

.. code-block:: python

    fade_from_black(dweebs[:96], frames=36).set_output()

.. image:: /images/fade_from_black.gif
    :align: center

----

**Non-linear Transitions**

.. autofunction:: vs_transitions.poly_fade

.. code-block:: python
    :emphasize-lines: 13

    red = core.std.BlankClip(format=vs.RGB24, color=[255, 0, 0], length=96, width=320, height=40)
    blue = core.std.BlankClip(format=vs.RGB24, color=[0, 0, 255], length=96, width=320, height=40)
    div = core.std.Merge(red, blue, weight=0.5).resize.Point(height=2)

    normal_fade = fade(blue, red, 96) + fade(red, blue, 96)

    poly1 = poly_fade(blue, red, 96) + poly_fade(red, blue, 96)

    poly2 = poly_fade(blue, red, 96, exponent=2) + poly_fade(red, blue, 96, exponent=2)

    poly5 = poly_fade(blue, red, 96, exponent=5) + poly_fade(red, blue, 96, exponent=5)

    core.std.StackVertical([normal_fade, div, poly1, div, poly2, div, poly5]).set_output()

.. image:: /images/poly_fade_diff.gif
    :align: center


Directional Transitions
=======================

**Simple Transitions**

.. autofunction:: vs_transitions.push

.. code-block:: python

    push(hero[:84], dweebs[:84], frames=48).set_output()

.. image:: /images/push.gif
    :align: center

.. autofunction:: vs_transitions.wipe

.. code-block:: python

    wipe(hero[:84], dweebs[:84], frames=56).set_output()

.. image:: /images/wipe.gif
    :align: center

.. autofunction:: vs_transitions.squeeze_expand

.. code-block:: python

    squeeze_expand(hero[:84], dweebs[:84], frames=56).set_output()

.. image:: /images/squeeze_expand.gif
    :align: center
