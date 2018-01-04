import time

import database
import ranclient

# https://stackoverflow.com/a/14917171/1754089
def nested_sum(L):
    return sum(nested_sum(x) if isinstance(x, list) else x for x in L)


class Dice(object):
    def __init__(self, dices, sides, api_key=None):
        import set_api_key
        super(Dice, self).__init__()
        self.__dices = int(dices)
        self.__sides = int(sides)
        self.__client = None
        if api_key:
            self.api_key = api_key
        else:
            try:
                api_key = database.ApiKey.get_key()
                self.api_key = api_key.key
            except AttributeError:
                try:
                    set_api_key.verify_api_key()
                    api_key = database.ApiKey.get_key()
                    self.api_key = api_key.key
                except Exception:
                    print('apikey set failed')

    @property
    def client(self):
        if self.__client:
            return self.__client
        else:
            client, cache = ranclient.initialize_client(self.api_key, live_results=True)
            self.__client = client
            return client

    @client.setter
    def client(self, new_value):
        if self.__client:
            pass
        else:
            self.__client = new_value

    @property
    def sides(self):
        return self.__sides

    @property
    def dices(self):
        return self.__dices

    @property
    def roll(self):

        arr = ranclient.request_random_integers(self.__dices, 1, self.__sides, self.client)
        result = nested_sum(arr)
        return result, arr

    def roll_times(self, n):
        results = []
        for i in range(0, n):
            results.append(self.roll)
        return results

    def __repr__(self):
        return str(self.dices) + "d" + str(self.sides)


class BufferedDice(Dice):
    def __init__(self, dices, sides, cache_size=10, api_key=None):
        super(BufferedDice, self).__init__(dices, sides, api_key=api_key)
        client, cache = ranclient.initialize_client(self.api_key, cached=True, cache_min=1, cache_max=sides,
                                                    cache_size=cache_size)
        self.client = client
        self.__cache = cache
        self.fifo_of_integers = []

    @property
    def roll(self):
        """Rolls the dice

        :return: tuple containing (sum of thrown dices and array with individual dices
        """
        if len(self.fifo_of_integers) < self.dices:
            # print('getting more dices')
            success = False
            while not success:
                try:
                    arr = ranclient.request_random_integers(self.dices, 1, self.sides, self.client, self.__cache)
                    for i in arr:
                        self.fifo_of_integers.append(i)
                        success = True
                except TypeError:
                    time.sleep(0.1)

        ds = []
        for i in range(0, self.dices):
            ds.append(self.fifo_of_integers.pop())

        result = sum(ds)
        return result, ds
