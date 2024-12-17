#! /bin/bash

pyenv install 3.7.17
pyenv virtualenv 3.7.17 carla-env
pyenv activate carla-env
pip install -r requirements.txt
