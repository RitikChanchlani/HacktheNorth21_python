import json, falcon
from MySQLdb import _mysql

host = 'xinyanglu66.mysql.pythonanywhere-services.com'
user = 'xinyanglu66'
password = 'keybored2021'
database = 'xinyanglu66$keybored'

class AddKeystrokeList:
    def add_keystokes(self, req, resp, id):
        db = _mysql.connect(host=host,user=user, passwd=password,db=database)
        user_id = id
        print('')


class AllInfo:
    def send_info(self,req,resp):
        content = {

        }

api = falcon.API()
api.add_route('/add/{id}',AddKeystrokeList())
