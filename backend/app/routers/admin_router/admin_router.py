from fastapi import APIRouter, Depends
from app.dbManager.Entities import AdminEntity, AdminTokenEntity
from app.routers.admin_router.admin_models import AdminChangeInfoModel, AdminModel

from app.routers.admin_router.admin_service import AdminService
from app.routers.common_functions.common_models import AccountVerificationModel, TokenModel

admin_router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"},
               200: {"description": "Success"}},
)

service = AdminService()


@admin_router.get("/")
async def hello_function(body: TokenModel):
    return service.get_current_user(body, AdminEntity, AdminTokenEntity)


@admin_router.post("/create_user")
async def create_user(body: AdminModel):
    return service.create_user(body)

@admin_router.get("/sign_in")
async def sign_in(body: AccountVerificationModel):
    return service.verify_user(body, AdminEntity, AdminTokenEntity)


@admin_router.patch("/change_info")
async def change_info(body: AdminChangeInfoModel):
    return service.change_admin_inf(body)