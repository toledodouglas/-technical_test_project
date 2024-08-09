from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, autoincrement=True, primary_key=True,)
    cpf: Mapped[str] = mapped_column(unique=True, nullable=True)
    username: Mapped[str] = mapped_column(unique=True)
    uf: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    dataNasc: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
