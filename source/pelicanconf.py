#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'gabriell'
SITENAME = u'gabriell nascimento'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'pt'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

ARTICLE_URL = '{lang}/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{lang}/{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{lang}/{date:%Y}/{date:%m}/{slug}.html'
PAGE_LANG_URL = 'pages/{lang}/{date:%Y}/{date:%m}/pages/{slug}.html'
ARTICLE_SAVE_AS = '{lang}/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{lang}/{date:%Y}/{date:%m}/{slug}.html'
PAGE_SAVE_AS = 'pages/{lang}/{date:%Y}/{date:%m}/{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{lang}/{date:%Y}/{date:%m}/{slug}.html'

