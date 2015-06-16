from fabric.api import local


def deploy():
    sprite()
    local('./manage.py staticsitegen')
    local('./manage.py collectstatic --noinput')


def sprite():
    local('grunt sprite')
