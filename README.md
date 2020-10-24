本项目用于学习Google的Protobuf，入门级别。

### 文件说明

#### 序列化与反序列化

- person_and_book.proto
- person_and_book_pb2.py
- add_person.py

参考网址：https://blog.csdn.net/u013210620/article/details/81317731

#### 读取文本格式消息

- book_example.ini
- read_message_from_text.py

#### oneof字段的例子

- oneof_test.proto
- oneof_test_pb2.py
- set_oneof_field.py

#### 更新tensorflow/serving中的models.config文件

脚本：`update_models_config.py`

### 参考网址

1. python基础--protobuf的使用(一)： https://blog.csdn.net/u013210620/article/details/81317731
2. Github/protobuf: https://github.com/protocolbuffers/protobuf
3. gRPC快速入门（一）——Protobuf简介: https://blog.51cto.com/9291927/2331980?source=drh
4. Protobuf3语法详解: https://blog.csdn.net/qq_36373500/article/details/86551886
5. protobuf文本格式解析地图: http://www.voidcn.com/article/p-yrhvscxz-bwp.html
6. Question: How to set oneof fields in python?: https://github.com/protocolbuffers/protobuf/issues/5012