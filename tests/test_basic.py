from algorithms_lib.arrays import two_sum, max_subarray
from algorithms_lib.graphs import bfs, dijkstra, topo_sort_kahn
from algorithms_lib.dp import lis_length, coin_change, edit_distance
def test_two_sum():
    assert two_sum([2,7,11,15],9) in ([0,1],[1,0])
def test_max_subarray():
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
def test_bfs():
    adj = {0:[1,2],1:[2],2:[0,3],3:[3]}
    assert bfs(adj, 2) == [2,0,3,1]
def test_dijkstra():
    n=3; edges=[(0,1,4),(0,2,1),(2,1,2)]
    dist = dijkstra(n, edges, 0)
    assert dist == [0,3,1]
def test_topo_sort_kahn():
    assert topo_sort_kahn(4, [(0,1),(1,2),(2,3)]) == [0,1,2,3]
def test_lis_length():
    assert lis_length([10,9,2,5,3,7,101,18]) == 4
def test_coin_change():
    assert coin_change([1,2,5], 11) == 3
def test_edit_distance():
    assert edit_distance("kitten","sitting") == 3
