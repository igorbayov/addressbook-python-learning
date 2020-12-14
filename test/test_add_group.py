from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group_name", header="Header_value", footer="Footer_value"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
