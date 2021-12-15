from flask import render_template

from app.controllers.controller import ControllerBase


class TopicController(ControllerBase):

    @staticmethod
    def get():
        return render_template('topic.html')
