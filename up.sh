#!/bin/bash


while : ; do
    git fetch --all
    git merge --no-edit snorlax/main
    git merge --no-edit origin/main
    sleep 60
done
