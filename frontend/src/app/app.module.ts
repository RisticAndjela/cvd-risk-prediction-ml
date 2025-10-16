import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { App } from './app.component';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from "./auth/nav-bar/nav-bar.component";
import { HistoryComponent } from './history/history.component';

@NgModule({
  declarations: [
    App,
    NavbarComponent,
    HistoryComponent
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
