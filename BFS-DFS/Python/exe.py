import sys #System import
import graphs

if __name__=="__main__":
    #Script execution
    #Generate graph
    g = graphs.Graph()

    #Searchs
    searchs = [2, 3, 0]

    #Add edges
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    for s in searchs:
        print("BFS from", s)
        distances, parents, visitOrder = g.BFS(s)
        print("Distances:", distances)
        print("Parents list:", parents)
        print("Order:", visitOrder)
        print()

    for s in searchs:
        print("DFS from", s)
        initialTime, visitOrder, distances, discoverTimestamps, parents = g.DFS(s)
        print("Distances:", distances)
        print("Parents list:", parents)
        print("Order:", visitOrder)
        print("Discover times:", list(map(lambda x: x - initialTime, discoverTimestamps)))
        print()



