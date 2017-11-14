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
				# catchCycle(connectedNode)
				return false # This is not an acyclic graph. 
		node.status = explored # After all is said and done, this node has been explored. 

		return true # If we've gone through the queue and there are no nodes pointing to previous nodes that aren't their parents, then it's an acyclic graph. 

catchCycle(connectedNode):
	cycle = [] # The array to print. 
	d = connectedNode.distance # The distance of the node that first loops back in the check. 
	while distance > 0: # While we haven't reached the root...
		cycle.append(connectedNode.parent) # Add the parent of this node.
		distance = distance - 1 # Subtract distance to keep adding the parent of the parent, and so on until the root.
	for i in range(d-1,0,-1): # Counting down from end of array (the root) until the first element...
		print(str(cycle[i])) # Print that node. 
		print(str(cycle[d-1]))

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
