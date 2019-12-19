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
<br>
&nbsp;
<br>    ㅤ
  
### OpenCV 및 라즈베리파이
-----------------------------------------------
라즈베리파이, 카메라 모듈과 openCV를 활용하여 People Counter(인원 계수기)를 만들고 이를 경로당 출입문에 설치합니다.  
카메라에서 전송되는 영상을 실시간으로 분석해 People Counting기능을 구현하고, 해당 공간에 몇 명이 있는지 알려줍니다.  
  
![](./image/silverfriend/people_count.png)

> **공간에 들어온 인원 수 - 공간을 나간 인원 수 = 현재 공간에 있는 인원 수**  
  
#### * OpenCV란?
Open Source Computer Vision의 약자로 다양한 영상/동영상 처리에 사용할 수 있는 오픈소스 라이브러리입니다.  C++, C, Python 및 Java와 같은 다양한 인터페이스를 지원하며 Windows, Linux, Mac OS, iOS 및 Android 같은 다양한 OS를 지원합니다. 원래 실시간 컴퓨터 비전을 목적으로한 프로그래밍 라이브러리라 성능과 속도가 탁월해서 실시간 이미지 처리나 영상분석에 적합한 라이브러리로 영상 분석시 널리 활용되고있습니다. 다양한 성능과 속도 최적화 알고리즘 또한 포함하고있습니다. openCV를 활용하여 윤곽선 검출 노이즈 제거 이미지 스티칭을 이용한 파노라믹 사진 제작 등에 활용됩니다.  
   
#### * 라즈베리파이란?
한마디로 말해 저렴한 초소형 컴퓨터입니다. 운영체제(os)는 리눅스 기반의 라즈비안을 주로 사용하고, 가격이 저렴한 만큼 성능도 낮지만 CPU, RAM, USB 포트 등 갖출 것은 다 갖춰져있는 형태로 센서 등과 연결하여 원하는 동작을 제어하고 서버와 통신하는 등의 역할을 할 수 있습니다. '경로당 친구들'에서는 간단한 센서 조작 만이 아닌 인공 지능을 이용한 영상 분석 기술이 사용되기때문에 라즈베리파이를 사용하였습니다. 라즈베리 파이는 리눅스 기반으로 파이썬 프로그래밍과 조합이 좋아 파이썬 openCV 라이브러리를 사용하여 만들었습니다.  
<br>
&nbsp;
<br>    ㅤ
  
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
<br>
&nbsp;
<br>    ㅤ
  
### 프로젝트 과정
--------------------------
'경로당 친구들'프로젝트는 다음과 같이 4개의 부분으로 나누어져 진행되었습니다.  
 
> A. 라즈베리파이를 이용한 People Counter 개발  
> B. 프록시 서버 및 DB 개발  
> C. 경로당 등록 기능 프로토타이핑  
> D. NUGU Play개발(Play Builder) 및 연동  
<br>
&nbsp;
<br>    ㅤ
  
### A. 라즈베리파이를 이용한 People Counter 개발
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
##### * cv2
open cv python 라이브러리입니다. 이미지를 읽어온 후 배경을 제거하여 움직이는 물체를 검출할 수 있는 Mog2 Substractor 알고리즘을 사용합니다.  

##### * Person
카메라로 인식한 사람 객체를 정의한 클래스 파일입니다.  
  
##### * imutils
openCV관련 오픈 소스 라이브러리입니다. 영상의 처리 속도를 개선하기 위해 사용하였습니다.

<br>
&nbsp;
<br>    ㅤ
  
#### 2. Mog2 Substractor 적용 및 프레임 바이너리화  
<br>
지나가는 사람의 인식률을 높이기 위해 가우시안 혼합 기반 배경/전경 분할 알고리즘인 Mog2를 활용한 Mog2 Substractor를 사용하여 배경을 제거합니다.
그 후, 프레임 binarization을 이용하여 프레임의 동적인 부분은 흰색으로, 정적인 부분은 검은색으로 변경합니다. 배경과 움직이는 물체를 쉽게 구분할 수 있습니다.
이 과정은 완료된 프레임 대상으로 컨투어링(외곽선 그리기)를 진행하기 위한 기반이 됩니다.

~~~python
    # Mog2 Substractor 적용
    fgmask = fgbg.apply(frame)

    try:
        ret,imBin= cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        mask0 =  cv2.morphologyEx(imBin ,  cv2.MORPH_OPEN, kernelOp2)
        mask =  cv2.morphologyEx(mask0 , cv2.MORPH_CLOSE, kernelCl2) # substraction 및 binarization이 완료된 프레임
    except:
        print('EOF')
        break
~~~
  
  
#### 3. 컨투어링(외곽선 그리기) 및 분할 작업
<br>
인식된 각 객체의 너비(width)가 설정한 wmax 값 보다 크다면 이는 한사람 이상의 사람이 하나의 컨투어링된 객체 안에 있다는 의미이므로,
객체의 중심점을 기준으로 반으로 나눠줍니다.(현재는 최대 2명까지 지원합니다.) 
아래의 4.오브젝트 트래킹은 mask2 프레임을 대상으로 진행되는데, 만약 분할해야 할 객체가 존재할 경우(mask2_flag=1 인 경우) mask 프레임에 분할선을 그어 mask2에 할당해주고 분할해야 할 객체가 존재 하지 않는 경우에는 그대로 mask 프레임을 mask2 프레임에 할당합니다.

~~~python
    mask2_flag=0

    for cnt in contours0:
        area = cv2.contourArea(cnt)
        if area > areaTH :
            x,y,w,h = cv2.boundingRect(cnt)

            # wmax는 한사람의 최대 길이입니다. 만약 바운딩 렉트의 넓이가 설정한 wmax 보다 크다면 한사람이상이기 때문에 반으로 나눕니다.
            if w > wmax:

                mask2 = cv2.line( mask, (int(x+w/2), 0), (int(x+w/2),min(320, frame.shape[1])),(0,0,0), 10) # 분할선 작업

                mask2_flag=1

    if mask2_flag==0:
        mask2=mask
~~~


#### 4. 오브젝트 트래킹  
<br>
InvisibleCount는 프레임 카운트 딜레이 수입니다. 인식된 객체는 Person 객체로 생성되고 persons 리스트에 더해집니다. 따라서 persons 리스트에는 현재 프로그램이 트래킹 중인 Person 객체가 모두 들어있는데, 여기서는 해당 Person 객체 리스트에 들어있는 각각의 Person 객체에 대해 InvisibleCount 값을 1씩 증가시키고, 만약 이 값이 if 문을 통해 지정한 값보다 클 경우, 해당 Person 객체는 현재 카메라가 보고 있는 화면 내에 일정 프레임 수 이상 동안 존재하지 않았다는 것을 의미하기 때문에 persons 리스트에서 해당 Person 객체를 제거합니다.  
그리고 설정한 areaTH 값보다 큰 area를 가진 컨투어링 된 객체가 있을 때 마다 해당 객체를 persons 리스트에 존재하는 모든 Person 객체들의 중심값과 컨투어링 객체를 bounding 한 사각형의 시작 포인트 (x, y)와 비교했을 때 x와 Person 객체의 중심값 x의 차가 설정한 너비마진 보다 작거나 같고, 또 y와 객체의 중심값 y의 차가 설정한 높이마진 보다 작거나 같은 경우, 해당 컨투어링 객체는 비교한 Person 객체와 동일한 객체라고 볼 수 있기 때문에(따라서 너비마진 값과 높이 마진 값을 어떻게 설정하느냐에 따라 인식률이 달라진다.) 중심값을 해당 컨투어링 박스의 중심값으로 새로 업데이트 해주고 InvisibleCount 값을 0으로 업데이트 해준다. 0으로 업데이트 해주는 이유는, InvisibleCount 값이 일정 값 이상 넘어가면 해당 객체를 더이상 트래킹 하지 않아도 되는 것으로 판단 하기 때문에 현재 프레임에서 발견된 Person 객체는 최근에 발견되었으므로 다시 0으로 업데이트 해주는 것이다. 만약 계속해서 프레임 내에서 발견되지 않아서 0으로 업데이트 되지 않은 Person 객체는 프레임이 지나갈수록 InvisibleCount 값이 쌓여서 얼마 후에 persons 리스트에서 제거 될 것이다.

~~~python
        for i in persons: # 현재 추척하고 있는 Person 객체의 리스트
            i.outdateInvisibleCount(i.getInvisibleCount()+1) # 각 퍼슨 객체가 인식되지 않은 프레임 수를 1씩 더해서 계산.
            # 만약 InvisibleCount가 25 이상이면,(즉 25 프레임 동안 해당 퍼슨 객체가 프레임 내에서 발견되지 않았으면)
            # 해당 퍼슨은 더이상 프레임 내에 존재하지 않는다는 의미로 간주하고 해당 퍼슨을 퍼슨스 리스트에서 제거.
            # 그 이유는 현재 프레임 내에 존재하는 컨투어와 퍼슨을 비교해서 동일한 영역이 발견될 경우 해당 퍼슨의 InvisibleCount를
            # 0으로 업데이트 하기 때문.
            if i.getInvisibleCount() > 10:
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
                # 각각의 퍼슨 객체와 비교했을때 그 차가 설정한 너비마진과 높이마진 보다 작거나 같으면
                # 해당 컨투어 영역은 새로 발견된 사람이 아니다.
                # 따라서 new 를 False로 바꾼다
                # 즉, 같은사람에게 계속해서 새로운 번호가 할당되는 문제가 발생할 경우 높이 마진과 넓이 마진을 셋팅하면 됨.
                if abs(x-i.getX()) <= w_margin and abs(y-i.getY()) <= h_margin:
                    new = False
                    i.outdateCoords(cx,cy)  # 해당 사람의 중심값 새로 업데이트.
                    i.outdateInvisibleCount(0) # dingima 초기화 하기.
                    break

                # 그게 아닐경우 해당 컨투어는 새로운 사람으로 인식된다.
                # 따라서 새로운 퍼슨객체를 생성하고 퍼슨객체 리스트인 퍼슨스에 추가한다.
            if new == True:
                p = Person.MyPerson(pid,cx,cy, max_p_age)
                persons.append(p)
                pid += 1

            cv2.circle(frame,(cx,cy), 5, (0,0,255), -1)
~~~  
  
#### 5. 트래킹 라인 출력
<br>
트래킹 라인은 프레임마다 트래킹되는 Person 객체가 가진 중심값들을 이용해 그려집니다. 중심값은 Person 객체의 tracks 리스트 속성에 담겨있습니다. 최소 tracks 리스트의 길이가 2보다 큰 객체들을 대상으로 라인이 그려지고 객체의 방향이 out(나가는 방향)인지 in(들어오는 방향)인지 판단합니다.
kurEina 함수가 객체의 방향을 판단해 dir속성을 in 혹은 out으로 할당하고 이에 해당하는 카운트 변수를 증가시키는 역할을 합니다.

~~~python
    # 추적중인 객체의 트래킹 라인을 출력합니다.
    for i in persons:
        if len(i.getTracks()) >= 2:
            pts = np.array(i.getTracks(), np.int32)
            pts = pts.reshape((-1,1,2))
            frame = cv2.polylines(frame,[pts],False,i.getRGB())
            
         #  선이 교차하는지 확인합니다. 즉 트래킹라인과 업라인 혹은 다운라인이 교차하는지 파악합니다.
         #  선이 교차했다면 지나간 라인에 해당하는 수를 증가시킵니다.
        if i.getDir() == None:
            i.kurEina( pts_L2[0,1] ,pts_L1[0,1]) 
    
    # Person 클래스 내에 존재하는 kurEina 함수. pts_L2는 out 라인이고 pts_L1는 in 라인이다
    # def kurEina(self,bottom_line,top_line):
    #     if len(self.tracks) >= 2:
    #         if self.dir == None:
    #             self.cross_bottom(bottom_line)
    #             self.cross_top(top_line)
            # 각각 line과 line2는 해당 Person 객체의 트래킹 라인이 첫번째로 만난 라인과 두번째로 만난 라인을 의미한다.
            # 따라서 첫번째로 만난 라인이 위에 있는 in 라인이고 두번째로 만난 라인이 밑에 있는 out 라인일 경우에, 방향을 in 으로 한다.
    #             if  self.line1== 'top' and self.line2== 'bottom':
    #                 self.dir = 'in'
            # 그 외 첫번째 만난 라인이 아래쪽에 있는 out 라인이고 두번째로 만난 라인이 위에 있는 in 라인인 경우에는 방향을 out으로 한다.
    #             elif  self.line1== 'bottom' and self.line2== 'top':
    #                 self.dir = 'out'
    #     else:
    #         return False              
    
    # kurEina 함수를 통해 계산된 방향이 out일 경우에 out 카운트를 증가시키고, in 일 경우에 in 카운트를 증가 시킵니다.
            if i.getDir() == 'out':
                cnt_out+=1
                print('Timestamp: {:%H:%M:%S} OUT {}'.format(datetime.datetime.now(), cnt_out))
            elif i.getDir() == 'in':
                cnt_in+=1
                print('Timestamp: {:%H:%M:%S} IN {}'.format(datetime.datetime.now(), cnt_in))



        cv2.putText(frame, str(i.getId()),(i.getX(),i.getY()),font,0.7,i.getRGB(),1,cv2.LINE_AA)
~~~
  
  
#### 6. 결과값 출력
<br>
화면에 인라인(들어오는 사람을 카운트하는 라인)을 파란색으로, 아웃라인(나가는 사람을 카운트하는 라인)을 빨간색으로 표시하고 각 카운트 수를 화면 위에 표시해 줍니다.

~~~python
    str_out='OUT: '+ str(cnt_out)
    str_in='IN: '+ str(cnt_in)
    frame = cv2.polylines( frame, [pts_L1], False, line_in_color,thickness=4)
    frame = cv2.polylines( frame, [pts_L2], False, line_out_color,thickness=4)
    cv2.putText(frame, str_out, (10,30), font,0.5,(0,0,255), 1,cv2.LINE_AA)
    cv2.putText(frame, str_in, (10,50), font,0.5,(255,0,0), 1,cv2.LINE_AA)
~~~
  
<u>'경로당 친구들' 코드 전체를 보고 싶은 분은 [경로당 친구들 openCV](https://github.com/hyunjuhw/five14.github.io/blob/master/silver_friends_opencv.py)를 참고해주세요. </u> 
<br>
&nbsp;
<br>    ㅤ
  
### B. 프록시 서버 및 DB 개발
--------------------------
코드는 내일 옵니다.
<br>
&nbsp;
<br>    ㅤ
  
### C. 경로당 등록 기능 프로토타이핑
--------------------------
프로토 타이핑된 이미지 넣으면 될 듯
<br>
&nbsp;
<br>    ㅤ
  
### 관련 및 참고 자료
--------------------------
#### 1. OpenCV 영상 참고 자료 및 관련 코드
[![openCV Video](http://img.youtube.com/vi/S26G0a7u9d4/0.jpg)](https://www.youtube.com/watch?v=S26G0a7u9d4)  
Pedestrians-counter-raspberry[(https://github.com/donce71/Pedestrians-counter-raspberry)](https://github.com/donce71/Pedestrians-counter-raspberry)
  
<br>
&nbsp;
<br>    ㅤ
  
### 결론
--------------------------
