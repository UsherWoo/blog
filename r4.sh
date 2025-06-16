case $1 in
start|stop|restart|graceful|graceful-stop)
apache-wsgi/apachectl $1
esac
