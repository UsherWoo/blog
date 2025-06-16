case $1 in
start|stop|restart|graceful|graceful-stop)
sudo systemctl $1 blog
esac
