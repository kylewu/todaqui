from fabric.api import local, env, sudo

env.use_ssh_config = True
env.hosts = ['vps', ]


def deploy():
    collect()
    upload()


def collect():
    sprite()
    local('./manage.py staticsitegen')
    local('./manage.py collectstatic --noinput')


def upload():
    local('cd output && tar -zcvf ../upload.tar.gz .')
    local('scp upload.tar.gz vps:/tmp')
    sudo('rm -rf /var/www/todaqui.es/public_html/*')
    sudo('tar -zxvf /tmp/upload.tar.gz -C /var/www/todaqui.es/public_html/')


def sprite():
    local('grunt sprite')


def run():
    local('cd output && python -m SimpleHTTPServer')


def dump():
    local('./manage.py dumpdata --indent 2 auth contenttypes hotsite topic > fixtures.json')


def load():
    local('./manage.py loaddata fixtures.json')
