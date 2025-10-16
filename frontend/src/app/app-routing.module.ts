import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PredictComponent } from './predict/predict-form/predict.component';
import { EvaluateComponent } from './evaluate/evaluate-form/evaluate.component';
import { HistoryComponent } from './history/history.component';
import { HomepageComponent } from './homepage/homepage.component';
const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomepageComponent },
  { path: 'predict', component: PredictComponent },
  { path: 'evaluate', component: EvaluateComponent },
  { path: 'history', component: HistoryComponent },
  { path: '**', redirectTo: 'home' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}