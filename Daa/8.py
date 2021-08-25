class Graph:
  def __init__(self,vertices):
    self.n = vertices
    self.graph = []
  def AddEdge(self,u,v,w):
    self.graph.append([u,v,w])
  def IsCyclic(self):
    parent =[-1]*(self.n)
    result = []
    count = 0
    self.graph = sorted(self.graph,key=lambda x:x[2])
    for i in self.graph:
      x = self.FindParent(parent,i[0])
      y = self.FindParent(parent,i[1])
      if(x == y):
        continue
      else:
        result.append(i)
      self.Union(parent,x,y)
    print("Minimum Spanning Tree")
    print("[Edge,Edge,weight]")
    for x in result:
      print(x)
  def FindParent(self,parent,i):
    if(parent[i] < 0):
      return i
    else:
      return self.FindParent(parent,parent[i])
  def Union(self,parent,i,j):
    parent[j] = i
    parent[i] = parent[i] - 1
g = Graph(4)
g.AddEdge(0,1,1)
g.AddEdge(1,2,2)
g.AddEdge(2,3,3)
g.AddEdge(3,1,2)
print("[Edge,Edge,weight]")
for x in g.graph:
  print(x)
g.IsCyclic()