# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 576,623 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"User Name", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"User ID", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText3.Wrap( -1 )
		bSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Team ID", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText4.Wrap( -1 )
		bSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"PlayerID", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText5.Wrap( -1 )
		bSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Team Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl9, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Jersey Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Firstname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer4.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Lastname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gSizer4.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl12, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer4, 0, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Add Team ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Add Player", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button6, 0, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer1.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"End", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.addteam )
		self.m_button6.Bind( wx.EVT_BUTTON, self.addplayer )
		self.m_button1.Bind( wx.EVT_BUTTON, self.StartVideo )
		self.m_button2.Bind( wx.EVT_BUTTON, self.stop_process )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addteam( self, event ):
		event.Skip()
	
	def addplayer( self, event ):
		event.Skip()
	
	def StartVideo( self, event ):
		event.Skip()
	
	def stop_process( self, event ):
		event.Skip()
	

