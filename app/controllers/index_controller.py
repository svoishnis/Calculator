from app.controllers.controller import ControllerBase
from flask import render_template, request

class IndexController(ControllerBase):
    @staticmethod
    def index():
        return render_template('index.html')