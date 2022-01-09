from json_dao import AbstractPostDao


class TargetController:

    @classmethod
    def get_api(cls, id):
        id = int(id)
        print(id)
        return AbstractPostDao.get(id)

    @classmethod
    def getall_api(cls):
        return AbstractPostDao.get_all()

    @classmethod
    def post_api(cls, new_json):
        return AbstractPostDao.add(new_json)

    @classmethod
    def update_api(cls, renew_json):
        return AbstractPostDao.update(renew_json)

    @classmethod
    def delete_api(cls, id):
        return AbstractPostDao.delete(id)


    