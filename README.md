# cron_parser.py

This utility can be used to interpret CRON expressions. More information about CRON expressions can be found at: 
* https://en.wikipedia.org/wiki/Cron
* https://www.baeldung.com/cron-expressions

## Usage

Requirements:
* Python 3

Usage is simply:
```
$ ./cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"

minute        0
hour          0
day of month  10 15 20 25 30
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   0 1 2 3 4 5 6
command       /usr/bin/find -name test
```

This implementation does not support the characters: L, W, #, ?

## Development

The below development tests are primarily for the purpose of running tests. To simply run the tool, see Usage above.

Requirements:
* Python 3
* `python3-venv` package (use `apt` or `yum` as appropriate)

Steps to configure for development
1. Set up a Python virtual environment
    ```
    $ python -m venv venv
    ```
2. Activate the virtual environment
    ```
    $ source venv/bin/activate
    ```
3. Download dependencies
    ```
    $ pip install -r requirements.txt
    ```

Now, it will be possible to run the tests:
```
$ pytest
==================== test session starts =====================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: 
collected 15 items                                           

cron_parser_test.py ...............                    [100%]

===================== 15 passed in 0.04s =====================


```