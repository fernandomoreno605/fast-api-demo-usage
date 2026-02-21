from functools import wraps
from http import HTTPStatus
from typing import NamedTuple

from sqlalchemy.orm import Session
from src.users.application.services import UserServices
from src.users.factory import get_user_services

def handle_errors(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    try:
      return fn(*args, **kwargs)
    except ValueError as error:
      print("Value error: ", error)
      return {"error": str(error)}, HTTPStatus.BAD_REQUEST
    except TypeError as error:
      print("Type error: ", error)
      return {"error": str(error)}, HTTPStatus.BAD_REQUEST
    except Exception as error:
      print("Unexpected error: ", error)
      return {"error": "Unexpected error"}, HTTPStatus.INTERNAL_SERVER_ERROR

  return wrapper

class CommonContext(NamedTuple):
  user_services: UserServices

  @staticmethod
  def load(session: Session) -> "CommonContext":
    return CommonContext(
      user_services=get_user_services(session=session)
    )
