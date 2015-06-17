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
