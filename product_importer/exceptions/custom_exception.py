from flask import Flask
import flask

""" CustomException """
class CustomException(Exception):

    def __init__(self, status_code, se_code, message, hint=None):
        self.message = message
        self.status_code = status_code
        self.se_code = se_code
        self.hint = hint
    """
    # To Throw Custom SeException
    # @param self.statusCode string
    # @param se_code number
    # @param message string
    # @return response json
    """
    def throw_se_exception(self):
        response = flask.jsonify({
            'code': self.status_code,
            'data':[],
            'notification': {
                'hint':self.hint, 
                'message':self.message,
                'seCode': self.se_code, 
                'type':'error'
            }
        })
        response.status_code = self.status_code
        return response 