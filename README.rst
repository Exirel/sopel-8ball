===========
sopel-8ball
===========

Sopel magic 8 ball plugin::

    <User> .8ball Do you know the future?
    <Sopel> User: You may rely on it.
    <User> .8ball Do you like me?
    <Sopel> User: Better not tell you now.
    <User> .8ball Will I live forever?
    <Sopel> User: Very doubtful.

Install
=======

The preferred way to install this plugin is through ``pip``::

    $ pip install sopel-8ball

Note that you may need to use ``pip3``, depending on your system and your
installation.

Once this is done, you should configure and enable the plugin::

    $ sopel-plugins configure 8ball
    $ sopel-plugins enable 8ball

And then, restart your bot: this, again, depends on your system and how you run
your bot.

Magic 8 ball choices
====================

There are more than one style of choices you can select:

* ``classic``: the classic version (10 yes, 5 maybe, 5 no)
* ``snarky``: this version is rude (5 yes, 5 maybe, 10 no)
* ``spooky``: use at your own risk (5 yes, 10 maybe, 5 no, 100% freaky)
* ``weeaball``: for japanese style fan ＼(＾▽＾)／ (7 yes, 9 maybe, 7 no,
  100% kaomoji)

This can be configured with the Sopel configuration wizard::

    $ sopel-plugins configure 8ball

Or manually, by editing your configuration and adding this section::

    [magic8ball]
    choices = classic

Replace ``classic`` (the default) by one of the value above.
