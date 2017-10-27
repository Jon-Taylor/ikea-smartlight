#!/usr/bin/env python

# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import os.path
import json

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file
import sandbox as sb
import piLight as pilight
import re

local_commands=['blue', 'lounge', 'lights', 'off', 'on', 'downstairs','dim']
def process_event(event,assistant):
    """Pretty prints events.
    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.
    Args:
        event(event.Event): The current event to process.
    """
    if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        print(event.args['text'])
        if any(set(local_commands) & set(event.args['text'].lower().split())):
            assistant.stop_conversation()
            pilight.ledOff()
            BrightnessValue = re.findall('\d+',event.args['text'])
            cmmd=list(set(local_commands) & set(event.args['text'].lower().split()))
            
            if 'on' in cmmd or 'dim' in cmmd and 'downstairs' in cmmd:
                if len(BrightnessValue) == 0:
                    print('Turing downstairs lights on')
                    sb.downstairsLights(100)
                else:
                    print('Dimming downstairs lights on')
                    sb.downstairsLights(int(BrightnessValue[0]))
            if 'off' in cmmd and 'downstairs' in cmmd:
                print('Turing downstairs lights off')
                sb.downstairsLights(0)

            if 'on' in cmmd or 'dim' in cmmd and 'blue' in cmmd:
                if len(BrightnessValue) == 0:
                    sb.BlueLoungeLights(100)
                else:
                    sb.BlueLoungeLights(int(BrightnessValue[0]))
            if 'off' in cmmd and 'blue' in cmmd:
                sb.BlueLoungeLights(0)

            if 'on' in cmmd or 'dim' in cmmd and 'kitchen' in cmmd:
                if len(BrightnessValue) == 0:
                    print('Turing kitchen lights on')
                    sb.kitchenLights(100)
                else:
                    print('Dimming downstairs lights on')
                    sb.kitchenLights(int(BrightnessValue[0]))
            if 'off' in cmmd and 'kitchen' in cmmd:
                print('Turing downstairs lights off')
                sb.kitchenLights(0)

            if 'on' in cmmd or 'dim' in cmmd and 'brown' in cmmd:
                if len(BrightnessValue) == 0:
                    sb.BrownLoungeLights(100)
                else:
                    sb.BrownLoungeLights(int(BrightnessValue[0]))
            if 'off' in cmmd and 'brown' in cmmd:
                sb.BrownLoungeLights(0)

            if 'on' in cmmd or 'dim' in cmmd and 'dining' in cmmd:
                if len(BrightnessValue) == 0:
                    sb.DiningRoomLights(100)
                else:
                    sb.DiningRoomLights(int(BrightnessValue[0]))
            if 'off' in cmmd and 'dining' in cmmd:
                sb.DiningRoomLights(0)



    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        pilight.ledQuestionMark()
        print()
        

    print(event)

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        pilight.ledOff()
        print()

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event,assistant)


if __name__ == '__main__':
    main()
