# SKT NUGU PLAY 푹 잔 느낌  
   
> **아침에 가장 상쾌하게 일어나기 위해서 몇 시에 자야 할까?**  
> 푹 잔 기분으로 일어나고 싶은 현대인을 위한 취침 시각 계산기
  

##### 팀 멤버
한양대학교 정보시스템학과 김지민, kimjiminhy@gmail.com  
한양대학교 정보시스템학과 박철우, thoutan@mail.com  
한양대학교 정보시스템학과 변보선, eoqkr1217@hanyang.ac.kr    
한양대학교 정보시스템학과 장경희, gkdlfl1237@gmail.com  
한양대학교 정보시스템학과 황현주, dbsg0068@gmail.com  
  ㅤ
  ㅤ
  ㅤ
### 아이디어 및 배경 소개  
-----------------------------------------------
일찍 잤는데도 다음날 아침 알람을 듣는 것조차 힘들 때가 있습니다.
한편 새벽 늦게 잠들었는데도 아침에 상쾌하고 푹 잤다는 느낌을 받으며 깨기도 합니다.
많이 잤는데도 피곤하고, 적게 잤는데도 개운한 이유가 무엇일까요?
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

원하는 기상 시각에 수면의 1,2 단계에 진입하려면 어떻게 해야할까요? 수면의 단계별 시간은 이미 과학적으로 확인된 바가 있습니다. ([『Physiology, Sleep Stages Aakash K. Patel; John F. Araujo.』](https://www.ncbi.nlm.nih.gov/pubmed/30252388))
이에 따르면 수면의 5단계를 모두 거치기 위해서는 약 90분 정도의 시간이 필요합니다.
따라서 우리가 7, 8시간정도 잠을 자면 그동안 수면의 5단계가 대략 4, 5번정도 반복됩니다.
이를 역으로 계산하면 언제 자야 할 지 알 수 있습니다.

하지만 바쁜 현대인에게 매번 몇시에 자야 할 지를 계산하는 것은 매우 귀찮은 일입니다.
‘푹 잔 느낌’ 서비스는 이용자가 원하는 기상 시각을 입력하면, 수면의 1, 2단계에서 깨어날 수 있는 취침 시각을 대신 계산해 줍니다.

계산된 취침 시각에 잠들면, 수면의 1단계 혹은 2단계일 때 기상하므로 피로감을 덜 느끼며 개운하게 일어날 수 있습니다.

‘푹 잔 느낌’ 서비스는 잠에 드는 시각이 불규칙하여 기상 시에 피로감을 느끼는 현대인들에게 개운한 아침을 선사합니다! 
  ㅤ
  ㅤ
  ㅤ
### 구성도 및 예상 발화
-----------------------------------------------
코드를 살펴보기에 앞서, '푹 잔 느낌'의 구성도를 살펴볼까요?  
  
아래 그림은 첫 실행 발화(Ex. ‘아리아, 푹 잔 느낌 실행해줘’)를 통해 서비스에 진입한 후를 보여주는 구상도입니다. 예를 들어 사용자가 자신이 일어나고 싶은 ‘오전 6시 30분’을 NUGU에게 전달하면, NUGU는 ‘푹 잔 느낌’의 프록시 서버와 통신하여 사용자가 잠들어야 할 시각(앞으로 ‘취침 시각’이라고 지칭) 목록을 받아옵니다. 취침 시각은 발화가 시작된 시각(앞으로 ‘현재 시각’이라고 지칭)과 수면 시간을 모두 고려하여 계산합니다.
  
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

가장 기본이 되는 발화 흐름입니다. ‘푹 잔 느낌’ 서비스는 사용자로부터 입력받은 기상 시각 ‘오전 8시 30분’에 대해 3개의 취침 시각을 계산합니다. 수면 사이클이 90분간 지속되므로, ’7시간 30분’, ‘6시간’ 그리고 ‘4시간 30분’이 수면의 1,2단계에 기상하기 위해 적절한 수면 시간입니다. 따라서 취침 시각 목록은 ‘오전 1시’, ‘오전 2시 30분’과 ‘오전 4시’가 됩니다. 이 중에서 현재 시각을 고려해 두개의 값을 골라 사용자에게 전달합니다. 사용자에게 알려준 취침 시각이 이미 지나갔다면 의미가 없을테니까요. 혹시 더 늦게 취침하고 싶은 사용자를 위해 ‘더 늦게 주무실 예정인가요?’ 와 같은 추가질문도 제공합니다. 만약 시각이 너무 늦어 사용자에게 알려줄 수 있는 시각이 하나 뿐일 경우에는 어떻게 될까요?
  
  
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


### 코드 설명
-----------------------------------------------
  
~~~python
# time_term 만큼 시간을 빼고 한글로 오전 혹은 오후를 붙여서 만들어주는 함수.
def time_calc(input_time, time_term):
    # 입력된 시각에서 time_term만큼 빼준다.
    sleep_time = input_time - timedelta(minutes=time_term)
    sleep_hour = sleep_time.hour
    # 12시가 넘으면 오후이므로 오후를 붙여주고 아니면 오전을 붙여준다
    ampm = "오후" if sleep_time.hour > 12 else "오전"
    # 계산된 시각이 오후일때는 12를 빼준다.
    if sleep_time.hour > 12:
        sleep_hour = sleep_time.hour - 12
    # 오전 00시 일 때 오전 12시로 바꿔줌
    if sleep_hour == 0:
        sleep_hour = 12

    result = "{} {}시".format(ampm, sleep_hour)
    # minute이 0일때는 안붙여줘도 되므로 0이 아닌 경우에만 xx분이라고 붙여준다.
    if sleep_time.minute != 0:
        result += " {}분".format(sleep_time.minute)

    return result


@application.route("/later", methods=['POST'])
@application.route("/answer.go_to_bed_time", methods=['POST', 'GET'])
def wakeup_time():
    # 파라미터 처리
    data = request.get_json(silent=True, force=True)
    data = data["action"].get('parameters')
    wakeup_time_duration = data.get('wakeup_time_duration')
    wakeup_time_duration = wakeup_time_duration.get('value')
    data['wakeup_time_duration'] = wakeup_time_duration
    hour = data.get('wakeup_time_hour')
    hour = hour.get('value')
    data['wakeup_time_hour'] = hour
    min = data.get('wakeup_time_min', 0)
    if min != 0:
        min = min.get('value')
        data['wakeup_time_min'] = min
    later = data.get('later')

    output_times = data

    if not hour:
        return make_response({"resultCode": "exception_1",
                              "output": 'exception_1'})
    hour = int(hour)
    min = int(min)
    if hour > 12:
        hour = hour - 12

    if wakeup_time_duration == '오후':
        hour = hour + 12

    current_time = time(hour=hour, minute=min)
    input_time = datetime.combine(date.today(), current_time)

    # later 없을 때와 있을때 파라미터 다르게 들어가기
    output_times['best_sleep_time1'] = time_calc(input_time, 375)
    output_times['best_sleep_time2'] = time_calc(input_time, 465)
    if later:
        output_times['best_sleep_time3'] = time_calc(input_time, 285)
        output_times['best_sleep_time4'] = time_calc(input_time, 555)
    # output 형태느 다음과 같다.
    output = {
                "resultCode": "OK",
                "output": output_times
            }

    return make_response(output)
~~~
