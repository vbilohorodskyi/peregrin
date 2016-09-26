# peregrin
Peregrin is a light-weight performance tool for frontend QA to measure page load time in the right way.


====================DESCRIPTION:============================

Peregrin architecture consists of 3 files:

map.txt - file where you can specify pages to test
! ALL URLs from the new line, no EOF-EOL symbols,
! ALL URLs must be specified with excact protocol, as it is done in URL string of browser


config.py - configuration and system constants, that can be changed with simple text editors:

    MAP_FILE = 'map.txt' -- map file, 'map.txt' by default. If you want to specify some additional tests, pages can be
                            added to other file and you will need to specify it before running tests

    TRIES_COUNT = 5 -- integer number of iterations of performance measurement for each page, it's needed to make a
                        clear vision about average load time

peregrin.py -- main script to run tests.

=====================INSTALLATION:============================

1. Depending on your OS, install python 2.7 or later to your platform

2. Please note that you should have clean Firefox and Google Chrome browsers installed to your PC/Server.

3. Installing selenium:
Execute following commands:
pip install selenium | On linux

OR

sudo easy_install selenium | On MacOS X

OR

C:\Python35\Scripts\pip.exe install selenium | On Windows Systems

4. Now you will need to install chromedriver, because it is not included to default webdriver configuration:

Go to http://chromedriver.storage.googleapis.com/index.html?path=2.20/ and download archive depending on your distro
Save it into your hard drive and run specified executable

=====================EXECUTION:============================

change path to your peregrin folder
type python peregrin.py

And that's it.


=====================SUPPORT AND MAINTENANCE:============================

To get a contributor access, clone from repo or in case of any errors, email to vlad.belogorodskiy@gmail.com
