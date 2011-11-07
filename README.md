Upload To Gist
==============
A simple Sublime Text 2 plugin to upload the current file to Github.

Usage
-----
Run 'Upload To Gist' from the command palette.

Setup
------------

Git method:
First, ensure that git is in path.
Run `git config --global github.user <username>` and `git config --global github.token <token>`.
There have been some reports that this method doesn't work with msysgit. If that's the case, use the other method.

Settings file:
The username and token (in addition to description and public/private flag) can be specified in `upload-to-gist.sublime-settings`.

This plugin depends on curl on Linux, as the Python interpreter is compiled without SSL support there. It *should* work fine on Windows, but this is not tested.