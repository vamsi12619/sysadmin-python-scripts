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
    
    if response == 0:
        print('Host is up') 
        sc.chat_postMessage(channel='#your-channel-here', text='Host is up')
    else:
        print('Host is down')
        sc.chat_postMessage(channel='#your-channel-here', text='Host is down')

checkPing(str(sys.argv[1]))