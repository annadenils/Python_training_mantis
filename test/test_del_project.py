from model.project import Project
import random


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.get_projects_list()) == 0:
        app.project.init_project(Project(project_name="тестовый", description="проверка связи"))
    old_projects = app.soap.get_projects_list("administrator", "root")
    project = random.choice(old_projects)
    app.project.del_project(project.id)
    new_projects = app.soap.get_projects_list("administrator", "root")
    old_projects.remove(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(),
                                                                 key=Project.id_or_max)