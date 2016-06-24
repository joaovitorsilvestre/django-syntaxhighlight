<<<<<<< HEAD
#Syntax Highlight
=======
#Syntax Highlight 1.0
>>>>>>> 3ca36821043a3a7aabd3cb38d322b8d5def9c53b

This is a implementation of http://shjs.sourceforge.net/. 

This app come with a template tag and a filter. Both make the template engine
add the javascript and css needed to show the code display.

<<<<<<< HEAD
#How works?
=======
#Demo app
https://demo-django-highlight.herokuapp.com/

#How it works?
>>>>>>> 3ca36821043a3a7aabd3cb38d322b8d5def9c53b

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
<<<<<<< HEAD
pip install django-syntaxhighlight-1.0.tar.gz
or 
pip install --user django-syntaxhighlight-1.0.tar.gz

On settings.py:
=======

    pip install django-syntaxhighlight-1.0.tar.gz
    
or 

    pip install --user django-syntaxhighlight-1.0.tar.gz

On settings.py:

>>>>>>> 3ca36821043a3a7aabd3cb38d322b8d5def9c53b
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

<<<<<<< HEAD
#How use in template engine?
=======
#How to use it in the template?
>>>>>>> 3ca36821043a3a7aabd3cb38d322b8d5def9c53b

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

<<<<<<< HEAD
#Your own theme

Get the example of css in the folder 'custom_theme' and Make your chages.
Then put it in any static folder of any app. You will just need the url
of this css. 

So if you put it in the 'home' app, the url may be '/static/home/my_theme.css'

Then...

    <head>
        {% code_script 'python,custom,/static/home/my_theme.css' %}
            ...
    <head>

=======
>>>>>>> 3ca36821043a3a7aabd3cb38d322b8d5def9c53b
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
<<<<<<< HEAD
    python;
    java;
    php;
    ruby;
    javascript;
    pascal;

Themes:
    atom;  (yes, it is just the same that atom program)
    custom;
=======

    python;
    pascal

Themes:

    atom  (yes, it is just the same that atom program)
>>>>>>> 3ca36821043a3a7aabd3cb38d322b8d5def9c53b
