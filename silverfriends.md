# SKT NUGU PLAY 경로당 친구들  
    
> **경로당에 가기 전에 미리 경로당에 몇 명이 있는지 알 수는 없을까?**  
> 노인을 위한 실시간 경로당 인원 알림 서비스  
  
##### 팀 멤버  
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 김지민, kimjiminhy@gmail.com  
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 박철우, thoutan@gmail.com  
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 변보선, eoqkr1217@hanyang.ac.kr    
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 장경희, gkdlfl1237@gmail.com  
&nbsp;&nbsp;&nbsp;&nbsp;한양대학교 정보시스템학과 황현주, dbsg0068@gmail.com    
  ㅤ
  ㅤ
  ㅤ
### 아이디어 및 배경 소개  
-----------------------------------------------
나이가 들어도 친구는 필요합니다.
새로이 친구를 사귀기 힘든 노인 세대가 마음 맞는 친구를 만날 수 있는 곳이 바로 경로당입니다.
친구를 만나러 가는 장소이기 때문에, 경로당에 혼자 있는 것은 누구도 원치 않는 상황이죠.
홀로 오래도록 친구를 기다리다 지쳐 집에 가본 경험을 해본 이도 있을 겁니다.  

할아버지, 할머니들이 하는 일종의 눈치게임이라고도 할 수 있는데요, 현재에는 ‘전화’를 해결책으로 사용하고 있습니다.
경로당으로 전화를 걸어 사람이 있는지 확인하거나, 아는 친구들에게 연락해 경로당에 있는 지 확인하고 경로당으로 출발합니다.
다소 번거로운 일이죠.  

그래서 저희들은 생각했습니다.  

*‘전화를 하지 않고도 경로당에 몇 명이 있는지 알 수 있다면 일일이 전화할 필요가 없지 않을까?’*  
  
  ㅤ
  ㅤ
  ㅤ
### 사용 기술
-----------------------------------------------
##### * OpenCV & People Counting
라즈베리파이, 카메라 모듈과 openCV를 활용하여 People Counter(인원 계수기)를 만들고 이를 경로당 출입문에 설치합니다.  
카메라에서 전송되는 영상을 실시간으로 분석해 People Counting기능을 구현하고, 해당 공간에 몇 명이 있는지 알려줍니다.  
  
![](./image/silverfriend/people_count.png)

> **공간에 들어온 인원 수 - 공간을 나간 인원 수 = 현재 공간에 있는 인원 수**  
  
  ㅤ
  ㅤ
  ㅤ
### 서비스 구성도 및 예상 발화
-----------------------------------------------
구성도를 통해 ‘경로당 친구들’ 서비스를 살펴볼까요?

사용자가 NUGU에게 경로당에 몇 명이 있는지 질문하면, NUGU는 사용자의 ID를 '경로당 친구들’ 서비스의 프록시 서버로 전달합니다. 프록시 서버는 데이터베이스에 접근하여 해당 사용자 ID에 등록된 경로당이 어디인지와 그 경로당에 설치되어 있는 라즈베리파이(People Counter)가 무엇인지 확인합니다. 이후 프록시 서버는 해당 People Counter에게 해당 공간 내 인원 수를 요청합니다. 이에 따른 응답을 NUGU를 통해 사용자에게 전달합니다.  
  
![](./image/silverfriend/service_flow.jpeg)
  
그럼 이제 여러 시나리오를 통해, '경로당 친구들'서비스가 어떻게 작동하는 지 살펴볼게요.
  
 #### 기본 시나리오  
 | | |
 |------------|---------------|
 | 사용자 | 아리아, 경로당 친구들 시작해줘 |
 | NUGU | 안녕하세요, 경로당 친구들입니다. 경로당에 친구 몇 분이 계신지 궁금하세요? '궁금해' 혹은 '아니'라고 말해주세요. |
 | 사용자 | 궁금해 |
 | NUGU | 현재 행당동 경로당에는 다섯 분이 계세요. 놀러가셔도 좋을 것 같아요. 즐거운 시간 보내세요~ |
   
주 사용자의 연령대를 감안하여 최소한의 발화를 통해 서비스를 제공할 수 있도록 설계하였습니다. 문장 형태의 발화를 하지 않고도 서비스 실행 후 '궁금해' 라고만 말하면 원하는 정보를 얻을 수 있습니다. NUGU 서비스 활용에 능숙하고 ‘경로당 서비스'를 좀 더 빠르게 이용하고자 하는 사용자들을 위해 아래와 같은 시나리오도 제공합니다.  
 
  
#### 시나리오 2  
 | | |
 |------------|---------------|
 | 사용자 | 아리아, 경로당 친구들에서 친구 몇 명 있는지 알려줘 |
 | NUGU | 안녕하세요, 경로당 친구들입니다. 현재 행당동 경로당에는 5분이 계세요. 즐거운 시간 보내세요~ |

시나리오 1보다는 필요로 하는 사용자의 발화가 길지만 더욱 빠르게 경로당의 인원을 파악할 수 있다는 장점이 있습니다. 위의 두 시나리오는 사용자의 경로당 위치가 미리 설정이 되어있을 때를 가정한 예상 발화 흐름입니다. 만약 사전에 사용자의 경로당 위치가 설정이 안된 경우엔 어떻게 될까요?  
  
  
#### 시나리오 3(경로당 설정이 안 된 경우)  
 | | |
 |------------|---------------|
 | 사용자 | 아리아, 경로당 친구들에서 친구 몇 명 있는지 알려줘 |
 | NUGU | 안녕하세요, 경로당 친구들입니다. 현재 어느 경로당을 이용하시는지 알 수 없어요. 어플리케이션을 실행하여 경로당 주소를 설정해주세요. |
   
 이처럼 경로당 위치를 설정해달라는 안내와 함께 서비스가 종료됩니다. '경로당 친구들' 어플리케이션을 통해 경로당 위치를 사전 등록한 후에 서비스 이용이 가능합니다.  
  
 
 ### 프로젝트 과정
 --------------------------
 프로젝트의 진행 과정은 다음과 같이 4개의 부분으로 나누어져 진행되었습니다.  
 
 > 1. 라즈베리파이를 이용한 People Counter 개발
 > 2. 프록시 서버 및 DB 개발
 > 3. 경로당 등록 기능 프로토타이핑
 > 4. NUGU Play개발(Play Builder) 및 연동
 
 
### 코드 설명  
--------------------------
#### 1. 필요한 모듈
~~~python
    import numpy as np
import cv2
import Person
import time
import imutils
import datetime
from imutils.video import VideoStream
~~~
  

#### 2. Mog2 Substractor 적용 및 프레임 바이너리화   
~~~python
    # Mog2 Substractor 적용
    fgmask = fgbg.apply(frame)

    try:
        ret,imBin= cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        mask0 =  cv2.morphologyEx(imBin ,  cv2.MORPH_OPEN, kernelOp2)
        mask =  cv2.morphologyEx(mask0 , cv2.MORPH_CLOSE, kernelCl2)
    except:
        print('EOF')
        break
~~~
  
  
#### 3. 컨투어가 너무 큰경우 반으로 자른다   
~~~python
########컨투어가 너무 큰경우 반으로 자른다
    mask2_flag=0

    for cnt in contours0:
        area = cv2.contourArea(cnt)
        if area > areaTH :
            x,y,w,h = cv2.boundingRect(cnt)

            # wmax 는 한사람의 최대넓이. 만약 바운딩 렉트의 넓이가 설정한 wmax 보다 크다면 두사람이 붙어있는 거니까
            # 중간을 딱 잘라버린다.
            if w > wmax:

                mask2 = cv2.line( mask, (int(x+w/2), 0), (int(x+w/2),min(320, frame.shape[1])),(0,0,0), 10)

                mask2_flag=1

    if mask2_flag==0:
        mask2=mask
~~~


#### 4. 펄슨 객체 리스트에 등록된 객체가 여전히 프레임 안에 있으면서 제대로 인식이 되고 있는지 확인   
~~~python
            #################
            #   펄슨 객체 리스트에 등록된 객체가 여전히 프레임 안에 있으면서 제대로 인식이 되고 있는지 확인
            #################
        for i in persons:
            i.updateDingimas(i.getDingimas()+1) # 각 퍼슨 객체가 인식되지 않은 프레임 수를 1씩 더해서 계산.
            # 만약 Dingimas가 25 이상이면,(즉 25 프레임 동안 해당 퍼슨 객체가 프레임 내에서 발견되지 않았으면)
            # 해당 퍼슨은 더이상 프레임 내에 존재하지 않는다는 의미로 간주하고 해당 퍼슨을 퍼슨스 리스트에서 제거.
            # 그 이유는 현재 프레임 내에 존재하는 컨투어와 퍼슨을 비교해서 동일한 영역이 발견될 경우 해당 퍼슨의 dingimas를
            # 0으로 업데이트 하기 때문.
            if i.getDingimas() > 10:
                persons.remove(i)

        if area > areaTH:
            #################
            #   오브젝트 트래킹
            #################
            M = cv2.moments(cnt)
            # 무게중심 구하기
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x,y,w,h = cv2.boundingRect(cnt)

            # 현재 프레임 안에서 발견되는 컨투어에 각각 일단 new True로 하고
            new = True
            # 현재 펄슨스 객체 리스트에 등록된 각 펄슨 객체에 대하여 비교.
            for i in persons:
                # 각각의 퍼슨 객체와 비교했을때 그 차가 설정한 넓이마진과 높이마진 보다 작거나 같으면
                # 해당 컨투어 영역은 새로 발견된 사람이 아니다.
                # 따라서 new 를 False로 바꾼다
                # 즉, 같은사람에게 계속해서 새로운 번호가 할당되는 문제가 발생할 경우 높이 마진과 넓이 마진을 셋팅하면 됨.
                if abs(x-i.getX()) <= w_margin and abs(y-i.getY()) <= h_margin:
                    new = False
                    i.updateCoords(cx,cy)  # 해당 사람의 중심값 새로 업데이트.
                    i.updateDingimas(0) # dingima 초기화 하기.
                    break

                # 그게 아닐경우 해당 컨투어는 새로운 사람으로 인식된다.
                # 따라서 새로운 퍼슨객체를 생성하고 퍼슨객체 리스트인 퍼슨스에 추가한다.
            if new == True:
                p = Person.MyPerson(pid,cx,cy, max_p_age)
                persons.append(p)
                pid += 1

            cv2.circle(frame,(cx,cy), 5, (0,0,255), -1)
~~~  
  
#### 5. 추적중인 객체의 트래킹 라인을 출력한다. & 선이 교차했다면 지나간 라인에 해당하는 수를 카운트한다
~~~python
    #########################
    # 추적중인 객체의 트래킹 라인을 출력한다.
    #########################
    for i in persons:
        if len(i.getTracks()) >= 2:
            pts = np.array(i.getTracks(), np.int32)
            pts = pts.reshape((-1,1,2))
            frame = cv2.polylines(frame,[pts],False,i.getRGB())
         #################
         #  선이 교차하는지 확인한다. 즉 트래킹라인과 업라인 혹은 다운라인이 교차하는지 파악한다.
         #  선이 교차했다면 지나간 라인에 해당하는 수를 카운트한다.
         #################
        if i.getDir() == None:
            i.kurEina( pts_L2[0,1] ,pts_L1[0,1])   #      def kurEina(bSottom_line,top_line):
            if i.getDir() == 'up':
                cnt_up+=1
                print('Timestamp: {:%H:%M:%S} UP {}'.format(datetime.datetime.now(), cnt_up))
            elif i.getDir() == 'down':
                cnt_down+=1
                print('Timestamp: {:%H:%M:%S} DOWN {}'.format(datetime.datetime.now(), cnt_down))



        cv2.putText(frame, str(i.getId()),(i.getX(),i.getY()),font,0.7,i.getRGB(),1,cv2.LINE_AA)
~~~
  
  
#### 6. 화면에 카운트와 인 라인, 아웃 라인, 텍스트를 표시하기 위한 부분.
~~~python
    #########################
    # 화면에 카운트와 인 라인, 아웃 라인, 텍스트를 표시하기 위한 부분.
    #########################
    str_up='IN: '+ str(cnt_up)
    str_down='OUT: '+ str(cnt_down)
    frame = cv2.polylines( frame, [pts_L1], False, line_down_color,thickness=4)
    frame = cv2.polylines( frame, [pts_L2], False, line_up_color,thickness=4)
    cv2.putText(frame, str_up, (10,30), font,0.5,(0,0,255), 1,cv2.LINE_AA)
    cv2.putText(frame, str_down, (10,50), font,0.5,(255,0,0), 1,cv2.LINE_AA)
~~~
