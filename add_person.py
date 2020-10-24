# -*- coding: utf-8 -*-
import person_and_book_pb2

# 书籍信息
book = person_and_book_pb2.Book()
book.name = "Introduction to Protobuf"
book.price = 8.5
book.press = "NY Press"

# 添加人物信息
person = book.people.add()
person.id = 1
person.name = "protobuf"
person.age = 25
person.email = "protobuf@163.com"
person.job = "college professor"
person.work_status = True
person.city = "Shanghai"

# 添加人物的地址信息
address_maps = person.maps
address_maps.tell_address["born place"] = "SX"
address_maps.tell_address["living place"] = "SH"
address_maps.tell_address["visited place"] = "BJ, GZ, SY"

# 序列化
serializeToString = book.SerializeToString()
print(type(serializeToString), serializeToString)

# 反序列化
parsed_book = person_and_book_pb2.Book()
parsed_book.ParseFromString(serializeToString)
print(type(parsed_book))

# 输出书籍信息
print("book_name: %s, book_price: %s, book_press: %s" % (parsed_book.name, parsed_book.price, parsed_book.press))

# 输出人物信息
for person in parsed_book.people:
    print("p_id: %s, p_name: %s, p_age: %s, p_email: %s, p_job: %s, p_work_status: %s, p_city: %s"
          % (person.id, person.name, person.age, person.email, person.job, person.work_status, person.city))

    for key in person.maps.tell_address:
        print(key, person.maps.tell_address[key])