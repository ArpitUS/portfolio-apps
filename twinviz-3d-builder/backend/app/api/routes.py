from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from typing import List
from ..models import ProjectOut
from ..db import database, projects
from ..storage import save_upload, get_upload_path, remove_file
from ..core.config import settings

router = APIRouter()

@router.get('/health')
async def health():
    return {'status': 'ok', 'service': settings.APP_NAME}

@router.get('/info')
async def info():
    return {'name': settings.APP_NAME, 'version': '1.0.0', 'author': 'Arpit Srivastava'}

@router.post('/upload', response_model=ProjectOut)
async def upload(name: str, file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename
    save_upload(contents, filename)
    query = projects.insert().values(name=name, filename=filename, content_type=file.content_type)
    pid = await database.execute(query)
    row = await database.fetch_one(projects.select().where(projects.c.id == pid))
    return ProjectOut(**row)

@router.get('/projects', response_model=List[ProjectOut])
async def list_projects():
    rows = await database.fetch_all(projects.select().order_by(projects.c.created_at.desc()))
    return [ProjectOut(**r) for r in rows]

@router.get('/projects/{pid}', response_model=ProjectOut)
async def get_project(pid: int):
    row = await database.fetch_one(projects.select().where(projects.c.id == pid))
    if not row:
        raise HTTPException(404, 'Project not found')
    return ProjectOut(**row)

@router.get('/projects/{pid}/file')
async def get_file(pid: int):
    row = await database.fetch_one(projects.select().where(projects.c.id == pid))
    if not row:
        raise HTTPException(404, 'Not found')
    return FileResponse(get_upload_path(row['filename']), media_type=row['content_type'], filename=row['filename'])

@router.delete('/projects/{pid}')
async def delete_project(pid: int):
    row = await database.fetch_one(projects.select().where(projects.c.id == pid))
    if not row:
        raise HTTPException(404, 'Not found')
    remove_file(row['filename'])
    await database.execute(projects.delete().where(projects.c.id == pid))
    return {'status': 'deleted'}
