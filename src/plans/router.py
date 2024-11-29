from fastapi import APIRouter, Query
from src.plans.services import (
    create_plan,
    get_plan,
    get_plans,
    update_plan,
    delete_plan,
    get_monthly_plans,
    get_annual_plans
)
from src.plans.dtos import (
    CreatePlanDTO,
    UpdatePlanDTO,
    PlanResponseDTO,
    PlansListResponseDTO,
    DeletePlanResponseDTO
)

router = APIRouter()

@router.post("/", response_model=PlanResponseDTO)
async def create_new_plan(plan_data: CreatePlanDTO):
    return await create_plan(plan_data)

@router.get("/{uniquelink}", response_model=PlanResponseDTO)
async def retrieve_plan(uniquelink: str):
    return await get_plan(uniquelink)

@router.get("/", response_model=PlansListResponseDTO)
async def list_plans(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1)
):
    return await get_plans(skip, limit)

@router.put("/{uniquelink}", response_model=PlanResponseDTO)
async def modify_plan(uniquelink: str, plan_data: UpdatePlanDTO):
    return await update_plan(uniquelink, plan_data)

@router.delete("/{uniquelink}", response_model=DeletePlanResponseDTO)
async def remove_plan(uniquelink: str):
    return await delete_plan(uniquelink)

@router.get("/monthly/list", response_model=PlansListResponseDTO)
async def list_monthly_plans(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1)
):
    return await get_monthly_plans(skip, limit)

@router.get("/annual/list", response_model=PlansListResponseDTO)
async def list_annual_plans(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1)
):
    return await get_annual_plans(skip, limit)

