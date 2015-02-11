# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""
from collective.z3cform.aceeditorwidget.testing import COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestInstall(unittest.TestCase):
    """Test installation of collective.z3cform.aceeditorwidget into Plone."""

    layer = COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.z3cform.aceeditorwidget is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.z3cform.aceeditorwidget'))

    def test_uninstall(self):
        """Test if collective.z3cform.aceeditorwidget is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.z3cform.aceeditorwidget'])
        self.assertFalse(self.installer.isProductInstalled('collective.z3cform.aceeditorwidget'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ILayer is registered."""
        from collective.z3cform.aceeditorwidget.interfaces import ILayer
        from plone.browserlayer import utils
        self.assertIn(ILayer, utils.registered_layers())
