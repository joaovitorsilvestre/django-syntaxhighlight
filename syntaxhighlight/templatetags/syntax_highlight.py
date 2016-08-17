import os, re

from django.template import Library
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text

module_dir = os.path.dirname(__file__)

register = Library()

@register.simple_tag
def code_script(theme):
    theme = theme.strip()

    theme_path = os.path.join(module_dir, 'themes/{}_style.css'.format(theme))
    theme = open(theme_path).read()

    sh_main = open(os.path.join(module_dir, 'sh_main.js')).read()

    html = """
        <script type='text/javascript'>{0};</script>
        <style type="text/css">{1}</style>
    """.format(sh_main, theme)

    return mark_safe(force_text(html))

@register.filter
def code_body(value,language_code):
    def format_lines(found):
        codigo = found.group(1).splitlines()

        if codigo[0] == '':
            codigo.pop(0)

        for i, linha in enumerate(codigo):
            codigo[i] = "<span class='linha_span'>" + linha + "</span>"
        codigo = ''.join(codigo)

        replacer = r"""
            <div class="bloco_codigo">
                <pre class="sh_{0}">{1}</pre>
            </div>
            <script type="text/javascript">sh_highlightDocument()</script>
        """.format(language_code, codigo)

        return replacer

    regex = re.compile('@@(.*?)@@', re.S)
    body = re.sub(regex, format_lines, value)

    body = body.splitlines()

    for i, item in enumerate(body):
        if '<div class="bloco_codigo">' not in item:
            body[i] = '<span class="text_span">' + item + '</span>'

    for i, item in enumerate(body):
        body[i] = item + '\n'
    body = ''.join(body)

    # loads the script for the languege
    language_path = os.path.join(module_dir, 'languages/sh_{}.js'.format(language_code))
    language_js = open(language_path).read()

    body = '<script>'+ language_js +'</script>' + body

    return mark_safe(force_text(body))
