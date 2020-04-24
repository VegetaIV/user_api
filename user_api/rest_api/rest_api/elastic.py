from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": "9200"}])


# Tạo index "chat_user" để chứa các user
def create_user_index():
    if not es.indices.exists(index="chat_user"):
        body = {
            "mappings": {
                "properties": {
                    "username": {"type": "keyword"},
                    "email": {"type": "text"},
                    "hashed_password": {"type": "text"},
                    "public_key": {"type": "text"},
                    "encrypted_private_key": {"type": "text"},
                    "transaction_unique_id": {"type": "text"}
                }
            }
        }
        try:
            res = es.indices.create(index="chat_user", body=body)
            return res
        except Exception as e:
            print("Already exists")


# Tạo index "chat_user"
create_user_index()


# Truy vấn thông tin user theo tên
async def get_user_by_username(username):
    body = {
        "query": {
            "match": {
                "username": username
            }
        }
    }
    res = es.search(index='chat_user', body=body)
    try:
        return res['hits']['hits'][0]['_source']
    except:
        return []


# Tạo user mới
async def create_user(username, mail, hashed_password, public_key, encrypted_private_key, transaction_unique_id):
    body = {
        "username": username,
        "email": mail,
        "hashed_password": hashed_password,
        "public_key": public_key,
        "encrypted_private_key": encrypted_private_key,
        "transaction_unique_id": transaction_unique_id
    }
    res = es.index(index='chat_user', doc_type='_doc', body=body)
    return res


# Kiểm tra id đã dùng hay chưa
async def check_id(id):
    body = {
        "query": {
            "match": {
                "id": id
            }
        }
    }
    res = es.search(index="chat_user", body=body)
    try:
        return res['hits']['hits'][0]['_source']
    except:
        return []
