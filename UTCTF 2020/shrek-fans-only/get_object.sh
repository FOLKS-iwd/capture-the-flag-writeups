#!/bin/bash

dir=${1:0:2}
obj=${1:2}
mkdir git/.git/objects/$dir
./get_img.sh ".git/objects/$dir/$obj" > git/.git/objects/$dir/$obj
