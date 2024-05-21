from talon import Context, actions

ctx = Context()
ctx.matches = r"""
code.language: sql
"""

# these vary by dialect
ctx.lists["user.code_common_function"] = {
    "count": "count",
    "min": "min",
    "max": "max",
    "sum": "sum",
    "over": "over",
    "as": "as",
}


@ctx.action_class("user")
class UserActions:
    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_equal():
        actions.auto_insert(" = ")

    def code_operator_not_equal():
        actions.auto_insert(" <> ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_in():
        actions.user.insert_between(" in (", ")")

    def code_operator_not_in():
        actions.user.insert_between(" not in (", ")")

    def code_operator_and():
        actions.auto_insert("and ")

    def code_operator_or():
        actions.auto_insert("or ")

    def code_insert_null():
        actions.auto_insert("null")

    def code_insert_is_null():
        actions.auto_insert(" is null")

    def code_insert_is_not_null():
        actions.auto_insert(" is not null")

    def code_comment_line_prefix():
        actions.auto_insert("-- ")

    def code_insert_function(text: str, selection: str):
        actions.user.insert_between(f"{text}({selection or ''}", ")")
