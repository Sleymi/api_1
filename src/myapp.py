from flask import Flask
#from flask_restful import Resource, Api
from flask_restful import Resource, Api,reqparse,abort


app = Flask(__name__)
api = Api(app)


def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404,message="Could not find this Video ...")


video_put_args=reqparse.RequestParser()
video_put_args.add_argument('name',type=str,help="Name of the video is required",required=True)
video_put_args.add_argument('views',type=int,help="Views of the video is required",required=True)
video_put_args.add_argument('likes',type=int,help="Likes of the video is required",required=True)

#videos={}
videos={100:{
    "name": "How to be productive",
    "views": 10000,
    "likes": 1000
}}

class Video(Resource):
    def get(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    def put(self,video_id):
        args=video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id],201




#api.add_resource(HelloWorld, '/')
#api.add_resource(Sleymi, '/ads/<string:name>')
api.add_resource(Video, '/video/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)


