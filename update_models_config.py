# -*- coding: utf-8 -*-
# 该脚本用于更新tensorflow/serving中的models.config
import grpc
from google.protobuf import text_format
from tensorflow_serving.apis import model_service_pb2_grpc, model_management_pb2
from tensorflow_serving.config import model_server_config_pb2
from tensorflow_serving.sources.storage_path.file_system_storage_path_source_pb2 import FileSystemStoragePathSourceConfig

# models.config所在路径
model_config_file_path = "./models.config"
with open(model_config_file_path, 'r+') as f:
    config_ini = f.read()

request = model_management_pb2.ReloadConfigRequest()
model_server_config = model_server_config_pb2.ModelServerConfig()
config_list = model_server_config_pb2.ModelConfigList()
model_server_config = text_format.Parse(text=config_ini, message=model_server_config)

# Create a config to add to the list of served models
one_config = config_list.config.add()
one_config.name = "lmj"
one_config.base_path = "/models/lmj"
one_config.model_platform = "tensorflow"
servable_version_policy = FileSystemStoragePathSourceConfig().ServableVersionPolicy()
one_config.model_version_policy.all.CopyFrom(servable_version_policy.All())

model_server_config.model_config_list.MergeFrom(config_list)
request.config.CopyFrom(model_server_config)

# 服务地址：192.168.1.168:8510, 其中8510对应tensorflow/serving的8500端口
channel = grpc.insecure_channel('192.168.1.193:8510')
stub = model_service_pb2_grpc.ModelServiceStub(channel)
response = stub.HandleReloadConfigRequest(request, 10)
if response.status.error_code == 0:
    with open(model_config_file_path, 'w+') as f:
        f.write(request.config.__str__())
    print("Updated TF Serving conf file")
else:
    print("Failed to update model_config_list!")
    print(response.status.error_code)
    print(response.status.error_message)