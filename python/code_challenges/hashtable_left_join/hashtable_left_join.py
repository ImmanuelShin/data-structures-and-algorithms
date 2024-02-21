from code_challenges.hashtable.hashtable import Hashtable


def left_join(map1, map2):
    return_map = map1
    for key in map1:
        if key in map2:
            return_map[key] = [map1.get(key), map2.get(key)]
        else:
            return_map[key] = [map1.get(key), None]
    return return_map