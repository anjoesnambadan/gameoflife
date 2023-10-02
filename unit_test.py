from game import next_board_state
import numpy as np

def test(init_state, expected_next_state, test_number):
    actual_next_state = next_board_state(init_state)
    # print(actual_next_state)
    # print(expected_next_state)
    if(np.equal(actual_next_state, expected_next_state).all()):
        print("PASSED TEST " + str(test_number))
    else:
        print("FAILED TEST " + str(test_number))

if __name__ == "__main__":
    #TEST 1: dead cell with no neighbours
    init_state1 = np.asarray([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])

    expected_next_state1 = np.asarray([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    
    test(init_state1, expected_next_state1, 1)

    #TEST 2: dead cell with 3 neighbours

    init_state2 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ])

    expected_next_state2 = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ])

    test(init_state2, expected_next_state2, 2)

    #TEST 3: live cell with 0 neighbour

    init_state3 = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0]
    ])

    expected_next_state3 = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])

    test(init_state3, expected_next_state3, 3)

    #TEST 4: live cell with 1 neighbour

    init_state4 = np.array([
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ])

    expected_next_state4 = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])

    test(init_state4, expected_next_state4, 4)

    #TEST 5: live cell with 2 neighbour

    init_state5 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ])

    expected_next_state5 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ])

    test(init_state5, expected_next_state5, 5)

    #TEST 6: live cell with 3 neighbour

    init_state6 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ])

    expected_next_state6 = np.array([
        [1, 1, 0],
        [1, 1, 1],
        [1, 1, 0]
    ])

    test(init_state6, expected_next_state6, 6)

    #TEST 7: live cell with 4 neighbour

    init_state7 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [1, 1, 0]
    ])

    expected_next_state7 = np.array([
        [1, 1, 0],
        [0, 0, 1],
        [1, 1, 0]
    ])

    test(init_state7, expected_next_state7, 7)

    #TEST 8: live cell with 5 neighbour

    init_state8 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [1, 1, 1]
    ])

    expected_next_state8 = np.array([
        [1, 1, 0],
        [0, 0, 0],
        [1, 0, 1]
    ])

    test(init_state8, expected_next_state8, 8)

    #TEST 9: live cell with 6 neighbour

    init_state9 = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [1, 1, 1]
    ])

    expected_next_state9 = np.array([
        [1, 1, 1],
        [0, 0, 0],
        [1, 0, 1]
    ])

    test(init_state9, expected_next_state9, 9)
