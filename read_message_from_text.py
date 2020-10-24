# -*- coding: utf-8 -*-
from google.protobuf import text_format
import person_and_book_pb2

# message: Book
book = person_and_book_pb2.Book()

model_config_file_path = "book_example.ini"
with open(model_config_file_path, 'r+') as f:
    book_ini = f.read()

parsed_book = text_format.Parse(text=book_ini, message=book)

# 输出解析信息
# 输出书籍信息
print("book_name: %s, book_price: %s, book_press: %s" % (parsed_book.name, parsed_book.price, parsed_book.press))

# 输出人物信息
for person in parsed_book.people:
    print("p_id: %s, p_name: %s, p_age: %s, p_email: %s, p_job: %s, p_work_status: %s, p_city: %s"
          % (person.id, person.name, person.age, person.email, person.job, person.work_status, person.city))

    for key in person.maps.tell_address:
        print("{}: {}".format(key, person.maps.tell_address[key]))
