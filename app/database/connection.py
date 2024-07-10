from sqlalchemy import BigInteger,String,ForeignKey,select,distinct
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker,create_async_engine
engine = create_async_engine(url = 'url')
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs,DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employees'
    
    first_name:Mapped[str] = mapped_column(primary_key = True)
    last_name:Mapped[str] = mapped_column(primary_key = True)
    occupation:Mapped[str] = mapped_column(primary_key = True)
    department:Mapped[str] = mapped_column(primary_key = True)

async def get_departments():
    async with async_session() as session:
        result = await session.scalars(select(distinct(Employee.department)))
        print(result)
        return result.all()

async def get_occupations():
    async with async_session() as session:
        result = await session.scalars(select(distinct(Employee.occupation)))
        return result.all()

async def get_employees_by_occupation():
    async with async_session() as session:
        result = await session.execute(select(Employee.first_name, Employee.last_name,Employee.occupation))
        employees = result.all()
        return [f"{first} {last} {job} " for first, last,job in employees]

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)#creates the database
