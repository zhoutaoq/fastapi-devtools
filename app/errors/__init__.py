from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from .validation_error import validation_exception_handler


def register_custom_error_handle(server: FastAPI):
    # register the handle to app server
    server.add_exception_handler(RequestValidationError, validation_exception_handler)
