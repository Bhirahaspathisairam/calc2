from app.controllers.controller import ControllerBase
from flask import render_template

class SoftwareController(ControllerBase):
    @staticmethod
    def get():
        return render_template('software.html')