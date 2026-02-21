from sqlalchemy.orm import Session

class UnitOfWork:
  
  def __init__(self, session_factory):
    self.session_factory = session_factory
  
  def __enter__(self):
    self.session: Session = self.session_factory()
    self.session_readonly: Session = self.session_factory(readonly=True) 
    return self
  
  def __exit__(self, exc_type, *args):
    if self.session:
      self.session.rollback()
      self.session.close()
    if hasattr(self, 'session_readonly'):
      self.session_readonly.rollback()
      self.session_readonly.close()

  def commit(self):
    self.session.commit()

  def rollback(self):
    self.session.rollback()