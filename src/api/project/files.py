import logging
import os
import json
import requests
from RDS import Util
from flask import jsonify, request, g, abort
from io import BytesIO, BufferedReader

logger = logging.getLogger()


def index(project_id):
    abort(500)


def get(project_id, file_id):
    abort(500)


def post(project_id):
    abort(500)


def patch(project_id, file_id):
    abort(500)


def delete(project_id, file_id=None):
    abort(500)
