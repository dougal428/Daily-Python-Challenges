#create node class
class Node:
    #initate with name and pathtype
    def __init__(self, name, pathtype):
        self.name = name
        self.type = pathtype
        #set chidldren to empty list
        self.children = list()
        #lenth to len(name)
        self.length = len(name)
        #max child length to 0
        self.max_child_length = 0

    #set string representation
    def __repr__(self):
        return "(name={}, type={}, len={}, max_child_len={})".format(
            self.name, self.type, self.length, self.max_child_length)


def create_graph(node_list):
    if not node_list:
        return None
    
    #parent directory is node before last bit
    parent_node = node_list[0][1]
    #parent level is how many got to go through to final bit
    level = node_list[0][0]
    
    #loop throguh the rest of path to the end
    for index, (node_level, _) in enumerate(node_list[1:]):
        #if is the same level of path break
        if node_level <= level:
            break
        #if is on the next part of direcoty path go on
        if node_level == level + 1:
            #then move onto next part of directpry path
            child_node = create_graph(node_list[index + 1:])
            #append the child node path to parent node child attribute
            parent_node.children.append(child_node)
            #if cild node child or type afgile
            if child_node.children or child_node.type == 'file':
                #and then if  those lengths to file combined greater then parent length to it
                if child_node.max_child_length + child_node.length > parent_node.max_child_length:
                    #then longest path equal to that
                    parent_node.max_child_length = child_node.max_child_length + child_node.length

    print("current_parent: {}".format(parent_node))
    print("it's children: {}".format(parent_node.children))

    return parent_node


def get_path_type(name):
    #file if contains a '.' a file if nit directory
    return 'file' if '.' in name else 'directory'

#end fucntion take in string
def get_longest_path(s):
    #not string return 0
    if not s:
        return 0
    
    #split as\n
    individual_lines = s.split('\n')
    #further split at\t
    split_lines = [x.split('\t') for x in individual_lines]
    
    #len(x)-1 is how many directoty levels; and make new node class taking each row of path in the directory
    annotated_lines = [
        (len(x) - 1, Node(name=x[-1], pathtype=get_path_type(x[-1])))
        for x in split_lines]
    
   #create graph of annotation
    graph = create_graph(annotated_lines)
    
    #add max lenghth to length to see how long path else 0
    return graph.max_child_length + graph.length if graph.max_child_length > 0 else 0


assert get_longest_path("dir\n\tsubdir1\n\tsubdir2") == 0
get_longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
