import Queue

from rdoclient import RandomOrgClient


def get_capacity_left(api_key):
    r = RandomOrgClient(api_key)
    bits = r.get_bits_left()
    reqs = r.get_requests_left()
    return reqs, bits


def has_capacity(api_key):
    reqsbits = get_capacity_left(api_key)
    if reqsbits[0] < 5 and reqsbits[1] < 300:
        return False
    return True


def test_connection(api_key):
    try:
        print(api_key)
        left = get_capacity_left(api_key)
        print(left)
        return True
    except TypeError as te:
        print(te)

    except ValueError as ve:
        print(ve)

    return False


def initialize_client(api_key, blocking_timeout=None, http_timeout=None, cached=False, live_results=False, **kwargs):
    r = None
    c = None
    if has_capacity(api_key):
        if blocking_timeout and http_timeout:
            r = RandomOrgClient(api_key, blocking_timeout, http_timeout)

        if cached:
            if r is None:
                r = RandomOrgClient(api_key, blocking_timeout=60.0 * 60.0, http_timeout=30.0)
            cache_size = kwargs['cache_size']
            cache_min = kwargs['cache_min']
            cache_max = kwargs['cache_max']
            # print(kwargs)
            c = r.create_integer_cache(cache_size, cache_min, cache_max)


        elif live_results:
            r = RandomOrgClient(api_key, blocking_timeout=0.0, http_timeout=10.0, serialized=False)
    return r, c


def request_random_integers(amount, min_int, max_int, client, cache=None):
    if cache is not None:
        # print(catche)
        try:
            return cache.get()
        except Queue.Empty:
            # print('queue is empty, shit')
            pass
    else:
        return client.generate_integers(amount, min_int, max_int)


# key = verify_api_key()
# print(get_capacity_left(key))


if __name__ == '__main__':
    t = initialize_client(True, cache_size=5, cache_min=1, cache_max=10)
