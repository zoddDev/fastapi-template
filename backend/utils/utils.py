from bson import json_util
import json

def to_json(data):
    return json.loads(json_util.dumps(data))