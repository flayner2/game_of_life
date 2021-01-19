import life

if __name__ == '__main__':
    # TEST 1: dead cells should stay dead with no live neighbors
    initial_state_1 = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
    expected_state_1 = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
    actual_state_1 = life.next_board_state(initial_state_1)

    assert actual_state_1 == expected_state_1, 'Test 1 failed'

    # TEST 2: dead cells should become alive with 3 live neighbors
    initial_state_2 = [[0, 0, 1],
                       [0, 1, 1],
                       [0, 0, 0]]
    expected_state_2 = [[0, 1, 1],
                        [0, 1, 1],
                        [0, 0, 0]]
    actual_state_2 = life.next_board_state(initial_state_2)
    assert actual_state_2 == expected_state_2, 'Test 2 failed'

    # TEST 3: cells should die or stay dead with <= 1 neighbor
    initial_state_3 = [[1, 0, 0],
                       [0, 0, 1],
                       [0, 0, 1]]
    expected_state_3 = [[0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0]]
    actual_state_3 = life.next_board_state(initial_state_3)
    assert actual_state_3 == expected_state_3, 'Test 3 failed'

    # TEST 4: cells should die with > 3 live neighbors
    initial_state_4 = [[0, 1, 1],
                       [0, 1, 1],
                       [0, 1, 0]]
    expected_state_4 = [[0, 1, 1],
                        [1, 0, 0],
                        [0, 1, 1]]
    actual_state_4 = life.next_board_state(initial_state_4)
    assert actual_state_4 == expected_state_4, 'Test 4 failed'

    # TEST 5: cells should stay alive with 2 or 3 live neighbors
    initial_state_5 = [[0, 1, 1],
                       [0, 0, 1],
                       [0, 1, 0]]
    expected_state_5 = [[0, 1, 1],
                        [0, 0, 1],
                        [0, 0, 0]]
    actual_state_5 = life.next_board_state(initial_state_5)
    assert actual_state_5 == expected_state_5, 'Test 5 failed'
