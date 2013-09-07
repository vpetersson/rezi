import os
import platform

from bottle import route, run

# Avoid binding on public OS on OS X.
bind = None
if 'Darwin' in platform.platform():
    bind = '127.0.0.1'
else:
    bind = '0.0.0.0'


@route('/')
def hello_world():
    return 'Hello World!'


run(host=bind, port=int(os.environ.get('PORT', 5000)))
