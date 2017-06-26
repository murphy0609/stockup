import threading

from utils.thread import global_start_threads

t = threading.Thread(target=global_start_threads)
t.setDaemon(True)
t.start()
