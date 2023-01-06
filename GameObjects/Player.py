import pygame
import globals

class PlayerClass:
    def __init__(self):
        self.path = Path()
        self.globals = globals.Globals._instance
        self.unvisited_nodes = None
        self.last_node_visited = None
        self.current_node = None
        self.start_node = None
        self.is_circle = False

    def set_nodes(self, nodes):
        self.unvisited_nodes = nodes.copy()
        print(self.unvisited_nodes)

    def add_vertex_to_path(self, vertex):
        self.current_node = vertex
        if not self.last_node_visited:
            print("If")
            self.start_node = vertex
        else:
            print("else")
            pos_1 = (self.last_node_visited.rect.x+5, self.last_node_visited.rect.y+5)
            pos_2 = (self.current_node.rect.x+5, self.current_node.rect.y+5)
            pygame.draw.line(self.globals.screen, self.globals.blue, pos_1, pos_2, 5)
        self.path.add(vertex)
        self.path.draw(self.globals.screen)
        self.unvisited_nodes.remove(vertex)
        if self.start_node == self.current_node and self.last_node_visited:
            self.is_circle = True
            self.check_if_path_complete()
            print("is circle")
        self.last_node_visited = self.current_node

    def check_if_path_complete(self):
        print("path gets check")
        if len(self.unvisited_nodes) == 0:
            print("end of game")
            return True
        else:
            print("not all nodes visited")
            return False



class Path(pygame.sprite.Group):
    def __init__(self):
        super(Path, self).__init__()
