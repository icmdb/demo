# Sentry

[TOC]


> https://sentry.io/icmdb/python/getting-started/python/

## Installation

```bash
pip install virtualenv virtualenvwrapper

mkvirtualenv demo

pip install --upgrade raven
```

## Capture an Error

```python
from raven import Client

client = Client('https://xxxxxxx:xxxxxx@sentry.io/256679')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
```

## Reporting an Event

```python
client.captureMessage('Something went fundamentally wrong')
```

## Adding Context

> https://docs.sentry.io/clients/python/api/#raven.Client.user_context

```python
def handle_request(request):
    client.user_context({
        'email': request.user.email
    })
```
