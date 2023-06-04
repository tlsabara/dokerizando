from sqlalchemy import Table, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import registry

mapper_registry = registry()

tb_default_reponses = Table(
    "tb_default_reponses",
    mapper_registry.metadata,
    Column("default_reponses_id", Integer, primary_key=True),
    Column("default_reponses_route", String(100)),
    Column("default_reponses_tag", String(100)),
    Column("default_reponses_content", Text()),
    Column("default_reponses_is_active", Boolean()),
)


class TbDefaultResponses:
    """A simple table to store the responses for specifc routes"""
    pass


mapper_registry.map_imperatively(tb_default_reponses, TbDefaultResponses)

