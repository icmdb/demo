#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys

from raven import Client

PUBLIC_KEY = os.getenv("PUBLIC_KEY", "PUBLIC_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "SECRET_KEY")
PROJECT_ID = os.getenv("PROJECT_ID", "PROJECT_ID")
DOMAINNAME = os.getenv("DOMAINNAME", "sentry.io")

DSN = ''.join(['https://',PUBLIC_KEY,':',SECRET_KEY,'@', DOMAINNAME, '/', PROJECT_ID])

client = Client(DSN)

def test1():
    try:
        1 / 0
    except ZeroDivisionError:
        client.captureException()

def test2():
    client.captureMessage('This is a sentry captureMessage test.')

def test3():
    try:
        f = open("notexists.txt", "bs")
        f.write("test")
        f.close()
    except Exception:
        client.captureException()

def handle_request(request):
    client.user_context({
        'email': request.user.email
    })


def main():
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()

