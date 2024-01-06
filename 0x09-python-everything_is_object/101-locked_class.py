#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
	"""
	Only allows instace attribute called first_name
	"""
	__slot__ = ["first_name"]
