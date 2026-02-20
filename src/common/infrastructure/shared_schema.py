from pydantic import BaseModel, ConfigDict
from src.common.utils import to_camelcase

class APIOutput(BaseModel):
  model_config = ConfigDict(
    alias_generator=to_camelcase,
    populate_by_name=True
  )
