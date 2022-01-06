from json_dao import AbstractJsonDao
from model import Post
from json_service import AbstractJsonService

class TargetController:

    @classmethod
    def get_api(cls, id):
        id = int(id)
        print(id)
        return AbstractJsonService.get_json(id)

    @classmethod
    def getall_api(cls):
        return AbstractJsonService.get_all_json()

    @classmethod
    def post_api(cls, new_json):
        return AbstractJsonService.post_json(new_json)

    @classmethod
    def update_api(cls, renew_json):
        return AbstractJsonService.update_json(renew_json)

    @classmethod
    def delete_api(cls, id):
        return AbstractJsonService.delete_json(id)


    