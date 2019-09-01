
graph = {'A':['B','E'],'B':['A', 'D','C'],'C':['B','E'],'D':['B'],'E':['C','F'],'F':['E']}
start = input("Enter start node - ")
end = input("Enter end node - ")

def bfs( start, end, graph ):
	current = [(start, [start])]
	while len( current ):
		node, path = current.pop( 0 )
		for next_node in graph[node]:
			if next_node in path:
				continue
			elif next_node == end:
				yield path + [next_node]
			else:
				current.append( (next_node, path + [next_node]) )



	[ print( x ) for x in bfs( start, end, graph ) ]
