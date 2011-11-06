import urllib2
from subprocess import Popen, PIPE
from os import path
import json
import httplib


CREATE_URL = u'https://gist.github.com/gists'


def config(key):
    cmd = Popen([u'git', u'config', u'--global', key], stdout=PIPE)
    return cmd.communicate()[0].decode(u'utf-8').strip()


def post_urllib2(url, data):
    req = urllib2.Request(url,
        headers={u'Content-Type': u'application/json'},
        data=json.dumps(data).encode(u'utf-8'))
    return urllib2.urlopen(req).geturl()


def post_curl(url, data):
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile() as f:
        f.write(data)
        f.flush()
        cmd = [u'curl', u'-H', 'Content-Type: application/json', u'-w',
            u'%{url_effective}', u'-L', u'--data', u'@{0}'.format(f.name),
            u'-o', u'/dev/null', url]
        out, err = Popen(cmd, stdout=PIPE).communicate()
    return out.decode(u'utf-8').strip()


if hasattr(httplib, "HTTPSConnection"):
    post = post_urllib2
else:
    post = post_curl


def create(files, private=False, description=None):
    data = {
        u'files': {},
        u'public': not private,
        u'description': description if description else u'Uploaded by gist.py',
        u'login': config(u'github.user'),
        u'token': config(u'github.token'),
    }
    for fn in files:
        #data[u'files'][path.basename(fn)] = {
        #    u'content': open(fn).read(),
        #}
        data[u'files'][path.basename(fn)] = open(fn).read()
    return post(CREATE_URL, json.dumps(data))

if __name__ == u'__main__':
    import sys
    print create(sys.argv[1:])
