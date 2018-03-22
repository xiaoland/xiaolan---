# -*- coding: utf-8 -*-
# 百度STT
import sys
import signal
import requests
import os
import json
import xlpath
import wave
import pyaudio
import hyper
import logging
import time
import os.path
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class baidu_stt(object):
    def __init__(self, intent, voice, text, states, token, url, turl, AK, SK, transcribed, domain, query, json):
        self.voice = voice.wav
        self.text = text
        self.AK = '87oa8ZdtoVLSuVwV4YPqaeD3'
        self.SK = 'wi8G8UEa1tkgAKZbKsUHaZk8V6p4NxvL'
        self.turl = 'http://openapi.baidu.com/oauth/2.0/token'
        self.url = ''
        self.token = ''
        self.states = ['far', 'near', 'middle']
        self.transcribed = transcribed
        self.sttstates = sttstates
        self.domain = domain
        self.intent = intent
        self.json = json

    def get_token():
        try:
            pms = cache.readlines()
            if len(pms) > 0:
                time = pms[0]
                token = pms[1]
                time = dparser.parse(time)
                endtime = datetime.datetime.now()
                if (endtime - time).days <= 29:
                    return token
        finally:
            cache.close()
        url = 'http://openapi.baidu.com/oauth/2.0/token'
        params = urllib.urlencode({'grant_type': 'client_credentials',
                                   'client_id': self.AK,
                                   'client_secret': self.SK})
        r = requests.get(url, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            return token
        except requests.exceptions.HTTPError:
            self._logger.critical('Token request failed with response: %r',
                                  r.text,
                                  exc_info=True)
            tokenstates = r.states()
            return tokenstates
            return token

    def stt(self, fp):
        if self.token == '':
            self.token = self.get_token()
        try:
            wav_file = wave.open(fp, 'rb')
        except IOError:
            self._logger.critical('wav file not found: %s',
                                  fp,
                                  exc_info=True)
            return []
        n_frames = wav_file.getnframes()
        frame_rate = wav_file.getframerate()
        audio = wav_file.readframes(n_frames)
        base_data = base64.b64encode(audio)
        if self.token == '':
            self.token = self.get_token()
        data = {"format": "wav",
                "token": self.token,
                "len": len(audio),
                "rate": frame_rate,
                "speech": base_data,
                "cuid": str(get_mac())[:32],
                "channel": 1}
        data = json.dumps(data)
        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})
        json = r.json()
        domain = r.json()['domain']
        intent = r.json()['intent']
        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
        except requests.exceptions.HTTPError:
            self._logger.critical('Request failed with response: %r',
                                  r.text,
                                  exc_info=True)
            return []
        except requests.exceptions.RequestException:
            print ('Request failed.')
            return []
        except ValueError as e:
            print ('Cannot parse response: %s',
                                  e.args[0])
            return []
        except KeyError:
            print ('Cannot parse response')
            return []
        else:
            transcribed = []
            if text:
                transcribed.append(text.upper())
            print (u'百度语音识别到了: %s' % text)
            return transcribed

    def nlp(self):
        if intent == 'query':
            if self.domain == 'train':
                arrival_city = r.json()['arrival_city']
                start_city = r.json()['start_city']
                start_station = r.json()['start_station']
                train_type = r.json()['train_type']
            elif self.domain == 'weather':
                date = r.json()['date']
                region = r.json()['region']
            elif self.domain == 'flight':
                start_date = r.json['start_date']
                start_city = r.json()['start_city']
                arrival_city = r.json()['arrival_city']
                airline = r.json()['airline']
            elif self.domain == 'map':
                start = r.json()['start']
