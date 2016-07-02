#!/usr/bin/env python
SITENAME = 'Elijah\'s Website'
WWW_ROOT = 'http://elijahcaine.me/'

AUTHOR = 'Elijah Caine'
EMAIL = 'elijahcainemv@gmail.com'

STATIC = 'static'
CONTENT_IGNORE = ['.*.swp', '.*.swo', '*.scss~', '.sass-cache/', '*.map']

FILTERS = ['rst+codehilite(css_class=highlight)', 'hyphenate', 'h1']
VIEWS = {
    # main pages
    '/:slug/':
    {
        'filters': ['h2', 'nohyphenate'],
        'view': 'page',
        'template': 'page.html',
        'if': lambda e: 'page' == e.type and 'liveblog-meta' not in e.tags,
    },

    # blog posts pages
    '/blog/:slug/':
    {
        'view': 'entry',
        'template': 'post.html',
        'if': lambda e: 'blogpost' in e.tags,
    },

    # liveblog related stuffs
    '/liveblog/:slug/':
    {
        'filters': 'h2',
        'view': 'page',
        'template': 'page.html',
        'if': lambda e: 'liveblog-adventure' in e.tags,
    },
    '/liveblog/europe-2015/:slug/':
    {
        'view': 'entry',
        'template': 'post.html',
        'if': lambda e: 'europe-2015' in e.tags,
    },

    # comics related stuffs
    '/comics/:slug/':
    {
        'view': 'entry',
        'template': 'post.html',
        'if': lambda e: 'comic' in e.tags,
    },

    # creative writing stuffs
    '/creative-writing/:year/:month/:day/:slug/':
    {
        'view': 'entry',
        'template': 'post.html',
        'if': lambda e: 'creative-writing' in e.tags,
    },

    '/atom/':
    {
        'filters': ['h2', 'nohyphenate'],
        'view': 'atom',
    },
    '/rss/':
    {
        'filters': ['h2', 'nohyphenate'],
        'view': 'rss',
    },

    '/sitemap.xml':
    {
        'view': 'sitemap',
    },
}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%Y-%m-%d'
DEPLOYMENT = {
    'default': 'bash gh-build.sh',
    'site': 'bash gh-build.sh',
    'blog': 'bash gh-build.sh',
}
