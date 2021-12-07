import itertools as it

from typing import Any, Iterator, List, Tuple, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


def grouper(
    n: int, iterable: Iterator[T], fillvalue: Any = None
) -> Iterator[List[Union[T, U]]]:
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return it.zip_longest(fillvalue=fillvalue, *args)


def sliding_window(iterable: Iterator[T], length: int) -> Iterator[Tuple[T, ...]]:
    result = tuple(it.islice(iterable, length))
    if len(result) == length:
        yield result
    for elem in iterable:
        result = result[1:] + (elem,)
        yield result
