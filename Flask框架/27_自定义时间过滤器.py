from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.template_filter('hander_time')
def hander_time(time):
    # 获取当前时间
    now = datetime.now()
    # 将相差的时间转化为秒
    temp_stamp = (now-time).total_seconds()
    if temp_stamp < 60:
        return "1分钟之前"
    elif temp_stamp >= 60 and temp_stamp <= 60 * 60:
        return "1小时之前"
    elif temp_stamp >= 60 * 60 and temp_stamp <= 60 * 60 * 24:
        hours = int(temp_stamp / (60 * 60))
        return f'{hours}小时之前'
    elif temp_stamp >= 60 * 60 * 24 and temp_stamp < 60 * 60 * 24 * 30:
        day = int(temp_stamp / (60 * 60 * 24))
        return f'{day}天之前'
    else:
        return '很久以前'


@app.route('/')
def index():
    tmp_time = datetime(2023, 10, 10, 10, 10, 10)
    return render_template('index27.html', tmp_time=tmp_time)


if __name__ == '__main__':
    app.run(debug=True)
