import json
from model import Post

class AbstractJsonDao:
    """
    讀取 json 檔案
    
    """
    def __init__(self, id):
        self.id = int(id)

    @classmethod
    def read(cls):
        with open("post.json", "r") as file:
            data = json.load(file)
        return data

    @classmethod
    def write(cls, context):
        with open("post.json", "w") as wf:
                json.dump(context, wf, indent=4)
        
        




# post = AbstractJsonDao.read()
# print(type(post))