#!/usr/bin/python3

from distutils.core import setup

from argopt.info import info

setup(name=info.NAME
		version=info.VERSION
		description=info.DESCR
		author=info.AUTHOR.name
		author_email=info.AUTHOR.mail
		url=info.URL
		packages=['argopt']
	)

