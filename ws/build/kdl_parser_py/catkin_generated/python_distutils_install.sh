#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/flysnow/ws/src/kdl_parser_py"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/flysnow/ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/flysnow/ws/install/lib/python2.7/dist-packages:/home/flysnow/ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/flysnow/ws/build" \
    "/usr/bin/python" \
    "/home/flysnow/ws/src/kdl_parser_py/setup.py" \
    build --build-base "/home/flysnow/ws/build/kdl_parser_py" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/flysnow/ws/install" --install-scripts="/home/flysnow/ws/install/bin"
