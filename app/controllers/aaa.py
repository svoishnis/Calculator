from flask import render_template

from app.controllers.controller import ControllerBase


class AAAController(ControllerBase):

    @staticmethod
    def get():
        return render_template('aaa.html')
