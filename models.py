from sqlalchemy import ForeignKey , String , BigInteger
from sqlalchemy.orm import Mapped , DeclarativeBase , mapped_column 
from sqlalchemy.ext.asyncio import AsyncAttrs , async_sessionmaker , create_async_engine


#echo потом отключить
engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3', echo=True)

async_sessionmaker = async_sessionmaker(bind=engine , expire_on_commit=False)

class Base(AsyncAttrs , DeclarativeBase):
    pass



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    FIO:Mapped[str] = mapped_column(String(256))
    Komanda:Mapped[str] = mapped_column(String(256)) 


class Sportsman(Base):
    __tablename__ = "sportsmans"

    id: Mapped[int] = mapped_column(primary_key=True)
    category:Mapped[int] = mapped_column()
    name:Mapped[str] = mapped_column(String(128))
    comanda:Mapped[str] = mapped_column(String(256))
    sportorg:Mapped[str] = mapped_column(String(256))
    dataage:Mapped[int] = mapped_column()
    dan:Mapped[str] = mapped_column(String(32))
    razrad:Mapped[str] = mapped_column(String(64))
    FIOTren:Mapped[str] = mapped_column(String(128)) 
    dso:Mapped[str] = mapped_column(String(32))
    vozrascategor[str] = mapped_column(String(64))
    user: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))

    async def _init_db():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all) 