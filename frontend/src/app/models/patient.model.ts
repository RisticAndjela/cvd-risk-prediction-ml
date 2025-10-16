export enum Gender {
    Male = 2,
    Female = 1
}
export interface Patient {
    id?: string,
    age: number;       
    gender: Gender;
    height: number;
    weight: number;
    ap_hi: number;
    ap_lo: number;
    cholesterol: 1 | 2 | 3;
    gluc: 1 | 2 | 3;
    smoke: boolean;
    alco: boolean;
    active: boolean;
}
