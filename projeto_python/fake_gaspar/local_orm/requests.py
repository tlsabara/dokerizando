from sqlalchemy import Table, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import registry

mapper_registry = registry()

tb_requests = Table(
    "tb_requests",
    mapper_registry.metadata,
    Column("request_id", Integer, primary_key=True),
    Column("request_route", String(50)),
    Column("request_content", Text()),
    Column("request_timestamp", DateTime()),
)


class TbRequests:
    """A simple table to store the request data"""
    pass


mapper_registry.map_imperatively(tb_requests, TbRequests)
