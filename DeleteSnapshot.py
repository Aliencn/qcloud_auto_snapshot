import json
from QcloudApi.qcloudapi import QcloudApi

def DeleteSnapshot(user_region,user_secretId,user_secretKey,snapshotId):
    status = None
    module = 'snapshot'
    action = 'DeleteSnapshot'
    config = {
        'Region': user_region,
        'secretId': user_secretId,
        'secretKey': user_secretKey,
        'method': 'GET',
        'SignatureMethod': 'HmacSHA1'
    }
    action_params = {
        'snapshotIds.n':snapshotId,
    }
    
    try:
        service = QcloudApi(module, config)
        # 生成请求的URL，不发起请求
        #print(service.generateUrl(action, action_params))
        # 调用接口，发起请求
        status = service.call(action, action_params)
    except Exception as e:
        import traceback
        print('traceback.format_exc():\n%s' % traceback.format_exc())

    return(status)