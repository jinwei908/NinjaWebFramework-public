from rest_framework_mongoengine import viewsets, generics
from restapi.serializers import *
from django.conf import settings
from datetime import datetime, date, timedelta
from rest_framework import mixins, status
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.response import Response
from django.http import HttpResponse
from restapi.operations import *
from restapi.error_handler import *
import json

class GetHomeDashboardData(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = DashboardDataSerializer

    def get_queryset(self):
        today = date.today()
        date_a_week_ago = today - timedelta(days=7)
        #get all the data here, then collate into 1 JSON
        totalImages = settings.MONGO_DB.image_col.aggregate([{"$match": {"log_time": { "$gt": datetime.combine(date_a_week_ago, datetime.min.time())}}},{"$group":{"_id":"TotalImages", "count":{"$sum":1}}}])
        for data5 in totalImages:
            totalImagesCount = data5;
        mostClicks =  settings.MONGO_DB.all_packets_data.aggregate([{"$match": {"log_time": { "$gt": datetime.combine(date_a_week_ago, datetime.min.time())}}},{"$group":{"_id":"$computer_name", "count":{"$sum":"$click_count"}}},{"$sort" : {"count" : -1}}, {"$limit" : 1 }])
        for data6 in mostClicks:
            mostClicksCount = data6;
        mostPackets = settings.MONGO_DB.all_packets_data.aggregate([{"$match": {"log_time": { "$gt": datetime.combine(date_a_week_ago, datetime.min.time())}}},{"$group":{"_id":"$computer_name", "count":{"$sum":1}}}, {"$sort" : {"count" : -1}}, {"$limit" : 1 }])
        for data7 in mostPackets:
            mostPacketsCount = data7;
        
        dataPackets = settings.MONGO_DB.all_packets_data.aggregate([{"$match": {"log_time": { "$gt": datetime.combine(date_a_week_ago, datetime.min.time())}}},{"$group":{"_id":"TotalDataPackets", "count":{"$sum":1}}}])
        for data8 in dataPackets:
            dataPacketsCount = data8;
        #machineCount = settings.MONGO_DB.host_log.distinct('computer_name').count
        machineCount = settings.MONGO_DB.host_log.aggregate([{"$group":{"_id":"$computer_name", "count":{"$sum":1}}}])
        machineCountList = [];
        for data4 in machineCount:
            machineCountList.append(data4)
        
        
        
        #counting them in
        
        interestingDiscoveries = settings.MONGO_DB.all_packets_data.find({"all_tags":{"$in":["Porn", "Sex", "Login"]}, "string_content": {"$regex": "(.*[a-z]){2}"}}).sort("log_time",-1)
        
        discoveryList = [];
        for data3 in interestingDiscoveries.limit(20):
            discoveryList.append(data3)
        
        
        wordCloud = settings.MONGO_DB.tags_counter.aggregate([
                {"$group":{"_id":"TagCount", 
                "General": { "$sum": "$tags_data.General" },
                "Discord": { "$sum": "$tags_data.Discord" },
                "WhatsApp": { "$sum": "$tags_data.WhatsApp" },
                "YouTube": { "$sum": "$tags_data.YouTube" },
                "GoogleChrome": { "$sum": "$tags_data.Google Chrome" },
                "Instagram": { "$sum": "$tags_data.Instagram" },
                "InternetExplorer": { "$sum": "$tags_data.Internet Explorer" },
                "Firefox": { "$sum": "$tags_data.Firefox" },
                "Facebook": { "$sum": "$tags_data.Facebook" },
                "Gmail": { "$sum": "$tags_data.Gmail" },
                "MicrosoftWord": { "$sum": "$tags_data.Microsoft Word" },
                "MicrosoftPowerpoint": { "$sum": "$tags_data.Microsoft Powerpoint" },
                "Steam": { "$sum": "$tags_data.Steam" },
                "MicrosoftVisualStudio": { "$sum": "$tags_data.Microsoft Visual Studio" },
                "Hotmail": { "$sum": "$tags_data.Hotmail" },
                "Unity": { "$sum": "$tags_data.Unity" },
                "GoogleSearch": { "$sum": "$tags_data.Google Search" },
                "Forums": { "$sum": "$tags_data.Forums" },
                "Telegram": { "$sum": "$tags_data.Telegram" },
                "Outlook": { "$sum": "$tags_data.Outlook" },
                "Excel": { "$sum": "$tags_data.Excel" },
                "AdobeReader": { "$sum": "$tags_data.AdobeReader" },
                "Skype": { "$sum": "$tags_data.Skype" },
                "OpenOffice": { "$sum": "$tags_data.OpenOffice" },
                "VLCMediaPlayer": { "$sum": "$tags_data.VLC Media Player" },
                "LiveMessenger": { "$sum": "$tags_data.Live Messenger" },
                "ITunes": { "$sum": "$tags_data.ITunes" },
                "Search": { "$sum": "$tags_data.Search" },
                "Amazon": { "$sum": "$tags_data.Amazon" },
                "eBay": { "$sum": "$tags_data.eBay" },
                "Paypal": { "$sum": "$tags_data.Paypal" },
                "Pinterest": { "$sum": "$tags_data.Pinterest" },
                "Wikipedia": { "$sum": "$tags_data.Wikipedia" },
                "Twitter": { "$sum": "$tags_data.Twitter" },
                "Spotify": { "$sum": "$tags_data.Spotify" },
                "Qoo10": { "$sum": "$tags_data.Qoo10" },              
                "LinkedIn": { "$sum": "$tags_data.LinkedIn" },
                "Tumblr": { "$sum": "$tags_data.Tumblr" },
                "Reddit": { "$sum": "$tags_data.Reddit" },
                "Quora": { "$sum": "$tags_data.Quora" },
                "Bing": { "$sum": "$tags_data.Bing" },
                "Yahoo": { "$sum": "$tags_data.Yahoo" },
                "Taobao": { "$sum": "$tags_data.Taobao" },
                "Netflix": { "$sum": "$tags_data.Netflix" },
                "Porn": { "$sum": "$tags_data.Porn" },
                "Sex": { "$sum": "$tags_data.Sex" },
                "SoundCloud": { "$sum": "$tags_data.SoundCloud" },
                "Twitch": { "$sum": "$tags_data.Twitch" },
                "StackOverflow": { "$sum": "$tags_data.Stack Overflow" },
                "Adobe": { "$sum": "$tags_data.Adobe" },
                "Acrobat": { "$sum": "$tags_data.Acrobat" },
                "Photos": { "$sum": "$tags_data.Photos" },
                "Login": { "$sum": "$tags_data.Login" },
                "Hotel": { "$sum": "$tags_data.Hotel" },
                "Accounting": { "$sum": "$tags_data.Accounting" },
                "Dropbox": { "$sum": "$tags_data.Dropbox" },
                "Netflix": { "$sum": "$tags_data.Netflix" }                       
                }}
                ])
        
        wordCloudObject = {}
        for data2 in wordCloud:
            wordCloudObject = data2
        
        
        hostsActivity = settings.MONGO_DB.all_packets_data.aggregate([{"$match": {"log_time": { "$gt": datetime.combine(date_a_week_ago, datetime.min.time())}}},{"$group":{"_id":"$computer_name", "count":{"$sum":"$click_count"},}},{"$sort" : {"count" : -1}}], useCursor=False)
        #MUST ITERATE THROUGH THE ARRAY/CURSOR: for limiting stuff (for data in imageCarousel.limit(2):)
        hostActivityList = [];
        for data1 in hostsActivity:
            hostActivityList.append(data1)
        
        imageCarousel = settings.MONGO_DB.image_col.find({"log_time":{"$gt":datetime.combine(date_a_week_ago, datetime.min.time())}}).sort("log_time",-1) #sort([("log_time",-1), ("id", 1)])
        #for limiting stuff (for data in imageCarousel.limit(2):)
        imageNew = [];
        for data in imageCarousel:
            imageNew.append(data)
            
        dashboardObject = [{
            "totalImages": totalImagesCount,
            "mostClicks": mostClicksCount,
            "mostPackets": mostPacketsCount,
            "machineCount": {"_id":"Distinct Hosts", "count":len(machineCountList)},
            "dataPackets": dataPacketsCount,
            "interestingDiscoveries": discoveryList,
            "wordCloudData": wordCloudObject,
            "hostActivity": hostActivityList,
            "imageCarousel": imageNew,
        }]
        
        #Report_Error("Get View Error", totalImagesCount, "Encountered error while trying to Get image: ", datetime.now())
        
        return dashboardObject
    
    
    
class ValidateUser(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = ToolSerializer

    def get_queryset(self):
        
        #get all the data here, then collate into 1 JSON
        
        result = settings.MONGO_DB.test_data.find({})
        return result