#! /bin/bash

wget https://tiny.carla.org/carla-0-9-15-linux
wget https://tiny.carla.org/additional-maps-0-9-15-linux

mkdir Simulator
tar -xvf carla-0-9-15-linux -C Simulator
rm  carla-0-9-15-linux

tar -xvf additional-maps-0-9-15-linux -C Simulator
rm additional-maps-0-9-15-linux

echo Download Finished
