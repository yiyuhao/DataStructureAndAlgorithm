"""
    基于队列实现事件驱动编程： 发布者与订阅者
"""
import threading
from queue import Queue, Empty


class EventManager:
    def __init__(self):
        self.__queue = Queue()
        self.__handlers = {}

    def save_event(self, event):
        """将新event放入队列"""
        self.__queue.put(event)

    def start(self):
        """启动"""

        def run():
            # 轮询处理事件
            while True:
                try:
                    event = self.__queue.get(block=True, timeout=1)
                    # 处理注册函数
                    if event.type_ in self.__handlers:
                        for f in self.__handlers[event.type_]:
                            f(event)
                except Empty:
                    pass

        th = threading.Thread(target=run)
        th.start()

    def add_event_listener(self, type_, handler):
        has_handler = self.__handlers.get(type_)

        if not has_handler:
            # 初始化为一个列表
            self.__handlers[type_] = []

        # 不重复注册同一handler
        if handler not in self.__handlers[type_]:
            self.__handlers[type_].append(handler)


class Event:
    def __init__(self, type_=None):
        self.type_ = type_
        self.data = {}


class Publisher:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def write_new_article(self):
        event = Event(type_='NewArticle')
        event.data['title'] = 'python是如何热门起来的'
        print('公众号发布了文章')
        self.event_manager.save_event(event)


class Subscriber:
    def __init__(self, name, event_manager):
        self.name = name
        event_manager.add_event_listener('NewArticle', self.get_article)

    def get_article(self, event):
        print('{name}收到了新文章: {title}'.format(name=self.name, title=event.data['title']))


if __name__ == '__main__':
    event_manager = EventManager()
    event_manager.start()

    publisher = Publisher(event_manager)
    subscriber1 = Subscriber('Alice', event_manager)
    subscriber2 = Subscriber('Bob', event_manager)

    publisher.write_new_article()
