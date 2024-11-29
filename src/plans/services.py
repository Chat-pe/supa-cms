from datetime import datetime
from typing import List, Optional
from fastapi import HTTPException
from src.database import plans_client
from src.plans.dtos import (CreatePlanDTO, DeletePlanResponseDTO, PlanResponseDTO,
                         PlansListResponseDTO, UpdatePlanDTO)
from src.plans.schemas import Plan

async def create_plan(plan_data: CreatePlanDTO) -> PlanResponseDTO:
    plan = Plan(**plan_data.dict())
    await plans_client.insert_one(plan.dict())
    print(plan.dict())
    return PlanResponseDTO(**plan.dict())

async def get_plan(uniquelink: str) -> PlanResponseDTO:
    plan = await plans_client.find_one({"uniquelink": uniquelink})
    if plan:
        return PlanResponseDTO(**plan)
    raise HTTPException(status_code=404, detail="Plan not found")   
    

async def get_plans(skip: int = 0, limit: int = 10) -> PlansListResponseDTO:
    cursor = plans_client.find().skip(skip).limit(limit)
    plans = []
    async for plan in cursor:
        plans.append(PlanResponseDTO(**plan))
    total = await plans_client.count_documents({})
    return PlansListResponseDTO(plans=plans, total=total)

async def update_plan(uniquelink: str, plan_data: UpdatePlanDTO) -> PlanResponseDTO:
    update_data = {k: v for k, v in plan_data.dict().items() if v is not None}
    update_data["updated_at"] = datetime.now()
    
    result = await plans_client.find_one_and_update(
        {"uniquelink": uniquelink},
        {"$set": update_data},
        return_document=True
    )
    
    if result:
        return PlanResponseDTO(**result)
    raise HTTPException(status_code=404, detail="Plan not found")

async def delete_plan(uniquelink: str) -> DeletePlanResponseDTO:
    result = await plans_client.find_one_and_delete({"uniquelink": uniquelink})
    if result:
        return DeletePlanResponseDTO(
            message="Plan deleted successfully",
            deleted_plan_id=uniquelink
        )
    raise HTTPException(status_code=404, detail="Plan not found")
async def get_monthly_plans(skip: int = 0, limit: int = 10) -> PlansListResponseDTO:
    cursor = plans_client.find({"is_monthly": True}).skip(skip).limit(limit)
    plans = []
    async for plan in cursor:
        plans.append(PlanResponseDTO(**plan))
    total = await plans_client.count_documents({"is_monthly": True})
    return PlansListResponseDTO(plans=plans, total=total)

async def get_annual_plans(skip: int = 0, limit: int = 10) -> PlansListResponseDTO:
    cursor = plans_client.find({"is_monthly": False}).skip(skip).limit(limit)
    plans = []
    async for plan in cursor:
        plans.append(PlanResponseDTO(**plan))
    total = await plans_client.count_documents({"is_monthly": False})
    return PlansListResponseDTO(plans=plans, total=total)
