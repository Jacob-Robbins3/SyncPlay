def compute_multi_way_intersection(user_libraries):

    if not user_libraries:
        return set()
    
    intersection_set = set(user_libraries[0])
    for lib in user_libraries[1:]:
        intersection_set.intersection_update(lib)
        
    return intersection_set
