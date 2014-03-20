#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Faraday Penetration Test IDE - Community Version
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information

'''

class CommandRunInformation(object):
    """Command Run information object containing:
        command, parameters, time, workspace, etc."""

    class_signature = "CommandHistory"

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        