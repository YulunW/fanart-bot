from pydantic.dataclasses import dataclass


@dataclass
class UploadedFile:
    busid: int
    id: str
    name: str
    size: int
    url: str
