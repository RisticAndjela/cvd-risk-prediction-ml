from pydantic import BaseModel, Field
from typing import Optional

class Patient(BaseModel):
    id: Optional[int] = Field(None, description="Unique patient ID")
    age: int = Field(..., description="Age in days")
    gender: int = Field(..., description="Gender (1=female, 2=male)")
    height: int = Field(..., description="Height in cm")
    weight: float = Field(..., description="Weight in kg")
    ap_hi: int = Field(..., description="Systolic BP")
    ap_lo: int = Field(..., description="Diastolic BP")
    cholesterol: int = Field(..., description="Cholesterol level (1-3)")
    gluc: int = Field(..., description="Glucose level (1-3)")
    smoke: int = Field(..., description="Smoking (0/1)")
    alco: int = Field(..., description="Alcohol (0/1)")
    active: int = Field(..., description="Physical activity (0/1)")
    cardio: Optional[int] = Field(None, description="Has cardiovascular disease (0/1)")