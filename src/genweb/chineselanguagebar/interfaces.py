# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from genweb.chineselanguagebar import _
from zope import schema
from five import grok
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IGenwebChineselanguagebarLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""