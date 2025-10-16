import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css'],
  standalone: false
})
export class HistoryComponent implements OnInit {
  history: any[] = [];

  ngOnInit() {
    this.loadHistory();
  }

  loadHistory() {
    const stored = localStorage.getItem('cvd_history');
    this.history = stored ? JSON.parse(stored) : [];
  }

  clearHistory() {
    localStorage.removeItem('cvd_history');
    this.history = [];
  }
}
