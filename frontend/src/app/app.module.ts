import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { App } from './app.component';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from "./auth/nav-bar/nav-bar.component";

@NgModule({
  declarations: [
    App,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    CommonModule,
    HttpClientModule
  ],
  bootstrap:[App]
})
export class AppModule {}
