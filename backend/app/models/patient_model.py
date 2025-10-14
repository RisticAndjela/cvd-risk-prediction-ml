from pydantic import BaseModel, Field
from typing import Optional

class Patient(BaseModel):
    id: Optional[int] = Field(None, description="Unique patient ID")
    age: int = Field(..., description="Patient age in days")
    gender: int = Field(..., description="Gender (1 = female, 2 = male)")
    height: int = Field(..., description="Height in cm")
    weight: float = Field(..., description="Weight in kg")
    ap_hi: int = Field(..., description="Systolic blood pressure")
    ap_lo: int = Field(..., description="Diastolic blood pressure")
    cholesterol: int = Field(..., description="Cholesterol level (1 = normal, 2 = above normal, 3 = well above normal)")
    glucose: int = Field(..., description="Glucose level (1 = normal, 2 = above normal, 3 = well above normal)")
    smoke: int = Field(..., description="Smoking status (0 = no, 1 = yes)")
    alco: int = Field(..., description="Alcohol intake (0 = no, 1 = yes)")
    active: int = Field(..., description="Physical activity (0 = no, 1 = yes)")
    cardio: Optional[int] = Field(None, description="Presence of cardiovascular disease (0 = no, 1 = yes)")