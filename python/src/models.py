from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
   
class Base(DeclarativeBase): pass
  
class Students(Base):
    __tablename__ = "students"
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    second_name : Mapped[str]
    date_bd : Mapped[str]
    course : Mapped[str]

