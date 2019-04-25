# 集合覆盖问题
# 每次遍历所有的广播台, 寻找能覆盖 未被覆盖的州 最多的广播台

# 需要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# 广播台
stations = {}
stations['one'] = set(['id', 'nv', 'ut'])
stations['two'] = set(['wa', 'id', 'mt'])
stations['thr'] = set(['or', 'nv', 'ca'])
stations['fou'] = set(['nv', 'ut'])
stations['fiv'] = set(['ca', 'az'])

# 总共需要的广播台
final_stations = []

while states_needed:
    best_station = None
    # 当前广播台能覆盖的州
    states_covered = {}
    # 寻找能覆盖 未被覆盖的州 最多的广播台
    for station, states in stations.items():
        coverd = states_needed & states
        if len(coverd) > len(states_covered):
            best_station = station
            states_covered = coverd
    # 去掉已覆盖的州, 添加广播台
    states_needed -= states_covered
    final_stations.append(best_station)

print(final_stations)
