docker build . -t cmdline-controller:v1
docker run -d -it \
    --name LED-CMDline-Controller \
    --privileged \
    cmdline-controller:v1
