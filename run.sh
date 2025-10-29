#!/bin/sh
# Run LED-CMDline-Controller interactively
docker build . -t cmdline-controller:v1
docker run -it --rm \
	--name LED-CMDline-Controller \
	cmdline-controller:v1
