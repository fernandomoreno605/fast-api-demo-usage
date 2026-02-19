from sqlalchemy.orm import Session

class SQLAlchemyUserRepository():
  def __init__(self, session: Session):
    self.session = session
  
  def get_all(self):
    pass
  
  def get_by_id(self, id: int):
    pass
  
  def create(self, user: User):
    pass
  
  def update(self, user: User):
    pass
  
  def delete(self, id: int):
    pass