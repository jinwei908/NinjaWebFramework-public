
from django.conf import settings

def Report_Error(eType, eError, eDescription, eTime):
    settings.MONGO_DB.errors.insert_one(
    {
        "errorType":eType,
        "errorMsg": eError,
        "errorData": eDescription,
        "log_time": eTime
    })
    return True