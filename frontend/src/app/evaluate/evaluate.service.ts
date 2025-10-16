import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environment/environment';

@Injectable({
  providedIn: 'root'
})
export class EvaluateService {

  constructor(private http: HttpClient) {}

  evaluate(model: string, dataset: string): Observable<any> {
    const params = new HttpParams()
      .set('model', model)
      .set('dataset', dataset);
    return this.http.get(`${environment.apiUrl}/evaluate`, { params });
  }
}
