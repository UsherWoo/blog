# mod_wsgi-express setup-server blog/wsgi.py --host=192.168.231.129 --port=8000 --user apache --group apache --server-root=apache-wsgi
# mod_wsgi-express setup-server blog/wsgi.py --host=192.168.231.128 --port=8000 --user apache --group apache --server-root=apache-wsgi
mod_wsgi-express setup-server blog/wsgi.py --user apache --group apache --server-root=apache-wsgi --url-alias '/static' '/mnt/django/blog/statics'
