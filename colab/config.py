
import asyncio
import importlib
import json
import nest_asyncio
import os
import subprocess
import threading
import time
import uvicorn

from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse

from google.colab import files, output, userdata

from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.sessions import SessionMiddleware

server = None
thread = None
port_g = 5000