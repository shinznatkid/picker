Picker - Django Assets Manager
======
Choose your javascript, css framework into your project.

Installation
------------
1. Clone this app to your project.

2. Add 'picker' to INSTALLED_APPS:

        'picker',
3. Define PICKER_INSTALLED_APPS in settings.py 

        PICKER_INSTALLED_APPS = (
            'jquery',
        )
4. Define following tag in templates

        {% load pickertags %}
5. Define following tag inside body in templates

        {% load pickertags %}
        <html>
            <body>
                {% load_js %}
            </body>
        </html>
        
