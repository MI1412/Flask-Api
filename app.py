import flask
import flask_restful


app = flask.Flask(__name__)
api = flask_restful.Api(app)
api_resource = flask_restful.Resource

data_json = {
    "minuman":"aqua"
}

# mengatur resource url
class products(api_resource):
    def get(self):
        return data_json

todos = {}
class Todo(api_resource):
    def get(self,todo_id):
        return {todo_id: todos[todo_id]}
    
    def put(self,todo_id):
        todos[todo_id] = flask.request.form['data']
        return {todo_id: todos[todo_id]}

# menambahkan resource api
api.add_resource(products, "/")
api.add_resource(Todo, "/<string:todo_id>")


# ambil semua isi variabel put
@app.route("/api", methods=['PUT'])
def isi_put():
    # ambil json
    data = flask.request.get_json()
    data_json = flask.jsonify({"put variabel":data})
    print(data_json)

if __name__ == "__main__":
    app.run(debug=True)