from typing import List
from fastapi import FastAPI
from contextlib import asynccontextmanager

from crud import create_engine, Crud, Movie

import api_types as ApiTypes