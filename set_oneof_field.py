# -*- coding: utf-8 -*-
from oneof_test_pb2 import Test, MessageA, MessageB

message_a = MessageA()
message_a.content = "Hello from MessagesA!"

message_b = MessageB()
message_b.content = 1

# 设置test.a为MessageA
test1 = Test()
test1.a.CopyFrom(message_a)
# 设置test.a为MessageB
test2 = Test()
test2.b.CopyFrom(message_b)

print(test1)
print(test2)