import wx 
import cv2
import time
import numpy as np
import time
#import the newly created GUI file 
import demo  
import videogenerater
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

class CalcFrame(demo.MyFrame1): 

   def __init__(self,parent): 
      demo.MyFrame1.__init__(self,parent) 


   
        
   def StartVideo(self,event): 
      username = self.m_textCtrl1.GetValue()
      password = self.m_textCtrl2.GetValue()
      playerid = self.m_textCtrl5.GetValue()
      teamname = self.m_textCtrl9.GetValue()

      if(username == 'csps_user' and password == '123456'):


      # self.m_textCtrl3.SetValue (str(num*num)) 
          self.m_staticText7.SetLabel('Login Success! Vieo is recording now!') 

          videogenerater.savevideo(25,False,playerid,teamname)
      else:
          self.m_staticText7.SetLabel('Login Fail! Please input again!') 

   def stop_process(self,event):
      playerid = self.m_textCtrl5.GetValue()
      teamname = self.m_textCtrl9.GetValue()
      videogenerater.savevideo(25,True,playerid,teamname)
      self.m_staticText7.SetLabel('Stop Recording.') 

   def addteam(self,event):
      userid =  self.m_textCtrl3.GetValue()
      teamname = self.m_textCtrl9.GetValue()

      c = Client(host='csps.tangyem.me', port=80)
      _, status = c.post('/add/team', {'userid': 3, 'teamname': '%s'%teamname})

      if status == 200:
        self.m_staticText9.SetLabel('Success add a team: %s!'%teamname) 
      else:
        self.m_staticText9.SetLabel('Sorry Please Check Again!') 

   def addplayer(self,event):
      jnumber =  int(self.m_textCtrl11.GetValue())
      firstname = self.m_textCtrl10.GetValue()
      lastname = self.m_textCtrl12.GetValue()
      teamid = int(self.m_textCtrl4.GetValue())


      c = Client(host='csps.tangyem.me', port=80)
      _, status = c.post('/add/player', {'teamid': teamid, 'jerseynumber': jnumber, 'firstname': firstname, 'lastname': lastname})

      if status == 200:
        self.m_staticText9.SetLabel('Success add a player: %s!'%firstname) 
      else:
        self.m_staticText9.SetLabel('Sorry Please Check Again!')



   
        
app = wx.App(False) 
frame = CalcFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 