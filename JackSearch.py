# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import youtube_dl
from PyQt4 import QtCore, QtGui
from bs4 import BeautifulSoup
import requests
import urllib
import os
import urllib2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def GetOpenloadVideo(path,filename):
    print path
    print filename
    ydl = youtube_dl.YoutubeDL({'outtmpl': filename})
    with ydl:
        youtube_dlresult = ydl.extract_info(
            path,
            download=True  # !!We just want to extract the info
        )
    if 'entries' in youtube_dlresult:
        # Can be a playlist or a list of videos
        video = youtube_dlresult['entries'][0]
    else:
        # Just a video
        video = youtube_dlresult
    return video

def GetOpenloadVideoDownloadInfo(VedioNumber):
    Result = {
        "result": "FAIL",
        "url": "",
        "filename": "",
    }
    keyword = VedioNumber
    # print keyword

    if unicode(VedioNumber) == "":
        return Result


    #SDDPOAV
    if Result['result'] == "FAIL":
    #if Result['result'] == "FAILs":
        res = requests.get('http://sddpoav.com/?s=' + keyword)
        if res.status_code == requests.codes.ok:
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.find('div', attrs={'class': 'video'})
            if data is not None:
                if data.find('a') is not None:
                    href = data.find('a').get('href')
                    res = requests.get(href)
                    if res.status_code == requests.codes.ok:
                        html = res.content
                        soup = BeautifulSoup(html, 'html.parser')
                        video_path = soup.find('div', attrs={'class': 'video_code'}).find('iframe').get('src')
                        # print video_path
                        ydl = youtube_dl.YoutubeDL({'quiet': True})
                        # ydl = youtube_dl.YoutubeDL()
                        with ydl:
                            youtube_dlresult = ydl.extract_info(
                                video_path,
                                download=False  # !!We just want to extract the info
                            )
                        if 'entries' in youtube_dlresult:
                            # Can be a playlist or a list of videos
                            video = youtube_dlresult['entries'][0]
                        else:
                            # Just a video
                            video = youtube_dlresult
                        #print(video)
                        Result['result'] = "PASS"
                        Result['url'] = video['url']
                        Result['filename'] = video['title']
                        #print urllib2.build_opener().open(video['url']).info()
                        return Result

    print "Cannot Find this AV Number in http://sddpoav.com/"

    #D18X
    if Result['result'] == "FAIL":
    #if Result['result'] == "FAILs":
        #print "Find the https://www.dl8x.com/"
        res = requests.get('https://www.dl8x.com/search?query=' + keyword)
        if res.status_code == requests.codes.ok:
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            for data in soup.find_all('div', attrs={'class': 'float-left dx-vertical-item dx-video-entry-frame'}):
                if data.find('div', attrs={'class': 'dx-video-entry-title'}) is not None and data.find('div', attrs={'class': 'dx-video-entry-site dx-video-entry-label '}) is not None:
                    if data.find('div', attrs={'class': 'dx-video-entry-site dx-video-entry-label '}).find('span').text == "Openload":
                        #print data.find('a').get('href')
                        res = requests.get('https://www.dl8x.com'+data.find('a').get('href'))
                        if res.status_code == requests.codes.ok:
                            html = res.content
                            soup = BeautifulSoup(html, 'html.parser')
                            video_path = soup.find('iframe', attrs={'allowfullscreen': ''}).get('src')
                            ydl = youtube_dl.YoutubeDL({'quiet': True})
                            # ydl = youtube_dl.YoutubeDL()
                            with ydl:
                                youtube_dlresult = ydl.extract_info(
                                    video_path,
                                    download=False  # !!We just want to extract the info
                                )
                            if 'entries' in youtube_dlresult:
                                # Can be a playlist or a list of videos
                                video = youtube_dlresult['entries'][0]
                            else:
                                # Just a video
                                video = youtube_dlresult
                            #print(video)
                            Result['result'] = "PASS"
                            Result['url'] = video['url']
                            Result['filename'] = video['title']
                            return Result
    print "Cannot Find this AV Number in https://www.dl8x.com/"

    #PORN68
    #if Result['result'] == "FAILs":
    if Result['result'] == "FAIL":
        res = requests.get('http://porn68jav.com/?s=' + keyword)
        if res.status_code == requests.codes.ok:
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            if soup.find('a', attrs={'class': 'clip-link'}) is not None:
                data = soup.find('a', attrs={'class': 'clip-link'}).get("href")
                res = requests.get(data)
                if res.status_code == requests.codes.ok:
                    html = res.content
                    soup = BeautifulSoup(html, 'html.parser')
                    video_path = soup.find('iframe', attrs={'id': 'mIframe'}).get("src")
                    ydl = youtube_dl.YoutubeDL({'quiet': True})
                    # ydl = youtube_dl.YoutubeDL()
                    with ydl:
                        youtube_dlresult = ydl.extract_info(
                            video_path,
                            download=False  # !!We just want to extract the info
                        )
                    if 'entries' in youtube_dlresult:
                        # Can be a playlist or a list of videos
                        video = youtube_dlresult['entries'][0]
                    else:
                        # Just a video
                        video = youtube_dlresult
                    #print(video)
                    Result['result'] = "PASS"
                    Result['url'] = video['url']
                    Result['filename'] = video['title']

                    return Result
    print "Cannot Find this AV Number in http://porn68jav.com"
    #http://highporn.net

    return Result

def Get7MMVedioInfo(VedioNumber):
    Result = {
        "result": "FAIL",
        "title": "",
        "number": "",
        "date": "",
        "avers": "",
        "video_long": "",
        "maker": "",
        "seller": "",
        "company": "",
        "img": "",
        "have": "",
    }

    if unicode(VedioNumber) == "":
        return Result


    res = requests.get('http://127.0.0.1/?sw='+unicode(VedioNumber)+'&info=0&mode=0&order=0&sort=num')
    if res.status_code == requests.codes.ok:
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        for line in soup.head.script:
            if unicode(VedioNumber).upper() in line:
                print "Almost has this video in av list"
                Result['have'] = "YES"

    if None:
        search_key = unicode(VedioNumber)
        search_key = u"shkd-545"
        search_key = search_key.replace(u"-", u"%20")
        res = requests.get(
            'http://www.dmm.co.jp/search/=/searchstr=' + search_key + '/analyze=V1EBAVcHUQA_/limit=30/n1=FgRCTw9VBA4GAVhfWkIHWw__/sort=ranking/')
        if res.status_code == requests.codes.ok:
            html = res.content
            soup = BeautifulSoup(html, 'html.parser')
            href = soup.find('p', attrs={'class': 'tmb'}).find('a').get("href")
            #print href
            res = requests.get(href)
            if res.status_code == requests.codes.ok:
                html = res.content
                soup = BeautifulSoup(html, 'html.parser')
                img = soup.find('div', attrs={'id': 'sample-video'}).find('a').get("href")
                print img
                tr = soup.find('table', attrs={'class': 'mg-b20'}).find_all('tr')
                for tds in tr:
                    for td in tds.find_all('td'):
                        if td.get("class") is None:
                            print '----'+td.text+'----'
            return Result


    res = requests.post('https://7mm.tv/zh/searchform_search/all/index.html',
                        data={'search_keyword': unicode(VedioNumber), 'search_type': 'censored',
                        'op': 'search'})
    if res.status_code == requests.codes.ok:
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        topic_area = soup.find('div', attrs={'class': 'topic_area'})
        topic_box = topic_area.find('div', attrs={'class': 'topic_box'})
        if topic_area is not None:
            if topic_box is not None:
                res = requests.get(topic_box.find('a').get('href'))
                if res.status_code == requests.codes.ok:
                    html = res.content
                    soup = BeautifulSoup(html, 'html.parser')
                    contents_title = soup.find('div', attrs={'id': 'contents_title'})
                    contents_title = contents_title.find('b').text
                    # print contents_title
                    # print '----------------'
                    for mvinfo_dmm_A in soup.find_all('div', attrs={'class': 'mvinfo_dmm_A'}):
                        if mvinfo_dmm_A.find('b').text == u"番號：":
                            # print mvinfo_dmm_A.text.lstrip(u"番號：")

                            Result["number"] = mvinfo_dmm_A.text.lstrip(u"番號：")

                            number = mvinfo_dmm_A.text.lstrip(u"番號：")
                            rm_string = "[" + mvinfo_dmm_A.text.lstrip(u"番號：") + "]"
                            contents_title = contents_title.replace(rm_string, "")

                        # print contents_title
                        if mvinfo_dmm_A.find('b').text == u"發行日期：":
                            # print mvinfo_dmm_A.text.lstrip(u"發行日期：")
                            date = mvinfo_dmm_A.text.lstrip(u"發行日期：")

                            Result["date"] = mvinfo_dmm_A.text.lstrip(u"發行日期：")

                        if mvinfo_dmm_A.find('b').text == u"影片時長：":
                            # print mvinfo_dmm_A.text.lstrip(u"影片時長：")

                            Result["video_long"] = mvinfo_dmm_A.text.lstrip(u"影片時長：")
                            Result["video_long"] = Result["video_long"].split(u"（")[0]
                            # Result["video_long"] = mvinfo_dmm_A.text.lstrip(u"影片時長：")

                        if mvinfo_dmm_A.find('b').text == u"導演：":
                            # print mvinfo_dmm_A.text.lstrip(u"導演：")
                            Result["maker"] = mvinfo_dmm_A.text.lstrip(u"導演：")
                        if mvinfo_dmm_A.find('b').text == u"製作商：":
                            # print mvinfo_dmm_A.text.lstrip(u"製作商：")
                            Result["seller"] = mvinfo_dmm_A.text.lstrip(u"製作商：")
                        if mvinfo_dmm_A.find('b').text == u"發行商：":
                            # print mvinfo_dmm_A.text.lstrip(u"發行商：")
                            Result["company"] = mvinfo_dmm_A.text.lstrip(u"發行商：")
                    mvinfo_introduction = soup.find('div', attrs={'class': 'mvinfo_introduction'}).text
                    avers = ""
                    for av_performer_name_box in soup.find_all('div', attrs={'class': 'av_performer_name_box'}):
                        contents_title = contents_title.replace(av_performer_name_box.text, "")
                        avers += av_performer_name_box.text + ","
                    # print avers.strip(",")
                    Result["avers"] = avers.strip(",")
                    contents_title = contents_title.lstrip(" ")
                    contents_title = contents_title.lstrip(u" ")
                    contents_title = contents_title.strip(" ")
                    contents_title = contents_title.strip(u" ")
                    Result["title"] = contents_title
                    img = soup.find('img').get('src')
                    # print "Download from ",img,".."
                    urllib.urlretrieve(img, 'tmp.jpg')
                    Result["img"] = img
                    # print "JackS: ", Result
                    Result['result'] = "PASS"
                    return Result
        # print Result
    res = requests.post('https://7mm.tv/zh/searchform_search/all/index.html',
                        data={'search_keyword': unicode(VedioNumber), 'search_type': 'amateurjav',
                              'op': 'search'})
    if res.status_code == requests.codes.ok:
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        topic_area = soup.find('div', attrs={'class': 'topic_area'})
        topic_box = topic_area.find('div', attrs={'class': 'topic_box'})
        if topic_area is not None:
            if topic_box is not None:
                res = requests.get(topic_box.find('a').get('href'))
                if res.status_code == requests.codes.ok:
                    html = res.content
                    soup = BeautifulSoup(html, 'html.parser')
                    contents_title = soup.find('div', attrs={'id': 'contents_title'})
                    contents_title = contents_title.find('b').text
                    # print contents_title
                    # print '----------------'
                    for mvinfo_dmm_A in soup.find_all('div', attrs={'class': 'mvinfo_dmm_A'}):
                        if mvinfo_dmm_A.find('b').text == u"番號：":
                            # print mvinfo_dmm_A.text.lstrip(u"番號：")

                            Result["number"] = mvinfo_dmm_A.text.lstrip(u"番號：")

                            number = mvinfo_dmm_A.text.lstrip(u"番號：")
                            rm_string = "[" + mvinfo_dmm_A.text.lstrip(u"番號：") + "]"
                            contents_title = contents_title.replace(rm_string, "")

                        # print contents_title
                        if mvinfo_dmm_A.find('b').text == u"發行日期：":
                            # print mvinfo_dmm_A.text.lstrip(u"發行日期：")
                            date = mvinfo_dmm_A.text.lstrip(u"發行日期：")

                            Result["date"] = mvinfo_dmm_A.text.lstrip(u"發行日期：")

                        if mvinfo_dmm_A.find('b').text == u"影片時長：":
                            # print mvinfo_dmm_A.text.lstrip(u"影片時長：")

                            Result["video_long"] = mvinfo_dmm_A.text.lstrip(u"影片時長：")
                            Result["video_long"] = Result["video_long"].split(u"（")[0]
                            # Result["video_long"] = mvinfo_dmm_A.text.lstrip(u"影片時長：")

                        if mvinfo_dmm_A.find('b').text == u"導演：":
                            # print mvinfo_dmm_A.text.lstrip(u"導演：")
                            Result["maker"] = mvinfo_dmm_A.text.lstrip(u"導演：")
                        if mvinfo_dmm_A.find('b').text == u"製作商：":
                            # print mvinfo_dmm_A.text.lstrip(u"製作商：")
                            Result["seller"] = mvinfo_dmm_A.text.lstrip(u"製作商：")
                        if mvinfo_dmm_A.find('b').text == u"發行商：":
                            # print mvinfo_dmm_A.text.lstrip(u"發行商：")
                            Result["company"] = mvinfo_dmm_A.text.lstrip(u"發行商：")
                    mvinfo_introduction = soup.find('div', attrs={'class': 'mvinfo_introduction'}).text
                    avers = ""
                    for av_performer_name_box in soup.find_all('div', attrs={'class': 'av_performer_name_box'}):
                        contents_title = contents_title.replace(av_performer_name_box.text, "")
                        avers += av_performer_name_box.text + ","
                    # print avers.strip(",")
                    Result["avers"] = avers.strip(",")
                    contents_title = contents_title.lstrip(" ")
                    contents_title = contents_title.lstrip(u" ")
                    contents_title = contents_title.strip(" ")
                    contents_title = contents_title.strip(u" ")
                    Result["title"] = contents_title
                    img = soup.find('img').get('src')
                    # print "Download from ",img,".."
                    urllib.urlretrieve(img, 'tmp.jpg')
                    Result["img"] = img
                    # print "JackS: ", Result
                    Result['result'] = "PASS"
                    return Result

    print "Cannot Find this AV Number in https://7mm.tv"

    return Result


def OnExit():
    if os.path.isfile('tmp.jpg'):
        os.remove('tmp.jpg')