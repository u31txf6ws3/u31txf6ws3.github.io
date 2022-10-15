# {
#     "TITLE": "Mypy",
#     "DATE": "2022-10-15",
#     "BODYPATH": "bodies/20221015_mypy_exhaustiveness.py",
#     "REDDIT_COMMENTS": "https://old.reddit.com/user/u31txf6ws3/comments/go0mve/optimizing_cellular_automata_in_python/",
#     "OUTPUT": "posts/20221015_mypy_exhaustiveness.html",
#     "HIDDEN": true
# }

import enum

class Fruit(enum.Enum):
    apple = enum.auto()
    banana = enum.auto()

def smell(fruit: Fruit) -> str:
    if   fruit is Fruit.apple:  return "nice"
    elif fruit is Fruit.banana: return "good"
    raise ValueError(f"{fruit} is not a fruit")

# This works fine and passes mypy.

class Fruit(enum.Enum):
    apple = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

# But now <code>taste(Fruit.durian)</code> fails

from typing import NoReturn

def assert_never(_: NoReturn) -> NoReturn:
    raise ValueError("Unreachable code reached")

# Then we rewrite our function like

def smell(fruit: Fruit) -> str:
    if   fruit is Fruit.apple:  return "nice"
    elif fruit is Fruit.banana: return "good"
    assert_never(fruit)

# If we add a case handling the new enum member

def smell(fruit: Fruit) -> str:
    if   fruit is Fruit.apple:  return "nice"
    elif fruit is Fruit.banana: return "good"
    elif fruit is Fruit.durian: return "oh lord"
    assert_never(fruit)

# But say one has a dictinary

smells: dict[Fruit, str] = {
    Fruit.apple:  "nice",
    Fruit.banana: "good",
}

# Mypy will not catch an error

# One way of doing it is with functions
# something of the sort

from typing import TypeVar

T = TypeVar("T")

class Fruit(enum.Enum):
    apple = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

    @classmethod
    def map(cls, apple: T, banana: T, durian: T) -> dict[Fruit, T]:
        return {
            cls.apple: apple,
            cls.banana: banana,
            cls.durian: durian,
        }

# and replace the dicts with

#$
smells: dict[Fruit, str] = Fruit.map(
    apple  = "nice",
    banana = "good",
)

# which mypy does identify as an error but now i need to keep track of the enum
# members in two places, no good

# i came to realisation i need to do two things
# * genrate the map function automatically
# * write a mypy plugin that type check that dynamic function

# the first one sounds easy, you can just subclass enum

class MappingEnum(enum.Enum):
    @classmethod
    def map(cls, **kwargs: T) -> dict["MappingEnum", T]:
        return {member: kwargs[member.name] for member in cls}


class Fruit(MappingEnum):
    apple = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

print(Fruit.map(apple=1, banana=2, durian=3))

# unfortunately the mypy plugins a finicky

E = TypeVar("E", bound=enum.Enum)

@classmethod
def enum_map(cls: type[E], **kwargs: T) -> dict[E, T]:
    return {member: kwargs[member.name] for member in cls}

class MappingEnumMeta(enum.EnumMeta):
    def __new__(
        cls: type[E],
        name: str,
        bases: tuple[type, ...],
        dct: enum._EnumDict,
    ) -> E:
        dict.__setitem__(dct, "map", enum_map)
        return super().__new__(cls, name, bases, dct)

class Fruit(enum.Enum, metaclass=MappingEnumMeta):
    apple  = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

print(Fruit.map(apple=1, banana=2, durian=3))

# Ever seen a <code>classmethod</code> defined outiside a class?
# Dont freakout, rember that

class A:
    @classmethod
    def f(cls): ...

# is just short for

@classmethod
def f(cls): ...

A = type("A", (), {"f": f})

# which is essentially what we're doing there
