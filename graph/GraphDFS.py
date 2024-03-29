import queue
import json
from enum import Enum
from typing import TypeVar, Generic

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
            self.adj_list[from_vertx_key] = []

        self.adj_list[from_vertx_key].append(to_vertx)

    def dfs(self, start_vertx):
        # recursive 需設定中止條件
        # 沒有相鄰 vertx 時就停止搜尋
        if start_vertx.key not in self.adj_list:
            return

        start_vertx.visited = VisitStatus.VISITED

        for adj_vertx in self.adj_list[start_vertx.key]:
            if adj_vertx.visited == VisitStatus.NOT_VISITED:
                adj_vertx.visited = VisitStatus.VISITED
                print(f'dfs_recursive:{adj_vertx.key}')
                self.dfs(adj_vertx)

    """ 自行維護一個 stack 進行 DFS, 一般不會使用此方法"""

    def dfs_with_stack(self, start_vertx):
        stack = [start_vertx]

        while stack:
            visit_vertx = stack.pop()
            visit_vertx.visited = VisitStatus.VISITED
            print(f'dfs_with_stack:{visit_vertx.key}')

            if visit_vertx.key not in self.adj_list:
                continue

            for adj_vertx in self.adj_list[visit_vertx.key]:
                if adj_vertx.visited == VisitStatus.NOT_VISITED:
                    adj_vertx.visited = VisitStatus.VISITED
                    stack.append(adj_vertx)

    def def_with_recursion(self, start_vertx):
        if start_vertx.key not in self.adj_list[start_vertx.key]:
            return


if __name__ == "__main__":

    graph = Graph()

    vertx_a = Vertx('A', 'A')
    vertx_b = Vertx('B', 'B')
    vertx_c = Vertx('C', 'C')
    vertx_d = Vertx('D', 'D')
    vertx_e = Vertx('E', 'E')
    vertx_f = Vertx('F', 'F')

    graph.add_edge_list(vertx_a.key, vertx_b)
    graph.add_edge_list(vertx_a.key, vertx_c)

    graph.add_edge_list(vertx_b.key, vertx_d)

    graph.add_edge_list(vertx_c.key, vertx_b)
    graph.add_edge_list(vertx_c.key, vertx_f)

    graph.add_edge_list(vertx_d.key, vertx_e)
    graph.add_edge_list(vertx_d.key, vertx_f)

    # graph.dfs(vertx_a)

    graph.dfs_with_stack(vertx_a)
