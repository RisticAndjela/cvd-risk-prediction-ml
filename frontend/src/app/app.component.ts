import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  standalone:false
})
export class App {
  protected readonly title = signal('frontend');
}
