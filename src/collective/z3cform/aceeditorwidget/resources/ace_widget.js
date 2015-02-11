/*global window, jQuery, document, CodeMirror, Mustache */

(function ($) {
    "use strict";


    $.fn.extend({
        aceedit: function () {
            var self = this;
            $.each(self.find('.aceeditor'), function(){
                var editor = ace.edit($(this).attr('id'));
                // TODO: make this stuff configurable
                editor.setTheme("ace/theme/monokai");
                editor.getSession().setMode("ace/mode/xml");
                editor.getSession().setUseWrapMode(true);
                editor.resize();
                var textarea = $('#' + $(this).attr('id') + '-field');
                editor.getSession().setValue(textarea.val(), 1);
                editor.getSession().on('change', function(){
                  textarea.val(editor.getSession().getValue());
                });
            })

        }
    });


    $(document).ready(function () {
        $('.aceeditor-wrapper').aceedit();
    });

}(jQuery));
