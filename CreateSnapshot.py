from QcloudApi.qcloudapi import QcloudApi

def CreateSnapshot(user_region,user_secretId,user_secretKey,user_disk_id,snapshotName):
    module = 'snapshot'
    action = 'CreateSnapshot'
    config = {
        'Region': user_region,
        'secretId': user_secretId,
        'secretKey': user_secretKey,
        'method': 'GET',
        'SignatureMethod': 'HmacSHA1'
    }
    action_params = {
        'storageId':user_disk_id,
        'snapshotName':snapshotName,
    }
    
    try:
        service = QcloudApi(module, config)
        # 生成请求的URL，不发起请求
        #print(service.generateUrl(action, action_params))
        # 调用接口，发起请求
        service.call(action, action_params)
       
    except Exception as e:
        import traceback
        print('traceback.format_exc():\n%s' % traceback.format_exc())