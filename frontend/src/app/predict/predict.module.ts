import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { PredictComponent } from './predict-form/predict.component';
import { DialogComponent } from "../shared/dialogs/message-dialog/dialog.component";

@NgModule({
    declarations:[PredictComponent],
    imports: [
    CommonModule,
    FormsModule,
    DialogComponent
],
    exports: [PredictComponent],
})
export class PredictModule {}
