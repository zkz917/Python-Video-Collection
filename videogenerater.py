#!/usr/bin/env python
 
import cv2
import time
import numpy as np
import time
import datetime
import re
import json
import requests


class Client:
    def __init__(self, host='127.0.0.1', port=5000):
        host = re.sub(r'^http[s]?://', '', host)
        host = re.sub(r'/*$', '', host)
        port = int(port)
        self.url = 'http://{}:{}'.format(host, port)

    # param should be a list or dict
    def post(self, route, param):
        if not re.match(r'^/', route):
            route = '/{}'.format(route)
        if type(param) is not list:
            param = [param]
        headers = {'Content-Type': 'application/json'}
        r = requests.post('{}{}'.format(self.url, route), data=json.dumps(param), headers=headers)
        if r.status_code == 200:
            return r.json(), r.status_code
        else:
            return None, r.status_code

def testfps():
    # Start default camera
    video = cv2.VideoCapture(0);
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
     

    # Number of frames to capture
    num_frames = 120;
     
     
    print "Capturing {0} frames".format(num_frames)

    # Start time
    start = time.time()
     
    # Grab a few frames
    for i in xrange(0, num_frames) :
        ret, frame = video.read()

     
    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    print "Time taken : {0} seconds".format(seconds)

    # Calculate frames per second
    fps  = num_frames // seconds;
    print "Estimated frames per second : {0}".format(fps);


    cap = cv2.VideoCapture(0)

    # Release video
    video.release()
    return fps

def savevideo(fps,condition,playerid,teamname):
    # Define the codec and create VideoWriter object
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('output1.mp4',fourcc, fps, (640,480))
    count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        count += 1
        status = 200
       
        if ret==True:
            # frame = cv2.flip(frame,0)

            # write the flipped frame
            if count% (10*fps)  == 0:
                # date = str(time.ctime())
                string = time.ctime().replace(':','-')
                current_time = generatetime()
                filename = "%s.mp4"%string

                out = cv2.VideoWriter("%s.mp4"%string,fourcc, fps, (640,480))
                link = generatelink(filename)

                status = upload_link(playerid,current_time,link,teamname)


            
            out.write(frame)
            if status != 200:
                break

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or condition:
            # if condition:
                break
        else:
            break
    return 'The record or upload fails!'

        # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def generatelink(filename):
    fn = filename.replace(' ','+')
    link = "https://s3.amazonaws.com/cspsvideos/%s"%fn
    print link 
    return link


def generatetime():
    now = datetime.datetime.now()

    # print now.year, now.month, now.day, now.hour, now.minute, now.second
    ctime = addzero(now.year) + '-' + addzero(now.month) + '-' + addzero(now.day) + ' ' + addzero(now.hour) + ':' + addzero(now.minute) + ':' + addzero(now.second)
    print ctime
    return ctime

def addzero(date):
    if date < 10:

        return '0'+ str(date)
    else:
        return str(date)



def upload_link(playerid,time,link,teamname):
    c = Client(host='csps.tangyem.me', port=80)
    # _, status = c.post('/add/team', {'userid': 3, 'teamname': '%s'%teamname})
    _, status = c.post('/add/link', {'playerid': playerid, 
                         'gamedatetime': time, 
                         'link': link, 
                         'teamname': teamname,
                         'simulationlink': None,
                         'simulationlink1': None,
                         'simulationlink2': None,
                         'simulationlink3': None,
                         'simulationlink4': None,
                         'videolink1': None,
                         'videolink2': None,
                         'videolink3': None,
                         'videolink4': None})
    return status






if __name__ == '__main__' :

    savevideo(25,False,22,'psuhockey')

    



 