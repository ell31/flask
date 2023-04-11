import av
import cv2
from flask import Flask, render_template, Response
import ssl
import time

app = Flask(__name__, template_folder='templates')
app.secret_key = '$aiware_web_key$'
version = '0.1.0'

rtmp_url = 'rtmp://210.99.70.120/live/cctv046.stream'
container = av.open(rtmp_url)
streams = container.streams


video_stream = streams.video[0]
#video_stream.thread_type = 'AUTO'


@app.route('/')
def index():
    return render_template('index.html')

period_value = 200
@app.route('/stream')
def stream():
    def generate():
        global period_value
        global video_stream
        
        for packet in container.demux(video_stream):
            for frame in packet.decode():
                try:
                    #image = cv2.cvtColor(frame.to_ndarray(format='bgr24'), cv2.COLOR_BGR2RGB)
                    #_, jpeg = cv2.imencode('.jpg', image)
                    #yield (b'--frame\r\n'
                    #    b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
                    #cv2.waitKey(period_value)
                    time.sleep(period_value / 1000)
                
                except:
                    period_value = period_value + 10
                    print("-------------- change : ", period_value)
                    #cv2.waitKey(200)
                    time.sleep(200 / 1000)
                    

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    #app.run(debug=True)
    print('------------------------------------------------')
    print('Wandlab CV - version ' + version )
    print('------------------------------------------------')
    

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='D:/1.AIWare/3.Project/U.Japen_Docker/1.Program/aiware-docker-web_20230322/zenai-cloud.com/fullchain2.pem',keyfile='D:/1.AIWare/3.Project/U.Japen_Docker/1.Program/aiware-docker-web_20230322/zenai-cloud.com/privkey2.pem')
    app.run(host='0.0.0.0',port=5202,ssl_context=ssl_context)# ,debug=True