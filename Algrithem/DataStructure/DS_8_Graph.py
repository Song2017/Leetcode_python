'''
检查你的朋友中有没有芒果销售商
使用散列表来实现图
'''
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['jonny'] = []
graph['thom'] = []
graph['peggy'] = []
mango_seller = ['thom']


# bfs
def search_mango_seller_nums(name):
    friends = graph[name]
    f_friends = []
    relation = 0
    while friends:
        relation += 1
        for person in friends:
            if person in mango_seller:
                return relation
            else:
                f_friends += graph[person]
        friends = f_friends
    return relation


print(search_mango_seller_nums('you'))

# add mango seller
graph['you'] = ['alice', 'bob', 'claire', 'tom']
mango_seller = ['thom', 'tom']
graph['tom'] = ['suny']


# dfs: get all path from you to mango seller
def search_mango_seller_relations(name):
    relation = []
    ans = []

    def dfs(name):
        # add friends who are going to be searched
        relation.append(name)
        if name in mango_seller:
            ans.append(relation.copy())
        else:
            for person in graph[name]:
                dfs(person)
        # reset friends for next search
        relation.pop()

    dfs(name)
    return ans


print(search_mango_seller_relations('you'))
