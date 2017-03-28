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
from plone.app.layout.navigation.interfaces import INavigationRoot

from genweb.core import _
from genweb.core import HAS_CAS
from genweb.core.interfaces import IHomePage
from genweb.theme.browser.interfaces import IHomePageView
from genweb.core.utils import genweb_config
from genweb.core.utils import havePermissionAtRoot
from genweb.core.utils import pref_lang
from genweb.chineselanguagebar.interfaces import IGenwebChineselanguagebarLayer



class viewletBase(grok.Viewlet):
    grok.baseclass()
    grok.context(Interface)

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

class gwHeader(viewletBase):
    grok.name('genweb.chineseheader')
    grok.template('header')
    grok.viewletmanager(IPortalHeader)
    grok.layer(IGenwebChineselanguagebarLayer)

    def get_image_class(self):
        if self.genweb_config().treu_menu_horitzontal:
            # Is a L2 type
            return 'l2-image'
        else:
            return 'l3-image'

    def show_login(self):
        isAnon = getMultiAdapter((self.context, self.request), name='plone_portal_state').anonymous()
        return not self.genweb_config().amaga_identificacio and isAnon

    # def show_directory(self):
    #     return self.genweb_config().directori_upc

    def show_directory(self):
        show_general = self.genweb_config().directori_upc
        return show_general

    def show_directory_filtered(self):
        show_filtered = self.genweb_config().directori_filtrat
        return show_filtered

    def getURLDirectori(self, codi):
        if codi:
            return "http://directori.upc.edu/directori/dadesUE.jsp?id=%s" % codi
        else:
            return "http://directori.upc.edu"

    def get_title(self):
        title = getattr(self.genweb_config(), 'html_title_{}'.format(self.pref_lang()))
        if title:
            return title
        else:
            return u''

    def is_logo_enabled(self):
        return self.genweb_config().right_logo_enabled

    def get_right_logo_alt(self):
        right_logo_alt = self.genweb_config().right_logo_alt
        return right_logo_alt if right_logo_alt else ""
