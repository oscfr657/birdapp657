
# Birdapp 657 #

A small Wagtail app

## Compatible ##

### Tested with ###

``` Python
django==4.1.8
wagtail==4.2.2
wagtailmedia==0.14.0
```

## Installation ###
  
### Pip requirements ###

``` Python
pip install -r requirements.txt
```

### Django settings ###

In the settings file,

add to the INSTALLED_APPS

``` Python

    'django.contrib.sites',  # extra
    'django.contrib.sitemaps',  # extra

    # wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings',  # extra
    'wagtail.contrib.search_promotions',  # extra
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',

    # custom
    'birdapp657',
    # birdapp657 media file block
    'wagtailmedia',

```

add to the MIDDLEWARE settings

``` python
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Extra
    'django.middleware.common.CommonMiddleware',

    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',  # wagtail
```

add to the TEMPLATES settings

``` python
    TEMPLATES = [
        {
            'OPTIONS': {
                'context_processors': [
                    'wagtail.contrib.settings.context_processors.settings',  # Extra
            },
        },
    ]
```

#### Optionaly set ####

the admin title

``` python
WAGTAIL_SITE_NAME = 'Birdapp657'
```

the password required template

``` python
PASSWORD_REQUIRED_TEMPLATE = 'birdapp657_password_required.html'
```

#### I recommend ####

the use of the database search backend, set the search backend settings

``` python
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    },
}
```

and set the WAGTAILIMAGES_FORMAT_CONVERSIONS setting

``` python
WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    'bmp': 'webp',
    'jpeg': 'webp',
    'jpg': 'webp',
    'JPG': 'webp',
    'webp': 'webp',
    'png': 'webp',
}
```

### Database configuration ###

> python3 manage.py migrate

### Search Index setup ###

``` Python
python3 manage.py update_index
```

### Django url ###

To the django projects' url.py add

``` python
from django.urls import path, re_path, include

# Wagtail
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from wagtail.contrib.sitemaps.views import sitemap

from birdapp657.views import search
```

and

``` python
urlpatterns += [
    path('search/', search),
    re_path('sitemap.xml', sitemap),
    #  Wagtail
    re_path(r'^birdapp/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
  ]
```

```python
handler403 = 'birdapp657.views.bird_page_403'
handler404 = 'birdapp657.views.bird_page_404'
handler500 = 'birdapp657.views.bird_page_500'
```

### Collectstatic ###

``` bash
python3 manage.py collectstatic
```

### [Management commands](https://docs.wagtail.io/en/stable/reference/management_commands.html) ###

Some commands is good to have in cron to run once every hour.

``` bash
crontab -e

0 * * * * /path/to/env/bin/python3 /path/to/project/manage.py publish_scheduled_pages

0 * * * * /path/to/env/bin/python3 /path/to/project/manage.py search_garbage_collect

crontab -l
```

### Memcached ###

``` Python
sudo apt install memcached
sudo systemctl start memcached
```

install pymemcache

``` Python
pip install pymemcache
```

In the settings file add

``` python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

## For development ##

To the Django settings.py add

``` python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

To the Django project url.py add

``` python
from django.conf import settings
from django.conf.urls.static import static
```

and at the bottom of the file add

``` python

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

### Build a new release ###

``` bash
    pip install black
    black . --skip-string-normalization
```

``` python
python3 -m build --sdist
```
