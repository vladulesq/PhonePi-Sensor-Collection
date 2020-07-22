import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def show_lightsensor_data():
        file = open('lightsensor.txt', "r")
        while file.readline():
            line = file.readline()

            startTime = line.find('"timeStamp":') + len('"timeStamp":')
            endTime = line.find(',', startTime)
            dataTime = line[startTime:endTime]

            startLight = line.find('"light":') + len('"light":')
            endLight = line.find('}', startLight)
            dataLight = line[startLight:endLight]

            json_data = json.dumps(
                {'time': dataTime, 'dataLight': dataLight})
            yield f"data:{json_data}\n\n"
            time.sleep(0.01)
        file.close()
        time.sleep(10000)

    return Response(show_lightsensor_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
