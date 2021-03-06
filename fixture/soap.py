from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password, baseUrl):
        client = Client(baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password, baseUrl):
        client = Client(baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            source = client.service.mc_projects_get_user_accessible(username, password)
            project_list = []
            for project in source:
                project_list.append(Project(id=project.id, project_name=project.name))
            return project_list
        except WebFault:
            return None

