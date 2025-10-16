import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PredictComponent } from './predict-form/predict.component';

@NgModule({
    declarations:[PredictComponent],
    imports: [
        CommonModule,
        FormsModule,
    ],
    exports: [PredictComponent],
})
export class PredictModule {}
