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
 
 
 ### 코드 설명  
 --------------------------
 
 ~~~python
     # USAGE
    # To read and write back out to video:
    # python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt \
    #	--model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/example_01.mp4 \
    #	--output output/output_01.avi
    #
    # To read from webcam and write back out to disk:
    # python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt \
    #	--model mobilenet_ssd/MobileNetSSD_deploy.caffemodel \
    #	--output output/webcam_output.avi

    # import the necessary packages
    from pyimagesearch.centroidtracker import CentroidTracker
    from pyimagesearch.trackableobject import TrackableObject
    from imutils.video import VideoStream
    from imutils.video import FPS
    import numpy as np
    import argparse
    import imutils
    import time
    import dlib
    import cv2

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--prototxt", required=True,
        help="path to Caffe 'deploy' prototxt file")
    ap.add_argument("-m", "--model", required=True,
        help="path to Caffe pre-trained model")
    ap.add_argument("-i", "--input", type=str,
        help="path to optional input video file")
    ap.add_argument("-o", "--output", type=str,
        help="path to optional output video file")
    ap.add_argument("-c", "--confidence", type=float, default=0.4,
        help="minimum probability to filter weak detections")
    ap.add_argument("-s", "--skip-frames", type=int, default=30,
        help="# of skip frames between detections")
    args = vars(ap.parse_args())

    # initialize the list of class labels MobileNet SSD was trained to
    # detect
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
        "sofa", "train", "tvmonitor"]

    # load our serialized model from disk
    print("[INFO] loading model...")
    net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

    # if a video path was not supplied, grab a reference to the webcam
    if not args.get("input", False):
        print("[INFO] starting video stream...")
        vs = VideoStream(src=0).start()
        time.sleep(2.0)

    # otherwise, grab a reference to the video file
    else:
        print("[INFO] opening video file...")
        vs = cv2.VideoCapture(args["input"])

    # initialize the video writer (we'll instantiate later if need be)
        writer = None

    # initialize the frame dimensions (we'll set them as soon as we read
    # the first frame from the video)
        W = None
        H = None

    # instantiate our centroid tracker, then initialize a list to store
    # each of our dlib correlation trackers, followed by a dictionary to
    # map each unique object ID to a TrackableObject
        ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
        trackers = []
        trackableObjects = {}

    # initialize the total number of frames processed thus far, along
    # with the total number of objects that have moved either up or down
        totalFrames = 0
        totalDown = 0
        totalUp = 0

    # start the frames per second throughput estimator
        fps = FPS().start()

    # loop over frames from the video stream
    while True:
	    # grab the next frame and handle if we are reading from either
	    # VideoCapture or VideoStream
	    frame = vs.read()
	    frame = frame[1] if args.get("input", False) else frame

	# if we are viewing a video and we did not grab a frame then we
	# have reached the end of the video
	if args["input"] is not None and frame is None:
		break

	# resize the frame to have a maximum width of 500 pixels (the
	# less data we have, the faster we can process it), then convert
	# the frame from BGR to RGB for dlib
	frame = imutils.resize(frame, width=500)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# if the frame dimensions are empty, set them
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	# if we are supposed to be writing a video to disk, initialize
	# the writer
	if args["output"] is not None and writer is None:
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
		writer = cv2.VideoWriter(args["output"], fourcc, 30,
			(W, H), True)

	# initialize the current status along with our list of bounding
	# box rectangles returned by either (1) our object detector or
	# (2) the correlation trackers
	status = "Waiting"
	rects = []

	# check to see if we should run a more computationally expensive
	# object detection method to aid our tracker
	if totalFrames % args["skip_frames"] == 0:
		# set the status and initialize our new set of object trackers
		status = "Detecting"
		trackers = []

		# convert the frame to a blob and pass the blob through the
		# network and obtain the detections
		blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)
		net.setInput(blob)
		detections = net.forward()

		# loop over the detections
		for i in np.arange(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated
			# with the prediction
			confidence = detections[0, 0, i, 2]

			# filter out weak detections by requiring a minimum
			# confidence
			if confidence > args["confidence"]:
				# extract the index of the class label from the
				# detections list
				idx = int(detections[0, 0, i, 1])

				# if the class label is not a person, ignore it
				if CLASSES[idx] != "person":
					continue

				# compute the (x, y)-coordinates of the bounding box
				# for the object
				box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
				(startX, startY, endX, endY) = box.astype("int")

				# construct a dlib rectangle object from the bounding
				# box coordinates and then start the dlib correlation
				# tracker
				tracker = dlib.correlation_tracker()
				rect = dlib.rectangle(startX, startY, endX, endY)
				tracker.start_track(rgb, rect)

				# add the tracker to our list of trackers so we can
				# utilize it during skip frames
				trackers.append(tracker)

	# otherwise, we should utilize our object *trackers* rather than
	# object *detectors* to obtain a higher frame processing throughput
	else:
		# loop over the trackers
		for tracker in trackers:
			# set the status of our system to be 'tracking' rather
			# than 'waiting' or 'detecting'
			status = "Tracking"

			# update the tracker and grab the updated position
			tracker.update(rgb)
			pos = tracker.get_position()

			# unpack the position object
			startX = int(pos.left())
			startY = int(pos.top())
			endX = int(pos.right())
			endY = int(pos.bottom())

			# add the bounding box coordinates to the rectangles list
			rects.append((startX, startY, endX, endY))

	# draw a horizontal line in the center of the frame -- once an
	# object crosses this line we will determine whether they were
	# moving 'up' or 'down'
	cv2.line(frame, (0, H // 2), (W, H // 2), (0, 255, 255), 2)

	# use the centroid tracker to associate the (1) old object
	# centroids with (2) the newly computed object centroids
	objects = ct.update(rects)

	# loop over the tracked objects
	for (objectID, centroid) in objects.items():
		# check to see if a trackable object exists for the current
		# object ID
		to = trackableObjects.get(objectID, None)

		# if there is no existing trackable object, create one
		if to is None:
			to = TrackableObject(objectID, centroid)

		# otherwise, there is a trackable object so we can utilize it
		# to determine direction
		else:
			# the difference between the y-coordinate of the *current*
			# centroid and the mean of *previous* centroids will tell
			# us in which direction the object is moving (negative for
			# 'up' and positive for 'down')
			y = [c[1] for c in to.centroids]
			direction = centroid[1] - np.mean(y)
			to.centroids.append(centroid)

			# check to see if the object has been counted or not
			if not to.counted:
				# if the direction is negative (indicating the object
				# is moving up) AND the centroid is above the center
				# line, count the object
				if direction < 0 and centroid[1] < H // 2:
					totalUp += 1
					to.counted = True

				# if the direction is positive (indicating the object
				# is moving down) AND the centroid is below the
				# center line, count the object
				elif direction > 0 and centroid[1] > H // 2:
					totalDown += 1
					to.counted = True

		# store the trackable object in our dictionary
		trackableObjects[objectID] = to

		# draw both the ID of the object and the centroid of the
		# object on the output frame
		text = "ID {}".format(objectID)
		cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

	# construct a tuple of information we will be displaying on the
	# frame
	info = [
		("Up", totalUp),
		("Down", totalDown),
		("Status", status),
	]

	# loop over the info tuples and draw them on our frame
	for (i, (k, v)) in enumerate(info):
		text = "{}: {}".format(k, v)
		cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
			cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

	# check to see if we should write the frame to disk
	if writer is not None:
		writer.write(frame)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# increment the total number of frames processed thus far and
	# then update the FPS counter
	totalFrames += 1
	fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # check to see if we need to release the video writer pointer
    if writer is not None:
	    writer.release()

    # if we are not using a video file, stop the camera video stream
    if not args.get("input", False):
	    vs.stop()

    # otherwise, release the video file pointer
    else:
	    vs.release()

    # close any open windows
    cv2.destroyAllWindows()







