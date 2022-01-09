import json

from flask import jsonify
from model import Post
from json_dao import AbstractPostDao

class PostFilesystemDao(AbstractPostDao):
    """
    讀取 json 檔案
    
    """

    @classmethod
    def get(cls, id):
        with open("post.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            userfind = None
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
    def get_all(cls):
        with open("post.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return jsonify(data)

    @classmethod
    def add(cls, data: json):
        with open("post.json", "r", encoding="utf-8") as rd:
            context = json.load(file)
            context.append(data)
            with open("post.json", "w", encoding="utf-8") as wf:
                json.dump(context, wf, indent=4)
        return jsonify({"add":data})

    @classmethod
    def update(cls, data: json):
        with open("post.json", "r", encoding="utf-8") as file:
            data_all = json.load(file)
            user_find = None
            for user in data_all:
                if user["id"] == data["id"]:
                    user_find = user
                    break
            if user_find:
                data_all.remove(user_find)
                user_find["userId"] = data["userId"]
                user_find["id"] = data["id"]
                user_find["title"] = data["title"]
                user_find["body"] = data["body"]
                data_all.append(user_find)
                with open("post.json", "w", encoding="utf-8") as file:
                    file.write(data_all)
        return jsonify({"updated":data})

    @classmethod
    def delete(cls, id):
        id_find = None
        with open("post.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        for i in data:
            if i["id"] == int(id):
                id_find = i
                break
        if id_find:
            data.remove(id_find)
            with open("post.json", "r", encoding="utf-8") as file:
                file.write(data)
        return jsonify({"deleted":id_find})     


        




# post = AbstractJsonDao.read()
# print(type(post))