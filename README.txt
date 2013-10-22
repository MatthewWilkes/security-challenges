To install this, create a new virtualenv on your system::

    mkdir security-challenges
    cd security-challenges
    virtualenv .
    ./bin/pip install -r https://raw.github.com/MatthewWilkes/security-challenges/master/requirements.txt
    ./bin/pserve src/xss/development.ini 

Then access the app at http://127.0.0.1:6543/

Installing with pip will take a few minutes, and you'll need to have
virtualenv installed. I've only tried this on PyPy 1.9.0, but it should work
on any Python2.7 implementation. I doubt it will work unmodified on Python3.
