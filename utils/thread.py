# coding=utf-8
import threading

import time

threads = []


# 增加线程函数
def add_thread_func(func):
    print '============add new thread func============='
    dict = {}
    thread = threading.Thread(target=func)
    dict['thread'] = thread
    dict['state'] = False
    threads.append(dict)


# 全局启动线程
def global_start_threads():
    print '============global thread starting============='
    try:
        while True:
            time.sleep(1)
            for t in threads:
                if t['state']:
                    continue
                print t['thread']
                t['thread'].setDaemon(True)
                t['thread'].start()
                t['state'] = True
                t['thread'].join()
    except Exception, e:
        print '!!!!!!!!!!!!!!got an exception !!!!!!!!!!!!!!!'
        print str(e)
