# SKT NUGU PLAY 푹 잔 느낌  
   
> **아침에 가장 상쾌하게 일어나기 위해서 몇 시에 자야 할까?**  
> 푹 잔 기분으로 일어나고 싶은 현대인을 위한 취침 시각 계산기


  
##### 팀 멤버
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 김지민, kimjiminhy@gmail.com  
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 박철우, thoutan@mail.com  
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 변보선, eoqkr1217@hanyang.ac.kr    
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 장경희, gkdlfl1237@gmail.com  
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 황현주, dbsg0068@gmail.com  
  ㅤ
  ㅤ
  ㅤ
### 아이디어 및 배경 소개  
-----------------------------------------------
일찍 잤는데도 다음날 아침 알람을 듣는 것조차 힘들 때가 있습니다.
한편 새벽 늦게 잠들었는데도 아침에 상쾌하고 푹 잤다는 느낌을 받으며 깨기도 합니다.

*'많이 잤는데도 피곤하고, 적게 잤는데도 개운한 이유가 무엇일까?'*

푹 잔 느낌 프로젝트는 이러한 의문에서 시작 되었습니다.  
  
사람의 수면은 단순히 잠에 들고 깨는 과정이 아닙니다.
수면에는 총 5단계가 있습니다. 1단계부터 4단계를 비렘수면(Non-REM), 나머지를 렘수면(REM)이라고 합니다.  
  
* 수면의 1단계: 작은소리에도 금방 눈이 떠지고, 5분 후 2단계로 진입  
* 수면의 2단계: 두 개의 뇌파가 확인되고 10~15분 후 3단계로 진입  
* 수면의 3단계: 깊은 수면 진입 단계, 맥박과 호흡 등이 안정됨.  
* 수면의 4단계: 숙면의 단계, 잠을 깨기 어렵고 온 몸이 쉬는 단계.  
* REM수면 단계: 최고 숙면의 단계, 온몸의 근육이 풀어지고 긴장도가 최소화.
  
![](https://inmun360.culture.go.kr/upload/board/image/95/2358895_201810251428505600.jpg)
  
이렇듯 수면에는 여러 단계가 있기 때문에 우리가 어떤 단계일 때 일어나냐에 따라 기상 시의 기분이 달라집니다.
수면의 3, 4단계나 REM수면 단계일 때 기상 알람이 울려 잠에서 깨면, 숙면 중에 억지로 깬 것이라 극심한 피로감을 느낄 수 밖에 없습니다.
따라서 보다 개운하게 일어나려면 수면의 1,2단계에서 깨어나야 합니다.

원하는 기상 시각에 수면의 1,2 단계에 진입하려면 어떻게 해야할까요? 수면의 단계별 시간은 이미 과학적으로 확인된 바 있습니다. ([『Physiology, Sleep Stages Aakash K. Patel; John F. Araujo.』](https://www.ncbi.nlm.nih.gov/pubmed/30252388))
이에 따르면 수면의 5단계를 모두 거치기 위해서는 약 90분 정도의 시간이 필요합니다.
따라서 우리가 7, 8시간정도 잠을 자면 그동안 수면의 5단계가 대략 4, 5번정도 반복됩니다.
이를 역으로 계산하면 언제 자야 할 지 알 수 있습니다.

하지만 바쁜 현대인에게 몇시에 자야 할 지를 매번 계산하는 것은 매우 귀찮은 일입니다.
‘푹 잔 느낌’ 서비스는 이용자가 원하는 기상 시각을 입력하면 수면의 1, 2단계에서 깨어날 수 있는 취침 시각을 대신 계산해 줍니다.

계산된 취침 시각에 잠들면 수면의 1단계 혹은 2단계일 때 기상하므로, 피로감을 덜고 개운하게 일어날 수 있습니다.

‘푹 잔 느낌’ 서비스는 잠에 드는 시각이 불규칙하여 기상 시에 피로감을 느끼는 현대인들에게 개운한 아침을 선사합니다!  
  ㅤ
  ㅤ
  ㅤ
### 구성도 및 예상 발화
-----------------------------------------------
코드를 살펴보기에 앞서, '푹 잔 느낌'서비스의 구성도를 살펴볼까요?  
  
아래 그림은 첫 실행 발화(Ex. ‘아리아, 푹 잔 느낌 실행해줘’)를 통해 서비스에 진입한 후를 보여주는 구상도입니다.

예를 들어 사용자가 자신이 일어나고 싶은 ‘오전 6시 30분’을 NUGU에게 전달하면, NUGU는 ‘푹 잔 느낌’의 프록시 서버와 통신하여 사용자가 잠들어야 할 시각(앞으로 ‘취침 시각’이라고 지칭) 목록을 받아옵니다. 취침 시각은 발화가 시작된 시각(앞으로 ‘현재 시각’이라고 지칭)과 수면 시간을 모두 고려하여 계산합니다.
  
![](./image/serviceflow.jpeg)
  
구성도가 이해되셨나요? 이어서 예상 발화를 통해 ‘푹 잔 느낌’이 제공하는 서비스를 좀 더 깊게 살펴보겠습니다.  

#### 기본 시나리오
  
  | | |  
  |----------|----------------|  
  | 사용자 | 아리아, 푹 잔 느낌 실행해줘 |  
  | NUGU | 안녕하세요, 푹 잔 느낌입니다. 몇 시에 일어나실 예정이세요? '오전 7시' 혹은 '오후 8시 30분' 처럼 말씀해 주세요. |  
  | 사용자 | 오전 8시 30분에 일어날거야. |  
  | NUGU | 오전 1시나 오전 2시 30분에 주무시면 개운하게 일어나실 수 있어요. 더 늦게 주무실 예정인가요? |  
  | 사용자 | 아니, 괜찮아 |  
  | NUGU | 푹 잔 느낌 서비스를 종료합니다. 안녕히 주무세요~ |  

가장 기본이 되는 발화 흐름입니다. ‘푹 잔 느낌’ 서비스는 사용자로부터 입력받은 기상 시각 ‘오전 8시 30분’에 대해 3개의 취침 시각을 계산합니다. 수면 사이클이 90분간 지속되므로, ’7시간 30분’, ‘6시간’ 그리고 ‘4시간 30분’이 수면의 1,2단계에 기상하기 위해 적절한 수면 시간입니다. 따라서 취침 시각 목록은 ‘오전 1시’, ‘오전 2시 30분’과 ‘오전 4시’가 됩니다.

이 중에서 현재 시각을 고려해 두개의 값을 골라 사용자에게 전달합니다. 사용자에게 알려준 취침 시각이 이미 지나갔다면 의미가 없을테니까요. 혹시 더 늦게 취침하고 싶은 사용자를 위해 ‘더 늦게 주무실 예정인가요?’ 와 같은 추가질문도 제공합니다.

만약 시각이 너무 늦어 사용자에게 알려줄 수 있는 시각이 하나 뿐일 경우에는 어떻게 될까요?  
  
  
#### 시나리오 2(알려줄 수 있는 시각이 1개인 경우)
  
  | | |  
  |----------|----------------|  
  | 사용자 | 아리아, 푹 잔 느낌 실행해줘 |  
  | NUGU | 안녕하세요, 푹 잔 느낌입니다. 몇 시에 일어나실 예정이세요? '오전 7시' 혹은 '오후 8시 30분' 처럼 말씀해 주세요. |  
  | 사용자 | (현재 시각이 오전 3시)오전 8시 30분에 일어날거야. |  
  | NUGU | 오전 4시에 주무시면 됩니다. 1시간 남았네요. 안녕히 주무세요~ |  
  
  
위의 예시처럼, 하나의 취침 시각을 알려주고 그 시각까지 남은 시간을 계산하여 알려줍니다. 그리고 취침 시각 목록에 더 남은 시각이 없기 때문에 ‘더 늦게 주무실 예정인가요?’ 등의 추가 질문 없이 서비스를 종료합니다.  

#### 시나리오 3(알려줄 수 있는 시각이 없는 경우)
  
  | | |  
  |----------|----------------|  
  | 사용자 | 아리아, 푹 잔 느낌 실행해줘 |  
  | NUGU | 안녕하세요, 푹 잔 느낌입니다. 몇 시에 일어나실 예정이세요? '오전 7시' 혹은 '오후 8시 30분' 처럼 말씀해 주세요. |  
  | 사용자 | (현재 시각이 오전 4시 30분)오전 8시 30분에 일어날거야. |  
  | NUGU | 수면 시간이 부족하니 지금 바로 주무시는 건 어떤가요? 다음부턴 꼭 4시간 30분 이상 주무시길 바라요. 푹 잔 느낌 서비스를 종료합니다. |  
  
‘푹 잔 느낌’ 서비스가 계산하는 최소 수면 시간은 4시간 30분입니다. 따라서 가능한 수면 시간이 4시간 30분 보다 적을 경우, 취침 시각을 계산해드리지 않습니다. 취침 시각을 알려줄 수 없기 때문에 4시간 30분 이상의 수면을 권장하는 멘트과 함께 서비스를 종료합니다.  
  ㅤ
  ㅤ
  ㅤ
### 코드 설명
-----------------------------------------------
  
~~~python
import pytz
import datetime
from flask import Flask, make_response
from flask_cors import CORS
from helper import request
import json

application = Flask(__name__)
CORS(application, max_age=31536000, supports_credentials=True)

def time_calculate(hour, min):

    # input_time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=hour, minute=min))
    input_time = datetime.datetime.now().astimezone(pytz.timezone('Asia/Seoul')).replace(hour=hour,minute=min,second=0,microsecond=0)
    kst_now = datetime.datetime.now().astimezone(pytz.timezone('Asia/Seoul'))
    # input_time = input_time.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))

    if input_time.hour < kst_now.hour:
        input_time = input_time.replace(day=input_time.day+1)
    elif input_time.hour == kst_now.hour:
        if input_time.minute < kst_now.minute:
            input_time = input_time.replace(day=input_time.day+1)

    time_one = input_time - datetime.timedelta(minutes=465)
    time_two = input_time - datetime.timedelta(minutes=375)
    time_three = input_time - datetime.timedelta(minutes=285)

    return kst_now, time_one, time_two, time_three


def time_transform(input_time):

    try:
        ampm = "오후" if input_time.hour>12 else "오전"
        sleep_hour = input_time.hour-12 if input_time.hour>12 else input_time.hour
        if sleep_hour == 0:
            sleep_hour = 12

        
        result = f"{ampm} {sleep_hour}시"
        
        if input_time.minute != 0:
            result += f" {input_time.minute}분"

        return result

    except AttributeError:

        sleep_hour = input_time.seconds // 3600
        sleep_min = input_time.seconds % 3600 // 60

        if sleep_hour != 0:
            result = f"{sleep_hour}시간"
            if sleep_min != 0:
                result += f" {sleep_min}분"
        else:
            result = f"{sleep_min}분"

        return result


@application.route("/answer.go_to_bed_time", methods=['POST', 'GET'])

def go_to_bet_time():

    data = request.get_json(silent=True, force=True)['action'].get('parameters')
    wakeup_time_duration = data.get('wakeup_time_duration').get('value')
    wakeup_time_hour = data.get('wakeup_time_hour').get('value')
    wakeup_time_min = data.get('wakeup_time_min',dict()).get('value', '0')

    wakeup_time_hour = int(wakeup_time_hour)
    wakeup_time_min = int(wakeup_time_min)

    if wakeup_time_duration == "오전":
        if wakeup_time_hour > 12:
            return make_response({"resultCode": "exception_common",
                                "output": "exception_common"})
    else:
        if wakeup_time_hour < 12:
            wakeup_time_hour += 12

    kst_now, time_one, time_two, time_three = time_calculate(wakeup_time_hour, wakeup_time_min)

    output_times = dict()

    print(f"wakeup_time_hour = {wakeup_time_hour}")
    print(f"wakeup_time_min = {wakeup_time_min}")
    print(kst_now)
    print(time_one)
    print(time_two)
    print(time_three)

    if kst_now < time_one:
        output_times['best_sleep_time1'] = time_transform(time_one)
        output_times['best_sleep_time2'] = time_transform(time_two)
        output_times['best_sleep_time3'] = time_transform(time_three)
        output_times['remain_time'] = time_transform(time_one-kst_now)
    elif time_one < kst_now < time_two:
        output_times['best_sleep_time2'] = time_transform(time_two)
        output_times['best_sleep_time3'] = time_transform(time_three)
        output_times['remain_time'] = time_transform(time_two-kst_now)
    elif time_two < kst_now < time_three:
        output_times['best_sleep_time3'] = time_transform(time_three)
        output_times['remain_time'] = time_transform(time_three-kst_now)
    elif time_three < kst_now:
        output_times['default_lack_of_sleep'] = "True"


    # output 형태느 다음과 같다.
    output = {
                "resultCode": "OK",
                "output": output_times
            }

    return make_response(output)


@application.route("/time1", methods=['POST'])
def time_one():
    data = request.get_json(silent=True, force=True)['action'].get('parameters')

    output_times = dict()
    print(data)

    output_times['best_sleep_time1'] = data['best_sleep_time1'].get('value')
    output_times['remaine_time'] = data['remain_time'].get('value')

    output = {
        "resultCode": "OK",
        "output": output_times
    }

    return make_response(output)


@application.route("/time2", methods=['POST'])
def time_two():
    data = request.get_json(silent=True, force=True)['action'].get('parameters')

    output_times = dict()
    print(data)

    output_times['best_sleep_time2'] = data['best_sleep_time2'].get('value')
    output_times['remain_time'] = data['remain_time'].get('value')

    output = {
        "resultCode": "OK",
        "output": output_times
    }

    return make_response(output)



@application.route("/time3", methods=['POST'])
def time_three():
    data = request.get_json(silent=True, force=True)['action'].get('parameters')

    output_times = dict()
    print(data)

    output_times['best_sleep_time3'] = data['best_sleep_time3'].get('value')
    output_times['remain_time'] = data['remain_time'].get('value')

    output = {
        "resultCode": "OK",
        "output": output_times
    }

    return make_response(output)


@application.route("/later_time1", methods=['POST'])
def later_time_one():
    data = request.get_json(silent=True, force=True)['action'].get('parameters')

    output_times = dict()
    print(data)

    output_times['best_sleep_time2'] = data['best_sleep_time2'].get('value')
    output_times['best_sleep_time3'] = data['best_sleep_time3'].get('value')

    output = {
        "resultCode": "OK",
        "output": output_times
    }

    return make_response(output)


@application.route("/later_time2", methods=['POST'])
def later_time_two():
    data = request.get_json(silent=True, force=True)['action'].get('parameters')

    output_times = dict()
    print(data)

    output_times['best_sleep_time3'] = data['best_sleep_time3'].get('value')

    output = {
        "resultCode": "OK",
        "output": output_times
    }

    return make_response(output)


@application.route("/default_lack_of_sleep", methods=['POST','GET'])
def default_lack_of_sleep():

    output = {
        "resultCode": "OK",
        "output": dict()
    }

    return make_response(output)

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000, threaded=True)


~~~
