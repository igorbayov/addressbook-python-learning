from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Forced group name", header="Forced header value", footer="Forced footer value"))
    app.group.delete_first_group()
