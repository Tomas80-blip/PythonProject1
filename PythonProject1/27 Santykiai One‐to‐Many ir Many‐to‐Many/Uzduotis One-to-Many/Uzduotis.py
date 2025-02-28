# One-to-Many ryšys: Projektai ir užduotys
# Užduotis:
# Sukurkite lenteles:
# • Project(id, name, deadline)
# • Task(id, project_id, description, status)
# 1. Pridėkite bent 5 projektus su skirtingais pavadinimais.
# 2. Kiekvienam projektui priskirkite bent 3 užduotis, turinčias skirtingus statusus
# ("Pending", "In Progress", "Completed").
# 3. Parašykite SQL užklausą, kuri grąžina visas užduotis, priklausančias tam tikram
# projektui.
# 4. Parašykite SQL užklausą, kuri pateikia projektus, kuriuose yra bent viena nebaigta
# užduotis.



from sqlalchemy import Column, create_engine, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date

engine = create_engine("sqlite:///one_to_many1.db")
Base = declarative_base()

class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    deadline = Column(Date, nullable=False)

    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    description = Column(String, nullable=False)
    status = Column(String(20), nullable=False)

    project = relationship("Project", back_populates="tasks")

# Sukuriame lenteles duomenų bazėje
Base.metadata.create_all(engine)

# Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()


# 1. Pridėkite bent 5 projektus su skirtingais pavadinimais.
projects = [
    Project(name="Projektas A", deadline=date(2025, 6, 1)),
    Project(name="Projektas B", deadline=date(2025, 7, 15)),
    Project(name="Projektas C", deadline=date(2025, 8, 20)),
    Project(name="Projektas D", deadline=date(2025, 9, 10)),
    Project(name="Projektas E", deadline=date(2025, 10, 5))
]
session.add_all(projects)
session.commit()

# 2. Kiekvienam projektui priskirkite bent 3 užduotis, turinčias skirtingus statusus
# ("Pending", "In Progress", "Completed").
tasks = [
    Task(project_id=1, description="Užduotis 1-1", status="Pending"),
    Task(project_id=1, description="Užduotis 1-2", status="In Progress"),
    Task(project_id=1, description="Užduotis 1-3", status="Completed"),

    Task(project_id=2, description="Užduotis 2-1", status="Pending"),
    Task(project_id=2, description="Užduotis 2-2", status="In Progress"),
    Task(project_id=2, description="Užduotis 2-3", status="Completed"),

    Task(project_id=3, description="Užduotis 3-1", status="Pending"),
    Task(project_id=3, description="Užduotis 3-2", status="In Progress"),
    Task(project_id=3, description="Užduotis 3-3", status="Completed"),

    Task(project_id=4, description="Užduotis 4-1", status="Pending"),
    Task(project_id=4, description="Užduotis 4-2", status="In Progress"),
    Task(project_id=4, description="Užduotis 4-3", status="Completed"),

    Task(project_id=5, description="Užduotis 5-1", status="Pending"),
    Task(project_id=5, description="Užduotis 5-2", status="In Progress"),
    Task(project_id=5, description="Užduotis 5-3", status="Completed")
]
session.add_all(tasks)
session.commit()

# 3. Užklausa, kuri grąžina visas užduotis, priklausančias tam tikram projektui
project_id = 1
tasks_for_project = session.query(Task).filter(Task.project_id == project_id).all()
print(f"Užduotys projektui ID {project_id}:")
for task in tasks_for_project:
    print(f"- {task.description} ({task.status})")

# 4. Užklausa, kuri pateikia projektus, kuriuose yra bent viena nebaigta užduotis
unfinished_tasks = session.query(Project).join(Task).filter(Task.status != "Completed").distinct().all()
print("\nProjektai su nebaigtomis užduotimis:")
for project in unfinished_tasks:
    print(f"- {project.name}")

# Uždarymas
session.close()


