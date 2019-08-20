#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
My own sorting algorithm ha !
"""

__author__ = "Santhosh Balasa"
__version__ = "1.0.1"
__maintainer__ = "Santhosh Balasa"
__email__ = "santhosh.kbr@gmail.com"
__status__ = "Production"



def santee_sort(items, reverse=False):
    count = len(items)
    while count:
        for pos, i in enumerate(items):
            try:
                if not reverse:
                    if i > items[pos+1]:
                        items[pos] = items[pos+1]
                        items[pos+1] = i
                else:
                    if i < items[pos+1]:
                        items[pos] = items[pos+1]
                        items[pos+1] = i
            except IndexError:
                pass
        count -= 1
