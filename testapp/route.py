from testapp import app
from testapp.tasks import delay_print

@app.route('/')
def index():
    delay_print.delay("hello")
    return "ok"
