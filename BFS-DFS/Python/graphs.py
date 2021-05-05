import math #For infinites
from collections import defaultdict #Dict
import time #For timestamps

class Graph:
    def __init__(self):
        #Adjacent list
        self.graph = defaultdict(list)

    #Add a new edge to the graph
    def addEdge(self,u,v):
            self.graph[u].append(v)

    #BFS algorithm
    def BFS(self, s):
        n = (max(self.graph) + 1)
        visited = [False] * n #Initialized not visited
        distances = [math.inf] * n #Distances
        parents = [None] * n #Parents list
        visitOrder = [] #Visit order

        queue = [] #BFS queue

        distanceTrack = 0 #Distance traker

        queue.append(s)

        visited[s] = True #Mark as visited
        distances[s] = distanceTrack #0 distance
        parents[s] = None #No parent
        visitOrder.append(s) #First visited

        while len(queue) > 0:
            distanceTrack += 1
            s = queue.pop(0) #Pop first
            for i in self.graph[s]: #Iterate adjacents
                if visited[i] == False: #Not visited
                    queue.append(i) #Is the frontier with not visited
                    visited[i] = True #Mark as visited
                    distances[i] = distanceTrack #Set distance
                    parents[i] = s #Set parent
                    visitOrder.append(i) #Stack in visited order

        return distances, parents, visitOrder

    #DFS algorithm
    def DFSUtil(self, s, visited, visitOrder, distances, discoverTimestamps, parents, distance):
        #Mark as visited
        visited.add(s) #Add to helper set

        for adjacent in self.graph[s]: #Iterate adjacents
            if adjacent not in visited: #For non visited adjacents (Stop condition: all adjacents visited)
                #Node has been visited, modify things
                visitOrder.append(adjacent) #Append to visit order
                distances[adjacent] = distance #Distance from start
                parents[adjacent] = s #s is parent
                discoverTimestamps[adjacent] = time.time() * 1000 #Discover timestamp in ms
                self.DFSUtil(adjacent, visited, visitOrder, distances, discoverTimestamps, parents, distance + 1) #Do another round of search
        else:
            return visitOrder, distances, discoverTimestamps, parents


    #DFS wrapper
    def DFS(self, s):
        n = (max(self.graph) + 1)

        distance = 0 #Initial distance

        #Initial time in ms
        initialTime = time.time() * 1000

        #Initialize vars
        visited = set() #Visited dict
        visitOrder = [] #Visit order
        distances = [math.inf] * n #Distances
        discoverTimestamps = [math.inf] * n #Discover timestamps
        parents = [None] * n #Parents
        
        #Initial node visiting
        visitOrder.append(s) #Add to visit order
        distances[s] = distance #Set 0 distance
        parents[s] = None #No parents in tree
        discoverTimestamps[s] = initialTime #First discovered is initial time
        
        #Start iterations
        rvo, rd, rdt, rp = self.DFSUtil(s, visited, visitOrder, distances, discoverTimestamps, parents, distance + 1)
        
        #Returns
        return initialTime, rvo, rd, rdt, rp
