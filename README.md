# Extempore Function Documentation generator

A Python/Django application for navigating the Extempore codebase. 

The app allows to extract functions definitions from Extempore's source code, save it into a database and render it via a simple HTML interface. 

Online: http://extempore.michelepasin.org/


## Building the Extempore functions index

First of all, set the path to your local extempore source repo in `local_settings.py`, using the `XTM_LOCAL_FILES` variable.

```bash
$ python manage.py parse_xtm
```

or the helper script:

```bash
$ ./tools/load-xtm-src
```


## Running the Django app

```bash
./tools/run-dev-local-db
```


## Development

With Python 3.9 and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

```bash
$ git clone git@github.com:lambdamusic/xtm-docs.git
$ mkvirtualenv xtmdocs
$ pip install -r requirements.txt
```

Then adjust your local settings in `src/local_settings_example.py`

```bash
$ cp src/local_settings_example.py src/src/local_settings.py
$ open src/local_settings.py
```

In particular this part

```python
XTM_VERSION = "v0.8.9"
XTM_GITHUB_URL = "https://github.com/digego/extempore/tree/" + XTM_VERSION
# LOCATION OF EXTEMPORE SRC
XTM_LOCAL_FILES = ['/Applications/path/to/extempore']
# =====================
```



## Project status

Just an idea, but feel free to get in touch if you're willing to improve/extend it.  


## Changelog

### March 7, 2022

* improved search
* improve code extraction with comments before functions


### December 13, 2021

* adding site search in front end
* reorg urls
  * make a unique URL for function index (both custom and not)
  * make list pages functions list
  * updated fundetails so that it takes '.html' version of pages 


## Links

* http://extempore.michelepasin.org/
* http://extempore.moso.com.au/
* https://github.com/digego/extempore
