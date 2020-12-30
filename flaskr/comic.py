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
def search():
    try:
        search_criteria = request.json

        if not search_criteria:
            return jsonify(error="Please provide search criteria, like series title."), 400
        data = {
            'filter': build_filter_string(search_criteria)
        }
        
        r = send_cv_request('/volumes', request.headers.get('User-Agent'), data=data)

        if r.ok:
            return jsonify(r.json())
        else:
            return jsonify(r.json()), 500
    except:
        e = sys.exc_info()[0]
        print('### Error: ', str(e))

        return jsonify(error='Something bad happened when trying to search. Please try again'), 500
    

@bp.route('/series/<int:series_id>', methods=['GET'])
def get_series(series_id):
    """
    Request basic details of series includes specific issue info of a given series. Defaults to 100 results.

    Keyword arguments:
    series_id -- *Required* Comic Vine "volume" id.
    """
    try:
        if not series_id:
            return jsonify(error="Please provide a series id."), 400

        data = {
            'filter': f"volume:{series_id}"
        }
        
        r = send_cv_request("/issues", request.headers.get('User-Agent'), data=data)

        if r.ok:
            return jsonify(r.json())
        else:
            return jsonify(r.json()), 500
    except:
        e = sys.exc_info()[0]
        print('### Error: ', str(e))

        return jsonify(error='Something bad happened when trying getting issues for a series. Please try again'), 500
    


