from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text
import os, re

module_dir = os.path.dirname(__file__)
register = Library()
language = None # global, utilizada na função format_lines e setada na code body

@register.simple_tag
def code_script(args):
    args_list = [arg.strip() for arg in args.split(',')]

    language_js = open(os.path.join(module_dir, 'languages/sh_{}.js'.format(args_list[0]))).read() ## 0 argumento é a linguagem utilizada
    sh_main = open(os.path.join(module_dir, 'sh_main.js')).read()

    if args_list[1] != 'custom':
        theme = open(os.path.join(module_dir, 'themes/{}_style.css'.format(args_list[1]))).read()      ## 1 argumento é o tema
        html = """
            <script type='text/javascript'>{0};{1};</script>
            <style type="text/css">
                {2}
            </style>
        """.format(sh_main, language_js, theme)
    else:
        theme = args_list[2] # this last argument is the custom css
        html = """
            <script type='text/javascript'>{0};{1};</script>
            <link rel="stylesheet" type="text/css" href="{2}">
        """.format(sh_main, language_js, theme)

    theme = open(os.path.join(module_dir, 'themes/{}_style.css'.format(args_list[1]))).read()      ## 1 argumento é o tema
    sh_main = open(os.path.join(module_dir, 'sh_main.js')).read()

    html = """
        <script type='text/javascript'>{0};{1};</script>
        <style type="text/css">
            {2}
        </style>
    """.format(sh_main, language_js, theme)

    return mark_safe(force_text(html))

def format_lines(found):
    codigo = found.group(1).splitlines()  # .group(1) é a string que foi encontrada e passada como argumento, .group(0) é uma str com o o restante da RE

    if codigo[0] == '':  ## se a primeira linha for em branca ele apaga
        codigo.pop(0)

    for i, linha in enumerate(codigo):     # para cada linha
        codigo[i] = "<span class='linha_span'>" + linha + "</span>" # esse span está com uma classe especifica que sera utilizada para a numeração das linhas no display do codiog
    codigo = ''.join(codigo) #transformando a lista em strin

    #esse abaixo é a o elemento inteiro do codigo, ou seja, todo o highlight do display é feito usando o elemento <pre> com o style de alguma linguagem
    # o script no final é para executar o script que faz o highlight, sendo assim a função sera chamada para cada 'bloco_codigo' abaixo
    replacer = r'<div class="bloco_codigo"><pre class="sh_{0}">{1}</pre></div><script type="text/javascript">sh_highlightDocument()</script>'.format(globals()[language], codigo)
    return replacer


@register.filter
def code_body(value,language_code):
    globals()[language] = language_code   # alterando a variavel global
    regex = re.compile('@@(.*?)@@', re.S)  # as linhas de codigos ficam entre '@@' e '@@'
    body = re.sub(regex, format_lines, value)  # para cada grupo a função será chamada e o grupo achado sera substituido pelo valor retornado pela func...! É EXECUTADO PARA CADA GRUPO
    body = body.splitlines()

    for i, item in enumerate(body):
        if '<div class="bloco_codigo">' not in item:
            body[i] = '<span class="text_span">' + item + '</span>'
        body[i] = item + '\n'

    body = ''.join(body)
    return mark_safe(force_text(body))
