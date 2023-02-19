import pygame
import globals

class PlayerClass:
    def __init__(self, parent_session):
        self.path = Path()   # initialize a Path Object
        self.globals = globals.Globals._instance     # load instance of globals
        self.unvisited_nodes = None     # need to keep track of Nodes not yet visited
        self.last_node_visited = None   # the last node the player clicked and processing for which is done
        self.current_node = None    # need during analysis of Path player has Chose
        self.start_node = None      # the first node a Player clicks
        self.is_circle = False      # boolean checking if path is a circle
        self.parent_session = parent_session
    # copy all the nodes on the map
    def set_nodes(self, nodes):
        self.unvisited_nodes = nodes.copy()

    # called when a Vertex is clicked, add the Vertex to the Path and
    def add_vertex_to_path(self, vertex):

        self.current_node = vertex

        if not self.last_node_visited:
            self.start_node = vertex


        else:
            pos_1 = (self.last_node_visited.rect.x+5, self.last_node_visited.rect.y+5)
            pos_2 = (self.current_node.rect.x+5, self.current_node.rect.y+5)
            pygame.draw.line(self.globals.screen, self.globals.blue, pos_1, pos_2, 5)

        self.path.add(vertex)
        self.path.draw(self.globals.screen)
        self.unvisited_nodes.remove(vertex)

    def check_if_game_completed(self):
        if self.start_node == self.current_node and self.last_node_visited:
            self.is_circle = True
            if self.check_if_path_complete():
                self.parent_session.is_game_complete = True

        self.last_node_visited = self.current_node

    def check_if_path_complete(self):
        print("path gets check")
        if len(self.unvisited_nodes) == 0 and self.last_node_visited is not None:
            return True
        else:
            print("not all nodes visited")
            return False

    def end_game(self):
        pass


class Path(pygame.sprite.Group):
    def __init__(self):
        super(Path, self).__init__()
