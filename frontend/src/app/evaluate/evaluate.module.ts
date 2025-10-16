import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DialogComponent } from "../shared/dialogs/message-dialog/dialog.component";
import { EvaluateComponent } from './evaluate-form/evaluate.component';

@NgModule({
    declarations:[EvaluateComponent],
    imports: [
    CommonModule,
    FormsModule,
    DialogComponent
],
    exports: [EvaluateComponent],
})
export class EvaluateModule {}
