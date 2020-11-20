# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:14:18 2019

@author: toshida
"""

import os
import win32com.client

#get python file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

#assigning library to variables. Allow access to outlook account
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
account = accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts

#input asking which outlook folder to extract messages from
folderName = input('Outlook Folder: ')
inbox = outlook.GetDefaultFolder(6).Folders(folderName)

#characters that cannot be used as part of a file name
specialChar = '[]:*?/\\\''

#folder to save attachemnts
att_path = dir_path[:-6] + '\\' + '_reference'

#loop to get messages from selected outlook folder
messages = inbox.Items

for items in messages:
 
#getting email metadata  
  subject = items.subject
  subject = str(subject)
  date = str(items.receivedTime)[:10]
  sender = items.SenderName

#removing special characters from file name  
  for char in specialChar:
    subject = subject.replace(char, '')

#extracting attachments from email and saving into _referece folder
  for attch in items.Attachments:
    attch.SaveAsFile(att_path + '\\' + 'email_' + attch.FileName)

#saving message files into the same folder as the python file  
  items.SaveAs(dir_path + '\\' + '(' + date + ')' + '_' + sender + '_' + subject + '.msg')
