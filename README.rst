Intro
-----

z3c.form widget that integrates ACE editor.

Usage
-----

You can apply it on a field on your schema like this::

    from zope import schema
    from plone.supermodel import model
    from plone.autoform import directives as form

    from collective.z3cform.aceeditorwidget.aceeditor import AceEditorFieldWidget


    class ITextTileSchema(model.Schema):

        form.widget(text=AceEditorFieldWidget)
        text = schema.Text(
            title=u'Text'
        )

