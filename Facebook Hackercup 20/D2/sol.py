import sys
import heapq
from typing import List, Iterator, Tuple, Set


def adjacent(city: int, mapp: List[Set[int]]) -> Iterator[int]:
    yield from mapp[city]


def shortest_way(
    source: int,
    destination: int,
    fuel_cap: int,
    city: int,
    mapp: List[Set[int]],
    total_price: List[int],
) -> int:
    heap = [(0, -fuel_cap, source)]

    cheapest = [float("+inf")] * city
    fuel_left = [float("-inf")] * city
    cheapest[source] = 0
    fuel_left[source] = fuel_cap

    while heap:
        price, fuel, city = heapq.heappop(heap)

        fuel = -fuel
        cheapest[city] = min(price, cheapest[city])
        fuel_left[city] = max(fuel, fuel_left[city])

        if city == destination:
            return price

        for adj in adjacent(city, mapp):
            if fuel > 0:
                adj_price = price
                neigh_fuel = fuel - 1

                if (
                    adj_price < cheapest[adj]
                    or neigh_fuel > fuel_left[adj]
                ):
                    heapq.heappush(heap, (adj_price, -neigh_fuel, adj))

            if fuel != fuel_cap and total_price[city] != 0:
                adj_price = price + total_price[city]
                neigh_fuel = fuel_cap - 1

                if (
                    adj_price < cheapest[adj]
                    or neigh_fuel > fuel_left[adj]
                ):
                    heapq.heappush(heap, (adj_price, -neigh_fuel, adj))

    return -1


def take_number_jobs(lines: Iterator[str]) -> int:
    return int(next(lines))


def take_para(lines: Iterator[str]) -> Tuple[int, int, int, int]:
    cities_str, max_fuel_str, src_str, dst_str = next(lines).split()
    return int(cities_str), int(max_fuel_str), int(src_str) - 1, int(dst_str) - 1


def take_parent_price_in(lines: Iterator[str]) -> Tuple[int, int]:
    parent_str, cost_str = next(lines).split()
    return int(parent_str) - 1, int(cost_str)


def take_parent_price(
    lines: Iterator[str], city: int
) -> Tuple[List[int], List[int]]:
    total_price: List[int] = []
    parents: List[int] = []

    for _ in range(city):
        parent, price = take_parent_price_in(lines)
        parents.append(parent)
        total_price.append(price)

    return parents, total_price


def grapher_top(parents: List[int], city: int) -> List[Set[int]]:
    mapp: List[Set[int]] = [set() for _ in range(city)]

    for pos, parent in enumerate(parents):
        if parent != -1:
            mapp[pos].add(parent)
            mapp[parent].add(pos)

    return mapp


def take_jobs(lines: Iterator[str]) -> Tuple[int, int, List[Set[int]], List[int], int, int]:
    city, fuel_cap, source, destination = take_para(lines)
    parents, total_price = take_parent_price(lines, city)

    mapp = grapher_top(parents, city)

    return city, fuel_cap, mapp, total_price, source, destination


def take_job_in(
    lines: Iterator[str],
) -> Iterator[Tuple[int, int, List[Set[int]], List[int], int, int]]:
    jobs = take_number_jobs(lines)

    for _ in range(jobs):
        yield take_jobs(lines)


def main() -> None:
    testcase = 1

    for city, fuel_cap, mapp, total_price, source, destination in take_job_in(sys.stdin):
        answer = shortest_way(source, destination,
                              fuel_cap, city, mapp, total_price)
        print("Case #" + str(testcase) + ": " + str(answer), file=f)
        testcase += 1


if __name__ == "__main__":
    with open("output.txt", 'w') as f:
        main()
