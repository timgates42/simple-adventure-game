#!/bin/bash


while : ; do
    git fetch --all
    git merge snorlax/main
    git merge origin/main
    sleep 60
done
