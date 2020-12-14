from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group name", header="Header value", footer="Footer value"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
