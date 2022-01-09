

class Post(object):
    """
    Attributes:
        userId  (str):
            ID of the user of the post
        id      (str):
            id of the post
        title   (str):
            title of the post
        body    (str):
            body of the post    
    """
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body
    
    @staticmethod
    def from_dict(new_dict: dict):
        post = Post(
            userId = new_dict.get("userId"),
            id = new_dict.get("id"),
            title = new_dict.get("title"),
            body = new_dict.get("body")
        )
        return post

    def to_dict(self):
        demo_dict = {
            "userId": self.userId,
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
        return demo_dict

     def __repr__(self):
        return (f'''Post(
            userId={self.userId},
            post_id={self.id},
            title={self.title},
            body={self.body}
        )''')