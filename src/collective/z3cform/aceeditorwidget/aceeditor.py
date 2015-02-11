# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from Acquisition import aq_parent
from zope.interface import implementer_only
from zope.interface import implementer
from zope.schema.interfaces import IField
from zope.component import adapter
from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import textarea
from Products.CMFCore.interfaces import IFolderish


class IAceEditorWidget(interfaces.ITextAreaWidget):
    """Marker interface for the AceEditorWidget Widget
    """


@implementer_only(IAceEditorWidget)
class AceEditorWidget(textarea.TextAreaWidget):

    klass = u'aceeditor-widget'

    @property
    def popup_name(self):
        return getattr(self.field, 'popup_name', 'referencewidget-popup')

    def query_contenttypes(self):
        # Display only images
        query = ['pt=Image']
        return "?%s" % '&'.join(query)

    def folder_listing_url(self):
        url = "%s/%s" % (
            self.context_url(), self.popup_name
        )
        view_type = "viewtype=thumbview&thumbselector=1"

        filters = self.query_contenttypes()
        if filters:
            url += '&'.join((filters, view_type))
        else:
            url += '?%s' % view_type

        return url

    def get_context(self):
        """return context form or the closest context"""
        context = getattr(self.form, 'get_closest_content', None)
        if context:
            context = context()
        else:
            context = self.context
        return context

    def context_url(self):
        """return the url from the context or the closest content
        """
        context = self.get_context()

        if not IFolderish.providedBy(context):
            context = aq_parent(aq_inner(context))
        return context.absolute_url()


@adapter(IField, interfaces.IFormLayer)
@implementer(interfaces.IFieldWidget)
def AceEditorFieldWidget(field, request):  # noqa
    """IFieldWidget factory for IAceEditorWidget."""
    return widget.FieldWidget(field, AceEditorWidget(request))
