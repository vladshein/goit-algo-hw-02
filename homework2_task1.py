#Homework2 task1
from queue import Queue
import random
import time

#Створити чергу заявок
queue = Queue()

# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги

def generate_request(queue: Queue):
    #генерація рандомного id
    request_id = random.randint(1000, 9999)
    request_data = f"Request {request_id}"
    
    #додавання до черги
    queue.put(request_data)
    print(f"Generated: {request_data}")
# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста

def process_requests(queue: Queue):
    if queue.empty():
        print("Queue is empty")
    else:
        request_data = queue.get()
        print(f"Processing: {request_data}")

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок

while(True):
    generate_request(queue)
    time.sleep(1)
    process_requests(queue)
    time.sleep(1)
    value = input("Do you want to stop processing? Enter y to stop, n to add new requests\n")
    if value == 'y':
        break

