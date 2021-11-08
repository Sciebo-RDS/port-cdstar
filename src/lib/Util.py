from functools import wraps
from flask import request, g, current_app, abort
import os
import requests
import logging
from pyld import jsonld
import json
from RDS import Util

logger = logging.getLogger()


def require_api_key(api_method):
    @wraps(api_method)
    def check_api_key(*args, **kwargs):
        try:
            req = request.get_json(force=True, cache=True)
        except:
            req = request.form.to_dict()

        service, userId, apiKey = Util.parseUserId(req.get("userId"))

        logger.debug("req data: {}".format(req))

        if apiKey is None and userId is not None:
            apiKey = Util.loadToken(userId, "port-owncloud").access_token

        if apiKey is None:
            logger.error("apiKey or userId not found.")
            abort(401)

        logger.debug("found apiKey")
        g.apiKey = apiKey

        return api_method(*args, **kwargs)

    return check_api_key
