import math
import random as rand


def rands(num):
    return rand.randrange(0,num)

def create_network(num_nodes, num_unions):
    unions=[]
    for i in range(num_unions):
        unions.append([rands(num_nodes), rands(num_nodes)])
    return unions

def union_check(num_nodes,num_unions):
    unions=[]
    for i in range(num_unions):
        unions.append([rands(num_nodes), rands(num_nodes)])
    return unions
    
