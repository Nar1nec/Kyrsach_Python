from Parsing_class import *

#.....Для RBC.....

def search_time(n):
    return RBC_News.time[n]

def search_images_RBC(n):
    return RBC_News.image[n].get_attribute('src')

def search_href_RBC(n):
    return RBC_News.href[n].get_attribute('href')

def parsing_RBC(n):
    return RBC_News.text_mini[n].text

#.....Для SecureNews.....

def search_images(n):
    return Secure_News.image[n].get_attribute('src')

def search_href(n):
    return Secure_News.href[n].get_attribute('href')

def search_text_mini(n):
    return Secure_News.text_mini[n].text

#.....Для SecureLab.....

def search_images_AM(n):
    return ANTI_MALWARE.href[n].get_attribute('src')

def search_href_AM(n):
    return ANTI_MALWARE.href[n].get_attribute('href')

def parsing_AM(n):
    return ANTI_MALWARE.text_mini[n].text

def search_images_AM(n):
    return ANTI_MALWARE.image[n].get_attribute('src')