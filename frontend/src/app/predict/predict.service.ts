import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../environment/environment';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PredictService {

  constructor(private httpClient: HttpClient) {}

  predict(model: string, patient: any): Observable<any> {
    return this.httpClient.post(`${environment.apiUrl}/predict`, { model, patient });
    }
}
