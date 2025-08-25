class TreeNode :
    def __init__ (self,val,left =  None ,right = None):
        self.val =  val 
        self.left =  left
        self.right   =  right
    
    
    def __str__(self):
        lines = []
        self._build_str(lines, "")
        return "\n".join(lines)

    def _build_str(self, lines, prefix):
        lines.append(prefix + str(self.val))
        if self.left:
            self.left._build_str(lines, prefix + "  L-")

        if self.right:
            self.right._build_str(lines, prefix + "  R-")


def bfs_r_aux(nodos_nivel,recorrido):
    #print(nodos_nivel)

    if not nodos_nivel  :
        return recorrido
    siguiente_nivel = []

    for node in nodos_nivel:  #Procesamos los nodos del nivel actual
        #print(nodos_nivel)
        recorrido.append(node.val)

        if node.left:
            siguiente_nivel.append(node.left)
        if node.right:
            siguiente_nivel.append(node.right)

    return bfs_r_aux(siguiente_nivel,recorrido)



def bfs_recurivso(root):
    if root is None :
        return  []

    nodos  =  [root]
    
    return bfs_r_aux(nodos,[])

def bfs (root):
    queue =  [root]
    res =  []

    while queue :
        #current = queue[0]  Acceder al primer elemento 
        current  =  queue.pop(0) # -> la funcion pop(i) extrae y elimina el elemento en la posicion i
        res.append(current.val)
        
        if current.left :
            queue.append(current.left)
        if current.right :
            queue.append(current.right)

    return res
    

def in_order (root):
    "Completar"
    return []

def pre_order (root):
    "Completar"
    return []

def post_order(root):
    "Completar"
    return []


class Tree_nary:
    def __init__(self,value,children = []):
        self.value =  value 
        self.children =  children

    def bfs(self):
        "Completar"
        return []


if __name__ == "__main__":

    root  =  TreeNode(1) 
    root.left  =  TreeNode(2)
    root.right =  TreeNode(3)
    root.right.left = TreeNode(50)
    root.left.right =  TreeNode(4)
    
    print("Bfs")
    print(bfs(root))

    print("bfs recursivo")
    print(bfs_recurivso(root))

    print("\n toString del arbol binario: \n")
    print(root)

    #Agregar ejecuciones de funciones aqui


    #ESTA ES LA PRUEBA DE CAMBIOS



