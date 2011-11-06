Upload To Gist
==============
A simple Sublime Text 2 plugin to upload the current file to Github.

Usage
-----
Run 'Upload To Github' from the command palette.

Setup
------------
First ensure that git is in PATH.
If you haven't already, run `git config --global github.user <username>` and `git config --global github.token <token>`.
This plugin depends on curl on Linux, as the Python interpreter is compiled without SSL support there. It *should* work fine on Windows, but this is not tested.