import sys, os.path
import datetime
sys.path.append("./../../")

from flask import Flask,Response,request
import jsonpickle
from db.db_manager import DbManager

class TmfWebService:
    def __init__(self,name="WebService",host="0.0.0.0",port=80):
        self.name = name
        self.port = port
        self.host = host
        self.api = Flask(self.name)
    
    def get_formated_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%dT%H:%M:%S%z")

    def register(self, url,func,func_pointer,methods=['GET']):
        self.api.add_url_rule(url,func,func_pointer,methods=methods)
    
    def start(self):
        self.api.run(host=self.host,port=self.port)
    
    def get_all(self, helper):
        fields = request.args.get("fields") if (request.args.get("fields") is not None) else None
        offset = int(request.args.get("offset")) if (request.args.get("offset") is not None) else None
        limit = int(request.args.get("limit")) if (request.args.get("limit") is not None) else None
        row = helper.get_all(fields=fields,offset=offset,limit=limit)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')
    
   
    def get_by_id(self,helper,id):
        fields = request.args.get("fields")
        row = helper.get_by_id(id,fields)
        response_str = jsonpickle.encode(row)
        return Response(response_str, 200, mimetype='application/json')

    def get_field_from_path(self,path):
        if path.startswith("/"):
            path = path[1:]
        path = path.replace('/','.')
        return path

    def patch(self, helper, id, patch_data):
        for row in patch_data:
            if (row['op'] == "replace"):
               path = row['path']
               field_name = self.get_field_from_path(path)
               value = row['value']
               change_data = {}
               change_data[field_name] = value
               print(change_data)
               helper.update(id,change_data)  
            elif row['op'] == "add":
               path = row['path']
               field_name = self.get_field_from_path(path)
               value = row['value']
               change_data = {}
               change_data[field_name] = value
               helper.update(id,change_data) 
            elif row['op'] == "remove":
               path = row['path']
               field_name = self.get_field_from_path(path)
               helper.delete_field(id,field_name)      
        return Response("", 200, mimetype='application/json')
 