# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from genweb.chineselanguagebar.testing import GENWEB_CHINESELANGUAGEBAR_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that genweb.chineselanguagebar is properly installed."""

    layer = GENWEB_CHINESELANGUAGEBAR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if genweb.chineselanguagebar is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('genweb.chineselanguagebar'))

    def test_uninstall(self):
        """Test if genweb.chineselanguagebar is cleanly uninstalled."""
        self.installer.uninstallProducts(['genweb.chineselanguagebar'])
        self.assertFalse(self.installer.isProductInstalled('genweb.chineselanguagebar'))

    def test_browserlayer(self):
        """Test that IGenwebChineselanguagebarLayer is registered."""
        from genweb.chineselanguagebar.interfaces import IGenwebChineselanguagebarLayer
        from plone.browserlayer import utils
        self.assertIn(IGenwebChineselanguagebarLayer, utils.registered_layers())
