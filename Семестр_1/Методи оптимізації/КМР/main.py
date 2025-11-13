import itertools
import random
import time

from faker import Faker
import math

from fontTools.misc.cython import returns
from matplotlib import pyplot as plt


class City:
    def __init__(self, name, x, y):
        self.__name = str(name)
        self.__x = float(x)
        self.__y = float(y)

    def __str__(self):
        return f"Name: {self.__name}.\t(x; y) = ({self.__x}; {self.__y}).\n"

    def __repr__(self):
        return f"Name: {self.__name}.\t(x; y) = ({self.__x}; {self.__y}).\n"

    def __eq__(self, other):
        return str(self.__name) == (other.__name) or (self.__x == other.__x) and (self.__y == other.__y)

    def get_name(self):
        return self.__name
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def distance(self, another_city):
        return float(math.sqrt((another_city.__x - self.__x) ** 2 + (another_city.__y - self.__y) ** 2))


def random_city(fake, size, Class):
    size = 1 if size == 0 else size if size > 0 else -size

    values = [Class(fake.city(), random.uniform(-100, 100), random.uniform(-100, 100))]

    for i in range(size):

        while True:
            name = fake.city()
            x = random.uniform(-100, 100)
            y = random.uniform(-100, 100)
            value = Class(name, x, y)
            if value not in values:
                values.append(value)
                break

    values.append(values[0])
    return values

def cope_without_zero_last(values):
    result = []
    for i, value in enumerate(values):
        if i == len(values) - 1 or i == 0:
            continue
        result.append(values[i])

    return result

def do_n_random_paths(values, size, results=[]):

    if len(values) == 3:
        return [[0,1,2]]
    elif len(values) == 4:
        return [[0,1,2,3]]

    while len(results) != size:

        result = []

        temp_values = cope_without_zero_last(values)

        while len(temp_values) != 0:
            temp = random.choice(temp_values)
            temp_values.remove(temp)

            for i,value in enumerate(values):
                if value == temp:
                    result.append(int(i))
                    break


        if result not in results:
            result.reverse()
            if result not in results:
                result.reverse()
                results.append(result)

    for result in results:
        if len(result) != len(values):
            result.insert(0, 0)
            result.append(int(len(values)-1))

    return results


def distance(values, way):

    result = float(0.0)

    for i,temp in enumerate(way):
        if i == len(values) - 1:
            continue
        result += values[temp].distance(values[way[i+1]])

    return result

def copy(values):
    array = []
    for value in values:
       array.append(value)
    return array

def bee(values, paths, N, n=0,INDEX=0):
    if n < 0:
        n = -n

    if len(values) <= 2:
        return [[]]
    elif len(values) == 3:
        return [[0,1,2]]
    elif len(values) == 4:
        return[[0,1,2,3]]

    the_same = 0
    last_the_same = 0
    index = 0
    if INDEX == 0:
        if len(values) <= 100:
            INDEX = 100
        else:
            INDEX = 50

    TEMP = itertools.count() if n == 0 else range(n)

    for _ in TEMP:
        paths = do_n_random_paths(values, N, paths)

        distances = []
        for path in paths:
            distances.append(distance(values, path))

        distances, paths = my_sort(distances, paths)

        M = 1 if 0 <= int(0.1 * N) <= 1 else int(0.1 * N)
        m = 1 if 0 <= (int(0.25 * (N - M))) <= 1 else (int(0.25 * (N - M)))

        bests = []
        middles = []
        weeks = []

        for j,path in enumerate(paths):
            if j < M:
                bests.append(path)
            elif j < M + m:
                middles.append(path)
            else: weeks.append(path)


        def work_bees(array, iterations):
            for j in range(iterations):
                for path in array:
                    if j % 2:
                        a = random.randint(1, len(values) - 2)
                        b = random.randint(1, len(values) - 2)

                        while a == b:
                            a = random.randint(1, len(values) - 2)
                            b = random.randint(1, len(values) - 2)
                    else:
                        a = random.randint(2, len(values) - 3)
                        b = a + random.choice([1, -1])
                    long = distance(values, path)
                    path[a], path[b] = path[b], path[a]
                    if long <= distance(values, path):
                        path[a], path[b] = path[b], path[a]


        work_bees(bests,100)
        work_bees(middles, 50)
        work_bees(weeks, 10)

        paths = []
        for path in bests:
            del path[len(path) - 1]
            del path[0]
            paths.append(path)
        for path in middles:
            del path[len(path) - 1]
            del path[0]
            paths.append(path)
        for path in weeks:
            del path[len(path) - 1]
            del path[0]
            paths.append(path)


        demo_paths = []
        for path in paths:
            if path not in demo_paths:
                path.reverse()
                if path not in demo_paths:
                    path.reverse()
                    demo_paths.append(path)

        for path in demo_paths:
            path.insert(0, 0)
            path.append(len(values) - 1)

        paths = demo_paths


        distances = []
        for j,path in enumerate(paths):
            distances.append(distance(values, path))


        distances,paths = my_sort(distances,paths)

        if len(paths) > M+m:
            paths = paths[:M+m]

        this_the_same = distance(values, paths[0])
        if this_the_same == last_the_same:
            index += 1
            if index == INDEX:
                break
        else:
            index = 0
            last_the_same = this_the_same

        #print(index)

    return paths


def my_sort(first_array, second_array):
    combined = list(zip(first_array, second_array))

    combined.sort(key=lambda x: x[0])

    first_array, second_array= zip(*combined)

    first_array = list(first_array)
    second_array = list(second_array)

    return first_array, second_array

def show_cities(values):
    for value in values:
        print(value)


def fill_paths_distances(values, size):

    results_path = do_n_random_paths(values, size)

    results_ways = []
    for j, result_path in enumerate(results_path):
        results_ways.append(distance(values, result_path))


    results_ways, results_path = my_sort(results_ways,results_path)

    return results_path


def greedy(values):
    path = [0]

    for i,value in enumerate(values):
        if i == 0 or i == len(values)-1:
            continue

        minimum = -1
        for j,_ in enumerate(values):
            if j == 0 or j == len(values) - 1 or j in path:
                continue
            if minimum == -1:
                minimum = j
            elif values[path[len(path)-1]].distance(_) < values[path[len(path)-1]].distance(values[minimum]):
                minimum = j

        if minimum != -1:
            path.append(minimum)

    path.append(len(values)-1)


    return [path]


def classic(values):
    paths = []

    n = len(values) - 2

    if n == 1:
        return [[0,1,2]]

    for value in itertools.permutations(range(1,n+1)):
        value = list(value)
        value.reverse()
        if value not in paths and value.reverse() not in paths:
            paths.append(value)

    for value in paths:
        value.insert(0, 0)
        value.append(len(values)-1)

    distances = []
    for j, path in enumerate(paths):
        distances.append(distance(cities, path))

    distances,paths = my_sort(distances, paths)

    return paths

def show_cities_in_paths(values,ways):
    for way in ways:

        print(f"{values[0].get_name()}", end='')

        for _ in way:
            if _ == 0:
                continue
            print(f" -> {values[_].get_name()}", end='')
        print(f".\ndistance: {distance(values, way)}.")


if __name__ == "__main__":

    faker = Faker()
    cities = []

    size_cities = 500
    size_paths = 50 if size_cities >50 else size_cities if size_cities != 0 else 1

    cities = random_city(faker, size_cities, City)

    #show_cities(cities)

    paths = []

    paths = fill_paths_distances(cities, size_paths)

    #show_cities_in_paths(cities,paths)

    #print("\n\nThe result of bees.\n\n")
    start = time.time()
    paths = bee(cities, paths, size_paths,50)
    end = time.time()
    times = [float(end - start)]
    the_best = [paths[0]]
    methods = ["bee"]
    lens=[len(paths)]
    #show_cities_in_paths(cities, paths)

    # print("\n\nThe result of greedy.\n\n")
    start = time.time()
    paths = greedy(cities)
    end = time.time()
    times.append(end - start)
    the_best.append(paths[0])
    methods.append("greedy")
    lens.append(len(paths))

    '''
    for i,_ in enumerate(cities):
        print()
        for j, _ in enumerate(cities):

            print(f"{i} {j} {cities[i].distance(cities[j])}")

    print("\n\n")
    '''



    # show_cities_in_paths(cities, paths)

    # print("\n\nThe result of classic.\n\n")
    '''
    start = time.time()
    paths = classic(cities)
    end = time.time()
    times.append(end - start)
    the_best.append(paths[0])
    methods.append("classic")
    lens.append(len(paths))
    #show_cities_in_paths(cities, paths)
    '''

    def show_bests():
        for i, method in enumerate(methods):
            print(f"{method}:")
            show_cities_in_paths(cities, [the_best[i]])
            print(f"{times[i]} seconds;")
            print(f"{lens[i]} size.\n\n")


    show_bests()

    #show_cities_in_paths(cities, paths)


