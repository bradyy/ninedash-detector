from waitress import serve
import api


import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

serve(api.app, host='0.0.0.0', port=5000)

