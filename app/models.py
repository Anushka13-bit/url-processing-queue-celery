from pydantic import BaseModel
from typing import List, Optional

class URLRequest(BaseModel):
    urls: List[str]