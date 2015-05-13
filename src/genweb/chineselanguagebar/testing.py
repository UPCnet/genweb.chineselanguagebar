# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import genweb.chineselanguagebar


class GenwebChineselanguagebarLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            genweb.chineselanguagebar,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'genweb.chineselanguagebar:default')


GENWEB_CHINESELANGUAGEBAR_FIXTURE = GenwebChineselanguagebarLayer()


GENWEB_CHINESELANGUAGEBAR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GENWEB_CHINESELANGUAGEBAR_FIXTURE,),
    name='GenwebChineselanguagebarLayer:IntegrationTesting'
)


GENWEB_CHINESELANGUAGEBAR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GENWEB_CHINESELANGUAGEBAR_FIXTURE,),
    name='GenwebChineselanguagebarLayer:FunctionalTesting'
)


GENWEB_CHINESELANGUAGEBAR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GENWEB_CHINESELANGUAGEBAR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='GenwebChineselanguagebarLayer:AcceptanceTesting'
)
