# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.z3cform.aceeditorwidget


class CollectiveZ3CformAceeditorwidgetLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.z3cform.aceeditorwidget,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.z3cform.aceeditorwidget:default')


COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_FIXTURE = CollectiveZ3CformAceeditorwidgetLayer()


COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_FIXTURE,),
    name='CollectiveZ3CformAceeditorwidgetLayer:IntegrationTesting'
)


COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_FIXTURE,),
    name='CollectiveZ3CformAceeditorwidgetLayer:FunctionalTesting'
)


COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_Z3CFORM_ACEEDITORWIDGET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveZ3CformAceeditorwidgetLayer:AcceptanceTesting'
)
