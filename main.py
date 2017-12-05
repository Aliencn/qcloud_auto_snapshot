from DescribeSnapshots import DescribeSnapshots
from DeleteSnapshot import DeleteSnapshot
from CreateSnapshot import CreateSnapshot
import json

def jsonread(j):
    if j != None:
        s = json.loads(str(j,encoding='utf-8'))
    return(s)

user_region = 'ap-guangzhou'
user_secretId = 'secretKey'
user_secretKey = 'secretKey'
user_disk_id = 'diskid'
user_snapshotName='auto'

Describe = jsonread(DescribeSnapshots(user_region,user_secretId,user_secretKey,user_disk_id))
if Describe != None and Describe['code'] == 0 and Describe['totalCount'] >= 7:
    snapshotId = Describe['snapshotSet'][0]['snapshotId']
    Delete = jsonread(DeleteSnapshot(user_region,user_secretId,user_secretKey,snapshotId))
    if Delete != None and Delete['code'] == 0:
        CreateSnapshot(user_region,user_secretId,user_secretKey,user_disk_id,user_snapshotName)
elif Describe != None and Describe['code'] == 0:
    CreateSnapshot(user_region,user_secretId,user_secretKey,user_disk_id,user_snapshotName)