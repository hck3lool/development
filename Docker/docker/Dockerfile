FROM ubuntu:14.04
RUN apt-get update && apt-get install --yes --no-install-recommends \
tightvncserver \
at-spi2-core \
cups-daemon \
cups-filters \
cups-pdf \
dbus \
dbus-x11 \
feh \
gir1.2-atk-1.0 \
gir1.2-atspi-2.0 \
gir1.2-freedesktop \
gir1.2-gdkpixbuf-2.0 \
gir1.2-gtk-3.0 \
gir1.2-pango-1.0 \
gir1.2-wnck-3.0 \
git \
gsoap \
language-pack-ar \
language-pack-ar-base \
language-pack-en-base \
libao-dev \
libarchive13 \
libatk-adaptor \
libcos4-1 \
libcups2 \
libcupsimage2 \
libcurlpp0 \
libevdev2 \
libgail-common \
libgail18 \
libglib2.0-0 \
libgtkmm-3.0-1 \
libjack-jackd2-0 \
liblog4cxx10 \
libnet1 \
libomniorb4-1 \
libowcapi-2.8-15 \
libpcsclite1 \
libpng12-0 \
libprotobuf8 \
libqrencode3 \
libsdl2-mixer-2.0-0 \
libsigc++-2.0-0c2a \
libsoundtouch0 \
libudev1 \
libusb-1.0-0 \
libuuid1 \
libwebkit2gtk-3.0-25 \
libwnck-3-0 \
libwnck-3-common \
libxerces-c3.1 \
libxml-security-c17 \
libxml2 \
libxml2-dev \
libxslt1-dev \
libxslt1.1 \
libzbar0 \
netplug \
openbox \
openssl \
pcscd \
ppp \
python-dev \
python-gobject \
python-paramiko \
python-pip \
python-pyatspi \
python-pyatspi2 \
python-twisted \
python-twisted-web \
python-wnck \
ttf-devanagari-fonts \
udevil \
usb-modeswitch \
usbutils \
x11-xserver-utils \
xfonts-base \
xserver-xorg-video-dummy \
xfonts-intl-asian \
xfonts-intl-chinese \
xfonts-wqy \
xinit \
zlib1g-dev \
git \
wget \
librsvg2-common

ADD machine-scripts /root/machine-scripts
ADD vnc /root/.vnc
ADD automated-tests /root/automated-tests
ADD main-files /root/main-files
ADD packages /root/packages

ENV DISPLAY=:1
ENV USER=root

CMD  /bin/bash 
