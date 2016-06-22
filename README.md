#Syntax Highlight 1.0

This is a implementation of http://shjs.sourceforge.net/. 

This app come with a template tag and a filter. Both make the template engine
add the javascript and css needed to show the code display.

#How it works?

Imagine that you have a post, this post basically is a string, and in this string
you want that some part of this be in a display, and the rest keep as normal string.

To define which part is code and which is not, you put what do you want between
'@@' and '@@'. See the exemple:

    ... and this is an example of code made in python:
    @@
    if (1>2):
        print('It's True') 
    @@
    this was an example of use of if.

You see that everything that is out off the '@@' you keep normally.
The template tags will convert each line of code to a <span> element, this element
will have a class that have the colors to do the syntax highlight.

#Installation

You need just download the package called 'django-syntaxhighlight-1.0.tar.gz'.
In terminal do:

    pip install django-syntaxhighlight-1.0.tar.gz
    
or 

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

#How use in template engine?

In the head of html you add the following with the arguments of which language is and
the theme that do your what to display the code, in this order.
And in the string that do you want to be displayed put the filter with the language again.
Example:

    <html>
        <head>
            {% code_script 'python,atom' %}
            ...
        <head>
        <body>
            {{ string_with_code|code_body:'python'}}
            ...
        <body>
    <html>

And it's it.

#Important
If your string is just the code, you put the @@ in the begin and at end of the string. Example:
"""
@@
    for num in range(0,10):
        print(num)
@@
"""  

And Remember, the code in javascript was not made by me. I just make a template tag that put
the code automatically for you on html.
You can see in: http://shjs.sourceforge.net/

#Language and themes
Language:

    python;
    pascal

Themes:

    atom  (yes, it is just the same that atom program)
