# {
#     "TITLE": "More Exhaustiveness Checks With mypy",
#     "SUBTITLE": "or How to Write a Basic mypy Plugin",
#     "DATE": "2022-10-15",
#     "BODYPATH": "bodies/20221015_mypy_exhaustiveness.py",
#     "OUTPUT": "posts/20221015_mypy_exhaustiveness.html",
#     "HIDDEN": true
# }

# Modern type checkers are capable of analysing whether all members of an
# enumeration type are being handled in a if-else or match statement, which is
# referred as exhaustiveness check. In a dynamic language like python this is
# a nicety that makes adding or removing member to an enum a safer process. Take
# the following for example

import enum

class Fruit(enum.Enum):
    apple  = enum.auto()
    banana = enum.auto()

def smell(fruit: Fruit) -> str:
    if   fruit is Fruit.apple:  return "nice"
    elif fruit is Fruit.banana: return "good"
    raise ValueError(f"{fruit} is not a fruit")

# This works as expected and passes all mypy checks, but if I were to change
# the definition of <code>Fruit</code> to add a new member

class FruitMore(enum.Enum):
    apple  = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

# the function <code>smell</code> would raise a <code>ValueError</code> if
# <code>FruitMore.durian</code> were passed to it, even if the type annotatios
# were patched to take a <code>FruitMore</code> instead of <code>Fruit</code>.
# That's the expected behaviour, but in a large codebase it's easy to lose
# track of all the places where I'd need to handle the new member. It is more
# helpful to have such errors flagged during static analysis. Mypy is cabaple
# of doing such checks, but it's not very obvious how. The trick (better
# described <a
# href="http://web.archive.org/web/20221004031954/https://hakibenita.com/python-mypy-exhaustive-checking">here</a>)
# is to define a test fucntion with the following signature

from typing import NoReturn

def assert_never(_: NoReturn) -> NoReturn:
    raise ValueError("Unreachable code reached")

# which is meant to be called in unreachable areas of the code. So if I rewrite
# the <code>smell</code> function like so

def smell_incomplete(fruit: FruitMore) -> str:
    if   fruit is FruitMore.apple:  return "nice"
    elif fruit is FruitMore.banana: return "good"
    assert_never(fruit)

# then mypy helpfully points an error at the last line of the function:
# <code>Argument 1 to "assert_never" has incompatible type
# "Literal[FruitMore.durian]"; expected "NoReturn"</code>. Adding a case to
# account for all members of <code>FruitMore</code> makes the error go away.

def smell_complete(fruit: FruitMore) -> str:
    if   fruit is FruitMore.apple:  return "nice"
    elif fruit is FruitMore.banana: return "good"
    elif fruit is FruitMore.durian: return "oh lord"
    assert_never(fruit)  # no errors here

# This works fine in many situations, but not all of them. At the moment I am
# currently converting a heavily stringly typed codebase to use enums. It so
# happens there are many constant dictionaries that map enums to values like so

smells: dict[FruitMore, str] = {
    FruitMore.apple:  "nice",
    FruitMore.banana: "good",
}

# I would like to staticaly check that the dictionary above is missing a
# member, but I couldn't find a trick as simple as <code>assert_never</code> to
# make it happen.

# One work around is to use a class method to generate the dictionary

from typing import TypeVar

T = TypeVar("T")

class FruitMapping(enum.Enum):
    apple = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

    @classmethod
    def map(cls, *, apple: T, banana: T, durian: T) -> dict["FruitMapping", T]:
        return {
            cls.apple: apple,
            cls.banana: banana,
            cls.durian: durian,
        }

# This way if I rewrite the dictionaries like so

#$
smells_broken: dict[FruitMapping, str] = FruitMapping.map(
    apple  = "nice",
    banana = "good",
)

# mypy will identify that there's a missing argument <code>durian</code> with a
# <code>Missing named argument "durian"</code> error.

# The problem with the solution above is that it imposes the burdern of
# maintaining the enum members in two different places (the body of the enum,
# and in the definition of <code>map</code>). And because there are no static
# checks to guarantee that they match, it allows developers to accidentally
# write code that should be illegal. Finally I'd rather not have to litter all
# enums with a definition of <code>map</code>.

# Of course writing a generic version of <code>map</code> is quite easy

from pprint import pprint as print

class MappingEnum(enum.Enum):
    @classmethod
    def map(cls, **kwargs: T) -> dict["MappingEnum", T]:
        return {member: kwargs[member.name] for member in cls}


class FruitMappingGeneric(MappingEnum):
    apple = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

print(FruitMappingGeneric.map(apple=1, banana=2, durian=3))

# But as you may expect, mypy is not cabaple of telling that

#$
FruitMappingGeneric.map(apple=1, banana=2)

# is missing an argument.

# After a little research, it seems to me that I have to both generate
# <code>map</code> automatically and on top of that write a mypy plugin that
# patches its type annotation for each subclass of <code>MappingEnum</code>, so
# it ends looking like the one in <code>FruitMapping</code>.

# So I went on to learn how to write a mypy plugin. Unfortunaly that is not
# what I would call accessible. The plugin system is very imature and poorly
# documented. So I think

# So it started my first foray into writing mypy plugins. Unfortunaly the API
# for that is very imature and thinly documented. The best way to get the gist
# of it is to look at examples and the read the source code.

# There are two plugin hooks that give me acces to the class definition, so I can patch it:

# I decided to go with a metaclass because it's a bit more straightforward. All I have to do
# is move the definition of <code>map</code> to a metaclas

from typing import cast, Iterable
E = TypeVar("E")

class MappingEnumMeta(enum.EnumMeta):
    def map(cls: type[E], **kwargs: T) -> dict[E, T]:
        # mypy can't tell that type[E] is iterable
        # so I'm just gonna ignore the types here
        return {member: kwargs[member.name] for member in cls}  # type: ignore

class FruitWithMetaMapping(enum.Enum, metaclass=MappingEnumMeta):
    apple  = enum.auto()
    banana = enum.auto()
    durian = enum.auto()

print(FruitWithMetaMapping.map(apple=1, banana=2, durian=3))

# That works the same, which is good. And just like before

#$
FruitWithMetaMapping.map(apple=1, banana=2)

# raises an exception. Creating an enum is a bit clunkier, having to both
# subclass <code>enum.Enum</code> and setting the metaclass to
# <code>MappingEnumMeta</code>, but I think that's an acceptable burden.

# Now to the fun part, writing the mypy plugin. I quote straight from
# <code>mypy.plugin</code>'s docstring <blockquote> At several steps during
# semantic analysis and type checking mypy calls special `get_xxx` methods on
# user plugins with a single string argument that is a fully qualified name
# (full name) of a relevant definition </blockquote> you can check the full
# list of special methods in the documentation, but the one that I need is
# <code>get_metaclass_hook</code>. Here's what the main body of the plugin
# looks like

from typing import Callable, Optional, Type
from mypy.plugin import ClassDefContext, Plugin

class EnumMapPlugin(Plugin):
    def get_metaclass_hook(
            self,
            fullname: str,
    ) -> Optional[Callable[[ClassDefContext], None]]:
        # a better way of checking would be to do
        # a direct comparision
        # fullname == "whatever_module.ClassName"
        # but the below is better for rendering this blog post
        if fullname.endswith(".MappingEnumMeta"):
            return add_enum_map_signature
        return None

def plugin(version: str) -> Type[Plugin]:
    return EnumMapPlugin

# When the plugin encounters a definition it doesn't cares about, the hook
# returns <code>None</code>, telling mypy to keep chugging as normal. When it
# does meet a class that has <code>MappingEnumMeta</code> as metaclass, then it
# returns a callback whose signature depends on the specific hook. Refer to the
# souce code for the signature of each hook.

# Now I have to write <code>add_enum_map_signature</code>, which I remind is
# meant to add the signature of the following function to
# <code>FruitWithMetaMapping</code>

@classmethod
def map(cls: Type[E], *, apple: T, banana: T, durian: T) -> dict[E, T]: ...

# Here is how I go about doing it. Worth mentioning that this uses the latest
# unreleased version (0.990+dev.5e1e26eba)

from mypy import nodes
from mypy import types
from mypy.typevars import fill_typevars
from mypy.plugins.common import add_method_to_class

def add_enum_map_signature(ctx: ClassDefContext) -> None:

    # Collect the names of the members of the enum in question they are
    # instances of mypy.nodes.Var any method extra method added to an enum has
    # type mypy.nodes.FuncDef
    enum_members = [
        member
        for member, symbol_table in ctx.cls.info.names.items()
        if isinstance(symbol_table.node, nodes.Var)
    ]

    # This creates the type of the arguments, that is, the type
    # T = TypeVar("T", bound=object)
    obj = ctx.api.named_type("builtins.object")
    t_var = types.TypeVarType("T", "T", -1, [], obj)

    # Create the argument nodes. Setting the kind to nodes.ARG_NAMED
    # means they are keyword only arguments
    args = [
        nodes.Argument(
            variable=nodes.Var(member, t_var),
            type_annotation=t_var,
            initializer=None,
            kind=nodes.ARG_NAMED,
        )
        for member in enum_members
    ]

    # create the type of the cls argument, Type[E],
    # where E = TypeVar("E", bound=FruitWithMetaMapping)
    self_type = types.TypeType(fill_typevars(ctx.cls.info))

    # create the return type, that is, dict[E, T]
    return_type = ctx.api.named_type("builtins.dict", [self_type, t_var])

    # quite self explanatory
    add_method_to_class(
        api=ctx.api,
        cls=ctx.cls,
        name="map",
        args=args,
        self_type=self_type,
        return_type=return_type,
        is_classmethod=True,
        tvar_def=t_var,
    )

# You can add a plugin to mypy by adding the following line to your config
# file of preference
# <pre>[mypy]
# plugins = mapping_enum.py</pre>

# And with that you should see helpful 

#$
FruitWithMetaMapping.map(apple=1, banana=2)

# This gives an error <code>Missing named argument "durian" for "map" of "FruitWithMetaMapping"</code>
