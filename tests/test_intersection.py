from app.matchmaker.intersection import compute_multi_way_intersection

def test_multi_way_intersection():
    user1_lib = {10, 20, 30, 40}
    user2_lib = {20, 30, 50}
    user3_lib = {20, 30, 60}
    
    result = compute_multi_way_intersection([user1_lib, user2_lib, user3_lib])
    assert result == {20, 30}

def test_empty_intersection():
    user1_lib = {10, 20}
    user2_lib = {30, 40}
    
    result = compute_multi_way_intersection([user1_lib, user2_lib])
    assert result == set()
