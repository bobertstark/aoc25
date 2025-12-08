def main(coords: list[str], conns: int = 1000):
    circuits = []
    connections = []

    while coords:
        coord = coords.pop(0)
        for i in range(len(coords)):
            coord2 = coords[i]
            dist = euclidean(coord, coord2)
            connections.append((dist, name(coord), name(coord2)))
        circuits.append(set((name(coord),)))

    connections.sort(key=lambda x: x[0])


    def connect(max_connections: int) -> list:
        for dist, box1, box2 in connections[:max_connections]:
            #print(f'Distance: {dist} - connecting {box1} and {box2}')

            for i, circuit in enumerate(circuits):
                if box1 in circuit and box2 in circuit:
                    #print('\tAlready connected!')
                    break

                if box1 in circuit:
                    box1_idx = i

                if box2 in circuit:
                    box2_circuit = circuit

            else:
                circuits[box1_idx].update(box2_circuit)
                circuits.remove(box2_circuit)

        return circuits


    circuits = connect(conns)
    res = 1
    for cir in sorted(circuits, key=len)[-3:]:
        print(len(cir))
        res *= len(cir)

    print(res)


def name(coord):
    return f'box-{",".join(coord)}'



def euclidean(coord1, coord2) -> int:
    import math
    x1, y1, z1 = [int(i) for i in coord1]
    x2, y2, z2 = [int(i) for i in coord2]

    return int(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


if __name__ == '__main__':
    import sys
    in_file = sys.argv[-1]
    with open(in_file) as f:
        data = [fline.strip().split(',') for fline in f.readlines()]
    main(data)