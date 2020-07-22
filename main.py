from bs4 import BeautifulSoup
import requests

url ='https://magicseaweed.com/South-Beach-Surf-Report/359/'

def getSite():
  return(requests.get(url))

def parseSurfInfo():
  soup = BeautifulSoup(getSite().text, 'html.parser')
  size = soup.find(class_='rating-text')
  return(size.text)

def SobeSurf():
  print("Your Surf Info for South Beach is:" + parseSurfInfo() +' waves')

SobeSurf()