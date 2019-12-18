import numpy as np
import cv2
import Person
import time
import imutils
import datetime
from imutils.video import VideoStream


cap = VideoStream(src=0).start()
time.sleep(2.0)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True) #Create the background substractor

kernelOp = np.ones((3,3),np.uint8)
kernelOp1 = np.ones((7,7),np.uint8)
kernelOp2 = np.ones((5,5),np.uint8)

kernelCl = np.ones((11,11),np.uint8)
kernelCl1 = np.ones((20,20),np.uint8)
kernelCl2 = np.ones((25,25),np.uint8)

#Variables
font = cv2.FONT_HERSHEY_SIMPLEX
persons = []
max_p_age = 5
pid = 1
areaTH = 7500
w_margin= 100
h_margin= 120
wmax= 200

cnt_out=0
cnt_in=0
line_in_color=(255,0,0)
line_out_color=(0,0,255)

frame = cap.read()
frame = imutils.resize(frame, width=min(320, frame.shape[1]))
height = np.size(frame, 0)
width = np.size(frame, 1)

# out- line을 그리기 위한 height 값 계산
L1_figure = (height / 2)- 30
# in- line을 그리기 위한 height 값 계산
L2_figure = (height / 2)+ 30

# out- line 위치 정보
pts_L1= np.array([[0, int(L1_figure)],[320, int(L1_figure)]])
# in- line 위치 정보
pts_L2= np.array([[0, int(L2_figure)],[320, int(L2_figure)]])


counter=0



while True:
    frame = cap.read() #read a frame


    if frame is None:
        break

    frame = imutils.resize(frame, width=min(320, frame.shape[1]))

    # Mog2 Substractor 적용
    fgmask = fgbg.apply(frame)

    try:
        ret,imBin= cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        mask0 =  cv2.morphologyEx(imBin ,  cv2.MORPH_OPEN, kernelOp2)
        mask =  cv2.morphologyEx(mask0 , cv2.MORPH_CLOSE, kernelCl2)
    except:
        print('EOF')
        break


    _, contours0, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

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


    _, contours0, hierarchy = cv2.findContours(mask2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours0:
        area = cv2.contourArea(cnt)

            #################
            #   펄슨 객체 리스트에 등록된 객체가 여전히 프레임 안에 있으면서 제대로 인식이 되고 있는지 확인
            #################
        for i in persons:
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
                # 각각의 퍼슨 객체와 비교했을때 그 차가 설정한 넓이마진과 높이마진 보다 작거나 같으면
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
            if i.getDir() == 'out':
                cnt_out+=1
                print('Timestamp: {:%H:%M:%S} OUT {}'.format(datetime.datetime.now(), cnt_out))
            elif i.getDir() == 'in':
                cnt_in+=1
                print('Timestamp: {:%H:%M:%S} IN {}'.format(datetime.datetime.now(), cnt_in))



        cv2.putText(frame, str(i.getId()),(i.getX(),i.getY()),font,0.7,i.getRGB(),1,cv2.LINE_AA)

    #########################
    # 화면에 카운트와 인 라인, 아웃 라인, 텍스트를 표시하기 위한 부분.
    #########################
    str_out='OUT: '+ str(cnt_out)
    str_in='IN: '+ str(cnt_in)
    frame = cv2.polylines( frame, [pts_L1], False, line_in_color,thickness=4)
    frame = cv2.polylines( frame, [pts_L2], False, line_out_color,thickness=4)
    cv2.putText(frame, str_out, (10,30), font,0.5,(0,0,255), 1,cv2.LINE_AA)
    cv2.putText(frame, str_in, (10,50), font,0.5,(255,0,0), 1,cv2.LINE_AA)


    cv2.imshow('Frame',frame)


    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows