#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'gabriell'
SITENAME = u'gabriell nascimento'
SITEURL = 'http://gabriellhrn.github.com'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

PERMALINK_STRUCTURE = 'blog/{date:%Y}/{date:%m}'
ARTICLE_URL = '%s/{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s/{slug}.html' % PERMALINK_STRUCTURE
PAGE_URL = 'pages/%s/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = 'pages/%s/pages/{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s/{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s/{slug}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = 'pages/%s/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = 'pages/%s/{slug}.html' % PERMALINK_STRUCTURE

