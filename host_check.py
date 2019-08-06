#! /usr/bin/python3
import os
import sys
import slack

slackToken = 'xoxb-579175396576-717960508053-ENnz0qhuQlNdEODown7h8PvI'
sc = slack.WebClient(slackToken)

def checkPing(host):
    #host = str(sys.argv[1])
    response = os.system('ping -c 3 ' + host + ' >/dev/null 2>&1')
    
    if response == 0:
        print('Host is up') 
        sc.chat_postMessage(channel='#homelab', text='Host is up')
    else:
        print('Host is down')
        sc.chat_postMessage(channel='#homelab', text='Host is down')

checkPing(str(sys.argv[1]))
