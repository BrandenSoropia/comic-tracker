import requests
import sys
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('comic', __name__, url_prefix='/comic')

@bp.route('/search', methods=['POST'])
def index():
    try:
        data = dict({
            'api_key': os.environ["COMIC_VINE_API_KEY"],
            'format': 'json',
            # Remove this once figured out how to add lists in query params
            'filter': "name:monstress"
        })
        search_criteria = request.json
        headers = requests.utils.default_headers()

        headers.update(dict({
            'User-Agent': request.headers.get('User-Agent')
        }))

        if not search_criteria:
            return jsonify(error="Please provide search criteria, like series title."), 400
        # TODO: FIgure out how to add lists in query params
        # data.update(search_criteria)
        
        r = requests.get('https://comicvine.gamespot.com/api/volumes', params=data, headers=headers)
        print('### response ',r, r.url, r.headers)

        print('### response json', r.json())

        if r.ok:
            return jsonify(r.json())
        else:
            return jsonify(r.json()), 500
    except:
        e = sys.exc_info()[0]
        print('### Error: ', str(e))

        return jsonify(error='Something bad happened. Please try again'), 500
    
    

