from bitsandbytes import functional as F

NF4_MAG_dict = {
    0: 0.0,
    1: 0.0911,
    2: 0.1848,
    3: 0.2844,
    4: 0.3949,
    5: 0.5251,
    6: 0.6962,
    7: 1.0,
    8: -0.0,
    9: -0.0911,
    10: -0.1848,
    11: -0.2844,
    12: -0.3949,
    13: -0.5251,
    14: -0.6962,
    15: -1.0,
}


def test_custom_map_tree():

    num_pivots = 1
    values = sorted(list(NF4_MAG_dict.values()))
    print(values)
    while num_pivots < 16:
        idx = list(range(16 // num_pivots // 2, 16, 16 // num_pivots))
        # print(idx)
        num_pivots *= 2
        pivots = []
        for i in idx:
            pivots.append((values[i - 1] + values[i]) / 2)
        print(pivots)

def test_normal_map_tree():
    code = F.create_normal_map()
    values = code[:8].tolist() + code[-8:].tolist()
    num_pivots = 1
    print(values)
    while num_pivots < 16:
        idx = list(range(16 // num_pivots // 2, 16, 16 // num_pivots))
        # print(idx)
        num_pivots *= 2
        pivots = []
        for i in idx:
            pivots.append((values[i - 1] + values[i]) / 2)
        print(pivots)

if __name__ == "__main__":
    test_custom_map_tree()
    test_normal_map_tree()