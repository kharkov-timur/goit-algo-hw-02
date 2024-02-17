from queue import Queue
import time
import random


def generate_request(request_queue, request_id):
	print(f"Генерується нова заявка з ID: {request_id}")
	request_queue.put(request_id)


def process_request(request_queue):
	if not request_queue.empty():
		current_request = request_queue.get()
		print(f"Обробляється заявка з ID: {current_request}")
	else:
		print("Черга пуста, немає заявок для обробки.")


def main():
	request_queue = Queue()
	request_id = 1
	
	try:
		while True:
			if random.randint(0, 1):
				generate_request(request_queue, request_id)
				request_id += 1
			
			time.sleep(1)
			
			process_request(request_queue)
			
			time.sleep(2)
	except KeyboardInterrupt:
		print("\nПрограма завершена користувачем.")


if __name__ == "__main__":
	main()