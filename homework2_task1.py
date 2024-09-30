#Homework2 task1
from queue import Queue
import random

#Створити чергу заявок
queue = Queue()

# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги

def generate_request(queue: Queue):
    requests_count = random.randint(1,5)
    for i in range(requests_count):
        queue.put(i)
        print(f"New member added to queue")
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
        while not queue.empty():
            number = queue.get()
            print(f"Process qequest from queue is {number}")

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок

while(True):
    generate_request(queue)
    # print(queue)
    process_requests(queue)
    value = input("Do you want to stop processing? Enter y to stop, n to add new requests\n")
    if value == 'y':
        break

