# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.z3cform.aceeditorwidget')


from .aceeditor import AceEditorFieldWidget # noqa
