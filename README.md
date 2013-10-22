Installation
============

This installs via pip. It is strongly recommended to use a virtualenv.

    mkdir security-challenges
    cd security-challenges
    virtualenv .
    ./bin/pip install -r https://raw.github.com/MatthewWilkes/security-challenges/master/requirements.txt
    ./bin/pserve src/xss/development.ini 

Installing with pip will take a few minutes, and you'll need to have
virtualenv installed. This works on Python 2.7 and Python 3.3. Other
implementations *MAY* work.


Playing
=======

You can access the app at http://127.0.0.1:6543/

The welcome screen will link to various challenges, along with their source
code. Read the source code to try and find a way to create an XSS attack. The
best way of demonstrating this is to call `alert(1)` when a page is rendered.

The challenges get progressively harder, and are all based on real-world
vulnerabilities.

Try not to look at the source code of later challenges before you've completed
the earlier ones, as they may well give away the solution to the previous
challenge.

