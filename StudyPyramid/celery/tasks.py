# coding: utf-8

"""
0. Coming from:
http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

1. Install
$ sudo apt-get install rabbitmq-server
$ easy_install Celery
$ easy_install pytz

2. Running
$ celery -A tasks worker --loglevel=info
Daemon mode: http://docs.celeryproject.org/en/latest/tutorials/daemonizing.html#daemonizing
>>> from tasks import add
>>> add.delay(4, 4)

3. Help
$ celery worker --help # look up command help, e.g. 'worker' here
$ celery --help # list other commands
"""

from celery import Celery

# Set no backend
#
# celery = Celery('tasks', broker='amqp://guest@localhost//')
#
# You can't play with result, if there is no backend set like below

# Set backend if you want to store or send the states somewhere
#
# celery = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')
#
# Thus, you could do this:
# >>> result = add.deplay(4, 4)
# >>> result.ready()
# >>> result.get(timeout=1)
# >>> result.get(propagate=True)
# >>> result.traceback

# Go with configuration
celery = Celery('tasks')
celery.config_from_object('celeryconfig') # load configuration from celeryconfig.py

@celery.task
def add(x, y):
    return x + y

