from json_dao import AbstractJsonDao
from model import Post
from flask import request, jsonify

class AbstractJsonService:
    """
    獲得 json  服務
    1. GET方法 讀取特定 id 資訊
                讀取全部資訊
    2. POST 方法
    """
    @classmethod
    def get_json(cls, id):
        user_find = None
        data = AbstractJsonDao.read()
        for user in data:
            if user["id"] == id:
                user_find = user
                break
        if user_find:
            userId = user_find["userId"]
            id = user_find["id"]
            title = user_find["title"]
            body = user_find["body"]
        return Post(userId, id, title, body).to_dict()
    
    @classmethod
    def get_all_json(cls):
        return jsonify({"posts":AbstractJsonDao.read()})
    
    @classmethod
    def post_json(cls, new_json):
        data = AbstractJsonDao.read()
        data.append(new_json)
        AbstractJsonDao.write(data)
        return jsonify({"posted":new_json})

    @classmethod
    def update_json(cls, renew_json):
        id_find = None
        data = AbstractJsonDao.read()
        for i in data:
            if i["id"] == renew_json["id"]:
                id_find = i
                break
        if id_find:
            data.remove(id_find)                
            id_find["userId"] = renew_json["userId"]
            id_find["title"] = renew_json["title"]
            id_find["body"] = renew_json["body"]
            data.append(id_find)
            AbstractJsonDao.write(data)
        return jsonify({"updated":id_find})

    @classmethod
    def delete_json(cls, id):
        id_find = None
        data = AbstractJsonDao.read()
        for i in data:
            if i["id"] == int(id):
                id_find = i
                break
        if id_find:
            data.remove(id_find)
            AbstractJsonDao.write(data)
        return jsonify({"deleted":id_find})     



# info = AbstractJsonService.get_json(10)
# print(info)

# info_all = AbstractJsonService.get_all_json()
# print(info_all)