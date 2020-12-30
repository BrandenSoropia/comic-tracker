import requests
import sys
import os
from copy import deepcopy

base_url = 'https://comicvine.gamespot.com/api'
base_params = dict({
    'api_key': os.environ["COMIC_VINE_API_KEY"],
    'format': 'json',
})

def send_cv_request(endpoint: str, user_agent:str, data: dict[str, any] = None , headers: dict[str, str] = None) -> str:
    """
    Send a request to Comic Vine API, reading API key from env.
    Prints error if any thrown, but doesn't raise it up. (Should it?)

    Keyword arguments:
    endpoint -- *Required* Specific Comic Vine endpoint to hit
    data -- Params to be turned into query params
    headers -- Headers to attach to request. Updates/appends to request library's defaults
    user_agent -- *Required* Needed to make the API work since Comic Vine blocks server-side request. Can get a value fro this from http request.
    """
    try:
        _headers = deepcopy(requests.utils.default_headers())

        _headers.update(dict({
                 'User-Agent': user_agent
        }))

        params = deepcopy(base_params)

        if data:
            params.update(data)

        if headers:
            _headers.update(headers)

        print(params)

        r = requests.get(base_url + endpoint, params=params, headers=_headers)
        print(r.url)

        return r
    except:
        e = sys.exc_info()[0]
        print("### Error in 'send_cv_request': ", str(e))


