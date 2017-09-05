#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
import requests
from payload import payload


def makeSession(payload): 
	login_url = 'https://aprender.ead.unb.br/login/index.php'
	
	session_requests = requests.session() 
	
	result = session_requests.post(
		login_url, 
		data = payload
	) 
	
	return session_requests

def getCoursesUrl(session_requests): 
	list_Lcourses = list()
	url = 'https://aprender.ead.unb.br' 
	
	result = session_requests.get(url)
	
	site_in_text = result.text

	soup = BeautifulSoup(site_in_text, 'html.parser')
	
	for link in soup.find_all('h3',{ "class" : "coursename" }):
		list_Lcourses.append(link.a.get('href'))
	
	return list_Lcourses

def getAllPdfUrl(session_requests): 
	list = getCoursesUrl(session_requests) 
	list_Lpdf = []
	
	for url in list: 
		result = session_requests.get(url)
	
		site_in_text = result.text
	
		soup = BeautifulSoup(site_in_text, 'html.parser')
		
		for link in soup.find_all('div',{ "class" : "activityinstance" }):
			#print(link.span.span)
			if(str(link.span.span) == '<span class="accesshide "> Arquivo</span>'):
				list_Lpdf.append(link.a.get('href'))
	
	return list_Lpdf

def downloadFile(session_requests, url):  
	name = url.split('id=')  
	
	path = 'file/' + name[1] + '.pdf' 
	print(path)
	
	result = session_requests.get(url)
	with open(path, 'ab') as f: 
		f.write(result.content)

def downloadAllfiles(session_requests): 
	pdfs = getAllPdfUrl(session_requests)
	
	print(pdfs)
	
	for pdf in pdfs: 
		downloadFile(session_requests, pdf)
	
	
def main(): 
	session = makeSession(payload.payload)
	
	downloadAllfiles(session) 
	
	#print(list)
if __name__ == "__main__":
    main()
    
