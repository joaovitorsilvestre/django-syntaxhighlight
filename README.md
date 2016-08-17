#Syntax Highlight

This is a implementation of http://shjs.sourceforge.net/.

This app come with a template tag and a filter. Both make the template engine
add the javascript and css needed to show the code display.

<h2>Demo app</h2>
https://demo-django-highlight.herokuapp.com/

<h2>How it works?</h2>

Imagine that you have a post, this post basically is a string, and in this string
you want that some part of this be in a display, and the rest keep as normal string.

To define which part is code and which is not, you put what do you want between
'@@' and '@@'. See the exemple:

    string_with_code = """
        ... and this is an example of code made in python:
        @@
        if (1>2):
            print('It's True')
        @@
        this was an example of use of if.
    """

You see that everything that is out off the '@@' you keep normally.
The template tags will convert each line of code to a <span> element, this element
will have a class that have the colors to do the syntax highlight.

<h2>Installation</h2>

You need just download the package called 'django-syntaxhighlight-1.1.tar.gz'.
In terminal do:

    pip install django-syntaxhighlight-1.0.tar.gz
    #or
    pip install --user django-syntaxhighlight-1.0.tar.gz

On settings.py:

    INSTALLED_APPS = [
        'syntaxhighlight',
    ...

    TEMPLATES = [
    {
        ...
        'OPTIONS': {
            ... ,
            'builtins': ['syntaxhighlight.templatetags.syntax_highlight'],
            },
        },
    ]

<h2>Now how can use it in the template?</h2>

In the head of html you add the following with the arguments of which language is and
the theme that do your what to display the code, in this order.
And in the string that do you want to be displayed put the filter with the language again.
Example:

    <html>
        <head>
            {% code_theme 'atom' %}
            ...
        <head>
        <body>
            {{ string_with_code | code_body:'python'}}
            ...
        <body>
    <html>

And it's it.

<h2>Important, again...</h2>

The code in javascript was not made by me. I just make a template tag that put
the code automatically for you on html.
You can see the JavaScript code in: http://shjs.sourceforge.net/

<h2>Language and themes</h2>
Languages:

    python;
    ruby;
    javascript;
    java;
    php;
    pascal;


Themes:

    atom  (yes, it is just the same that atom program)
    custom
