.. _narrator:

Narrator
========

Telling the story
of your actors' screenplay
falls to the Narrator.

You can fit the Narrator's microphone
with adapters
to send the thrilling account
to different reporting tools.
Currently,
ScreenPy includes adapters for
`Allure <https://docs.qameta.io/allure/>`__
and stdout.

Using Adapters
==================

To include adapters
on the Narrator's microphone,
do this::

    from screenpy.narration.adapters.stdout_adapter import StdOutAdapter
    from screenpy.pacing import the_narrator

    the_narrator.adapters = [StdOutAdapter()]

Do the above in ``conftest.py``
or a similar setup file
to set the adapters
for your test suite.
You are able to
add any number of adapters
in any order.

Creating New Adapters
=====================

The :class:`~screenpy.protocols.Adapter` protocol
describes what an adapter looks like.

The function signatures
must remain completely intact.
The new adapter's methods
must also ``yield`` back a function.
Most likely this will be
the function passed to it
in the first place,
having been modified in some way.

Each adapter must also specify
which direction chaining occurs.
If the adapter decorates the functions it receives
or wraps context(s) around them,
the adapter should set
``chaining_direction = narrator.FORWARD``.
See :class:`~screenpy.narration.adapters.allure_adapter.AllureAdapter`
for an example of ``FORWARD`` chaining.
If the adapter wraps the function
and returns the wrapper,
the adapter should set
``chaining_direction = narrator.BACKWARD``.
See :class:`~screenpy.narration.adapters.stdout_adapter.StdOutAdapter`
for an example of ``BACKWARD`` chaining.

Narrator
========

.. autoclass:: screenpy.narration.narrator.Narrator
    :members:

Adapters
========

AllureAdapter
-------------

.. autoclass:: screenpy.narration.adapters.allure_adapter.AllureAdapter
    :members:


StdOutAdapter
-------------

.. autoclass:: screenpy.narration.adapters.stdout_adapter.StdOutAdapter
    :members:
