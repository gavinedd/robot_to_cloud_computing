from flask import Flask, json, after_this_request

json_file = open("data.json")
jsonToUpLoad = json.load(json_file)
json_file.close()

api = Flask(__name__)

@api.route('/data', methods=['GET'])
def get_companies():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return json.dumps(jsonToUpLoad)


if __name__ == '__main__':
    api.run(host='0.0.0.0')
