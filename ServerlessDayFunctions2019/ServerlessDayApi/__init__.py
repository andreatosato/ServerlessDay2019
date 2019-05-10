import logging
import json
import os
import io


# Imports for image procesing
from PIL import Image

# Imports for prediction
from .predict import initialize, predict_image, predict_url

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Load and intialize the model
    initialize()
    try:
        #image_url = json.loads(req.params.get('url'))
        image_url = req.params.get('url')
        results = predict_url(image_url)
        #return jsonify(results)
        return json.dumps(results)
    except Exception as e:
        print('EXCEPTION:', str(e))
        return 'Error processing image'
'''
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
'''