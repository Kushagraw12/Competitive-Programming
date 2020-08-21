import sys
import heapq
from typing import List, Iterator, Tuple, Set


def adj(city: int, mapp: List[Set[int]]) -> Iterator[int]:
    yield from mapp[city]


def shortest_way(
    source: int,
    destination: int,
    fuel_cap: int,
    city: int,
    mapp: List[Set[int]],
    price: List[int],
) -> int:
    heap = [(0, -fuel_cap, source)]

    cheapest = [float("+inf")] * city
    fuel_left = [float("-inf")] * city
    cheapest[source] = 0
    fuel_left[source] = fuel_cap

    while heap:
        cost, spent_fuel, city = heapq.heappop(heap)

        spent_fuel = -spent_fuel

        cheapest[city] = min(cost, cheapest[city])
        fuel_left[city] = max(spent_fuel, fuel_left[city])

        if city == destination:
            return cost

        for adjacent in adj(city, mapp):
            if spent_fuel > 0:
                adj_price = cost
                adj_fuel = spent_fuel - 1

                if (
                    adj_price < cheapest[adjacent]
                    or adj_fuel > fuel_left[adjacent]
                ):
                    heapq.heappush(heap, (adj_price, -adj_fuel, adjacent))

            if spent_fuel != fuel_cap and price[city] != 0:
                adj_price = cost + price[city]
                adj_fuel = fuel_cap - 1

                if (
                    adj_price < cheapest[adjacent]
                    or adj_fuel > fuel_left[adjacent]
                ):
                    heapq.heappush(heap, (adj_price, -adj_fuel, adjacent))

    return -1


def take_jobs(lines: Iterator[str]) -> int:
    return int(next(lines))


def take_city_fuel(lines: Iterator[str]) -> Tuple[int, int]:
    cities_str, max_fuel_str = next(lines).split()
    return int(cities_str), int(max_fuel_str)


def take_price(lines: Iterator[str]) -> int:

    return int(next(lines))


def take_price_number(lines: Iterator[str], city: int) -> List[int]:
    price = []

    for _ in range(city):
        price.append(int(next(lines)))

    return price


def read_job(lines: Iterator[str]) -> Tuple[int, int, List[int]]:
    city, fuel_cap = take_city_fuel(lines)
    price = take_price_number(lines, city)

    return city, fuel_cap, price


def take_input_job(lines: Iterator[str]) -> Iterator[Tuple[int, int, List[int]]]:
    jobs = take_jobs(lines)

    for _ in range(jobs):
        yield read_job(lines)


def make_city_map(city: int) -> List[Set[int]]:
    mapp: List[Set[int]] = [set() for _ in range(city)]

    for current in range(city):
        if current > 0:
            mapp[current].add(current - 1)
            mapp[current - 1].add(current)
        if current < city - 1:
            mapp[current].add(current + 1)
            mapp[current + 1].add(current)

    return mapp


def main() -> None:
    testcase = 1

    for city, fuel_cap, price in take_input_job(sys.stdin):

        mapp = make_city_map(city)
        source, destination = 0, city - 1
        answer = shortest_way(source, destination, fuel_cap, city, mapp, price)
        print("Case #" + str(testcase) + ": " + str(answer), end="", file=f)
        print(file=f)
        testcase += 1


if __name__ == "__main__":
    with open('grading_output.txt', 'w') as f:
        main()
