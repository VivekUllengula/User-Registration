import time
from functools import wraps
from fastapi.responses import JSONResponse

def log_executin_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = round((end - start) * 1000, 2)
        if isinstance(result, dict):
            result["Exexution Time"] = f"{exec_time} ms"
            return JSONResponse(content=result)
        return result
    return wrapper
