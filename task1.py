import hashlib


def hash_string(str_: str, **kwargs) -> str:
    if not isinstance(str_, str):
        raise ValueError(f'must be <class \'str\'> but {type(str_)} was given')

    algorithm = kwargs.pop('algorithm', 'sha256')
    try:
        h = hashlib.new(algorithm)
    except ValueError:
        raise ValueError('no such algorithm')

    h.update(s.encode('utf-8'))
    str_hexed = h.hexdigest()

    return str_hexed


if __name__ == "__main__":
    """
    There is string s = "Python Bootcamp". Write the code that hashes string.
    """

    s = "Python Bootcamp"
    hash_ = hash_string(s, algorithm='sha256')
    print(f"hash of string \"{s}\" is \"{hash_}\"")


