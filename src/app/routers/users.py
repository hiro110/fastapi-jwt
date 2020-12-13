from typing import List, Optional

from fastapi import Depends, APIRouter

from db import session
from models import *
from schemas import *
from utils.auth import get_current_active_user

router = APIRouter()

@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.name}]
