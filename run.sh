#!/bin/sh
# This script is used to run the LED-CMDline-Controller in a Docker container.
docker build . -t cmdline-controller:v1
docker run -d -it \
	--name LED-CMDline-Controller \
	--privileged \
	cmdline-controller:v1
