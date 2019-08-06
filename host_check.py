#! /usr/bin/python3
# Basic python script to check if a host is up
# and send a message through Slack
# it can be put inside cron to run automatically

import os
import sys
import slack

slackToken = 'YOUR-SLACK-AUTH-TOKEN'
sc = slack.WebClient(slackToken)

def checkPing(host):
    response = os.system('ping -c 3 ' + host + ' >/dev/null 2>&1')
    
    if response != 0:
        sc.chat_postMessage(channel='#your-channel-here', text=':exclamation: DISASTER: Host ' + host + ' is currently offline! :exclamation:')
    else:
        sc.chat_postMessage(channel='#your-channel-here', text=':white_check_mark: OK: Host ' + host + ' seems to be running smoothly! :slightly_smiling_face:')

checkPing(str(sys.argv[1]))