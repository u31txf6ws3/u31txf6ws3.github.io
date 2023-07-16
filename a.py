from mypy import nodes
from mypy import types
from mypy.plugin import ClassDefContext
from mypy.typevars import fill_typevars
from mypy.plugins.common import add_method_to_class
from typing import Callable, Optional, Type

def add_enum_map_signature(ctx: ClassDefContext) -> None:
    print([x.node for x in ctx.cls.info.names.values()])
    enum_members = [
        member
        for member, symbol_table in ctx.cls.info.names.items()
        if isinstance(symbol_table.node, nodes.Var)
    ]

    obj = ctx.api.named_type("builtins.object")
    t_var = types.TypeVarType("T", "T", -1, [], obj)

    args = [
        nodes.Argument(
            variable=nodes.Var(member, t_var),
            type_annotation=t_var,
            initializer=None,
            kind=nodes.ARG_NAMED,
        )
        for member in enum_members
    ]

    self_type = types.TypeType(fill_typevars(ctx.cls.info))
    return_type = ctx.api.named_type("builtins.dict", [self_type, t_var])

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


from mypy.plugin import Plugin

class EnumMapPlugin(Plugin):
    def get_metaclass_hook(
            self,
            fullname: str,
    ) -> Optional[Callable[[ClassDefContext], None]]:
        if fullname.endswith(".MappingEnumMeta"):
            return add_enum_map_signature
        return None


def plugin(version: str) -> Type[Plugin]:
    return EnumMapPlugin
