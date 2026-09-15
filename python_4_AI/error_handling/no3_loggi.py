"""print() is useful while learning
But production systems usually need logging

python has built-in import logging
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Application started")
"""
import logging

logging.basicConfig(level=logging.ERROR)
try:
    result = 10 / 0
    print(result)

except Exception:
    logging.exception("Calculation failed")