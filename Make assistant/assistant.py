from weather import WeatherApi
from tts import speak
from stt import SttEngine
from naver import search_naver

class Assistant:
    def __init__(self, weather_api_key):
        self.stt_engine = SttEngine()
        self.weather_api = WeatherApi(weather_api_key)
        self.action_phrase={'검색':{'type':'act','need_args':True,'msg':'검색하겠습니다.','command':search_naver},
                            '날씨':{'type':'speak','need_args':True,'msg':'실시간 날씨를 알려드릴게요.','command':self.weather_api.weather_sta},
                            '기온':{'type':'act','need_args':True,'msg':'실시간 기온을 알려드릴게요.','command':self.weather_api.weather_temp},
                            '미세먼지':{'type':'act','need_args':True,'msg':'실시간 대기정보를 알려드릴게요.','command':self.weather_api.weather_air}}
        self.error_phrase={'type':None, 'need_args':None, 'msg':'다시 말씀해주세요.', 'command':None}
        self.is_ready = True
        
    def analyze_phrase(self, phrase):
        splited_phrase = phrase.split()
        action = splited_phrase[-1].strip()
        argument = ''.join(splited_phrase[:-1])
        return action, argument

    def process_phrase(self, action, argument):
        payload = self.action_phrase.get(action, self.error_phrase)
        speak(payload['msg'])
        if not payload['type']:
            return
        result = payload['command'](argument) if payload['need_args'] else payload['command']()
        if payload['type'] == 'speak':
            speak(f"{result}입니다")
            
    # 메인 함수
    def start(self):
        while True:
            speech = self.stt_engine.recognize()
            if self.is_ready: 
                if speech is None: 
                    continue
                action, argument = self.analyze_phrase(speech) 
                self.process_phrase(action, argument) 
                self.is_ready = not self.is_ready 
            elif speech == self.name: 
                self.is_ready = True 
                speak('네 말씀하세요.')