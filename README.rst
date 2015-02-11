==================================
collective.z3cform.aceeditorwidget
==================================

Intro
-----

z3c.form widget that integrates ACE editor.

Usage
-----

You can apply it on a field on your schema like this:

    from zope import schema
    from plone.supermodel import model
    from plone.autoform import directives as form

    from collective.z3cform.aceeditorwidget import AceEditorFieldWidget


    class IText(model.Schema):

        form.widget(text=AceEditorFieldWidget)
        text = schema.Text(
            title=u'Text'
        )

