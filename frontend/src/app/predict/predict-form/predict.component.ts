import { Component } from '@angular/core';
import { PredictService } from '../predict.service';
import { Patient, Gender } from '../../models/patient.model';
import { DialogType, DialogComponent } from '../../shared/dialogs/message-dialog/dialog.component';

type BooleanFields = 'smoke' | 'alco' | 'active';
type Step3 = 1 | 2 | 3;

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['../../shared/themes/forms.css'],
  standalone: false
})
export class PredictComponent {
  birthDate: Date | null = null;
  isLoading: boolean = false;

  showDialog = false;
  dialogType: DialogType = 'message';
  dialogTitle = '';
  dialogMessage = '';

  patient: Patient = {
    age: 0,
    gender: Gender.Female,
    height: 0,
    weight: 0,
    ap_hi: 0,
    ap_lo: 0,
    cholesterol: 1,
    gluc: 1,
    smoke: false,
    alco: false,
    active: false
  };

  model: string = 'random_forest';
  result: { prediction: string; probability: any } | null = null;

  readonly steps: Step3[] = [1, 2, 3];

  constructor(private service: PredictService) {}

  updateAge() {
    if (this.birthDate) {
      const today = new Date();
      const birth = new Date(this.birthDate);
      const diffTime = today.getTime() - birth.getTime();
      this.patient.age = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    }
  }

  toggle(field: BooleanFields) {
    this.patient[field] = !this.patient[field];
  }

  onSubmit() {
    if (!this.birthDate) {
      this.openDialog('error', 'Invalid Input', 'Please enter your date of birth.');
      return;
    }
    
    this.updateAge();
    if (this.patient.age<=0) {
      this.openDialog('error', 'Invalid Input', 'Date of birth cannot be in the future.');
      return;
    }

    if (this.patient.height <= 0 || this.patient.weight <= 0) {
      this.openDialog('error', 'Invalid Input', 'Height and weight must be positive values.');
      return;
    }

    if (this.patient.ap_hi <= 0 || this.patient.ap_lo <= 0) {
      this.openDialog('error', 'Invalid Input', 'Blood pressure must be positive.');
      return;
    }

    if (this.patient.ap_lo >= this.patient.ap_hi) {
      this.openDialog('error', 'Invalid Input', 'Diastolic cannot exceed systolic.');
      return;
    }

    const payload = {
      ...this.patient,
      smoke: this.patient.smoke ? 1 : 0,
      alco: this.patient.alco ? 1 : 0,
      active: this.patient.active ? 1 : 0
    };

    this.result = null;
    this.isLoading = true;

    this.service.predict(this.model, payload).subscribe({
      next: res => {
        this.result = res;
        console.log(res);
        this.isLoading = false;
        this.openDialog('message',res['prediction'], res['probability'] )
      },
      error: err => (this.result = { prediction: 'Error', probability: err.message })
    });
  }

  get cholesterolProgress() {
    return ((this.patient.cholesterol - 1) / 2) * 100;
  }

  get glucoseProgress() {
    return ((this.patient.gluc - 1) / 2) * 100;
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
