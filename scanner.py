#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scanner for consolidating information from ViewPoint.
"""

import requests
import sys

VIEWPOINT_API = 'http://www.viewpoint.ca/api/v1/properties/'


def get_viewpoint_json(pid):
    """
    e.g. http://www.viewpoint.ca/api/v1/properties/40548778.json
    """
    response = requests.get(VIEWPOINT_API + pid + '.json')
    return response.json()


def filter_keys(dct):
    """ Filter to just be keys we're interested in. """
    keys = ['pid', 'list_price', 'assessment', 'listdate', 'area', 'age']
    tmp = [dct[k] for k in keys]
    tmp.append(dct['address']['civicnum'] + ' ' + dct['address']['street'])
    tmp.append(dct['address']['city'])
    return tmp


def to_csv(prop):
    """ Convert response to csv """
    return '\t'.join(filter_keys(prop))


def main():
    """ Init Runner """
    for pid in sys.argv[1:]:
        print(to_csv(get_viewpoint_json(pid)))


if __name__ == '__main__':
    main()
