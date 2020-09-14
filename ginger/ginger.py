"""
Created by Fanghl on 2020/9/10 11:51
"""
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    """
    捕捉所有异常
    :param  HTTPException APIException Exception
    """
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # log
        # 调试模式
        if not app.config['DEBUG']:
            return ServerError()
        else:
            return e


if __name__ == '__main__':
    app.run(debug=True)