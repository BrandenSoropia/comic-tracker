import requests
import sys
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

from .comic_vine.request import send_cv_request
from .comic_vine.utils import build_filter_string

bp = Blueprint('comic', __name__, url_prefix='/comic')

@bp.route('/search', methods=['POST'])
def index():
    try:
        search_criteria = request.json

        headers = requests.utils.default_headers()
        headers.update(dict({
            'User-Agent': request.headers.get('User-Agent')
        }))

        if not search_criteria:
            return jsonify(error="Please provide search criteria, like series title."), 400
        data = {
            'filter': build_filter_string(search_criteria)
        }
        
        r = send_cv_request('/volumes', request.headers.get('User-Agent'), data=data, headers=headers)

        if r.ok:
            return jsonify(r.json())
        else:
            return jsonify(r.json()), 500
    except:
        e = sys.exc_info()[0]
        print('### Error: ', str(e))

        return jsonify(error='Something bad happened. Please try again'), 500
    
    

