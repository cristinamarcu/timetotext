import logging
import azure.functions as func
from .convert import convert_time_to_text, get_current_time
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function processing a request.')

    time = req.params.get('time')
    if not time:
        time = get_current_time()
    
    time_text = convert_time_to_text(time)
    logging.info(f'Responing with time_text="{time_text}" for time="{time}".')

    response={'time_text': time_text}
    return func.HttpResponse(json.dumps(response))

        
        
