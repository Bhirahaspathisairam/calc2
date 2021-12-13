from app.controllers.controller import ControllerBase
from flask import render_template

class WebController(ControllerBase):
    @staticmethod
    def get():
        return render_template('web.html')