#!/bin/bash


SLACK_ADVENTURE_TOKEN="$(pass show slack-adventure-token)"
export SLACK_ADVENTURE_TOKEN
python3.9 ./run_slack.py
