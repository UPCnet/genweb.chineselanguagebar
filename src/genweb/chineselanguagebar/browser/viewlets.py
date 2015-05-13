# -*- coding: utf-8 -*-
import re
import requests
import socket
from five import grok
from plone import api
from time import time
from cgi import escape
from Acquisition import aq_inner
from AccessControl import getSecurityManager
from zope.interface import Interface
from zope.component import getMultiAdapter
from zope.security import checkPermission
from plone import api

from plone.memoize import ram
from plone.memoize.view import memoize_contextless

# from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile as ZopeViewPageTemplateFile
from Products.Five.browser.metaconfigure import ViewMixinForTemplates
from Products.CMFPlone.interfaces import IPloneSiteRoot

from plone.app.layout.viewlets.common import PersonalBarViewlet, GlobalSectionsViewlet, PathBarViewlet
from plone.app.layout.viewlets.common import SearchBoxViewlet, TitleViewlet, ManagePortletsFallbackViewlet
from plone.app.layout.viewlets.interfaces import IHtmlHead, IPortalTop, IPortalHeader, IBelowContent
from plone.app.layout.viewlets.interfaces import IPortalFooter, IAboveContentTitle, IBelowContentTitle
from plone.app.layout.navigation.interfaces import INavigationRoot

from genweb.core import _
from genweb.core import HAS_CAS
from genweb.core.interfaces import IHomePage
from genweb.theme.browser.interfaces import IHomePageView
from genweb.core.utils import genweb_config
from genweb.core.utils import havePermissionAtRoot
from genweb.core.utils import pref_lang
from genweb.chineselanguagebar.interfaces import IGenwebChineselanguagebarLayer

grok.context(Interface)


class viewletBase(grok.Viewlet):
    grok.baseclass()

    @memoize_contextless
    def root_url(self):
        return self.portal().absolute_url()

    @memoize_contextless
    def portal(self):
        return api.portal.get()

    def genweb_config(self):
        return genweb_config()

    def pref_lang(self):
        """ Extracts the current language for the current user
        """
        lt = getToolByName(self.portal(), 'portal_languages')
        return lt.getPreferredLanguage()


class gwChineseLanguageBarViewlet(viewletBase):
    grok.name('genweb.chineselanguagebar')
    grok.viewletmanager(IPortalHeader)
    grok.layer(IGenwebChineselanguagebarLayer)

    render = ViewPageTemplateFile('viewlets_templates/chinese_language_bar.pt')