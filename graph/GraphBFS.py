import queue
from enum import Enum
from typing import Counter, TypeVar, Generic

T = TypeVar("T")


class VisitStatus(Enum):
    VISITED = 1
    NOT_VISITED = 0


class Vertx(Generic[T]):
    def __init__(self, key, element: T):
        self.key = key
        self.element = element
        self.visited = VisitStatus.NOT_VISITED


class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
        self.vertx_distance = {}  # 紀錄每個 vertx 與 搜尋起點的距離
        self.vertx_predecessor = {}  # 紀錄每個 vertx 的 predecessor, 以便回溯路徑

    """ 為每個 vertx 增加相鄰節點"""

    def add_edge_list(self, from_vertx_key, to_vertx):
        if from_vertx_key not in self.adj_list:
            self.adj_list = []

        self.adj_list[from_vertx_key].append(to_vertx)

    """ 進行 BFS """

    def bfs(self, start_vertx):
        if start_vertx.key not in self.adj_list:
            print('查無該 vertx')
            return

        # 設定搜尋起點的初始值
        self.vertx_distance[start_vertx.key] = 0
        self.vertx_predecessor[start_vertx.key] = None


if __name__ == "__main__":

    graph = Graph()

    vertx_a = Vertx('A', 'A')
    vertx_b = Vertx('B', 'B')
    vertx_c = Vertx('C', 'C')
    vertx_d = Vertx('D', 'D')
    vertx_e = Vertx('E', 'E')
    vertx_f = Vertx('F', 'F')
    vertx_g = Vertx('G', 'G')
    vertx_h = Vertx('H', 'H')
    vertx_i = Vertx('I', 'I')

    graph.add_edge_list(vertx_a.key, vertx_b)
    graph.add_edge_list(vertx_a.key, vertx_c)
    graph.add_edge_list(vertx_a.key, vertx_d)

    graph.add_edge_list(vertx_b.key, vertx_a)
    graph.add_edge_list(vertx_b.key, vertx_e)
