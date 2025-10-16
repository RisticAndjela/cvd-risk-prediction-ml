import { Component } from '@angular/core';
import { DialogType } from '../../shared/dialogs/message-dialog/dialog.component';
import { EvaluateService } from '../evaluate.service';

@Component({
  selector: 'app-evaluate',
  templateUrl: './evaluate.component.html',
  styleUrls: ['../../shared/themes/forms.css'],
  standalone: false
})
export class EvaluateComponent {
  model: string = 'random_forest';
  dataset: string = 'test';
  isLoading: boolean = false;

  metrics: any = null;

  showDialog = false;
  dialogType: DialogType = 'message';
  dialogTitle = '';
  dialogMessage = '';

  constructor(private service: EvaluateService) {}

  onModelChange() {
    this.metrics = null;
  }

  onDatasetChange() {
    this.metrics = null;
  }

  onSubmit() {
    this.isLoading = true;
    this.metrics = null;

    this.service.evaluate(this.model, this.dataset).subscribe({
      next: res => {
        if (res.error) {
          this.openDialog('error', 'Evaluation Error', res.error);
        } else {
          this.metrics = res.metrics;
          this.openDialog('message', 'Evaluation Complete', `Model evaluated successfully.`);
        }
        this.isLoading = false;
      },
      error: err => {
        this.isLoading = false;
        this.openDialog('error', 'Request Failed', err.message);
      }
    });
  }

  openDialog(type: DialogType, title: string, message: string) {
    this.dialogType = type;
    this.dialogTitle = title;
    this.dialogMessage = message;
    this.showDialog = true;
  }

  onDialogClosed() {
    this.showDialog = false;
  }
}
