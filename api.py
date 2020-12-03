from flask import Flask
from flask_restful import Api, Resource, reqparse
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
api = Api(app)

def ActionPlug(p11, p15, p16, p13):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output (22, False)
    GPIO.output (18, False)
    GPIO.output (11, False)
    GPIO.output (15, False)
    GPIO.output (16, False)
    GPIO.output (13, False)
    GPIO.output (11, p11)
    GPIO.output (15, p15)
    GPIO.output (16, p16)
    GPIO.output (13, p13)
    time.sleep(0.1)
    GPIO.output (22, True)
    time.sleep(0.25)
    GPIO.output (22, False)
    GPIO.cleanup()
    return True


class AllPlugs(Resource):

  def get(self, state=0):
    if state == 1:
      ActionPlug(True, True, False, True)
      return 'now on', 200

    elif state == 0:
      ActionPlug(True, True, False, False)
      return 'now off', 200

    else:
      return 'Not a state', 404

class Plug1(Resource):

  def get(self, state=0):
    if state == 1:
      ActionPlug(True, True, True, True)
      return 'now on', 200

    elif state == 0:
      ActionPlug(True, True, True, False)
      return 'now off', 200

    else:
      return 'Not a state', 404

class Plug2(Resource):

  def get(self, state=0):
    if state == 1:
      ActionPlug(False, True, True, True)
      return 'now on', 200

    elif state == 0:
      ActionPlug(False, True, True, False)
      return 'now off', 200

    else:
      return 'Not a state', 404

api.add_resource(AllPlugs ,"/all-plugs/<int:state>")
api.add_resource(Plug1 ,"/plug1/<int:state>")
api.add_resource(Plug2 ,"/plug2/<int:state>")
if __name__ == '__main__':
    app.run()
