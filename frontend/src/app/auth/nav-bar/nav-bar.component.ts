import { Router } from '@angular/router';
import { Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css'],
  standalone:false
})
export class NavbarComponent {
    isLoggedIn = true;
    menuOpen = false;

    constructor(private router: Router ) {}

    toggleMenu(): void {
        this.menuOpen = !this.menuOpen;
    }
}
