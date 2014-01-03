WikiStyleMD
===========

Wanted to create a document that was very legible and straightforward, just like Wikipedia's documents. Markdown was the option and styling it just like Wikipedia is just what I did.

This is still a work in progress. Styles aren't 100% complete as of yet.

Usage
-----

If you have .md files in the subdirectory ``docs``, all you must do is set the ``f`` parameter equal to that file name

     http://your.com/md?f=README

If README.md is in the same directory, a pretty HTML WikiStyleMD version will be generated server side.

.htaccess
---------

Modifying your ``.htaccess`` to redirect a specific url to the above url would be ideal. The following is what I have added to my ``.htaccess``

	RewriteRule ^doc/([^/.]+)/?$ md/index.cgi?f=$1 [L]

Doing so will give pretty access to your ``.md`` files like so

	http://your.com/doc/README