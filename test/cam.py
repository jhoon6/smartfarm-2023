from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Webcam Streaming</title>
</head>
<body>
    <img src="{{ url_for('video_feed') }}" width="640" height="480" />
</body>
</html>"""

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    vc = VideoCamera()
    return Response(gen(vc), mimetype='multipart/x-mixed-replace; boundary=frame')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        if(self.video.read()[0] is False):
            self.video.release()
            self.video = cv2.VideoCapture(1)
        if(self.video.read()[0] is False):
            self.video.release()
            self.video = cv2.VideoCapture(2)
        if(self.video.read()[0] is False):
            self.video.release()
            self.video = cv2.VideoCapture(3)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    
    def are_you_here(self):
        return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)