import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib,base64
import codecs
import xbmc
import sys

"""

Leer Mensaje de entrada:

"""
crypto = '\x68\x65\x78\x68\x65\x78'
b16 = crypto.replace('\x68\x65\x78\x68\x65\x78','\x68\x65\x78')
bienvenida = 'https://pastebin.com/raw/G5ycuH8P'
texto_regex = 'texto1=[\'"](.*?)[\'"]\s*texto2=[\'"](.*?)[\'"]\s*texto3=[\'"](.*?)[\'"]\s*'

def read_file(file):
## FUNCION QUE LEE LOS FICHEROS:
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass

def make_request(url):
##ESTA FUNCION lee las url declaradas donde estan los videos. ||
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
			
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
        req.add_header('Referer', '%s'%url)
        req.add_header('Connection', 'keep-alive')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
		
		
def mensaje():
	
	
		try:
			content = make_request(bienvenida)
			match = re.compile(texto_regex).findall(content)
			for msg,texto1,texto2,texto3 in match:
				
				try:
	
					
				    msg1 = texto1
				    msg2 = texto2
				    msg3 = texto3

	
			
				    line1 = "[B]" + msg1 + "[/B]"
				    line2 = "" + msg2 + ""
				    line3 = "" +msg3 + ""

				    xbmcgui.Dialog().ok("Real Stream", line1, line2, line3)
				
				except:
			           pass
					
		except:
			pass

