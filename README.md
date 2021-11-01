# Extempore Function Documentation generator

A Python/Django application for navigating the Extempore codebase. 

The app allows to extract functions definitions from Extempore's source code, save it into a database and render it via a simple HTML interface. 

Online: http://extempore.michelepasin.org/


## Development

With Python 3.9 and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

```bash
$ git clone git@github.com:lambdamusic/xtm-docs.git
$ mkvirtualenv xtmdocs
$ pip install -r requirements.txt
```

Then adjust your local settings in `src/local_settings_example.py`

```
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

## Running the Django app

```
./tools/run-dev-local-db
```

## Refreshing the Extempore functions docs

1. Set the path to your local extempore source repo in `local_settings.py`, using the  `XTM_LOCAL_FILES` variable.

2. Run `python manage.py xtm_load`


## Project status

Just an idea, but feel free to get in touch if you're willing to improve/extend it.  


## Links

* http://extempore.moso.com.au/
* https://github.com/digego/extempore
