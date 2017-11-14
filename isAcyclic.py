# isAcyclic
# MJL - Courant - FA.F2017

isAcyclic(G,n): # G is graph with values as tuples {node, [connectedNodes] }
		
	for node in G: # For each node in the graph...
			node.status = unexplored # Default is unexplored.
			node.distance = infinity # Default distance to be written over.
			node.parent = NIL # Default parent is none yet.  

	s.status = exploring # Status of this node is 'exploring'.
	s.distance = 0 # This is the root, so distance = 0. 
	s.parent = NIL # This is the root, so there is no actual parent. 

	Q = [] # The queue.

	enqueue(Q, s) # Add the starting node to the queue. 

	while Q != []:  # While the queue isn't empty...
		node = dequeue(Q) # Take the node from the outpipe of the queue (also removing it from the queue).
		for connectedNode in node.connectedNodes # For each node connected to this node...
			if connectedNode.status = unexplored # If we haven't seen it...
				connectedNode.status = queued # ...add it to the queue! 
				connectedNode.distance = node.distance + 1 # Distance is one away from parent.
				connectedNode.parent = node # Formally define the parent.
			if connectedNode.status = explored & connectedNode.parent != node: # Main part: if we have seen the node *AND* it's not the parent (undirected graph means children can point back to their parents, which is not cyclic), then we have a cycle.
				print("Something's cyclic...")
				return false # This is not an acyclic graph. 
		node.status = explored

		return true


BFS(G,s):

	for node in G:
		node.status = unexplored
		node.distance = infinity
		node.parent = NIL

	start.status = exploring
	start.distance = 0
	start.parent = NIL

	Q = []

	enqueue(Q, s)

	while Q != []: 
		node = dequeue(Q)
		for connectedNode in node.connectedNodes
			if connectedNode.status = unexplored
				connectedNode.status = queued
				connectedNode.distance = node.distance + 1
				connectedNode.parent = node
		node.status = explored
