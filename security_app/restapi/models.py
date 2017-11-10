from mongoengine import Document, EmbeddedDocument, fields
from restapi.nested_models import *

class Tool(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    inputs = fields.EmbeddedDocumentField(ToolInput)
    #inputs_list = fields.ListView()
    
    
class InsertResult(Document):
    acknowledged = fields.BooleanField(required=False)
    insertedId = fields.ObjectIdField(required=False)
    
class InsertRequest(Document):
    keylogData = fields.StringField(required=False)
    
class CountInstance(Document):
    countData = fields.IntField(required=False)
     
class DashboardDataInstance(Document):
    totalImages = fields.EmbeddedDocumentField(HostActivityInstance)
    mostClicks = fields.EmbeddedDocumentField(HostActivityInstance)
    mostPackets = fields.EmbeddedDocumentField(HostActivityInstance)
    machineCount = fields.EmbeddedDocumentField(HostActivityInstance)
    dataPackets = fields.EmbeddedDocumentField(HostActivityInstance)
    interestingDiscoveries = fields.EmbeddedDocumentListField(PacketDataInstance)
    wordCloudData = fields.EmbeddedDocumentField(TagCountInstance)
    hostActivity = fields.EmbeddedDocumentListField(HostActivityInstance)
    imageCarousel = fields.EmbeddedDocumentListField(ImageInstance)