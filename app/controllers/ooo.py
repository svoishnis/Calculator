from flask import render_template

from app.controllers.controller import ControllerBase


class OOOController(ControllerBase):

    @staticmethod
    def get():
        return render_template('ooo.html')
