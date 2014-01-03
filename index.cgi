#!/usr/bin/perl
#
# Markdown.pl Converter
# Ken Lauguico | me@kenlauguico.com
#
# Generates a basic HTML page from a given .md file

use CGI ':standard';

#$mdFile = "barber.md";
$mdFile = param("f").".md";

print  "Content-type:text/html\n\n";


# Basic HTML tags and styling

print  "<html><head><title>".$mdFile."</title></head>\n";
print  "<link rel='stylesheet' href='../md/css/style.css'></head>\n\n";
print  "<body>\n";


# Run the Markdown.pl script

local @ARGV = ("--html4tags", "docs/".$mdFile);
do "Markdown.pl";


# Close and end script

print  "<script src='https://google-code-prettify.googlecode.com/svn/loader/run_prettify.js'></script>\n";
print  "</body></html>";
exit;